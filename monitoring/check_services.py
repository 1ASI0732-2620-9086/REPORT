"""Comprobaciones HTTP de lectura, sin autenticación ni datos clínicos."""

import argparse
import http.client
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MAX_BODY_BYTES = 512 * 1024
IDENTIFIER = re.compile(r"[a-z0-9][a-z0-9-]{0,63}\Z")


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def validate_config(config, allow_local_http=False):
    limits = {"timeout_seconds": (0.01, 30), "attempts": (1, 5),
              "retry_delay_seconds": (0, 10), "latency_warning_ms": (1, 60000)}
    for key, (lower, upper) in limits.items():
        value = config.get(key)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"Configuración numérica inválida: {key}")
        if not lower <= value <= upper:
            raise ValueError(f"Configuración fuera de límites: {key}")
    if not isinstance(config["attempts"], int):
        raise ValueError("attempts debe ser entero")
    targets = config.get("targets")
    if not isinstance(targets, list) or not 1 <= len(targets) <= 20:
        raise ValueError("Se requiere entre 1 y 20 servicios")
    identifiers = set()
    for target in targets:
        identifier = target.get("id", "")
        if not isinstance(identifier, str) or not IDENTIFIER.fullmatch(identifier):
            raise ValueError("Identificador de servicio inválido")
        if identifier in identifiers:
            raise ValueError("Identificador de servicio duplicado")
        identifiers.add(identifier)
        name = target.get("name")
        if not isinstance(name, str) or not name or len(name) > 100 or "\n" in name:
            raise ValueError("Nombre de servicio inválido")
        url = urllib.parse.urlsplit(target.get("url", ""))
        local_http = (allow_local_http and url.scheme == "http"
                      and url.hostname in {"127.0.0.1", "localhost", "::1"})
        if (url.scheme != "https" and not local_http) or not url.hostname:
            raise ValueError("Los servicios requieren HTTPS; HTTP solo en pruebas locales")
        if url.username is not None or url.password is not None or url.fragment or url.query:
            raise ValueError("La URL no debe contener credenciales, parámetros ni fragmentos")
        if target.get("kind") not in {"html", "health"}:
            raise ValueError("Tipo de comprobación inválido")
        if target["kind"] == "html" and not target.get("expected_text"):
            raise ValueError("HTML requiere una marca de contenido esperada")
    return config


class SameOriginRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        def origin(url):
            parsed = urllib.parse.urlsplit(url)
            return parsed.scheme, parsed.hostname, parsed.port
        if origin(request.full_url) != origin(new_url):
            raise urllib.error.URLError("redirect_outside_origin")
        return super().redirect_request(request, response, code, message, headers, new_url)


def probe(target, config):
    result = {"checked_at": utc_now(), "http_status": None, "status": "down"}
    started = time.monotonic()
    try:
        request = urllib.request.Request(target["url"], headers={
            "User-Agent": "MAX-Continuous-Monitoring/1.0",
            "Accept": "application/json" if target["kind"] == "health" else "text/html",
        })
        opener = urllib.request.build_opener(SameOriginRedirect())
        with opener.open(request, timeout=config["timeout_seconds"]) as response:
            result["http_status"] = response.status
            content_type = response.headers.get_content_type()
            declared_length = response.headers.get("Content-Length", "")
            body = response.read(MAX_BODY_BYTES + 1)
            if declared_length.isdecimal() and len(body) < int(declared_length) and len(body) <= MAX_BODY_BYTES:
                raise http.client.IncompleteRead(b"", int(declared_length) - len(body))
        if result["http_status"] != 200:
            result["reason"] = "unexpected_http_status"
        elif len(body) > MAX_BODY_BYTES:
            result["reason"] = "response_too_large"
        elif target["kind"] == "health":
            if "json" not in content_type:
                result["reason"] = "unexpected_content_type"
            else:
                payload = json.loads(body)
                health = payload.get("status") if isinstance(payload, dict) else None
                result["health_status"] = health if isinstance(health, str) and health in {"UP", "DOWN", "UNKNOWN", "OUT_OF_SERVICE"} else "UNEXPECTED"
                result["reason"] = "ok" if health == "UP" else "health_not_up"
        elif content_type != "text/html":
            result["reason"] = "unexpected_content_type"
        elif target["expected_text"].casefold() not in body.decode("utf-8", errors="replace").casefold():
            result["reason"] = "expected_content_missing"
        else:
            result["reason"] = "ok"
    except urllib.error.HTTPError as error:
        result.update(http_status=error.code, reason="http_error")
        error.close()
    except (ValueError, UnicodeError):
        result["reason"] = "invalid_health_json"
    except (OSError, urllib.error.URLError, http.client.HTTPException) as error:
        result.update(reason="request_failed", error_type=type(error).__name__)
    result["duration_ms"] = round((time.monotonic() - started) * 1000, 2)
    if result["reason"] == "ok":
        result["status"] = "healthy"
        if result["duration_ms"] > config["latency_warning_ms"]:
            result.update(status="degraded", reason="slow_response")
    return result


def monitor(config, scope="production", allow_local_http=False):
    validate_config(config, allow_local_http)
    if scope not in {"production", "drill"}:
        raise ValueError("Ámbito inválido")
    report = {"schema_version": 1, "scope": scope, "started_at": utc_now(),
              "observer": "github-actions" if os.getenv("GITHUB_ACTIONS") == "true" else "local",
              "policy": {key: config[key] for key in (
                  "timeout_seconds", "attempts", "retry_delay_seconds", "latency_warning_ms")},
              "results": []}
    for target in config["targets"]:
        attempts = []
        for number in range(config["attempts"]):
            attempt = probe(target, config)
            attempts.append(attempt)
            if attempt["status"] == "healthy":
                break
            if number + 1 < config["attempts"]:
                time.sleep(config["retry_delay_seconds"])
        final = attempts[-1]
        report["results"].append({"id": target["id"], "name": target["name"],
                                  "url": target["url"], **final, "attempts": attempts})
    report.update(finished_at=utc_now(), healthy=all(
        result["status"] == "healthy" for result in report["results"]))
    return report


def write_report(report, output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# MAX - Resultado de monitoreo", "",
             f"Ámbito: `{report['scope']}`. Observador: `{report['observer']}`.", "",
             f"Inicio UTC: {report['started_at']}. Fin UTC: {report['finished_at']}.", "",
             "| Servicio | Estado | HTTP | Tiempo (ms) | Intentos | Motivo |",
             "|---|---|---|---|---|---|"]
    for result in report["results"]:
        lines.append(f"| {result['name']} | {result['status']} | {result['http_status']} | "
                     f"{result['duration_ms']} | {len(result['attempts'])} | {result['reason']} |")
    lines += ["", "Muestra puntual de HTTP y contenido esperado; no acredita disponibilidad entre muestras, "
              "operaciones clínicas completas ni fallos internos del cliente móvil.", ""]
    (output / "report.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="monitoring/targets.json")
    parser.add_argument("--output", default="monitoring-results/production")
    args = parser.parse_args()
    try:
        config = json.loads(Path(args.config).read_text(encoding="utf-8"))
        report = monitor(config)
        write_report(report, args.output)
    except (ValueError, OSError, TypeError, KeyError) as error:
        print(f"No se pudo generar el monitoreo: {type(error).__name__}")
        return 2
    for result in report["results"]:
        print(f"{result['id']}: {result['status']}, HTTP={result['http_status']}, "
              f"{result['duration_ms']} ms, intentos={len(result['attempts'])}")
    return 0 if report["healthy"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
