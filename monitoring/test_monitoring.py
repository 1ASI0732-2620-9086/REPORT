"""Pruebas HTTP aisladas; no contactan servicios publicados ni GitHub real."""

import contextlib
import copy
import io
import json
import os
import sys
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest import mock

import check_services as checks
import exercise as drill
import sync_incidents as incidents


class MonitoringTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.responses = []
        cls.hits = 0

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                cls.hits += 1
                code, content_type, body, delay = cls.responses.pop(0) if len(cls.responses) > 1 else cls.responses[0]
                time.sleep(delay)
                self.send_response(code)
                self.send_header("Content-Type", content_type)
                if self.path == "/truncated":
                    self.send_header("Content-Length", "9999")
                if code == 302:
                    self.send_header("Location", "https://example.invalid/")
                self.end_headers()
                try:
                    self.wfile.write(body)
                except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                    pass

            def log_message(self, *args):
                pass

        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def setUp(self):
        type(self).responses = [(200, "application/json", b'{"status":"UP"}', 0)]
        type(self).hits = 0
        self.config = {"timeout_seconds": 0.5, "attempts": 3, "retry_delay_seconds": 0,
                       "latency_warning_ms": 3000, "targets": [{"id": "test-health", "name": "HTTP de prueba",
                           "url": f"http://127.0.0.1:{self.server.server_port}/health", "kind": "health"}]}

    def run_check(self):
        return checks.monitor(self.config, "drill", allow_local_http=True)

    def test_up_requires_only_one_request(self):
        report = self.run_check()
        self.assertTrue(report["healthy"])
        self.assertEqual(report["results"][0]["health_status"], "UP")
        self.assertEqual(type(self).hits, 1)

    def test_three_http_failures_make_service_down(self):
        type(self).responses = [(503, "application/json", b'{"status":"DOWN"}', 0)]
        report = self.run_check()
        self.assertFalse(report["healthy"])
        self.assertEqual(type(self).hits, 3)
        self.assertTrue(all(attempt["http_status"] == 503 for attempt in report["results"][0]["attempts"]))

    def test_transient_failure_recovers_before_alert(self):
        type(self).responses.insert(0, (502, "text/plain", b"unavailable", 0))
        report = self.run_check()
        self.assertTrue(report["healthy"])
        self.assertEqual(type(self).hits, 2)

    def test_http_200_with_down_health_is_not_healthy(self):
        type(self).responses = [(200, "application/json", b'{"status":"DOWN"}', 0)]
        self.assertEqual(self.run_check()["results"][0]["reason"], "health_not_up")

    def test_bad_json_is_reported_without_aborting_other_checks(self):
        type(self).responses = [(200, "application/json", b"not-json", 0)]
        self.assertEqual(self.run_check()["results"][0]["reason"], "invalid_health_json")

    def test_unexpected_json_types_are_not_healthy(self):
        for body in [b"[]", b'{"status":[]}', b'{"status":null}', b'{"status":{}}']:
            with self.subTest(body=body):
                type(self).responses = [(200, "application/json", body, 0)]
                self.assertFalse(self.run_check()["healthy"])

    def test_login_or_error_html_cannot_pass_as_health(self):
        type(self).responses = [(200, "text/html", b"<html>Login</html>", 0)]
        self.assertEqual(self.run_check()["results"][0]["reason"], "unexpected_content_type")

    def test_html_requires_expected_content_not_just_200(self):
        self.config["targets"][0].update(kind="html", expected_text="<app-root")
        type(self).responses = [(200, "text/html", b"<html>Maintenance</html>", 0)]
        self.assertEqual(self.run_check()["results"][0]["reason"], "expected_content_missing")
        type(self).responses = [(200, "text/html", b"<app-root></app-root>", 0)]
        self.assertTrue(self.run_check()["healthy"])

    def test_latency_threshold_creates_degraded_status(self):
        self.config["latency_warning_ms"] = 1
        type(self).responses = [(200, "application/json", b'{"status":"UP"}', 0.025)]
        result = self.run_check()["results"][0]
        self.assertEqual(result["status"], "degraded")
        self.assertEqual(len(result["attempts"]), 3)

    def test_timeout_is_recorded_as_failure(self):
        self.config.update(timeout_seconds=0.02, attempts=1)
        type(self).responses = [(200, "application/json", b'{"status":"UP"}', 0.1)]
        self.assertEqual(self.run_check()["results"][0]["reason"], "request_failed")

    def test_redirect_outside_origin_is_not_followed(self):
        self.config["attempts"] = 1
        type(self).responses = [(302, "text/html", b"", 0)]
        self.assertFalse(self.run_check()["healthy"])
        self.assertEqual(type(self).hits, 1)

    def test_unbounded_response_is_rejected(self):
        self.config["attempts"] = 1
        type(self).responses = [(200, "application/json", b"x" * (checks.MAX_BODY_BYTES + 1), 0)]
        self.assertEqual(self.run_check()["results"][0]["reason"], "response_too_large")

    def test_interrupted_response_does_not_abort_the_report(self):
        self.config["targets"][0]["url"] = f"http://127.0.0.1:{self.server.server_port}/truncated"
        self.config["attempts"] = 1
        report = self.run_check()
        self.assertFalse(report["healthy"])
        self.assertEqual(report["results"][0]["reason"], "request_failed")
        self.assertEqual(report["results"][0]["error_type"], "IncompleteRead")

    def test_invalid_config_cannot_send_requests(self):
        for changes in [{"attempts": True}, {"attempts": 2.5}, {"timeout_seconds": 0}, {"targets": []}]:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                checks.monitor({**self.config, **changes}, "drill", True)
        self.assertEqual(type(self).hits, 0)

    def test_production_rejects_http_and_credentials(self):
        with self.assertRaises(ValueError):
            checks.monitor(self.config)
        self.config["targets"][0]["url"] = "https://user:password@example.invalid/health"
        with self.assertRaises(ValueError):
            checks.monitor(self.config)
        self.assertEqual(type(self).hits, 0)

    def test_duplicate_targets_are_rejected(self):
        self.config["targets"].append(copy.deepcopy(self.config["targets"][0]))
        with self.assertRaises(ValueError):
            self.run_check()

    def test_evidence_preserves_attempts_without_response_bodies(self):
        report = self.run_check()
        with tempfile.TemporaryDirectory() as directory:
            checks.write_report(report, directory)
            saved = json.loads((Path(directory) / "report.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["results"][0]["attempts"][0]["http_status"], 200)
            self.assertNotIn("body", saved["results"][0])
            self.assertTrue((Path(directory) / "report.md").is_file())

    def test_exercise_uses_real_loopback_without_dispatching_notifications(self):
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(drill, "GitHubAPI") as api:
            manifest = drill.exercise(directory)
            api.assert_not_called()
            self.assertTrue(manifest["passed"])
            self.assertEqual([phase["observed_http"] for phase in manifest["phases"]], [200, 503, 200])
            self.assertEqual([phase["attempts"] for phase in manifest["phases"]], [1, 3, 1])
            self.assertEqual(manifest["notification_mode"], "not_dispatched")


class IncidentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.issues = []
        cls.writes = []

        class Handler(BaseHTTPRequestHandler):
            def respond(self, status, payload):
                body = json.dumps(payload).encode("utf-8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                if cls.reject:
                    self.respond(403, {"message": "denied"})
                else:
                    self.respond(200, cls.list_override if cls.list_override is not None else
                                 [copy.deepcopy(issue) for issue in cls.issues if issue["state"] == "open"])

            def do_POST(self):
                payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                cls.writes.append(("POST", copy.deepcopy(payload)))
                issue = {**payload, "number": len(cls.issues) + 1, "state": "open",
                         "assignees": [] if cls.drop_assignment else [{"login": user} for user in payload.get("assignees", [])],
                         "html_url": f"https://github.com/test/report/issues/{len(cls.issues) + 1}"}
                cls.issues.append(issue)
                self.respond(201, issue)

            def do_PATCH(self):
                payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                cls.writes.append(("PATCH", copy.deepcopy(payload)))
                issue = next(issue for issue in cls.issues if issue["number"] == int(self.path.rsplit("/", 1)[1]))
                if cls.ignore_close:
                    payload.pop("state", None)
                    payload.pop("state_reason", None)
                issue.update(payload)
                self.respond(200, issue)

            def log_message(self, *args):
                pass

        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def setUp(self):
        type(self).issues = []
        type(self).writes = []
        type(self).reject = False
        type(self).drop_assignment = False
        type(self).list_override = None
        type(self).ignore_close = False
        self.api = incidents.GitHubAPI("test/report", "synthetic-test-token",
                                       f"http://127.0.0.1:{self.server.server_port}", test_api=True)

    def report(self, status, scope="production", identifier="backend"):
        return {"schema_version": 1, "scope": scope, "results": [{"id": identifier, "name": "Backend de prueba",
                "status": status, "http_status": 200 if status == "healthy" else 503,
                "duration_ms": 5, "reason": "ok" if status == "healthy" else "http_error",
                "checked_at": "2026-11-12T00:00:00+00:00", "attempts": [{"http_status": 503}]}]}

    def test_failure_repeat_and_recovery_have_only_two_mutations(self):
        first = incidents.sync(self.report("down"), self.api, "production", assignee="test-user")
        repeated = incidents.sync(self.report("down"), self.api, "production")
        recovered = incidents.sync(self.report("healthy"), self.api, "production", assignee="test-user")
        self.assertEqual([first["events"][0]["action"], repeated["events"][0]["action"], recovered["events"][0]["action"]],
                         ["opened", "unchanged", "recovered"])
        self.assertEqual([write[0] for write in type(self).writes], ["POST", "PATCH"])
        self.assertEqual(type(self).issues[0]["assignees"], [{"login": "test-user"}])
        self.assertEqual(type(self).issues[0]["state"], "closed")
        self.assertIn("Recuperación observada", type(self).issues[0]["body"])

    def test_healthy_service_does_not_create_notification(self):
        result = incidents.sync(self.report("healthy"), self.api, "production")
        self.assertFalse(type(self).writes)
        self.assertEqual(result["delivery"], "no_notification_needed")

    def test_drill_cannot_close_a_production_incident(self):
        incidents.sync(self.report("down"), self.api, "production")
        incidents.sync(self.report("healthy", "drill"), self.api, "drill")
        incidents.sync(self.report("down", "drill"), self.api, "drill")
        incidents.sync(self.report("healthy", "drill"), self.api, "drill")
        self.assertEqual([issue["state"] for issue in type(self).issues], ["open", "closed"])

    def test_recovery_cannot_close_an_unobserved_service(self):
        incidents.sync(self.report("down", identifier="backend-a"), self.api, "production")
        incidents.sync(self.report("healthy", identifier="backend-b"), self.api, "production")
        self.assertEqual(type(self).issues[0]["state"], "open")

    def test_degradation_opens_an_incident(self):
        result = incidents.sync(self.report("degraded"), self.api, "production")
        self.assertEqual(result["events"][0]["action"], "opened")

    def test_duplicate_incidents_require_review_instead_of_more_writes(self):
        incidents.sync(self.report("down"), self.api, "production")
        duplicate = copy.deepcopy(type(self).issues[0])
        duplicate["number"] = 2
        type(self).issues.append(duplicate)
        with self.assertRaises(RuntimeError):
            incidents.sync(self.report("down"), self.api, "production")
        self.assertEqual(len(type(self).writes), 1)

    def test_report_scope_and_empty_report_are_rejected(self):
        with self.assertRaises(ValueError):
            incidents.sync(self.report("healthy", "drill"), self.api, "production")
        with self.assertRaises(ValueError):
            incidents.sync({"schema_version": 1, "scope": "production", "results": []}, self.api, "production")
        self.assertFalse(type(self).writes)

    def test_api_rejection_is_not_a_confirmed_notification(self):
        type(self).reject = True
        with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
            incidents.sync(self.report("down"), self.api, "production")

    def test_token_destination_is_fixed(self):
        with self.assertRaises(ValueError):
            incidents.GitHubAPI("test/report", "synthetic-test-token", "https://example.invalid")

    def test_requested_assignee_cannot_be_silently_ignored(self):
        type(self).drop_assignment = True
        with self.assertRaisesRegex(RuntimeError, "sin confirmar la asignación"):
            incidents.sync(self.report("down"), self.api, "production", assignee="test-user")
        with self.assertRaisesRegex(RuntimeError, "revisar su asignación"):
            incidents.sync(self.report("down"), self.api, "production", assignee="test-user")
        self.assertEqual(len(type(self).writes), 1)

    def test_new_incident_is_closed_even_when_listing_is_stale(self):
        type(self).list_override = []
        opened = incidents.sync(self.report("down"), self.api, "production")
        repeated = incidents.sync(self.report("down"), self.api, "production")
        recovered = incidents.sync(self.report("healthy"), self.api, "production")
        self.assertEqual([opened["events"][0]["action"], repeated["events"][0]["action"],
                          recovered["events"][0]["action"]], ["opened", "unchanged", "recovered"])
        self.assertEqual(type(self).issues[0]["state"], "closed")
        self.assertEqual(len(type(self).writes), 2)

    def test_stale_open_listing_does_not_repeat_a_confirmed_close(self):
        incidents.sync(self.report("down"), self.api, "production")
        snapshot = copy.deepcopy(type(self).issues)
        incidents.sync(self.report("healthy"), self.api, "production")
        type(self).list_override = snapshot
        result = incidents.sync(self.report("healthy"), self.api, "production")
        self.assertEqual(result["events"][0]["action"], "healthy")
        self.assertEqual(len(type(self).writes), 2)

    def test_api_must_confirm_closed_state(self):
        incidents.sync(self.report("down"), self.api, "production")
        type(self).ignore_close = True
        with self.assertRaisesRegex(RuntimeError, "no confirmó el cierre"):
            incidents.sync(self.report("healthy"), self.api, "production")
        self.assertEqual(type(self).issues[0]["state"], "open")

    def run_remote_exercise_against_local_api(self):
        environment = {"GITHUB_ACTIONS": "true", "GITHUB_RUN_ID": "12345", "GITHUB_RUN_ATTEMPT": "2",
                       "GITHUB_REPOSITORY": "test/report", "MONITORING_ASSIGNEE": "test-user"}
        with tempfile.TemporaryDirectory() as directory, mock.patch.dict(os.environ, environment), \
                mock.patch.object(drill, "GitHubAPI", return_value=self.api):
            return drill.exercise(directory, notify=True)

    def test_remote_exercise_requires_open_and_close_despite_stale_listing(self):
        type(self).list_override = []
        result = self.run_remote_exercise_against_local_api()
        self.assertTrue(result["passed"])
        self.assertEqual([phase["notification_events"][0]["action"] for phase in result["phases"]],
                         ["healthy", "opened", "recovered"])
        self.assertEqual(type(self).issues[0]["state"], "closed")
        self.assertIn("exercise-12345-2", type(self).issues[0]["body"])

    def test_remote_exercise_fails_when_api_does_not_close(self):
        type(self).ignore_close = True
        result = self.run_remote_exercise_against_local_api()
        self.assertFalse(result["passed"])
        self.assertEqual(result["phases"][-1]["notification_error"], "RuntimeError")

    def test_cli_without_apply_never_calls_github(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "report.json"
            source.write_text(json.dumps(self.report("down")), encoding="utf-8")
            args = ["sync_incidents.py", "--report", str(source), "--output", directory]
            with mock.patch.object(sys, "argv", args), mock.patch.object(incidents, "GitHubAPI") as api, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(incidents.main(), 0)
                api.assert_not_called()
            result = json.loads((Path(directory) / "notifications.json").read_text(encoding="utf-8"))
            self.assertEqual(result["delivery"], "not_dispatched")


if __name__ == "__main__":
    unittest.main()
