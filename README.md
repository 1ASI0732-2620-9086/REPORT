# Capítulo VII: DevOps Practices

El enfoque DevOps propuesto para MAX busca conectar el desarrollo, la verificación y la publicación de sus componentes mediante procesos reproducibles. Su propósito será detectar errores antes del despliegue y mantener trazabilidad entre el código evaluado y la versión publicada.

La estrategia se organizará en integración continua, entrega continua y despliegue continuo. Cada etapa tendrá condiciones de entrada y salida para evitar que una versión avance cuando incumpla las verificaciones establecidas.

> **Estado de la documentación:** las herramientas, plataformas y configuraciones pendientes deberán completarse con la información real de los repositorios y de las ejecuciones del proyecto.

## 7.1. Continuous Integration

La integración continua de MAX tendrá como objetivo verificar los cambios incorporados a los repositorios mediante la ejecución automatizada de tareas de construcción y pruebas.

El flujo propuesto contempla evaluar los cambios antes de integrarlos en las ramas compartidas. Cada ejecución deberá registrar la versión del código, los controles realizados y sus resultados, facilitando la identificación de errores y regresiones.

La validación se organizará según los componentes del producto: landing page, aplicación web, backend y aplicaciones móviles incluidas en la entrega. Cada componente ejecutará las comprobaciones correspondientes a su tecnología y alcance.

<!-- IMAGEN: diagrama del flujo de integración continua implementado.
Debe representar las ramas, revisiones y comprobaciones reales.
Nombre sugerido: MAX-CI-Flujo-General.png -->

<p align="center">
  <img src="assets/MAX-CI-Flujo-General.png" alt="Flujo general de integración continua de MAX" width="900">
</p>

<p align="center">
  <em>Flujo de integración continua de MAX.</em>
</p>

### 7.1.1. Tools and Practices

El control de versiones se apoyará en Git y en los repositorios de GitHub del proyecto. Las herramientas de automatización, construcción y pruebas deberán documentarse a partir de la configuración real de MAX.

| Componente | Herramienta | Función |
|---|---|---|
| Control de versiones | Git y GitHub | Mantener el historial del código y permitir la revisión mediante pull requests. |
| Motor de automatización | Por confirmar | Ejecutar las tareas definidas ante los eventos configurados del repositorio. |
| Construcción | Por confirmar según componente | Preparar y construir cada componente del producto. |
| Frameworks de pruebas | Por confirmar | Ejecutar las suites automatizadas correspondientes. |
| Almacenamiento de reportes y artefactos | Por confirmar | Conservar los resultados y productos de cada ejecución. |

Las prácticas propuestas comprenden:

- Trabajar mediante ramas y mantener convenciones de nombres.
- Revisar los cambios antes de integrarlos.
- Ejecutar las comprobaciones obligatorias sobre la versión que se desea integrar.
- Bloquear la integración cuando fallen los controles requeridos.
- Registrar las versiones de las herramientas utilizadas.
- Mantener reproducible la instalación de dependencias.
- Administrar las credenciales mediante la configuración protegida del entorno de automatización.

**Información técnica por completar:** herramientas y versiones, estrategia de ramas, eventos que activan las ejecuciones y controles obligatorios.

<!-- IMAGEN: captura de las comprobaciones de un pull request y/o de las reglas de protección de ramas.
No mostrar valores de credenciales.
Nombre sugerido: MAX-CI-Tools-Practices.png -->

<p align="center">
  <img src="assets/MAX-CI-Tools-Practices.png" alt="Herramientas y prácticas de integración continua de MAX" width="900">
</p>

<p align="center">
  <em>Configuración de las prácticas de integración continua.</em>
</p>

### 7.1.2. Build & Test Suite Pipeline Components

El pipeline de integración continua se plantea como una secuencia de tareas que comprueba si una versión puede integrarse de forma satisfactoria.

| Etapa | Responsabilidad | Condición para continuar |
|---|---|---|
| Obtención del código | Recuperar la revisión asociada con el cambio. | El código corresponde al commit que se desea evaluar. |
| Preparación del entorno | Configurar las herramientas e instalar las dependencias. | El entorno queda disponible sin errores. |
| Comprobaciones estáticas | Revisar convenciones y otras reglas configuradas. | Se cumplen los controles obligatorios. |
| Construcción | Compilar o generar la aplicación según su tecnología. | La construcción finaliza correctamente. |
| Pruebas automatizadas | Ejecutar las suites unitarias y de integración previstas. | Las pruebas obligatorias resultan satisfactorias. |
| Publicación de resultados | Guardar los reportes y los artefactos correspondientes. | Los resultados quedan asociados con la ejecución. |

El orden definitivo y las dependencias entre tareas deberán corresponder al workflow implementado. Cuando falle una comprobación obligatoria, el pipeline deberá finalizar con un estado que impida promover esa versión hacia las siguientes etapas.

**Información técnica por completar:** ubicación del workflow, eventos de activación, tareas configuradas, comandos utilizados y artefactos producidos.

<!-- IMAGEN 1: captura del workflow de construcción y pruebas.
Nombre sugerido: MAX-CI-Workflow.png -->

<p align="center">
  <img src="assets/MAX-CI-Workflow.png" alt="Configuración del workflow de construcción y pruebas de MAX" width="900">
</p>

<p align="center">
  <em>Configuración del pipeline de construcción y pruebas.</em>
</p>

<!-- IMAGEN 2: vista de una ejecución real con las tareas y sus estados.
Nombre sugerido: MAX-CI-Pipeline-Resultados.png -->

<p align="center">
  <img src="assets/MAX-CI-Pipeline-Resultados.png" alt="Resultados del pipeline de integración continua de MAX" width="900">
</p>

<p align="center">
  <em>Resultados de una ejecución del pipeline de integración continua.</em>
</p>

## 7.2. Continuous Delivery

La entrega continua de MAX tendrá como finalidad mantener versiones verificadas y preparadas para su publicación. A partir de los resultados de integración continua, se plantea generar artefactos identificables y comprobar su funcionamiento en un entorno previo a producción.

Esta etapa permitirá revisar la configuración, la interacción entre componentes y los recorridos principales antes de liberar una versión a los usuarios.

La disponibilidad de una versión para producción deberá sustentarse en los resultados de las verificaciones establecidas. Cuando exista una aprobación manual de publicación, deberá quedar registrada como parte del proceso.

<!-- IMAGEN: diagrama que muestre la preparación de la versión, su despliegue en staging y las validaciones previas a producción.
Nombre sugerido: MAX-Delivery-Flujo-General.png -->

<p align="center">
  <img src="assets/MAX-Delivery-Flujo-General.png" alt="Flujo general de entrega continua de MAX" width="900">
</p>

<p align="center">
  <em>Flujo de preparación y validación de versiones para su entrega.</em>
</p>

### 7.2.1. Tools and Practices

Las herramientas de entrega continua deberán permitir recuperar los artefactos validados, desplegarlos en un entorno de pruebas y conservar evidencias de los resultados.

| Componente | Función prevista |
|---|---|
| Repositorios del proyecto | Identificar el código correspondiente a cada versión candidata. |
| Motor de automatización — por confirmar | Coordinar la preparación y el despliegue de la versión. |
| Repositorio de artefactos — por confirmar | Conservar los paquetes o archivos generados por la construcción. |
| Entorno de staging — por confirmar | Evaluar la versión antes de su publicación en producción. |
| Configuración por ambiente | Mantener separados los parámetros de pruebas y producción. |
| Herramientas de validación — por confirmar | Comprobar que la versión desplegada cumple los controles establecidos. |

Se propone identificar cada versión mediante una referencia al commit y una etiqueta de versión. También se deberá conservar el artefacto validado, evitando modificaciones sin trazabilidad durante su promoción.

Para las aplicaciones móviles, se documentará el mecanismo de generación y distribución de las versiones de prueba utilizado por el equipo.

**Información técnica por completar:** plataforma de staging, almacenamiento de artefactos, parámetros por ambiente y mecanismo de distribución móvil.

<!-- IMAGEN: captura de los artefactos disponibles y/o de la configuración del entorno de staging.
No mostrar valores de credenciales.
Nombre sugerido: MAX-Delivery-Tools-Practices.png -->

<p align="center">
  <img src="assets/MAX-Delivery-Tools-Practices.png" alt="Herramientas y configuración para la entrega continua de MAX" width="900">
</p>

<p align="center">
  <em>Artefactos y configuración del entorno de entrega.</em>
</p>

### 7.2.2. Stages Deployment Pipeline Components

El pipeline de entrega continua deberá comprobar que los artefactos pueden ejecutarse en un ambiente representativo antes de considerarlos disponibles para producción.

| Etapa | Descripción | Resultado esperado |
|---|---|---|
| Selección de la versión candidata | Recuperar una versión que haya superado la integración continua. | Se identifica el código y la ejecución de origen. |
| Recuperación del artefacto | Obtener el producto generado por la construcción. | Se utiliza el artefacto correspondiente a la versión seleccionada. |
| Preparación del ambiente | Configurar parámetros, servicios y dependencias. | El entorno queda preparado para recibir la versión. |
| Despliegue en staging | Publicar los componentes que correspondan. | La versión queda accesible para su evaluación. |
| Validación posterior | Comprobar disponibilidad, comunicación y recorridos principales. | Los controles previstos se completan satisfactoriamente. |
| Preparación de la liberación | Registrar resultados y disponibilidad para producción. | La versión queda lista para su promoción según la política establecida. |

Cuando se requieran cambios en la estructura de datos, estos deberán incluirse en la planificación del despliegue y evaluarse antes de promover la versión.

**Información técnica por completar:** etapas implementadas, condiciones de avance, versión evaluada y resultados de validación en staging.

<!-- IMAGEN 1: ejecución del pipeline de entrega y sus etapas.
Nombre sugerido: MAX-Delivery-Pipeline.png -->

<p align="center">
  <img src="assets/MAX-Delivery-Pipeline.png" alt="Etapas del pipeline de entrega continua de MAX" width="900">
</p>

<p align="center">
  <em>Ejecución de las etapas del pipeline de entrega continua.</em>
</p>

<!-- IMAGEN 2: evidencia de la versión desplegada en staging y de sus verificaciones.
Nombre sugerido: MAX-Delivery-Staging-Validacion.png -->

<p align="center">
  <img src="assets/MAX-Delivery-Staging-Validacion.png" alt="Validación de MAX en el entorno de staging" width="900">
</p>

<p align="center">
  <em>Validación de la versión candidata en staging.</em>
</p>

## 7.3. Continuous Deployment

El despliegue continuo plantea publicar automáticamente en producción las versiones que superen los controles establecidos, sin requerir una autorización manual adicional para desplegar cada una.

Para MAX, este apartado define el comportamiento previsto del proceso de publicación. Su implementación deberá comprobarse mediante el workflow real y las evidencias de despliegue. Si la publicación requiere una aprobación manual después de las validaciones, deberá documentarse como entrega continua con despliegue aprobado.

El alcance deberá precisarse por componente, ya que la publicación del backend y de la aplicación web puede seguir un mecanismo diferente al de la distribución móvil.

<!-- IMAGEN: diagrama del flujo hacia producción que refleje sus controles y disparadores reales.
Nombre sugerido: MAX-Deployment-Flujo-General.png -->

<p align="center">
  <img src="assets/MAX-Deployment-Flujo-General.png" alt="Flujo de despliegue de MAX hacia producción" width="900">
</p>

<p align="center">
  <em>Flujo de publicación de versiones en producción.</em>
</p>

### 7.3.1. Tools and Practices

Las herramientas de despliegue deberán permitir publicar la versión validada, comprobar su disponibilidad y conservar información suficiente para identificar qué versión se encuentra activa.

| Componente | Función prevista |
|---|---|
| Motor de automatización — por confirmar | Iniciar el despliegue cuando se cumplan sus condiciones. |
| Plataforma de alojamiento — por confirmar | Ejecutar el backend y alojar los componentes web correspondientes. |
| Gestión de credenciales | Autorizar las operaciones necesarias para publicar la versión. |
| Registro de versiones | Relacionar el despliegue con el commit y el artefacto utilizado. |
| Verificaciones posteriores | Comprobar que los componentes publicados responden correctamente. |
| Mecanismo de recuperación | Facilitar el retorno a una versión estable cuando sea viable. |

Se propone desplegar el mismo artefacto que haya superado las verificaciones previas y conservar la identificación de la versión anterior. La estrategia de recuperación deberá considerar la compatibilidad de los datos cuando existan modificaciones en la base de datos.

La generación automática de un paquete móvil no deberá presentarse, por sí sola, como publicación automática a los usuarios. Se documentará el canal de distribución y las condiciones que realmente se hayan implementado.

**Información técnica por completar:** plataforma de publicación, condiciones del despliegue, identificación de versiones y procedimiento de recuperación.

<!-- IMAGEN: configuración del despliegue y del entorno de producción.
Mostrar los componentes relevantes sin exponer credenciales.
Nombre sugerido: MAX-Deployment-Tools-Practices.png -->

<p align="center">
  <img src="assets/MAX-Deployment-Tools-Practices.png" alt="Herramientas y configuración del despliegue de MAX" width="900">
</p>

<p align="center">
  <em>Configuración de las herramientas de despliegue en producción.</em>
</p>

### 7.3.2. Production Deployment Pipeline Components

El pipeline de producción deberá relacionar la versión aprobada por los controles de calidad con el artefacto publicado y las verificaciones realizadas después de su despliegue.

| Etapa | Responsabilidad | Resultado esperado |
|---|---|---|
| Comprobación de condiciones | Confirmar que la versión superó los controles previos. | Una versión con controles fallidos no inicia el despliegue. |
| Identificación del artefacto | Recuperar el artefacto validado y su referencia de versión. | Existe trazabilidad entre código, pruebas y producto desplegable. |
| Preparación de producción | Configurar parámetros y comprobar las dependencias necesarias. | El ambiente reúne las condiciones requeridas. |
| Despliegue | Publicar los componentes correspondientes. | La versión queda instalada en el entorno de destino. |
| Verificación posterior | Comprobar disponibilidad y operaciones esenciales. | Se confirma que la versión responde según lo previsto. |
| Registro del resultado | Conservar versión, fecha, estado y evidencias. | El equipo puede identificar y revisar la publicación. |
| Recuperación ante fallos | Aplicar la estrategia definida si la versión no supera las verificaciones. | Se recupera un estado operativo o se registra la incidencia para su atención. |

Las comprobaciones posteriores deberán cubrir, como mínimo, la disponibilidad de los componentes publicados y la comunicación necesaria para utilizar las funciones centrales de MAX. Una ejecución satisfactoria del comando de despliegue no sustituirá la verificación de funcionamiento.

**Información técnica por completar:** versión publicada, ejecución del pipeline, verificaciones posteriores y resultados del procedimiento de recuperación, si fue ejecutado.

<!-- IMAGEN 1: ejecución real del pipeline de producción, mostrando las etapas y sus resultados.
Nombre sugerido: MAX-Production-Pipeline-Resultados.png -->

<p align="center">
  <img src="assets/MAX-Production-Pipeline-Resultados.png" alt="Resultados del pipeline de producción de MAX" width="900">
</p>

<p align="center">
  <em>Resultados de ejecución del pipeline de producción.</em>
</p>

<!-- IMAGEN 2: evidencia de la versión publicada y su funcionamiento.
Puede incluir la aplicación accesible y la identificación de la versión desplegada.
Nombre sugerido: MAX-Production-Validacion.png -->

<p align="center">
  <img src="assets/MAX-Production-Validacion.png" alt="Validación de la versión de MAX publicada en producción" width="900">
</p>

<p align="center">
  <em>Verificación de la versión publicada en producción.</em>
</p>
