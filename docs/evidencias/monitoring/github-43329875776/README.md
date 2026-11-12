# Ejecución remota aprobada de Continuous Monitoring

- [Run 43329875776](https://github.com/1ASI0732-2620-9086/REPORT/actions/runs/43329875776), evento `push`, rama `feature/report-chapter-7`.
- Commit del código evaluado: `9e81225054ca93351fe6541cdc39777109b2b37e`.
- Jobs `monitor` y `exercise`: `success`. Las 34 pruebas pasaron en el runner.
- Landing, frontend y backend: HTTP 200; backend con estado `UP`.
- [Incidencia #2](https://github.com/1ASI0732-2620-9086/REPORT/issues/2): apertura y cierre automáticos; asignada a `Carbocnito5443`.
- Secuencia verificada del simulacro: `healthy` → `opened` → `recovered`. El servidor de prueba usa loopback; no se provocó una caída de producción.
- Aviso correspondiente observado en el buzón de GitHub del destinatario, motivo `assign`. El usuario aportó además dos capturas del correo recibido, que muestran detección, recuperación, asignación y cierre de la incidencia #2.
- Programación periódica: inactiva; el workflow permanece fuera de la rama predeterminada.

## Fuentes originales y verificación

| Archivo | Contenido |
|---|---|
| [run.json](run.json), [jobs.json](jobs.json) | Estado, commit, evento y pasos consultados mediante la API de GitHub |
| [artifacts.json](artifacts.json) | IDs, nombres y digest de los dos artefactos publicados |
| [production/report.json](production/report.json), [production/report.md](production/report.md) | Medidas obtenidas por el runner contra los tres servicios publicados |
| [drill/exercise.json](drill/exercise.json) | Tres fases HTTP y acciones de notificación exigidas |
| [Apertura](drill/02-failure/notifications.json), [cierre](drill/03-recovery/notifications.json) | Respuestas confirmadas por la API, con la misma URL de incidencia |
| [issue.json](issue.json), [issue-events.json](issue-events.json) | Estado final cerrado, responsable e historial consultados directamente |
| [remote-tests.log](remote-tests.log), [logs-source.json](logs-source.json) | Log original de las 34 pruebas y miembro del ZIP del que se extrajo |
| [notification-verification.json](notification-verification.json) | Verificación del aviso para esta incidencia; sin IDs privados del buzón ni estado de lectura |
| [screenshots.json](screenshots.json) | Procedencia, dimensiones y SHA-256 de las tres capturas originales aportadas por el usuario |
| [verification.json](verification.json) | Resumen de la comprobación, fechas y hashes de artefactos |

Las capturas se incorporaron sin editar al informe: [GitHub Actions](../../../../assets/MAX-Monitoring-Resultado-GitHub.png), [correo de incidente y recuperación](../../../../assets/MAX-Monitoring-Correo-Incidente.png) y [correo de asignación y cierre](../../../../assets/MAX-Monitoring-Correo-Asignacion-Cierre.png). Los JSON originales de los artefactos conservan `email_receipt: not_verified`, que corresponde al estado conocido durante el workflow; la verificación posterior agrega la evidencia aportada por el destinatario.

Los ZIP originales están en [archives/production.zip](archives/production.zip), [archives/drill.zip](archives/drill.zip) y [archives/logs.zip](archives/logs.zip). Los dos artefactos se contrastaron con el campo `digest` SHA-256 de GitHub antes de extraerlos. El ZIP de logs tiene su hash calculado en `logs-source.json`; no se presenta ese hash local como un digest publicado por GitHub.

Esta ejecución sustituye como evidencia de aceptación a la [primera comprobación incompleta](../github-43329041988/README.md), que permanece conservada con su diagnóstico y limpieza.
