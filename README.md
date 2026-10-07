# Capítulo VI: Product Verification & Validation

## 6.1. Testing Suites & Validation

La estrategia de verificación y validación de MAX tiene como propósito comprobar que sus componentes cumplen los requisitos funcionales y que las aplicaciones permiten realizar las tareas previstas para el usuario. Su alcance comprende la gestión de identidad y acceso, la administración de pacientes y la gestión de placas y estudios médicos.

La verificación se orienta a revisar la lógica de los componentes, sus interacciones y el cumplimiento de las reglas del sistema. La validación se enfoca en comprobar que los flujos implementados permiten al profesional de salud registrar, consultar y organizar la información de sus pacientes.

Las pruebas se organizarán en cuatro grupos:

| Grupo de pruebas | Propósito en MAX |
|---|---|
| Core Entities Unit Tests | Verificar de forma aislada las entidades y funciones que contienen reglas de negocio. |
| Core Integration Tests | Comprobar la interacción entre los clientes, la API, la persistencia y el almacenamiento de archivos. |
| Core Behavior-Driven Development | Expresar y comprobar el comportamiento esperado mediante escenarios vinculados con las historias de usuario. |
| Core System Tests | Validar recorridos completos desde las aplicaciones web y móvil. |

Cada caso deberá relacionarse con el requisito que verifica y registrar sus condiciones iniciales, resultado esperado, resultado obtenido y evidencia. Las ejecuciones utilizarán datos de prueba para permitir su repetición sin afectar información real.

> **Estado de la documentación:** los casos y procesos descritos en este capítulo constituyen la base de verificación de MAX. Los resultados, herramientas y evidencias se incorporarán a partir de las ejecuciones reales.

<!-- IMAGEN: colocar una captura del resumen de las suites ejecutadas.
Debe permitir identificar los grupos de pruebas y sus resultados reales.
Nombre sugerido: MAX-Testing-Suites-Resumen.png -->

<p align="center">
  <img src="assets/MAX-Testing-Suites-Resumen.png" alt="Resumen de las suites de pruebas de MAX" width="900">
</p>

<p align="center">
  <em>Resumen de las suites de pruebas de MAX.</em>
</p>

## 6.1.1. Core Entities Unit Tests

Las pruebas unitarias de MAX se enfocarán en las entidades y funciones responsables de procesar información de usuarios, pacientes y estudios. Su finalidad será detectar errores en las reglas de negocio antes de comprobar la interacción con bases de datos, servicios o interfaces.

Cada prueba seguirá la estructura **Arrange, Act y Assert**:

- **Arrange:** preparar los datos y las dependencias requeridas.
- **Act:** ejecutar la operación que se desea evaluar.
- **Assert:** comprobar que el resultado coincide con el comportamiento esperado.

Cuando la unidad dependa de un repositorio u otro servicio, se utilizarán dobles de prueba para mantener aislado el comportamiento evaluado.

Los siguientes casos constituyen una propuesta inicial que deberá vincularse con los nombres reales de las clases y métodos del proyecto:

| ID | Unidad o responsabilidad | Caso propuesto | Resultado esperado |
|---|---|---|---|
| UT-01 | Validación de datos de cuenta | Evaluar un registro con campos obligatorios incompletos. | La validación identifica los campos faltantes y rechaza los datos incompletos. |
| UT-02 | Verificación de contraseña | Comparar una contraseña correcta y una incorrecta con un hash de prueba. | La verificación acepta únicamente la contraseña correspondiente. |
| UT-03 | Entidad paciente | Crear un paciente con información válida. | La entidad conserva correctamente los datos personales y médicos proporcionados. |
| UT-04 | Actualización de paciente | Modificar los datos permitidos de un paciente. | Se actualizan los campos correspondientes y se conserva su identificador. |
| UT-05 | Asociación de estudios | Evaluar un estudio sin referencia al paciente. | La validación rechaza la ausencia de la asociación requerida. |
| UT-06 | Validación de archivos | Evaluar formatos permitidos y no permitidos. | Se aceptan los formatos definidos por MAX y se rechazan los demás. |

Estas pruebas comprobarán reglas locales. La existencia del paciente en la base de datos, la persistencia de los cambios y la carga efectiva de archivos se verificarán mediante pruebas de integración.

**Información técnica por completar:**

- Framework y versión utilizados.
- Ubicación de los archivos de pruebas.
- Clases y métodos evaluados.
- Cantidad de pruebas ejecutadas y resultados.
- Cobertura obtenida, cuando se disponga de esta medición.

<!-- IMAGEN 1: captura de una prueba unitaria representativa.
Mostrar el nombre de la prueba y la estructura Arrange, Act y Assert.
Nombre sugerido: MAX-Unit-Tests-Caso.png -->

<p align="center">
  <img src="assets/MAX-Unit-Tests-Caso.png" alt="Caso de prueba unitaria de MAX" width="900">
</p>

<p align="center">
  <em>Caso representativo de prueba unitaria.</em>
</p>

<!-- IMAGEN 2: captura del reporte real de ejecución de pruebas unitarias.
Nombre sugerido: MAX-Unit-Tests-Resultados.png -->

<p align="center">
  <img src="assets/MAX-Unit-Tests-Resultados.png" alt="Resultados de las pruebas unitarias de MAX" width="900">
</p>

<p align="center">
  <em>Resultados de ejecución de las pruebas unitarias.</em>
</p>

## 6.1.2. Core Integration Tests

Las pruebas de integración de MAX comprobarán que sus componentes intercambian información correctamente. Su alcance incluirá la comunicación de las aplicaciones con la API, la aplicación de controles de acceso, la persistencia de pacientes y la relación entre los estudios registrados y sus archivos.

Estas pruebas deberán ejecutarse en un entorno controlado y especificar cuáles dependencias son reales y cuáles se sustituyen. Esto permitirá interpretar correctamente el alcance de los resultados.

| ID | Componentes involucrados | Escenario propuesto | Resultado esperado |
|---|---|---|---|
| IT-01 | Cliente, autenticación y persistencia de usuarios | Registrar una cuenta e iniciar sesión con sus credenciales. | La cuenta queda registrada y permite autenticarse mediante el mecanismo definido. |
| IT-02 | Cliente, API y control de acceso | Solicitar información protegida sin credenciales válidas. | La API rechaza la solicitud y no devuelve información protegida. |
| IT-03 | API, lógica de pacientes y persistencia | Registrar un paciente y consultarlo posteriormente. | Los datos recuperados corresponden al registro creado. |
| IT-04 | API, búsqueda y persistencia | Buscar pacientes por nombre o DNI. | Se devuelven los registros que cumplen el criterio utilizado. |
| IT-05 | API, actualización y persistencia | Editar un paciente y volver a consultar su información. | Los cambios se conservan y aparecen en la consulta posterior. |
| IT-06 | API, pacientes y almacenamiento | Adjuntar un archivo permitido a un paciente existente. | El estudio conserva la asociación con el paciente y una referencia válida al archivo. |
| IT-07 | API, validación y almacenamiento | Intentar cargar un formato no permitido. | La operación es rechazada sin registrar un estudio válido ni dejar archivos huérfanos. |

La evaluación deberá comprobar tanto la respuesta de cada operación como el estado final de los datos. Una respuesta satisfactoria de la API no será suficiente si la información no se almacena correctamente o queda asociada con un registro equivocado.

**Información técnica por completar:**

- Herramientas y entorno de ejecución.
- Componentes reales y dependencias sustituidas.
- Endpoints evaluados.
- Datos utilizados y procedimiento de limpieza.
- Resultados obtenidos.

<!-- IMAGEN 1: evidencia de una prueba de integración representativa.
Mostrar los componentes involucrados y las comprobaciones realizadas.
Nombre sugerido: MAX-Integration-Tests-Caso.png -->

<p align="center">
  <img src="assets/MAX-Integration-Tests-Caso.png" alt="Caso de prueba de integración de MAX" width="900">
</p>

<p align="center">
  <em>Verificación de la interacción entre componentes de MAX.</em>
</p>

<!-- IMAGEN 2: reporte real de ejecución de las pruebas de integración.
Nombre sugerido: MAX-Integration-Tests-Resultados.png -->

<p align="center">
  <img src="assets/MAX-Integration-Tests-Resultados.png" alt="Resultados de las pruebas de integración de MAX" width="900">
</p>

<p align="center">
  <em>Resultados de ejecución de las pruebas de integración.</em>
</p>

## 6.1.3. Core Behavior-Driven Development

El enfoque de **Behavior-Driven Development (BDD)** permite describir el comportamiento esperado de MAX desde la perspectiva del profesional de salud. Los escenarios se relacionarán con las historias de usuario y expresarán las condiciones iniciales, la acción realizada y el resultado observable.

Para su documentación se empleará la estructura **Given–When–Then**. Los siguientes escenarios constituyen una base funcional para su posterior automatización:

| ID | Historia relacionada | Given: condición inicial | When: acción | Then: resultado esperado |
|---|---|---|---|---|
| BDD-01 | US-01: Iniciar sesión | El médico cuenta con una cuenta registrada y credenciales válidas. | Solicita iniciar sesión. | El sistema permite acceder al panel principal. |
| BDD-02 | US-01: Iniciar sesión | El médico proporciona una contraseña incorrecta. | Solicita iniciar sesión. | El sistema rechaza el acceso e informa que las credenciales no son válidas. |
| BDD-03 | US-06: Registrar paciente | El médico está autenticado y dispone de los datos requeridos del paciente. | Confirma el registro del paciente. | El sistema crea el expediente y permite consultarlo. |
| BDD-04 | US-08: Buscar pacientes | Existe un paciente registrado con un DNI determinado. | El médico realiza una búsqueda mediante ese DNI. | El sistema muestra el paciente correspondiente. |
| BDD-05 | US-12: Adjuntar estudio | El médico está autenticado, existe un paciente y el archivo tiene un formato permitido. | Registra el estudio y adjunta el archivo. | El sistema vincula el estudio con el paciente y permite consultarlo. |
| BDD-06 | TS-05: Validación de tipos | El médico selecciona un archivo de formato no permitido. | Intenta adjuntarlo como estudio. | El sistema rechaza la carga e informa la restricción. |
| BDD-07 | US-15: Visualizar archivo | Existe un estudio registrado con un archivo disponible. | El médico solicita visualizarlo. | El sistema presenta el documento asociado al estudio seleccionado. |

Los escenarios deberán mantenerse alineados con los criterios de aceptación del backlog. Su redacción describe el comportamiento esperado; la comprobación de su cumplimiento requerirá implementarlos y ejecutarlos con la herramienta seleccionada.

**Información técnica por completar:**

- Herramienta utilizada para ejecutar los escenarios.
- Ubicación de los archivos `.feature`.
- Implementación de los pasos.
- Relación entre escenarios e historias de usuario.
- Resultados de ejecución.

<!-- IMAGEN 1: captura del archivo .feature con escenarios reales de MAX.
Nombre sugerido: MAX-BDD-Escenarios.png -->

<p align="center">
  <img src="assets/MAX-BDD-Escenarios.png" alt="Escenarios BDD de MAX redactados en Gherkin" width="900">
</p>

<p align="center">
  <em>Escenarios de comportamiento vinculados con las historias de usuario.</em>
</p>

<!-- IMAGEN 2: reporte de ejecución de los escenarios BDD.
Nombre sugerido: MAX-BDD-Resultados.png -->

<p align="center">
  <img src="assets/MAX-BDD-Resultados.png" alt="Resultados de ejecución de los escenarios BDD de MAX" width="900">
</p>

<p align="center">
  <em>Resultados de ejecución de los escenarios BDD.</em>
</p>

## 6.1.4. Core System Tests

Las pruebas de sistema evaluarán MAX como una solución integrada, utilizando sus interfaces web y móvil. Su propósito será comprobar que el usuario puede completar las tareas principales y que la información permanece consistente durante los recorridos.

Se considerarán escenarios satisfactorios, validaciones de entrada, estados sin información y respuestas ante fallos de comunicación. Cada ejecución deberá identificar el navegador o dispositivo, la versión de la aplicación y el entorno utilizado.

| ID | Recorrido propuesto | Resultado esperado |
|---|---|---|
| SYS-01 | Crear una cuenta e iniciar sesión. | El usuario puede completar el registro y acceder con sus credenciales. |
| SYS-02 | Registrar un paciente, localizarlo y consultar su detalle. | La información registrada aparece correctamente en las vistas correspondientes. |
| SYS-03 | Modificar un paciente y volver a consultar sus datos. | Los cambios se mantienen después de actualizar o reabrir la vista. |
| SYS-04 | Adjuntar un estudio a un paciente y visualizar su archivo. | El estudio aparece asociado al paciente correcto y su archivo puede abrirse. |
| SYS-05 | Filtrar estudios mediante los criterios disponibles. | Los resultados corresponden a los filtros aplicados. |
| SYS-06 | Consultar secciones sin registros o realizar búsquedas sin coincidencias. | La interfaz comunica la ausencia de información y mantiene disponibles las acciones pertinentes. |
| SYS-07 | Cerrar sesión e intentar acceder nuevamente a una sección protegida. | La aplicación solicita autenticarse y no continúa mostrando información protegida. |
| SYS-08 | Interrumpir la comunicación durante una operación. | La interfaz informa el problema y no presenta como completada una operación fallida. |

Los recorridos deberán ejecutarse en cada plataforma donde la funcionalidad esté disponible. Cuando una función tenga un alcance distinto entre web y móvil, esa diferencia deberá registrarse explícitamente.

**Información técnica por completar:**

- Navegadores y dispositivos utilizados.
- Versiones de las aplicaciones evaluadas.
- Herramientas de automatización, cuando corresponda.
- Resultados por plataforma.
- Incidencias identificadas y estado de atención.

<!-- IMAGEN 1: evidencia de un recorrido completo en la aplicación web.
Puede ser una composición de capturas con pasos numerados.
Nombre sugerido: MAX-System-Tests-Web.png -->

<p align="center">
  <img src="assets/MAX-System-Tests-Web.png" alt="Prueba de sistema de la aplicación web de MAX" width="900">
</p>

<p align="center">
  <em>Evidencia de un recorrido funcional en la aplicación web.</em>
</p>

<!-- IMAGEN 2: evidencia de un recorrido completo en la aplicación móvil.
Nombre sugerido: MAX-System-Tests-Mobile.png -->

<p align="center">
  <img src="assets/MAX-System-Tests-Mobile.png" alt="Prueba de sistema de la aplicación móvil de MAX" width="700">
</p>

<p align="center">
  <em>Evidencia de un recorrido funcional en la aplicación móvil.</em>
</p>

<!-- IMAGEN 3: reporte o matriz de resultados de las pruebas de sistema.
Nombre sugerido: MAX-System-Tests-Resultados.png -->

<p align="center">
  <img src="assets/MAX-System-Tests-Resultados.png" alt="Resultados de las pruebas de sistema de MAX" width="900">
</p>

<p align="center">
  <em>Resultados de las pruebas de sistema por plataforma.</em>
</p>


