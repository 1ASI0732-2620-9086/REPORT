# Evidencias de Continuous Monitoring de MAX

Trabajo publicado en `feature/report-chapter-7`, sobre el commit base `1fa501e925ecf97289df27652a4066bbb4992cc2`. Fecha: 12/11/2026, America/Lima. El código aprobado en Actions corresponde a `9e81225054ca93351fe6541cdc39777109b2b37e`. Esta incorporación corresponde a 7.4; se conservaron las secciones anteriores del capítulo VII. MAX_COMERCIAL no forma parte del alcance.

## Qué está acreditado

- [Run 43329875776 aprobado](https://github.com/1ASI0732-2620-9086/REPORT/actions/runs/43329875776), con jobs `monitor` y `exercise` ejecutados en GitHub Actions.
- GET reales a landing académica, frontend y salud del backend, observados desde el runner; los tres devolvieron HTTP 200 y el backend `UP`.
- Simulacro con HTTP real en loopback: 200, tres respuestas 503 y recuperación a 200; incidencia #2 abierta y cerrada automáticamente.
- Asignación a `Carbocnito5443` y aviso correspondiente observado en el buzón de GitHub de esa cuenta. La verificación conservada no publica IDs privados ni estado de lectura.
- Recepción por correo evidenciada mediante dos capturas originales aportadas por el destinatario: detección y recuperación; asignación y cierre. Una tercera captura muestra el resumen real de Actions y sus artefactos.
- 34 pruebas automatizadas aprobadas localmente y en Actions, incluidas regresiones sobre listados atrasados y cierres no confirmados.
- Validación del YAML y expresiones con actionlint 1.7.11. Shellcheck y pyflakes no estaban instalados y se desactivaron explícitamente.
- ZIP originales de los dos artefactos descargados y contrastados con los SHA-256 publicados por GitHub.

La programación no está activa porque el workflow permanece en la rama indicada y no en la predeterminada. La recepción por correo se acredita mediante las capturas aportadas por el usuario; los registros originales del script conservan `not_verified` porque se generaron antes de recibirlas. Los tiempos de respuesta son muestras puntuales y no mediciones continuas de un SLA.

## Archivos originales

La evidencia principal es la [ejecución remota aprobada](github-43329875776/README.md), con [resumen verificado](github-43329875776/verification.json), [log original de las 34 pruebas](github-43329875776/remote-tests.log), [incidencia e historial](github-43329875776/issue-events.json) y [verificación del aviso](github-43329875776/notification-verification.json). La [validación local final](final-local-validation-2026-11-12/validation.json) conserva las pruebas y hashes del código antes de publicar la corrección.

Las figuras 33–35 del informe utilizan estas capturas sin modificar: [resumen de Actions](../../../assets/MAX-Monitoring-Resultado-GitHub.png), [correo de incidente y recuperación](../../../assets/MAX-Monitoring-Correo-Incidente.png) y [correo de asignación y cierre](../../../assets/MAX-Monitoring-Correo-Asignacion-Cierre.png). Su procedencia, dimensiones y hashes están en [screenshots.json](github-43329875776/screenshots.json).

La [primera ejecución](github-43329041988/README.md) se conserva con su defecto de cierre y la limpieza operativa. No forma parte de la evidencia de recuperación automática aceptada.

La fase previa local se conserva a continuación. Sus 29 pruebas y registros `not_dispatched` corresponden a esa etapa anterior, no al estado final:

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

## Estado de publicación y programación

1. Se autorizó y realizó commit y push a `feature/report-chapter-7`, sin fusionar ni cambiar `main`. No se modificó backend, frontend, MOBILE, landing ni MAX_COMERCIAL.
2. El workflow usa `Carbocnito5443` cuando no hay variable `MONITORING_ASSIGNEE`. Se comprobó antes de publicar que no existiera un valor diferente; la incidencia real confirma el responsable.
3. La ejecución acredita los permisos de Actions e Issues utilizados: creación y cierre confirmados por la API. El sincronizador verifica asignación y estado de cierre, y el simulacro exige ambos eventos para aprobar.
4. Los artefactos conservados son `monitoring-production-43329875776-1` y `monitoring-drill-43329875776-1`. La incidencia de aceptación es [#2](https://github.com/1ASI0732-2620-9086/REPORT/issues/2), cerrada automáticamente y verificada directamente. Se observó también la notificación de asignación en el buzón de la cuenta destinataria.
5. El apartado 7.4 incorpora esos resultados. Una ejecución por push acredita ese instante, no una programación activa. Los cambios únicamente en documentación o evidencias no disparan otro simulacro, según los filtros `paths` del workflow.
6. Para activar `schedule`, el workflow debe existir en la rama predeterminada. Esa integración o cualquier planificador externo necesita una decisión y autorización posteriores. GitHub puede retrasar ejecuciones y desactiva horarios de repositorios públicos tras 60 días sin actividad.

Configurar `MONITORING_ASSIGNEE` en las variables del repositorio permite elegir otro responsable sin cambiar el script. El valor predeterminado del workflow es `Carbocnito5443`. La retención de artefactos preparada es de 30 días; las evidencias requeridas para una entrega deben conservarse antes de su expiración.

Fuentes: [eventos programados](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule), [REST de Issues](https://docs.github.com/en/rest/issues/issues), [notificaciones de workflows](https://docs.github.com/en/actions/concepts/workflows-and-actions/notifications-for-workflow-runs), [Actuator](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html).
