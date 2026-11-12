"""Gestiona incidentes en GitHub únicamente con --apply y token explícito."""

import argparse
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

from check_services import IDENTIFIER, utc_now


class GitHubAPI:
    def __init__(self, repository, token, api_base="https://api.github.com", test_api=False):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise ValueError("Repositorio inválido")
        if api_base != "https://api.github.com" and not (
                test_api and re.fullmatch(r"http://127\.0\.0\.1:[0-9]+", api_base)):
            raise ValueError("Origen de API no permitido")
        if not token:
            raise ValueError("Falta GITHUB_TOKEN")
        self.base = f"{api_base}/repos/{repository}"
        self.token = token

    def request(self, method, path, payload=None):
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(self.base + path, data=body, method=method, headers={
            "Authorization": f"Bearer {self.token}", "Accept": "application/vnd.github+json",
            "Content-Type": "application/json", "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "MAX-Continuous-Monitoring/1.0"})
        # Sin redirecciones: un token nunca se reenvía a otro servidor.
        opener = urllib.request.build_opener(NoRedirect())
        try:
            with opener.open(request, timeout=20) as response:
                return json.loads(response.read())
        except urllib.error.HTTPError as error:
            code = error.code
            error.close()
            raise RuntimeError(f"GitHub rechazó la operación: HTTP {code}") from None
        except (OSError, ValueError) as error:
            raise RuntimeError(f"Operación GitHub sin confirmar: {type(error).__name__}") from None

    def open_issues(self):
        issues = []
        for page in range(1, 11):
            batch = self.request("GET", f"/issues?state=open&per_page=100&page={page}")
            issues.extend(issue for issue in batch if "pull_request" not in issue)
            if len(batch) < 100:
                return issues
        raise RuntimeError("Demasiadas incidencias: no se crearán posibles duplicados")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def validate_report(report, scope):
    if scope not in {"production", "drill"} or report.get("scope") != scope:
        raise ValueError("El ámbito del reporte no coincide")
    if report.get("schema_version") != 1 or not report.get("results"):
        raise ValueError("Reporte vacío o incompatible")
    seen = set()
    for result in report["results"]:
        identifier = result.get("id", "")
        if not IDENTIFIER.fullmatch(identifier) or identifier in seen:
            raise ValueError("Servicios inválidos o repetidos")
        seen.add(identifier)
        if result.get("status") not in {"healthy", "degraded", "down"}:
            raise ValueError("Estado de servicio inválido")


def assigned_to(issue, assignee):
    return any(isinstance(user, dict) and user.get("login", "").casefold() == assignee.casefold()
               for user in issue.get("assignees", []))


def sync(report, api, scope, run_url="", assignee=""):
    validate_report(report, scope)
    if run_url and not re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/actions/runs/[0-9]+", run_url):
        raise ValueError("Enlace de ejecución inválido")
    if assignee and not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", assignee):
        raise ValueError("Responsable GitHub inválido")
    issues = api.open_issues()
    events = []
    for result in report["results"]:
        marker = f"<!-- max-monitoring:v1:{scope}:{result['id']} -->"
        matches = [issue for issue in issues if marker in (issue.get("body") or "")
                   and issue.get("title", "").startswith("[MAX monitoring]")]
        if len(matches) > 1:
            raise RuntimeError("Incidencias duplicadas: se requiere revisión manual")
        issue = matches[0] if matches else None
        if issue is not None and assignee and not assigned_to(issue, assignee):
            raise RuntimeError("El incidente existente no tiene al responsable configurado; revisar su asignación")
        summary = (f"Servicio: **{result['name']}** (`{result['id']}`).\n\n"
                   f"Ámbito: **{scope}**. Estado: **{result['status']}**. "
                   f"HTTP: `{result['http_status']}`. Tiempo: `{result['duration_ms']} ms`.\n\n"
                   f"Motivo: `{result['reason']}`. Intentos: `{len(result['attempts'])}`.\n\n"
                   f"Observado en UTC: {result['checked_at']}.\n\n"
                   + (f"[Ejecución y reportes]({run_url}).\n\n" if run_url else ""))
        event = {"target_id": result["id"], "status": result["status"], "action": "healthy"}
        if result["status"] != "healthy" and issue is None:
            prefix = "[SIMULACRO] " if scope == "drill" else ""
            payload = {"title": f"[MAX monitoring] {prefix}{result['name']}: {result['status']}",
                       "body": marker + "\n\n" + summary +
                       "Canal de notificación: GitHub Issues. El correo depende de las preferencias del destinatario."}
            if assignee:
                payload["assignees"] = [assignee]
            issue = api.request("POST", "/issues", payload)
            issues.append(issue)
            if assignee and not assigned_to(issue, assignee):
                raise RuntimeError("GitHub creó la incidencia sin confirmar la asignación al responsable")
            event["action"] = "opened"
        elif result["status"] != "healthy":
            event["action"] = "unchanged"
        elif issue is not None:
            api.request("PATCH", f"/issues/{issue['number']}", {
                "state": "closed", "state_reason": "completed",
                "body": issue["body"] + "\n\n## Recuperación observada\n\n" + summary})
            event["action"] = "recovered"
            issues.remove(issue)
        if issue is not None:
            event["issue_url"] = issue["html_url"]
        events.append(event)
    dispatched = sum(event["action"] in {"opened", "recovered"} for event in events)
    return {"checked_at": utc_now(), "scope": scope, "channel": "github_issues",
            "delivery": "github_api_confirmed" if dispatched else "no_notification_needed",
            "dispatched_events": dispatched, "email_receipt": "not_verified", "events": events}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", required=True)
    parser.add_argument("--scope", choices=["production", "drill"], default="production")
    parser.add_argument("--output", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    try:
        report = json.loads(Path(args.report).read_text(encoding="utf-8"))
        validate_report(report, args.scope)
        if args.apply:
            repository = os.environ.get("GITHUB_REPOSITORY", "")
            api = GitHubAPI(repository, os.environ.get("GITHUB_TOKEN", ""))
            run_id = os.environ.get("GITHUB_RUN_ID", "")
            run_url = f"https://github.com/{repository}/actions/runs/{run_id}" if run_id else ""
            result = sync(report, api, args.scope, run_url, os.environ.get("MONITORING_ASSIGNEE", ""))
        else:
            result = {"checked_at": utc_now(), "scope": args.scope,
                      "delivery": "not_dispatched", "reason": "Sin --apply: no se consultó ni modificó GitHub"}
        (output / "notifications.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=True))
        return 0
    except (ValueError, OSError, KeyError, TypeError, RuntimeError) as error:
        failure = {"checked_at": utc_now(), "delivery": "unconfirmed", "error_type": type(error).__name__}
        failure["reason"] = str(error) if isinstance(error, (RuntimeError, ValueError)) else "Error al leer o procesar los datos"
        (output / "notifications.json").write_text(json.dumps(failure, indent=2) + "\n", encoding="utf-8")
        print(f"No se pudo confirmar el canal GitHub: {failure['reason']}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
