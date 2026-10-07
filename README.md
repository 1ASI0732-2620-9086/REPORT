
# Capítulo VII: DevOps Practices

La estrategia DevOps propuesta para MAX busca conectar el control de versiones, la construcción, las pruebas y la publicación de sus componentes mediante procesos reproducibles.

Su propósito será detectar errores antes de la publicación, mantener trazabilidad entre el código y las versiones desplegadas, y reducir tareas manuales repetitivas.

Los apartados siguientes describen el proceso previsto. Las herramientas, ramas, eventos y resultados se completarán con la configuración real de los repositorios.

## 7.1. Continuous Integration

La integración continua permitirá evaluar los cambios de código mediante tareas automatizadas de construcción y pruebas.

El flujo deberá validar los cambios antes de su integración en las ramas protegidas. Cada ejecución se asociará con el commit evaluado y conservará los resultados necesarios para identificar fallos.

El alcance se documentará por componente: backend, aplicación web, landing page y aplicaciones móviles incluidas en la entrega.

### 7.1.1. Tools and Practices

| Categoría | Herramienta | Uso previsto en MAX |
|---|---|---|
| Control de versiones | Git y GitHub | Administrar el historial y la revisión de cambios. |
| Motor de CI | Por confirmar | Ejecutar los workflows de validación. |
| Construcción del backend | Por confirmar | Preparar dependencias y generar el artefacto del backend. |
| Construcción web | Por confirmar | Generar los archivos publicables de la aplicación web y la landing page. |
| Construcción móvil | Por confirmar | Generar los paquetes de las plataformas incluidas en la entrega. |
| Pruebas automatizadas | Por confirmar según plataforma | Ejecutar las suites configuradas. |
| Reportes y artefactos | Por confirmar | Conservar resultados y productos de las ejecuciones. |
| Gestión de credenciales | Por confirmar | Proporcionar las credenciales requeridas sin incorporarlas al código. |

Las prácticas previstas comprenden:

- Mantener una estrategia de ramas alineada con la gestión de configuración del proyecto.
- Revisar los cambios mediante pull requests.
- Ejecutar los controles requeridos antes de integrar una modificación.
- Impedir la integración cuando fallen comprobaciones obligatorias.
- Registrar las versiones de las herramientas y dependencias.
- Conservar reportes vinculados con cada ejecución.
- Mantener las credenciales fuera del repositorio y de los logs.

<!-- COMPLETAR: herramientas, versiones y reglas efectivamente configuradas. -->

<!-- IMAGEN: comprobaciones de un pull request y reglas de protección de ramas. -->

<p align="center">
  <img src="assets/MAX-CI-Tools-Practices.png" alt="Herramientas y prácticas de integración continua de MAX" width="900">
</p>

<p align="center"><em>Configuración de las prácticas de integración continua.</em></p>

### 7.1.2. Build & Test Suite Pipeline Components

El pipeline de integración continua comprobará que una revisión del código puede construirse y superar las verificaciones establecidas.

| Etapa | Responsabilidad | Resultado esperado |
|---|---|---|
| Obtención del código | Recuperar la revisión que se desea evaluar. | El entorno contiene el commit correcto. |
| Preparación del entorno | Configurar herramientas e instalar dependencias. | El entorno queda preparado para la ejecución. |
| Comprobaciones estáticas | Ejecutar las reglas configuradas de análisis y convenciones. | Se obtiene un resultado verificable de los controles obligatorios. |
| Construcción | Compilar o generar el componente correspondiente. | Se genera el producto previsto sin errores. |
| Pruebas | Ejecutar las suites automatizadas definidas. | Se registran los resultados de cada suite. |
| Publicación de reportes | Conservar logs y reportes. | Los resultados pueden revisarse posteriormente. |
| Publicación de artefactos | Guardar los productos aptos para las etapas posteriores. | Los artefactos quedan identificados y asociados con la ejecución. |

El orden definitivo deberá respetar las dependencias de las herramientas utilizadas. Los reportes de diagnóstico deberán conservarse también cuando una prueba falle, mientras que la promoción de artefactos deberá depender del cumplimiento de los controles establecidos.

**Eventos de ejecución por documentar:**

| Elemento | Configuración real |
|---|---|
| Eventos que activan el workflow | Por completar |
| Ramas y filtros de archivos | Por completar |
| Ejecución manual, si existe | Por completar |
| Jobs y dependencias | Por completar |
| Condiciones para aprobar la integración | Por completar |

<!-- CÓDIGO: insertar el workflow real o un fragmento representativo.
COMPLETAR: ruta y enlace al archivo del repositorio. -->

<!-- IMAGEN 1: representación del pipeline con sus tareas. -->

<p align="center">
  <img src="assets/MAX-CI-Pipeline.png" alt="Componentes del pipeline de integración continua de MAX" width="900">
</p>

<!-- IMAGEN 2: ejecución real y resultados de construcción y pruebas. -->

<p align="center">
  <img src="assets/MAX-CI-Resultados.png" alt="Resultados del pipeline de construcción y pruebas de MAX" width="900">
</p>

## 7.2. Continuous Delivery

La entrega continua permitirá disponer de versiones verificadas y preparadas para su publicación. A partir de una construcción validada, se plantea recuperar el artefacto correspondiente y comprobarlo en un entorno previo a producción.

Esta etapa facilitará la revisión de la configuración, las dependencias y los recorridos principales del producto.

La disponibilidad de una versión deberá sustentarse en evidencias. Cuando exista una aprobación manual antes de publicar en producción, esta deberá registrarse como parte del proceso de liberación.

### 7.2.1. Tools and Practices

| Categoría | Herramienta o recurso | Uso previsto |
|---|---|---|
| Automatización | Por confirmar | Coordinar la preparación y evaluación de versiones candidatas. |
| Almacenamiento de artefactos | Por confirmar | Conservar los productos generados por la integración continua. |
| Entorno de staging | Por confirmar | Evaluar la versión antes de publicarla en producción. |
| Configuración por ambiente | Por confirmar | Separar parámetros y credenciales de pruebas y producción. |
| Validación funcional | Por confirmar | Comprobar los recorridos definidos para la versión candidata. |
| Distribución móvil de pruebas | Por confirmar, cuando corresponda | Facilitar la instalación y evaluación de paquetes móviles. |

Las prácticas previstas incluyen identificar cada versión mediante su commit y etiqueta, conservar el artefacto validado y separar los ambientes de ejecución.

Los cambios de esquema de datos deberán evaluarse junto con la versión candidata cuando sean necesarios. También se documentarán las condiciones requeridas para promover una versión a producción.

<!-- COMPLETAR: plataforma, configuración de ambientes, identificación de artefactos y política de liberación. -->

<!-- IMAGEN: artefactos generados y configuración del entorno de staging. -->

<p align="center">
  <img src="assets/MAX-Delivery-Tools-Practices.png" alt="Herramientas y recursos de entrega continua de MAX" width="900">
</p>

<p align="center"><em>Recursos utilizados para preparar las versiones candidatas.</em></p>

### 7.2.2. Stages Deployment Pipeline Components

El pipeline de entrega continua deberá comprobar que la versión candidata funciona en un ambiente representativo y puede promoverse de acuerdo con la política de liberación.

| Etapa | Responsabilidad | Condición de salida |
|---|---|---|
| Selección de versión | Identificar una construcción que superó la integración continua. | Se conoce su commit y ejecución de origen. |
| Recuperación del artefacto | Obtener el producto validado. | El artefacto corresponde a la versión seleccionada. |
| Preparación de staging | Configurar parámetros y dependencias. | El ambiente reúne las condiciones necesarias. |
| Despliegue en staging | Publicar los componentes de la versión. | La aplicación queda disponible para evaluación. |
| Verificación inicial | Comprobar disponibilidad y comunicación entre componentes. | Las comprobaciones iniciales resultan satisfactorias. |
| Validación funcional | Ejecutar los recorridos previstos. | Los resultados cumplen los criterios de liberación. |
| Preparación de publicación | Registrar la versión candidata y sus evidencias. | La versión queda disponible para su promoción. |

Si una verificación falla, la versión deberá permanecer sin promover hasta resolver la incidencia y repetir las comprobaciones necesarias.

<!-- CÓDIGO: insertar la configuración real del pipeline de entrega.
COMPLETAR: disparadores, jobs, ambiente, artefacto y condiciones de promoción. -->

<!-- IMAGEN 1: ejecución del pipeline de entrega continua. -->

<p align="center">
  <img src="assets/MAX-Delivery-Pipeline.png" alt="Etapas del pipeline de entrega continua de MAX" width="900">
</p>

<!-- IMAGEN 2: evidencia de la versión en staging y sus verificaciones. -->

<p align="center">
  <img src="assets/MAX-Delivery-Staging.png" alt="Validación de MAX en el entorno de staging" width="900">
</p>

## 7.3. Continuous Deployment

El despliegue continuo contempla publicar automáticamente en producción las versiones que superen los controles establecidos, sin una autorización manual adicional para desplegar cada versión.

Para MAX, su alcance deberá precisarse según la configuración de cada componente. Si existe una aprobación manual específica de publicación después de las validaciones, el proceso deberá describirse como entrega continua con despliegue aprobado.

La revisión de un pull request puede coexistir con el despliegue continuo cuando, una vez integrado el cambio elegible y superados los controles, su publicación se realiza automáticamente.

### 7.3.1. Tools and Practices

| Categoría | Herramienta o recurso | Uso previsto |
|---|---|---|
| Automatización del despliegue | Por confirmar | Publicar las versiones que cumplen las condiciones requeridas. |
| Alojamiento del backend | Por confirmar | Ejecutar la versión publicada del servicio. |
| Alojamiento web y landing page | Por confirmar | Servir los archivos correspondientes a la versión. |
| Distribución móvil | Por confirmar, cuando corresponda | Publicar o distribuir las versiones móviles mediante el canal definido. |
| Identificación de versiones | Commit, etiqueta y artefacto, según configuración | Relacionar la ejecución con el producto publicado. |
| Verificación posterior | Por confirmar | Comprobar la disponibilidad y las funciones esenciales. |
| Recuperación | Por confirmar | Restaurar un estado operativo ante una publicación fallida. |

Las prácticas previstas incluyen desplegar el artefacto validado, registrar la versión activa y conservar una referencia a la versión anterior.

La recuperación deberá considerar la compatibilidad de los datos. Cuando existan cambios en la base de datos, el retorno a un binario anterior no se asumirá como suficiente sin comprobar dicha compatibilidad.

La generación de un paquete móvil se documentará de forma separada de su distribución. Solo se afirmará que existe publicación automática si el canal de entrega correspondiente está configurado y cuenta con evidencia.

<!-- COMPLETAR: plataformas reales, mecanismo de autenticación, disparadores y procedimiento de recuperación. -->

<!-- IMAGEN: configuración real del entorno y del mecanismo de despliegue.
No mostrar valores de credenciales. -->

<p align="center">
  <img src="assets/MAX-Deployment-Tools-Practices.png" alt="Herramientas y configuración del despliegue de MAX" width="900">
</p>

<p align="center"><em>Configuración de los recursos utilizados para el despliegue.</em></p>

### 7.3.2. Production Deployment Pipeline Components

El pipeline de producción deberá conservar la relación entre el código evaluado, el artefacto validado y la versión publicada.

| Etapa | Responsabilidad | Resultado esperado |
|---|---|---|
| Comprobación de elegibilidad | Confirmar que la versión cumple las condiciones de publicación. | Las versiones con controles fallidos no avanzan. |
| Recuperación del artefacto | Obtener el producto validado. | Se identifica el artefacto y su origen. |
| Preparación del entorno | Verificar parámetros y dependencias de producción. | El ambiente reúne las condiciones requeridas. |
| Publicación | Desplegar los componentes correspondientes. | La versión queda instalada en el destino. |
| Verificación posterior | Comprobar disponibilidad y operaciones esenciales. | Se obtiene evidencia del funcionamiento de la versión. |
| Registro del resultado | Conservar versión, fecha, estado y reportes. | El despliegue puede identificarse y revisarse. |
| Recuperación ante fallos | Aplicar el procedimiento definido cuando sea necesario. | Se recupera un estado operativo o se registra la incidencia para su atención. |

Las comprobaciones posteriores deberán revisar la disponibilidad de los componentes publicados y la comunicación requerida para utilizar las funciones centrales de MAX. El resultado satisfactorio del comando de despliegue deberá complementarse con estas verificaciones.

**Registro de despliegue**

| Dato | Valor |
|---|---|
| Componente publicado | Por completar |
| Versión o etiqueta | Por completar |
| Commit asociado | Por completar |
| Artefacto utilizado | Por completar |
| Fecha de publicación | Por completar |
| Entorno de destino | Por completar |
| Resultado del pipeline | Por completar |
| Resultado de verificaciones posteriores | Por completar |
| Enlace a la ejecución | Por completar |

<!-- CÓDIGO: insertar la configuración real del despliegue de producción.
COMPLETAR: archivo, condiciones de ejecución y dependencias entre jobs. -->

<!-- IMAGEN 1: ejecución real del pipeline de producción. -->

<p align="center">
  <img src="assets/MAX-Production-Pipeline.png" alt="Ejecución del pipeline de producción de MAX" width="900">
</p>

<p align="center"><em>Ejecución del pipeline de producción.</em></p>

<!-- IMAGEN 2: identificación de la versión publicada y comprobaciones posteriores. -->

<p align="center">
  <img src="assets/MAX-Production-Validacion.png" alt="Verificación de la versión de MAX publicada en producción" width="900">
</p>

<p align="center"><em>Verificación de la versión publicada en producción.</em></p>

<!-- EVIDENCIA ADICIONAL, SI EXISTE:
Añadir aquí el reporte de una prueba del procedimiento de recuperación.
No presentarlo como ejecutado si únicamente se ha documentado el procedimiento. -->
