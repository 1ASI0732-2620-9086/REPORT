"""Simulacro con HTTP real en loopback; no provoca caídas de producción."""

import argparse
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from check_services import monitor, utc_now, write_report
from sync_incidents import GitHubAPI, sync


def exercise(output, notify=False):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    state = {"code": 200}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            body = b'{"status":"UP"}' if state["code"] == 200 else b'{"status":"DOWN"}'
            self.send_response(state["code"])
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    repository = os.environ.get("GITHUB_REPOSITORY", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    if notify and (os.environ.get("GITHUB_ACTIONS") != "true" or not run_id.isdigit()):
        raise ValueError("Las notificaciones del simulacro solo se activan explícitamente en Actions")
    api = GitHubAPI(repository, os.environ.get("GITHUB_TOKEN", "")) if notify else None
    identifier = "exercise-" + (run_id if notify else "local")
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    config = {"timeout_seconds": 2, "attempts": 3, "retry_delay_seconds": 0.05,
              "latency_warning_ms": 3000, "targets": [{"id": identifier,
                  "name": "Endpoint HTTP de prueba", "kind": "health",
                  "url": f"http://127.0.0.1:{server.server_port}/health"}]}
    manifest = {"started_at": utc_now(), "scope": "drill", "production_outage": False,
                "notification_mode": "github_issues" if notify else "not_dispatched", "phases": []}
    try:
        for phase, code, expected in [("01-healthy", 200, True), ("02-failure", 503, False),
                                      ("03-recovery", 200, True)]:
            state["code"] = code
            report = monitor(config, scope="drill", allow_local_http=True)
            write_report(report, output / phase)
            entry = {"phase": phase, "expected_http": code, "observed_http": report["results"][0]["http_status"],
                     "healthy": report["healthy"], "passed": report["healthy"] == expected and report["results"][0]["http_status"] == code,
                     "attempts": len(report["results"][0]["attempts"])}
            if api:
                try:
                    notification = sync(report, api, "drill",
                                        f"https://github.com/{repository}/actions/runs/{run_id}",
                                        os.environ.get("MONITORING_ASSIGNEE", ""))
                    (output / phase / "notifications.json").write_text(
                        json.dumps(notification, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                    entry["notification_events"] = notification["events"]
                except (RuntimeError, ValueError, KeyError, OSError) as error:
                    entry.update(passed=False, notification_error=type(error).__name__)
            manifest["phases"].append(entry)
            # Guardar cada fase permite inspeccionar resultados aunque la ejecución se interrumpa.
            (output / "exercise.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    finally:
        server.shutdown()
        server.server_close()
        worker.join(timeout=3)
    manifest.update(finished_at=utc_now(), passed=all(phase["passed"] for phase in manifest["phases"]))
    (output / "exercise.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="monitoring-results/drill")
    parser.add_argument("--notify", action="store_true")
    args = parser.parse_args()
    try:
        result = exercise(args.output, args.notify)
    except (ValueError, RuntimeError, OSError) as error:
        print(f"Simulacro no completado: {type(error).__name__}")
        return 1
    print(json.dumps(result, ensure_ascii=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
