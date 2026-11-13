# Primera ejecución: comprobación de cierre incompleta

La [ejecución 43329041988](https://github.com/1ASI0732-2620-9086/REPORT/actions/runs/43329041988), commit `aa18e3f4a7c424274125f3c46eb21110a8a7bdd8`, terminó con estado `success`. Las comprobaciones HTTP y la apertura de la incidencia funcionaron. La verificación posterior detectó que la [incidencia #1](https://github.com/1ASI0732-2620-9086/REPORT/issues/1) permanecía abierta: **esta ejecución no acredita cierre automático ni un ciclo completo de notificación**.

El artefacto `drill/exercise.json` muestra `opened` durante el fallo y `healthy` durante la recuperación, en lugar de `recovered`. El sincronizador dependía de volver a encontrar la incidencia mediante el listado inmediatamente después de crearla. La siguiente consulta no la incluyó; la condición original del simulacro solo comprobaba salud HTTP y ausencia de excepciones.

Se corrigió el sincronizador para conservar las respuestas de escritura de la API durante el proceso y confirmar el estado `closed` devuelto al cerrar. El simulacro ahora exige las acciones `healthy`, `opened` y `recovered`, y separa los intentos por ID. Las regresiones sobre listados atrasados y cierres rechazados están en la [validación posterior](../final-local-validation-2026-11-12/validation.json).

Los JSON y los ZIP de `archives/` son los resultados originales. Los SHA-256 de los ZIP se contrastaron con `digest` en `artifacts.json`. `issue.json` e `issue-events.json` conservan el estado observado antes de la limpieza. `cleanup.json`, `issue-after-cleanup.json` e `issue-events-after-cleanup.json` registran el cierre operativo posterior, que no se atribuye al workflow.
