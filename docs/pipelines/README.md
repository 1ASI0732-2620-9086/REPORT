# Pipelines MAX: configuración preparada

Estado: archivos locales revisables, sin commit, publicación ni ejecución de Actions.

## Integración continua

Los cuatro proyectos locales tienen `.github/workflows/ci.yml` para push y pull request a `main`, además de ejecución manual. Los reportes se conservan con `if: always()`. Los candidatos se generan únicamente después de comprobaciones exitosas y contienen commit y SHA-256. Las Actions están fijadas al SHA consultado el 07/10/2026 en `../evidencias/reportes/actions-pins.json`.

- Backend: Java 21, Maven Wrapper, MySQL nativo temporal del runner, JUnit con H2 y MySQL; no Docker. Cada suite MySQL crea y elimina su propio esquema sintético.
- Angular: Node 24.13.1, npm 10.9.3, lockfile, Vitest, build, Playwright con API sustituida y auditoría de dependencias de ejecución. Una auditoría fallida bloquea el candidato.
- Android: Flutter 3.41.9, Java 21, lockfile, analyze, unidades y APK debug interno. El workflow básico no ejecuta un emulador.
- Landing React local: Node, lockfile, oxlint, unidades y build. Su remoto actual es PersonalProjects5443/LANDING-PAGE-MAX; no corresponde al repositorio académico LANDING-PAGE, que contiene HTML estático. No se ha cambiado el remoto.

`MAX_FRONT/MAX/.github/workflows/integration.yml` requiere ejecución manual con `backend_ref` (SHA de 40 caracteres) y `MAX_BACKEND_READ_TOKEN` con `contents:read` exclusivamente en el backend. Construye ese backend, inicia API y MySQL locales en el runner y ejecuta BDD y sistema web sin consultar producción. No utiliza credenciales reales ni R2.

## Entrega continua

Cada `delivery.yml` recibe el ID de una ejecución exitosa de su `ci.yml` en main. Verifica workflow, evento, resultado, commit y sumas; recupera el mismo artefacto y genera un candidato identificable. No lo reconstruye ni despliega.

Antes de promover: confirmar staging, ejecutar pruebas reales allí, comprobar migraciones en una copia protegida, resolver la auditoría de Angular, validar R2 en un bucket de prueba y revisar el canal móvil. La expiración de artefactos puede exigir una nueva ejecución CI, identificada como una construcción nueva.

## Producción: revisión pendiente

El alojamiento previsto para la aplicación clínica es Cloudflare Pages (Angular/proxy), Railway (Spring/MySQL) y R2. No se verificaron sus dashboards ni disparadores actuales. La configuración local del proxy exige `MAX_API_ORIGIN` fijo y opcionalmente `MAX_PROXY_SECRET`; Railway debe recibir el mismo secreto cuando se active esa comprobación. No guardar valores en Git.

No se añadió un workflow de publicación automática: faltan destino de staging, acceso a controles remotos y autorización de un despliegue nuevo. El historial público de GitHub Pages de la landing académica acredita únicamente ese sitio estático y esos commits históricos.

Secuencia de revisión para una futura publicación: candidato aprobado → respaldo y ensayo de restauración → preflight/migración compatible → backend/proxy → Angular → health y smoke sintético autorizado → registro de versión activa. No ejecutar escrituras clínicas reales para verificar una entrega.

Recuperación: seleccionar una versión compatible anterior en Railway/Pages; conservar ampliaciones de esquema. No revertir eliminando tablas ni sobrescribir nuevas escrituras con un backup antiguo. Android requiere un artefacto firmado y canal de distribución antes de hablar de publicación móvil.

Fuentes de herramientas: [checkout](https://github.com/actions/checkout), [setup-node](https://github.com/actions/setup-node), [setup-java](https://github.com/actions/setup-java), [upload-artifact](https://github.com/actions/upload-artifact), [flutter-action](https://github.com/subosito/flutter-action).
