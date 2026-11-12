# Evidencias de Continuous Monitoring de MAX

Trabajo local en `feature/report-chapter-7`, sobre el commit base `1fa501e925ecf97289df27652a4066bbb4992cc2`. Fecha: 12/11/2026, America/Lima. Esta incorporación corresponde a 7.4; se conservaron las secciones anteriores del capítulo VII. MAX_COMERCIAL no forma parte del alcance.

## Qué está acreditado

- GET reales a landing académica, frontend y salud del backend, observados desde el equipo local.
- Simulacro con HTTP real en loopback: 200, tres respuestas 503 y recuperación a 200.
- 29 pruebas automatizadas aprobadas; las pruebas de gestión de incidentes utilizan una API HTTP local de pruebas.
- Validación del YAML y expresiones con actionlint 1.7.11. Shellcheck y pyflakes no estaban instalados y se desactivaron explícitamente.

No se acredita todavía una ejecución de este workflow en Actions, su programación activa, una incidencia real en GitHub ni recepción de correo. Los registros locales lo indican expresamente. Los tiempos de respuesta son muestras puntuales y no mediciones continuas de un SLA.

## Archivos originales

Todos los enlaces siguientes apuntan a resultados locales conservados, no a capturas de interfaces de GitHub:

- [Validación, rama, commit base y hashes del código](2026-11-12/validation.json).
- [Salida original de las 29 pruebas](2026-11-12/tests.log).
- [Versión y resultado de actionlint](2026-11-12/actionlint.log).
- [Servicios publicados: JSON](2026-11-12/production/report.json).
- [Servicios publicados: Markdown](2026-11-12/production/report.md).
- [Canal GitHub sin despacho](2026-11-12/production/notifications.json).
- [Comprobación pública de Issues, workflows y tipo de cuenta destinataria](2026-11-12/remote-preflight.json).
- [Simulacro: manifiesto de las tres fases](2026-11-12/drill/exercise.json).
- Fase inicial: [JSON](2026-11-12/drill/01-healthy/report.json), [Markdown](2026-11-12/drill/01-healthy/report.md).
- Fallo: [JSON](2026-11-12/drill/02-failure/report.json), [Markdown](2026-11-12/drill/02-failure/report.md).
- Recuperación: [JSON](2026-11-12/drill/03-recovery/report.json), [Markdown](2026-11-12/drill/03-recovery/report.md).

El inventario [changes.json](changes.json) enumera los archivos nuevos y el README modificado, con sus hashes. Se limita a esta incorporación; no describe modificaciones de otros proyectos.

## Reproducir localmente

Desde PowerShell, en la raíz de REPORT, con Python 3.12 o posterior:

```powershell
python -m unittest discover -s monitoring -p "test_*.py" -v
python monitoring/check_services.py --config monitoring/targets.json
python monitoring/exercise.py --output monitoring-results/drill
python monitoring/sync_incidents.py --report monitoring-results/production/report.json --scope production --output monitoring-results/production
```

Los resultados de nuevas comprobaciones quedan en `monitoring-results/`, excluido de Git. El checker termina con 0 si todos los servicios están saludables, 1 si detecta fallo/degradación y 2 si no puede generar la comprobación. El simulacro sin `--notify` no contacta GitHub. El sincronizador sin `--apply` tampoco contacta GitHub.

Si Python no está en PATH en este equipo, se puede usar el runtime proporcionado por Codex:

```powershell
$pythonMax = 'C:\Program Files\WindowsApps\OpenAI.CodexPrimaryRuntime.v26-1112-737-0_26.1112.737.0_x64__3k8sg7r9htsxt\dependencies\python\python.exe'
& $pythonMax -m unittest discover -s monitoring -p "test_*.py" -v
& $pythonMax monitoring/check_services.py --config monitoring/targets.json
```

La ubicación corresponde al runtime instalado durante esta validación; puede cambiar con una actualización de Codex. Para validar el workflow con el binario ya existente en el workspace:

```powershell
& '..\.max-test-runtime\tools\actionlint\actionlint.exe' -shellcheck= -pyflakes= .github/workflows/monitoring.yml
git diff --check
```

## Revisión y activación remota pendiente

1. Autorizar explícitamente commit y push a `feature/report-chapter-7`. El destinatario confirmado es `Carbocnito5443`; su cuenta personal y asignabilidad se comprobaron mediante la API pública (HTTP 204). No se requiere modificar backend, frontend, MOBILE ni la landing.
2. Antes del push, comprobar que la variable opcional `MONITORING_ASSIGNEE` no sustituya el destinatario confirmado por otro. El workflow usa `Carbocnito5443` cuando esa variable no está definida. El primer push que incorpore `monitoring/**` o el workflow disparará `MAX Continuous Monitoring`: consultará los destinos publicados y ejecutará el simulacro aislado con apertura y cierre de una incidencia `[SIMULACRO]` asignada al responsable configurado.
3. El repositorio debe permitir Actions, Issues y el permiso `issues: write` del token. El usuario elegido debe poder ser asignado. Un rechazo de permisos quedará registrado como error, no como entrega confirmada.
4. Conservar URL y resultado de la ejecución, artefactos `monitoring-production-<run_id>-<attempt>` y `monitoring-drill-<run_id>-<attempt>`, y URL/historial de la incidencia de prueba. Verificar la notificación personal desde la cuenta destinataria antes de afirmar su recepción.
5. Agregar esas evidencias reales a 7.4 y actualizar su estado. Una ejecución por push acredita ese instante, no una programación activa.
6. Para activar `schedule`, el workflow debe existir en la rama predeterminada. Esa integración o cualquier planificador externo necesita una decisión y autorización posteriores. GitHub puede retrasar ejecuciones y desactiva horarios de repositorios públicos tras 60 días sin actividad.

Configurar `MONITORING_ASSIGNEE` en las variables del repositorio permite elegir otro responsable sin cambiar el script. El valor predeterminado del workflow es `Carbocnito5443`. La retención de artefactos preparada es de 30 días; las evidencias requeridas para una entrega deben conservarse antes de su expiración.

Fuentes: [eventos programados](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule), [REST de Issues](https://docs.github.com/en/rest/issues/issues), [notificaciones de workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/notifications-for-workflow-runs), [Actuator](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html).
