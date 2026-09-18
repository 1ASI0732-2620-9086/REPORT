# Capítulo IV: Product Design

El diseño de MAX —Medical Assistance Expert— comprende tres experiencias complementarias: una landing page que presenta la propuesta de valor, una aplicación web para la gestión del consultorio y una aplicación móvil que facilita el acceso a sus principales operaciones.

Las interfaces web y móvil documentadas están orientadas al personal del consultorio. Incluyen autenticación, gestión de pacientes, consulta de citas, administración de estudios y opciones de cuenta. La landing page comunica la propuesta general de conexión entre médicos y pacientes.

Este capítulo presenta las guías de estilo, la arquitectura de información, los wireframes, los mock-ups y los diagramas de interacción. Las capturas originales sirven como referencias del producto; las reconstrucciones y los estados adicionales representan decisiones de diseño. Las adaptaciones responsive y para iOS se presentan como propuestas.

Los mapas de prototipado documentan las conexiones previstas entre pantallas. Su presentación estática no sustituye los prototipos interactivos ni los videos de demostración.

<!-- Las rutas de las imágenes asumen que este archivo Markdown está junto a la carpeta assets/. -->

## 4.1. Style Guidelines

Las guías de estilo de MAX establecen criterios compartidos para mantener una identidad reconocible en la landing page, la aplicación web y la aplicación móvil. Comprenden branding, colores, tipografías, composición, iconografía, componentes y comunicación.

La identidad utiliza tonos azules, superficies con bordes redondeados y agrupaciones visuales que permiten distinguir tareas. La landing page y la aplicación móvil presentan superficies claras, mientras que las referencias de la aplicación web muestran un tema oscuro.

<div align="center">
  <img src="assets/MAX-Experiencias-Visuales.png" alt="Comparación de las experiencias visuales de MAX en landing page, web y mobile" width="1000">
  <p><em>Identidad visual de MAX aplicada a sus tres experiencias.</em></p>
</div>

### 4.1.1. General Style Guidelines

**Branding**

La identidad de MAX busca transmitir organización, claridad y cercanía en la gestión del consultorio. El nombre de la plataforma constituye el principal elemento de reconocimiento y se acompaña de un símbolo gráfico en la landing page.

En las pantallas de autenticación, las letras de MAX reciben mayor protagonismo. En las interfaces autenticadas, la marca comparte espacio con la navegación y el contenido operativo.

**Typography**

La guía visual establece las siguientes familias tipográficas:

| Aplicación | Tipografía de referencia | Criterio de uso |
| --- | --- | --- |
| Títulos y encabezados | Plus Jakarta Sans | Destacar los mensajes principales y la estructura del contenido. |
| Párrafos y descripciones | Inter | Facilitar la lectura de información explicativa. |
| Etiquetas, botones y controles | Inter | Mantener claridad en las acciones y los formularios. |

La jerarquía diferencia títulos, subtítulos, contenido y textos auxiliares mediante variaciones de tamaño y peso. Las instrucciones y los mensajes de validación se ubican próximos al campo correspondiente.

Las láminas reconstruidas utilizan DejaVu Sans como sustitución tipográfica de exportación. La referencia del producto sigue siendo Plus Jakarta Sans e Inter; su aplicación exacta debe contrastarse con los estilos de la implementación.

**Colors**

| Color | Código hexadecimal | Aplicación |
| --- | --- | --- |
| Primario | `#2F78E6` | Identidad, acciones principales y elementos destacados. |
| Secundario | `#4F9DFF` | Acentos, selecciones e indicadores de interacción. |
| Terciario | `#5AA9F3` | Variaciones y elementos complementarios. |
| Neutro oscuro | `#0B1A2A` | Texto sobre superficies claras y referencia para fondos oscuros. |

La paleta se complementa con blancos y azules claros en la landing page y mobile. La web emplea fondos oscuros, paneles diferenciados y textos claros.

Los colores funcionales refuerzan el significado de las acciones. En la web, el verde aparece en botones de guardado y el rojo en acciones como eliminar. En mobile, el azul identifica las acciones principales y el rojo señala errores de formulario.

El significado de una acción se comunica mediante su etiqueta y contexto, además del color.

**Spacing y composición**

Los espacios separan secciones, diferencian acciones y agrupan campos relacionados. En escritorio, la distribución aprovecha el ancho mediante columnas; en mobile, los formularios utilizan una disposición vertical con desplazamiento.

Las tarjetas mantienen márgenes internos para diferenciar su contenido. Las acciones principales y secundarias se presentan separadas para facilitar su identificación.

**Iconografía y componentes**

La iconografía representa conceptos como pacientes, calendario, documentos, estudios, perfil y configuración. Los destinos principales combinan iconos y etiquetas.

Los componentes incluyen botones, tarjetas, campos de texto, selectores, pestañas, ventanas modales y mensajes de estado. Cada componente conserva una función reconocible dentro de la experiencia correspondiente.

**Tono de comunicación**

| Dimensión | Orientación | Aplicación en MAX |
| --- | --- | --- |
| Divertido / Serio | Serio | Mensajes centrados en las tareas y el manejo responsable de la información. |
| Formal / Casual | Formal y cercano | Instrucciones comprensibles, sin tecnicismos innecesarios. |
| Respetuoso / Irreverente | Respetuoso | Comunicación considerada con los usuarios. |
| Entusiasta / Sereno | Sereno | Explicaciones directas que orientan sin generar alarma innecesaria. |

Los mensajes deben explicar qué sucede y cuál es el siguiente paso. Por ejemplo, “Primero registra un paciente” comunica una condición necesaria para continuar.

<div align="center">
  <img src="assets/MAX-Style-Guidelines.png" alt="Guía visual original de MAX con colores, tipografías y componentes" width="1000">
  <p><em>Guía visual de referencia del proyecto MAX.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-General-Style-Guide.png" alt="Guía general de estilo de MAX" width="1000">
  <p><em>Síntesis de los criterios generales de identidad y comunicación.</em></p>
</div>

### 4.1.2. Web Style Guidelines

La aplicación web organiza el trabajo mediante una cabecera, un menú lateral y un área principal. La cabecera presenta la marca y las opciones generales de sesión; el menú lateral permite cambiar de módulo y destaca la sección seleccionada.

Las referencias muestran una presentación oscura con tarjetas y formularios diferenciados del fondo. La landing page utiliza una presentación clara orientada a comunicar beneficios y facilitar el ingreso.

| Elemento | Criterio de diseño |
| --- | --- |
| Cabecera | Mantener visibles la identidad y las opciones generales de sesión. |
| Menú lateral | Identificar los módulos con iconos y etiquetas. |
| Área principal | Presentar título, descripción y acciones del módulo. |
| Tarjetas | Agrupar indicadores, información de perfil y preferencias. |
| Formularios | Ordenar los campos por relación y distinguir guardar de cancelar. |
| Ventanas modales | Concentrar una tarea conservando el contexto de origen. |
| Estados vacíos | Explicar la ausencia de registros y orientar el siguiente paso. |

**Adaptación responsive**

Las propuestas para navegador móvil reorganizan el contenido en una columna y adaptan la navegación al espacio disponible. Los formularios y sus acciones deben permanecer accesibles mediante desplazamiento vertical.

Estas variantes constituyen propuestas de diseño; las capturas originales documentan la presentación de escritorio.

**Idioma y accesibilidad**

Las referencias muestran controles ES y EN. Conforme al Project Statement, la implementación debe evidenciar inglés como idioma predeterminado y español latinoamericano como alternativa. Las capturas incluidas corresponden al español.

Se establecen como criterios de implementación las etiquetas accesibles, el foco visible, la navegación por teclado y los mensajes de error comprensibles. Su cumplimiento requiere validación sobre la aplicación.

<div align="center">
  <img src="assets/MAX-Web-Style-Guide.png" alt="Guía de estilo de la aplicación web MAX" width="1000">
  <p><em>Componentes y criterios de composición de la experiencia web.</em></p>
</div>

### 4.1.3. Mobile Style Guidelines

La aplicación móvil adapta las operaciones del consultorio a una composición vertical. Utiliza fondos claros, tarjetas blancas, acentos azules y controles distribuidos según el ancho disponible.

La navegación inferior incluye Inicio, Pacientes, Consultas y Estudios. Cada destino combina un icono con una etiqueta, y la opción seleccionada recibe un tratamiento visual diferenciado.

| Elemento | Criterio de diseño |
| --- | --- |
| Barra superior | Identificar el módulo y presentar controles generales. |
| Navegación inferior | Facilitar el acceso a los cuatro destinos principales. |
| Formularios | Distribuir los campos verticalmente y agruparlos por información. |
| Acciones principales | Utilizar botones destacados con etiquetas descriptivas. |
| Validaciones | Combinar bordes de error con mensajes junto al campo. |
| Estados vacíos | Diferenciar ausencia de registros, falta de coincidencias y condiciones previas. |
| Contraseñas | Incorporar entrada protegida y control de visibilidad. |

<div align="center">
  <img src="assets/MAX-Mobile-Style-Guide.png" alt="Guía de estilo de la aplicación móvil MAX" width="1000">
  <p><em>Componentes, navegación y estados de la experiencia móvil.</em></p>
</div>

#### 4.1.3.1. iOS Mobile Style Guidelines

La propuesta para iOS conserva la identidad de MAX y los cuatro destinos principales. Considera las áreas reservadas del dispositivo, los controles de retorno y la interacción con el teclado.

Los formularios deben permitir revisar los datos y alcanzar las acciones finales sin que el teclado o los elementos del sistema oculten información necesaria.

La siguiente lámina documenta los criterios de adaptación. No representa evidencia de una implementación ejecutada en iOS.

<div align="center">
  <img src="assets/MAX-iOS-Style-Guide.png" alt="Propuesta de guía de estilo de MAX para iOS" width="1000">
  <p><em>Propuesta visual de adaptación de MAX para iOS.</em></p>
</div>

#### 4.1.3.2. Android Mobile Style Guidelines

Las referencias de Android presentan una barra superior para identificar la sección y una navegación inferior persistente para cambiar de módulo.

El registro de pacientes utiliza un formulario vertical dividido en información personal y médica. Las acciones Guardar y Cancelar se ubican al final.

Los estados vacíos orientan al usuario. En Consultas y Estudios se explica que primero debe registrarse un paciente, mientras los controles de creación aparecen visualmente inactivos. El registro de cuenta utiliza mensajes próximos a cada campo para comunicar errores.

<div align="center">
  <img src="assets/MAX-Android-Style-Guide.png" alt="Guía de estilo de MAX para Android" width="1000">
  <p><em>Criterios visuales de Android basados en las interfaces proporcionadas.</em></p>
</div>

## 4.2. Information Architecture

La arquitectura de información organiza los contenidos según el propósito de cada experiencia.

La landing page presenta el producto y conduce al ingreso. La aplicación web concentra operaciones clínicas y administrativas. La aplicación móvil prioriza el resumen del consultorio, los pacientes, las consultas y los estudios.

Esta estructura busca que el usuario reconozca su ubicación, identifique las acciones disponibles y encuentre la información necesaria para completar una tarea.

<div align="center">
  <img src="assets/MAX-Information-Architecture.png" alt="Arquitectura general de información de MAX" width="1000">
  <p><em>Organización general de la información en landing page, web y mobile.</em></p>
</div>

### 4.2.1. Organization Systems

MAX combina estructuras jerárquicas y secuenciales con agrupaciones visuales en cuadrícula.

| Sistema | Aplicación | Propósito |
| --- | --- | --- |
| Jerárquico | Módulos web y destinos móviles. | Organizar funciones desde categorías generales hacia tareas específicas. |
| Secuencial | Registro de cuenta, registro de paciente y carga de estudios. | Ordenar los pasos necesarios para completar una operación. |
| Matricial o de exploración por categorías | Funcionalidades del landing e indicadores de inicio. | Presentar accesos y contenidos relacionados para su exploración. |

La clasificación temática distingue pacientes, consultas, estudios y opciones de cuenta. La dimensión temporal aparece en próximas citas, actividad reciente y filtros por fecha.

Las agrupaciones conceptuales de los diagramas facilitan la lectura de la estructura; no implican necesariamente menús adicionales en la interfaz.

<div align="center">
  <img src="assets/MAX-Organization-Systems.png" alt="Sistemas de organización de contenidos de MAX" width="1000">
  <p><em>Estructuras de organización aplicadas a las experiencias de MAX.</em></p>
</div>

### 4.2.2. Labeling Systems

Las etiquetas utilizan términos relacionados con las tareas del consultorio. Los nombres de sección anticipan su contenido y los verbos de acción indican la operación disponible.

| Experiencia | Etiqueta | Significado |
| --- | --- | --- |
| Landing | Inicio | Presentación principal de MAX. |
| Landing | Nosotros | Información sobre la iniciativa. |
| Landing | Funcionalidades | Capacidades y beneficios del producto. |
| Landing | Misión y visión | Propósito y orientación de MAX. |
| Landing | Valores | Principios institucionales. |
| Landing | Contacto | Destino de contacto identificado en la navegación. |
| Landing | Ingresar a MAX | Acceso a la aplicación. |
| Web y mobile | Inicio | Resumen de la actividad del consultorio. |
| Web y mobile | Pacientes | Búsqueda y gestión de pacientes. |
| Web y mobile | Consultas | Información relacionada con citas y atención clínica. |
| Web y mobile | Estudios | Estudios y archivos asociados a pacientes. |
| Web | Perfil del Médico | Datos y opciones de cuenta. |
| Web | Configuración | Preferencias de presentación. |
| Web | Administrador | Gestión del límite de cuentas y perfiles. |
| Mobile | Agenda | Vista relacionada con citas. |
| Mobile | Atenciones | Vista relacionada con atenciones clínicas. |

Las acciones emplean etiquetas como Ingresar, Registrar, Guardar, Cancelar y Adjuntar. Los mensajes de estado explican la situación y, cuando corresponde, orientan hacia la siguiente acción.

<div align="center">
  <img src="assets/MAX-Labeling-Systems.png" alt="Sistema de etiquetas, iconos y acciones de MAX" width="1000">
  <p><em>Etiquetas utilizadas para identificar módulos, controles y estados.</em></p>
</div>

### 4.2.3. SEO Tags and Meta Tags

Se especifican títulos y metadatos para identificar el propósito de las páginas. La landing page comunica públicamente la propuesta de MAX; los módulos autenticados corresponden al entorno de trabajo del consultorio.

Los siguientes valores constituyen una propuesta para la versión en español. Deben contar con su equivalente en inglés y verificarse durante la implementación.

| Página | Title propuesto | Description propuesta |
| --- | --- | --- |
| Landing page | MAX - Atención médica organizada | MAX conecta médicos y pacientes mediante una plataforma para organizar citas y documentación médica. |
| Iniciar sesión | Iniciar sesión - MAX | Accede a MAX para gestionar la información y las actividades de tu consultorio. |
| Crear cuenta | Crear cuenta - MAX | Registra una cuenta para acceder a las herramientas de gestión del consultorio en MAX. |
| Inicio | Panel del consultorio - MAX | Consulta el resumen de pacientes, consultas, próximas citas y estudios del consultorio. |
| Pacientes | Gestión de pacientes - MAX | Organiza y localiza la información de los pacientes registrados en el consultorio. |
| Consultas | Consultas - MAX | Consulta la información de citas y atención clínica del consultorio. |
| Estudios | Estudios médicos - MAX | Organiza y localiza estudios y archivos asociados a los pacientes. |
| Perfil | Perfil del Médico - MAX | Consulta y actualiza los datos y opciones de tu cuenta. |
| Configuración | Configuración - MAX | Administra las preferencias de presentación de la aplicación. |
| Administrador | Administración de perfiles - MAX | Gestiona el límite de cuentas y consulta los perfiles registrados. |

| Metadato | Valor propuesto |
| --- | --- |
| Author | Equipo MAX |
| Keywords del landing | MAX, gestión de citas, documentación médica, médicos, pacientes |
| Keywords de la aplicación | MAX, consultorio, pacientes, consultas, estudios médicos |
| Viewport | `width=device-width, initial-scale=1.0` |
| Codificación | `UTF-8` |

<div align="center">
  <img src="assets/MAX-SEO-Meta-Tags.png" alt="Especificación propuesta de títulos y metadatos de MAX" width="1000">
  <p><em>Propuesta de metadatos; su presencia en el código requiere verificación.</em></p>
</div>

### 4.2.4. Searching Systems

Los controles de búsqueda se ubican dentro de los módulos que concentran registros. Sus criterios se relacionan con la identificación del paciente, el estudio o la fecha.

| Experiencia y módulo | Criterios de búsqueda |
| --- | --- |
| Web: Pacientes | Nombre y DNI. |
| Web: eliminación de paciente | Nombre o DNI. |
| Web: Consultas | Nombre y DNI. |
| Web: Estudios | Nombre o DNI y fecha. |
| Mobile: Pacientes | Nombre y DNI. |
| Mobile: Consultas | Nombre y DNI. |
| Mobile: Estudios | Buscar estudio y fecha. |

El diseño diferencia una búsqueda sin coincidencias de una condición previa no cumplida. Por ejemplo, no contar con pacientes registrados produce un mensaje distinto de no encontrar resultados para un filtro.

Las listas pobladas y los resultados adicionales representados en los diagramas describen el comportamiento esperado; las capturas originales muestran principalmente estados vacíos.

<div align="center">
  <img src="assets/MAX-Searching-Systems.png" alt="Sistemas de búsqueda y estados de resultados de MAX" width="1000">
  <p><em>Criterios de búsqueda, resultados y condiciones previas por módulo.</em></p>
</div>

### 4.2.5. Navigation Systems

MAX adapta la navegación al contexto de uso de cada experiencia.

| Experiencia | Navegación principal | Navegación complementaria |
| --- | --- | --- |
| Landing page | Menú superior de secciones. | Llamadas a la acción y enlaces del pie de página. |
| Aplicación web | Menú lateral de módulos. | Ventanas modales, acciones contextuales y opciones de sesión. |
| Aplicación móvil | Barra inferior con cuatro destinos. | Barra superior, pestañas y controles de cierre. |

La landing page permite recorrer sus secciones y acceder a la plataforma. La web mantiene el contexto del módulo durante las operaciones. En mobile, las pestañas Agenda y Atenciones añaden navegación local dentro de Consultas.

Los nodos de agrupación presentes en los mapas organizan la documentación. El contenido desplegado del menú superior móvil no forma parte de las capturas originales.

<div align="center">
  <img src="assets/MAX-Navigation-Landing.png" alt="Mapa de navegación de la landing page de MAX" width="1000">
  <p><em>Navegación de la landing page.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Navigation-Web.png" alt="Mapa de navegación de la aplicación web MAX" width="1000">
  <p><em>Navegación entre los módulos de la aplicación web.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Navigation-Mobile.png" alt="Mapa de navegación de la aplicación móvil MAX" width="1000">
  <p><em>Navegación principal y local de la aplicación móvil.</em></p>
</div>

## 4.3. Landing Page UI Design

La landing page presenta la propuesta de valor de MAX y orienta al visitante hacia el acceso a la plataforma.

El recorrido comienza con un mensaje sobre la organización de la atención médica. Continúa con información del producto, funcionalidades, misión, visión y valores. Las llamadas a la acción acompañan el recorrido, que finaliza con enlaces de navegación y contenido legal.

### 4.3.1. Landing Page Wireframe

Los wireframes representan la estructura y prioridad del contenido sin depender del acabado visual.

La versión de escritorio organiza la cabecera horizontalmente y distribuye la presentación principal en dos columnas. La propuesta para navegador móvil reorganiza los bloques verticalmente, conservando el mensaje principal y los accesos.

| Bloque | Propósito |
| --- | --- |
| Cabecera | Identificar la marca y facilitar la navegación. |
| Presentación principal | Comunicar la propuesta de valor y destacar el ingreso. |
| Nosotros | Explicar el propósito de la iniciativa. |
| Funcionalidades | Presentar las capacidades del producto. |
| Misión, visión y valores | Comunicar la orientación institucional. |
| Llamada final | Reforzar el acceso a MAX. |
| Pie de página | Reunir navegación y enlaces legales. |

<div align="center">
  <img src="assets/MAX-Landing-Wireframe-Desktop.png" alt="Wireframe de escritorio de la landing page MAX" width="1000">
  <p><em>Wireframe de la landing page para escritorio.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Landing-Wireframe-Mobile.png" alt="Wireframe propuesto de la landing page MAX para navegador móvil" width="420">
  <p><em>Propuesta de wireframe para navegador móvil.</em></p>
</div>

### 4.3.2. Landing Page Mock-up

Los mock-ups aplican la identidad visual sobre la estructura del landing. Utilizan fondos claros, títulos destacados, tarjetas redondeadas y botones azules.

El mensaje “Tu atención médica, organizada en un solo lugar” presenta la propuesta principal. El panel de citas y documentos que lo acompaña funciona como ilustración del beneficio comunicado; no constituye evidencia del funcionamiento de un portal de pacientes.

<div align="center">
  <img src="assets/MAX-Landing-Mockup-Desktop.png" alt="Mock-up de escritorio de la landing page MAX" width="1000">
  <p><em>Reconstrucción visual de la landing page para escritorio.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Landing-Mockup-Mobile.png" alt="Mock-up propuesto de la landing page MAX para navegador móvil" width="420">
  <p><em>Propuesta visual de la landing page para navegador móvil.</em></p>
</div>

**Inicio**

Presenta la propuesta de valor, los accesos principales y una composición ilustrativa relacionada con citas y documentación.

<div align="center">
  <img src="assets/MAX-Landing-Inicio.png" alt="Captura de la sección Inicio de la landing page MAX" width="1000">
  <p><em>Referencia de la sección Inicio.</em></p>
</div>

**Nosotros**

Explica el propósito de MAX y destaca la organización de citas y documentos como parte de una experiencia compartida entre médicos y pacientes.

<div align="center">
  <img src="assets/MAX-Landing-Nosotros.png" alt="Captura de la sección Nosotros de la landing page MAX" width="1000">
  <p><em>Referencia de la sección Nosotros.</em></p>
</div>

**Funcionalidades**

Agrupa los beneficios comunicados por el producto mediante tarjetas con títulos, iconos y descripciones breves.

<div align="center">
  <img src="assets/MAX-Landing-Funcionalidades.png" alt="Captura de funcionalidades de la landing page MAX" width="1000">
  <p><em>Referencia de la presentación de funcionalidades.</em></p>
</div>

**Misión y visión**

Presenta el propósito de facilitar la interacción entre médicos y pacientes y la aspiración de mejorar la experiencia de seguimiento de la atención.

<div align="center">
  <img src="assets/MAX-Landing-Mision-Vision.png" alt="Captura de misión y visión de MAX" width="1000">
  <p><em>Referencia de la sección Misión y visión.</em></p>
</div>

**Valores**

Expone los principios de innovación, seguridad, confianza, accesibilidad y responsabilidad.

<div align="center">
  <img src="assets/MAX-Landing-Valores.png" alt="Captura de los valores institucionales de MAX" width="1000">
  <p><em>Referencia de los valores institucionales.</em></p>
</div>

**Llamada a la acción**

El bloque final utiliza una superficie oscura y un botón destacado para reforzar el acceso a MAX.

<div align="center">
  <img src="assets/MAX-Landing-CTA.png" alt="Captura de la llamada final a la acción de MAX" width="1000">
  <p><em>Referencia de la llamada final a la acción.</em></p>
</div>

**Pie de página**

Reúne la identidad del producto, los destinos principales y los enlaces legales.

<div align="center">
  <img src="assets/MAX-Landing-Footer.png" alt="Captura del pie de página de la landing page MAX" width="1000">
  <p><em>Referencia del pie de página.</em></p>
</div>

## 4.4. Mobile Applications UX/UI Design

La experiencia móvil facilita el acceso del personal del consultorio a pacientes, consultas y estudios. Su diseño prioriza una navegación breve, formularios verticales y mensajes que expliquen el estado de la información.

Las referencias corresponden a Android. Los wireframes, mock-ups y flujos reconstruyen estas pantallas y documentan los comportamientos previstos.

### 4.4.1. Mobile Applications Wireframes

Los wireframes representan la distribución de controles, contenido y acciones. Incluyen autenticación, registro, inicio, búsqueda de pacientes, registro de pacientes, consultas y estudios.

<div align="center">
  <img src="assets/MAX-Mobile-Wireframes-Overview.png" alt="Vista general de los wireframes móviles de MAX" width="1000">
  <p><em>Conjunto de wireframes de la aplicación móvil.</em></p>
</div>

**Autenticación y registro**

Las pantallas organizan los campos de acceso, la creación de cuenta y los mensajes de validación. El estado de error mantiene visible la relación entre cada campo y su mensaje.

<div align="center">
  <img src="assets/MAX-Mobile-Wireframe-Login.png" alt="Wireframe móvil de inicio de sesión" width="300">
  <img src="assets/MAX-Mobile-Wireframe-Registro.png" alt="Wireframe móvil de creación de cuenta" width="300">
  <img src="assets/MAX-Mobile-Wireframe-Registro-Errores.png" alt="Wireframe móvil de errores de registro" width="300">
  <p><em>Wireframes de inicio de sesión, registro y validaciones.</em></p>
</div>

**Inicio y pacientes**

Inicio reúne indicadores y actividad del consultorio. Pacientes presenta filtros y un acceso al registro de una nueva persona.

<div align="center">
  <img src="assets/MAX-Mobile-Wireframe-Inicio.png" alt="Wireframe del inicio móvil de MAX" width="320">
  <img src="assets/MAX-Mobile-Wireframe-Pacientes.png" alt="Wireframe del módulo móvil de pacientes" width="320">
  <p><em>Wireframes de Inicio y Pacientes.</em></p>
</div>

**Registro de paciente**

El formulario agrupa información personal y médica. Las siguientes imágenes representan dos zonas de un mismo formulario con desplazamiento vertical.

<div align="center">
  <img src="assets/MAX-Mobile-Wireframe-Nuevo-Paciente.png" alt="Wireframe de información personal de nuevo paciente" width="320">
  <img src="assets/MAX-Mobile-Wireframe-Nuevo-Paciente-Medica.png" alt="Wireframe de información médica de nuevo paciente" width="320">
  <p><em>Wireframes del registro de paciente: información personal y médica.</em></p>
</div>

**Consultas y estudios**

Consultas incorpora las pestañas Agenda y Atenciones. Estudios presenta búsqueda y filtro de fecha. Ambos contemplan mensajes cuando no se cumple la condición de contar con pacientes registrados.

<div align="center">
  <img src="assets/MAX-Mobile-Wireframe-Consultas.png" alt="Wireframe móvil de Consultas" width="320">
  <img src="assets/MAX-Mobile-Wireframe-Estudios.png" alt="Wireframe móvil de Estudios" width="320">
  <p><em>Wireframes de Consultas y Estudios.</em></p>
</div>

### 4.4.2. Mobile Applications Wireflow Diagrams

Los wireflows relacionan los wireframes mediante acciones y transiciones. Cada diagrama corresponde a un objetivo del usuario.

| Código | Objetivo | Recorrido principal |
| --- | --- | --- |
| M01 | Acceder a la aplicación | Introducir credenciales y acceder a Inicio. |
| M02 | Crear cuenta | Completar el registro y revisar el resultado. |
| M03 | Consultar el resumen | Revisar indicadores y actualizar la información. |
| M04 | Registrar paciente | Completar información personal y médica y guardar. |
| M05 | Localizar paciente | Introducir criterios y revisar coincidencias. |
| M06 | Consultar citas o atenciones | Acceder a Consultas y seleccionar la vista correspondiente. |
| M07 | Localizar estudio | Aplicar búsqueda o fecha y revisar resultados. |

Los estados que no aparecen en las capturas originales se representan como propuestas de interacción.

<div align="center">
  <img src="assets/MAX-Mobile-Wireflow-M01.png" alt="Wireflow M01 para acceder a la aplicación móvil MAX" width="1000">
  <p><em>M01. Acceder a la aplicación móvil.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-Wireflow-M02.png" alt="Wireflow M02 para crear una cuenta móvil en MAX" width="1000">
  <p><em>M02. Crear una cuenta.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-Wireflow-M03.png" alt="Wireflow M03 para consultar el resumen móvil del consultorio" width="1000">
  <p><em>M03. Consultar el resumen del consultorio.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-Wireflow-M04.png" alt="Wireflow M04 para registrar un paciente desde mobile" width="1000">
  <p><em>M04. Registrar un paciente.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-Wireflow-M05.png" alt="Wireflow M05 para localizar un paciente desde mobile" width="1000">
  <p><em>M05. Localizar un paciente.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-Wireflow-M06.png" alt="Wireflow M06 para consultar citas o atenciones desde mobile" width="1000">
  <p><em>M06. Consultar citas o atenciones.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-Wireflow-M07.png" alt="Wireflow M07 para localizar un estudio desde mobile" width="1000">
  <p><em>M07. Localizar un estudio.</em></p>
</div>

### 4.4.3. Mobile Applications Mock-ups

Los mock-ups incorporan colores, jerarquías visuales, iconografía y estados de los componentes.

En las comparaciones siguientes, la primera imagen corresponde al mock-up reconstruido y la segunda a la captura original de referencia.

<div align="center">
  <img src="assets/MAX-Mobile-Mockups-Overview.png" alt="Vista general de los mock-ups móviles de MAX" width="1000">
  <p><em>Conjunto de mock-ups de la aplicación móvil.</em></p>
</div>

**Inicio de sesión**

Presenta correo, contraseña, control de visibilidad y acceso a la creación de cuenta. La composición conserva la identidad de MAX y destaca la acción Ingresar.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Login.png" alt="Mock-up móvil de inicio de sesión" width="320">
  <img src="assets/MAX-Mobile-Login.png" alt="Captura original del inicio de sesión móvil" width="320">
  <p><em>Inicio de sesión: mock-up y captura de referencia.</em></p>
</div>

**Creación de cuenta**

Solicita nombres, apellidos, correo, contraseña y confirmación. Las instrucciones de contraseña se presentan junto al campo correspondiente.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Registro.png" alt="Mock-up móvil de creación de cuenta" width="320">
  <img src="assets/MAX-Mobile-Registro.png" alt="Captura original de creación de cuenta móvil" width="320">
  <p><em>Creación de cuenta: mock-up y captura de referencia.</em></p>
</div>

**Validaciones del registro**

El estado de error combina bordes rojos y mensajes específicos. Permite reconocer qué datos requieren corrección antes de continuar.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Registro-Errores.png" alt="Mock-up de validaciones del registro móvil" width="320">
  <img src="assets/MAX-Mobile-Registro-Errores.png" alt="Captura original de errores del registro móvil" width="320">
  <p><em>Validaciones del registro: mock-up y captura de referencia.</em></p>
</div>

**Inicio**

El panel resume pacientes, próximas citas, consultas y estudios. También incluye áreas para próximas citas y atenciones recientes.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Inicio.png" alt="Mock-up del inicio móvil de MAX" width="320">
  <img src="assets/MAX-Mobile-Inicio.png" alt="Captura original del inicio móvil de MAX" width="320">
  <p><em>Inicio: mock-up y captura de referencia.</em></p>
</div>

**Pacientes**

El módulo incorpora filtros por nombre y DNI, acceso al registro y un área de resultados. El estado vacío explica cuando no existen coincidencias.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Pacientes.png" alt="Mock-up móvil del módulo Pacientes" width="320">
  <img src="assets/MAX-Mobile-Pacientes.png" alt="Captura original del módulo móvil Pacientes" width="320">
  <p><em>Pacientes: mock-up y captura de referencia.</em></p>
</div>

**Nuevo paciente: información personal**

Esta parte del formulario incluye identificación, fecha de nacimiento, sexo, datos de contacto, dirección y ocupación.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Nuevo-Paciente.png" alt="Mock-up móvil de información personal de un nuevo paciente" width="320">
  <img src="assets/MAX-Mobile-Nuevo-Paciente-Personal.png" alt="Captura original de información personal de un nuevo paciente" width="320">
  <p><em>Información personal: mock-up y captura de referencia.</em></p>
</div>

**Nuevo paciente: información médica**

La continuación del formulario reúne alergias, diagnóstico principal, antecedentes, nota inicial y riesgo. Las acciones Guardar y Cancelar se presentan al final.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Nuevo-Paciente-Medica.png" alt="Mock-up móvil de información médica de un nuevo paciente" width="320">
  <img src="assets/MAX-Mobile-Nuevo-Paciente-Medica.png" alt="Captura original de información médica de un nuevo paciente" width="320">
  <p><em>Información médica: mock-up y captura de referencia.</em></p>
</div>

**Consultas**

La pantalla organiza el contenido mediante Agenda y Atenciones. Cuando no existen pacientes, explica esta condición antes de permitir continuar con registros asociados.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Consultas.png" alt="Mock-up móvil del módulo Consultas" width="320">
  <img src="assets/MAX-Mobile-Consultas.png" alt="Captura original del módulo móvil Consultas" width="320">
  <p><em>Consultas: mock-up y captura de referencia.</em></p>
</div>

**Estudios**

Presenta búsqueda y filtro por fecha. El estado inicial informa que todo estudio debe asociarse a un paciente.

<div align="center">
  <img src="assets/MAX-Mobile-Mockup-Estudios.png" alt="Mock-up móvil del módulo Estudios" width="320">
  <img src="assets/MAX-Mobile-Estudios.png" alt="Captura original del módulo móvil Estudios" width="320">
  <p><em>Estudios: mock-up y captura de referencia.</em></p>
</div>

### 4.4.4. Mobile Applications User Flow Diagrams

Los user flows relacionan los mock-ups con las decisiones necesarias para alcanzar cada objetivo. Incluyen el recorrido principal, las alternativas y los retornos para corregir información.

| Código | Resultado esperado | Alternativas consideradas |
| --- | --- | --- |
| M01 | Acceso al inicio de la aplicación. | Corregir credenciales inválidas. |
| M02 | Registro de cuenta completado. | Completar campos y corregir validaciones. |
| M03 | Consulta de indicadores y actividad. | Visualizar estados sin actividad registrada. |
| M04 | Paciente registrado. | Corregir datos o cancelar. |
| M05 | Paciente localizado. | Modificar criterios sin coincidencias. |
| M06 | Consulta de citas o atenciones. | Registrar previamente un paciente cuando sea necesario. |
| M07 | Estudio localizado. | Modificar filtros o resolver la falta de pacientes. |

Las rutas describen el comportamiento de diseño. Los estados de éxito y las listas de ejemplo no constituyen pruebas de ejecución.

<div align="center">
  <img src="assets/MAX-Mobile-UserFlow-M01.png" alt="User flow móvil M01 para iniciar sesión" width="1000">
  <p><em>M01. Acceso y corrección de credenciales.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-UserFlow-M02.png" alt="User flow móvil M02 para crear una cuenta" width="1000">
  <p><em>M02. Creación de cuenta y validación de datos.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-UserFlow-M03.png" alt="User flow móvil M03 para consultar el resumen del consultorio" width="1000">
  <p><em>M03. Consulta del resumen y estados de actividad.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-UserFlow-M04.png" alt="User flow móvil M04 para registrar un paciente" width="1000">
  <p><em>M04. Registro, corrección y cancelación de datos del paciente.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-UserFlow-M05.png" alt="User flow móvil M05 para buscar pacientes" width="1000">
  <p><em>M05. Búsqueda de pacientes y ausencia de coincidencias.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-UserFlow-M06.png" alt="User flow móvil M06 para consultar citas o atenciones" width="1000">
  <p><em>M06. Consulta de agenda y atenciones con sus condiciones previas.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Mobile-UserFlow-M07.png" alt="User flow móvil M07 para buscar estudios" width="1000">
  <p><em>M07. Búsqueda de estudios y revisión de resultados.</em></p>
</div>

## 4.5. Mobile Applications Prototyping

El prototipado móvil conecta las pantallas para representar tareas completas. Los mapas incluidos documentan los destinos y las transiciones que deben configurarse en el prototipo interactivo.

Los objetivos de revisión comprenden autenticación, creación de cuenta, consulta del resumen, registro y búsqueda de pacientes, consulta de agenda y localización de estudios.

### 4.5.1. Android Mobile Applications Prototyping

El mapa de Android se basa en las pantallas proporcionadas y organiza los recorridos M01–M07. Incluye transiciones principales y estados que requieren validación o cumplimiento de una condición previa.

Las pantallas móviles para crear consultas o cargar estudios no forman parte de las capturas disponibles. Por ello, no se presentan como funcionalidades demostradas mediante este mapa.

<div align="center">
  <img src="assets/MAX-Android-Prototyping-Map.png" alt="Mapa de prototipado de MAX para Android" width="1000">
  <p><em>Mapa visual de conexiones previstas para el prototipo Android.</em></p>
</div>

**Estado de la evidencia:** mapa visual disponible. Pendientes de incorporar el enlace al prototipo interactivo y el video de demostración en Microsoft Stream.

### 4.5.2. iOS Mobile Applications Prototyping

El mapa para iOS propone adaptar los mismos objetivos funcionales a esta plataforma, conservando la organización de módulos y revisando navegación, áreas reservadas y comportamiento de formularios.

La lámina representa una propuesta de prototipado. La interacción y la presentación específica en iOS requieren validación independiente.

<div align="center">
  <img src="assets/MAX-iOS-Prototyping-Map.png" alt="Mapa propuesto de prototipado de MAX para iOS" width="1000">
  <p><em>Propuesta de conexiones para el prototipo iOS.</em></p>
</div>

**Estado de la evidencia:** mapa visual propuesto. Pendientes de incorporar el prototipo interactivo, la validación en iOS y el video de demostración en Microsoft Stream.

## 4.6. Web Applications UX/UI Design

La aplicación web concentra las operaciones de gestión del consultorio. Su estructura permite acceder a pacientes, consultas, estudios, perfil, configuración y administración desde un menú lateral.

El diseño utiliza tarjetas para resúmenes, filtros para localizar registros y ventanas modales para tareas específicas. Las referencias muestran la aplicación de escritorio en tema oscuro; las variantes para navegador móvil son propuestas responsive.

### 4.6.1. Web Applications Wireframes

Los wireframes documentan la jerarquía y distribución de las pantallas. Permiten revisar los campos, las acciones y las relaciones entre áreas antes de considerar el acabado visual.

<div align="center">
  <img src="assets/MAX-Web-Wireframes-Overview.png" alt="Vista general de los wireframes web de MAX" width="1000">
  <p><em>Conjunto de wireframes de la aplicación web.</em></p>
</div>

**Inicio de sesión y registro**

Las pantallas de acceso organizan la presentación de MAX y los formularios de autenticación o creación de cuenta.

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Login.png" alt="Wireframe web de inicio de sesión" width="1000">
  <p><em>Wireframe de inicio de sesión.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Registro.png" alt="Wireframe web de creación de cuenta" width="1000">
  <p><em>Wireframe de creación de cuenta.</em></p>
</div>

**Inicio**

El panel agrupa indicadores, próximas citas y actividad reciente dentro de la estructura general de navegación.

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Inicio.png" alt="Wireframe del inicio web de MAX" width="1000">
  <p><em>Wireframe del resumen del consultorio.</em></p>
</div>

**Pacientes**

El módulo reúne filtros y acciones de gestión. El registro utiliza campos agrupados; la eliminación dispone de un espacio específico para localizar al paciente.

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Pacientes.png" alt="Wireframe web del módulo Pacientes" width="1000">
  <p><em>Wireframe del módulo Pacientes.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Nuevo-Paciente.png" alt="Wireframe web de registro de paciente" width="1000">
  <p><em>Wireframe del formulario de nuevo paciente.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Eliminar-Paciente.png" alt="Wireframe web de búsqueda para eliminar paciente" width="1000">
  <p><em>Wireframe del acceso a la eliminación de pacientes.</em></p>
</div>

**Consultas**

La vista presenta filtros y el área correspondiente a la agenda de citas.

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Consultas.png" alt="Wireframe web del módulo Consultas" width="1000">
  <p><em>Wireframe del módulo Consultas.</em></p>
</div>

**Estudios**

El módulo incluye filtros y una acción para adjuntar estudios. El formulario de registro organiza la asociación con el paciente, la consulta opcional y el archivo.

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Estudios.png" alt="Wireframe web del módulo Estudios" width="1000">
  <p><em>Wireframe del módulo Estudios.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Registrar-Estudio.png" alt="Wireframe web del formulario de registro de estudio" width="1000">
  <p><em>Wireframe del formulario para registrar un estudio.</em></p>
</div>

**Perfil y contraseña**

El perfil agrupa datos personales y opciones de cuenta. El cambio de contraseña se desarrolla en una ventana específica.

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Perfil-Medico.png" alt="Wireframe web del perfil del médico" width="1000">
  <p><em>Wireframe del Perfil del Médico.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Cambiar-Contrasena.png" alt="Wireframe web del cambio de contraseña" width="1000">
  <p><em>Wireframe del cambio de contraseña.</em></p>
</div>

**Configuración y administración**

Configuración reúne preferencias de presentación. Administrador contiene controles relacionados con el límite de cuentas y los perfiles registrados.

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Configuracion.png" alt="Wireframe web de Configuración" width="1000">
  <p><em>Wireframe del módulo Configuración.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Administrador.png" alt="Wireframe web de Administrador" width="1000">
  <p><em>Wireframe del módulo Administrador.</em></p>
</div>

**Adaptación responsive**

Las propuestas de Inicio y Pacientes para navegador móvil reorganizan los controles y el contenido en una distribución vertical.

<div align="center">
  <img src="assets/MAX-Web-Wireframe-Responsive-Inicio.png" alt="Wireframe responsive del inicio web en navegador móvil" width="380">
  <img src="assets/MAX-Web-Wireframe-Responsive-Pacientes.png" alt="Wireframe responsive de pacientes web en navegador móvil" width="380">
  <p><em>Propuestas responsive de Inicio y Pacientes para navegador móvil.</em></p>
</div>

### 4.6.2. Web Applications Wireflow Diagrams

Los wireflows muestran los cambios de pantalla o estado necesarios para completar los objetivos de la experiencia web.

| Código | Objetivo | Recorrido principal |
| --- | --- | --- |
| W01 | Acceder al panel | Ingresar credenciales y acceder a Inicio. |
| W02 | Crear cuenta | Completar datos y enviar el registro. |
| W03 | Registrar paciente | Abrir el formulario, completar datos y guardar. |
| W04 | Localizar paciente | Aplicar filtros y revisar coincidencias. |
| W05 | Eliminar paciente | Buscar, seleccionar y confirmar la eliminación propuesta. |
| W06 | Consultar citas | Acceder a Consultas y aplicar criterios. |
| W07 | Registrar estudio | Seleccionar paciente, completar información y adjuntar archivo. |
| W08 | Localizar estudio | Aplicar filtros de identificación o fecha. |
| W09 | Actualizar perfil | Modificar datos y revisar el resultado esperado. |
| W10 | Cambiar contraseña | Completar las contraseñas y validar los datos. |
| W11 | Ajustar preferencias | Seleccionar opciones de presentación. |
| W12 | Gestionar límite de cuentas | Modificar el límite y revisar su estado. |
| W13 | Cerrar sesión | Finalizar la sesión y regresar al acceso. |

Las capturas originales no documentan todas las transiciones. Los estados adicionales representan la interacción propuesta.

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W01.png" alt="Wireflow web W01 para acceder al panel" width="1000">
  <p><em>W01. Acceder al panel.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W02.png" alt="Wireflow web W02 para crear cuenta" width="1000">
  <p><em>W02. Crear cuenta.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W03.png" alt="Wireflow web W03 para registrar paciente" width="1000">
  <p><em>W03. Registrar paciente.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W04.png" alt="Wireflow web W04 para localizar paciente" width="1000">
  <p><em>W04. Localizar paciente.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W05.png" alt="Wireflow web W05 para eliminar paciente" width="1000">
  <p><em>W05. Eliminar paciente.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W06.png" alt="Wireflow web W06 para consultar citas" width="1000">
  <p><em>W06. Consultar citas.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W07.png" alt="Wireflow web W07 para registrar estudio" width="1000">
  <p><em>W07. Registrar estudio.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W08.png" alt="Wireflow web W08 para localizar estudio" width="1000">
  <p><em>W08. Localizar estudio.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W09.png" alt="Wireflow web W09 para actualizar perfil" width="1000">
  <p><em>W09. Actualizar perfil.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W10.png" alt="Wireflow web W10 para cambiar contraseña" width="1000">
  <p><em>W10. Cambiar contraseña.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W11.png" alt="Wireflow web W11 para ajustar preferencias" width="1000">
  <p><em>W11. Ajustar preferencias.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W12.png" alt="Wireflow web W12 para gestionar el límite de cuentas" width="1000">
  <p><em>W12. Gestionar el límite de cuentas.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-Wireflow-W13.png" alt="Wireflow web W13 para cerrar sesión" width="1000">
  <p><em>W13. Cerrar sesión.</em></p>
</div>

### 4.6.3. Web Applications Mock-ups

Los mock-ups desarrollan el acabado visual de las pantallas web mediante fondos oscuros, tarjetas, iconografía y acciones diferenciadas.

En cada comparación, la primera imagen corresponde al mock-up reconstruido y la segunda a la captura original. Las vistas responsive se presentan como propuestas.

<div align="center">
  <img src="assets/MAX-Web-Mockups-Overview.png" alt="Vista general de los mock-ups web de MAX" width="1000">
  <p><em>Conjunto de mock-ups de la aplicación web.</em></p>
</div>

**Inicio de sesión**

La pantalla combina la presentación de MAX con el formulario de acceso. Destaca los campos de credenciales y la acción principal.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Login.png" alt="Mock-up web de inicio de sesión" width="1000">
  <img src="assets/MAX-Web-Login.png" alt="Captura original del inicio de sesión web" width="1000">
  <p><em>Inicio de sesión: mock-up y captura de referencia.</em></p>
</div>

**Creación de cuenta**

El registro agrupa los datos necesarios para crear una cuenta y mantiene una composición coherente con el inicio de sesión.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Registro.png" alt="Mock-up web de creación de cuenta" width="1000">
  <img src="assets/MAX-Web-Registro.png" alt="Captura original de creación de cuenta web" width="1000">
  <p><em>Creación de cuenta: mock-up y captura de referencia.</em></p>
</div>

**Inicio**

El panel presenta indicadores del consultorio y áreas de actividad. Los estados vacíos comunican cuando todavía no existen registros.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Inicio.png" alt="Mock-up del inicio web de MAX" width="1000">
  <img src="assets/MAX-Web-Inicio.png" alt="Captura original del inicio web de MAX" width="1000">
  <p><em>Inicio: mock-up y captura de referencia.</em></p>
</div>

**Pacientes**

El módulo reúne filtros por nombre y DNI, acceso al registro y acceso a la eliminación de pacientes.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Pacientes.png" alt="Mock-up web del módulo Pacientes" width="1000">
  <img src="assets/MAX-Web-Pacientes.png" alt="Captura original del módulo web Pacientes" width="1000">
  <p><em>Pacientes: mock-up y captura de referencia.</em></p>
</div>

**Nuevo paciente**

El formulario organiza los datos personales y médicos. Las acciones de guardar y cancelar permiten finalizar o abandonar la operación.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Nuevo-Paciente.png" alt="Mock-up web del registro de nuevo paciente" width="1000">
  <img src="assets/MAX-Web-Nuevo-Paciente.png" alt="Captura original del registro web de nuevo paciente" width="1000">
  <p><em>Nuevo paciente: mock-up y captura de referencia.</em></p>
</div>

**Eliminar paciente**

La interfaz original presenta una advertencia y controles para localizar al paciente. La selección y confirmación posteriores se desarrollan como estados propuestos en los diagramas de flujo.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Eliminar-Paciente.png" alt="Mock-up web de eliminación de paciente" width="1000">
  <img src="assets/MAX-Web-Eliminar-Paciente.png" alt="Captura original de la búsqueda para eliminar paciente" width="1000">
  <p><em>Acceso a la eliminación de pacientes: mock-up y captura de referencia.</em></p>
</div>

**Consultas**

El módulo presenta la agenda y filtros de identificación. La referencia incluye un estado sin citas programadas.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Consultas.png" alt="Mock-up web del módulo Consultas" width="1000">
  <img src="assets/MAX-Web-Consultas.png" alt="Captura original del módulo web Consultas" width="1000">
  <p><em>Consultas: mock-up y captura de referencia.</em></p>
</div>

**Estudios**

La pantalla ofrece filtros por identificación y fecha, además del acceso para adjuntar un estudio.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Estudios.png" alt="Mock-up web del módulo Estudios" width="1000">
  <img src="assets/MAX-Web-Estudios.png" alt="Captura original del módulo web Estudios" width="1000">
  <p><em>Estudios: mock-up y captura de referencia.</em></p>
</div>

**Registrar estudio**

El formulario permite seleccionar un paciente, indicar una consulta asociada cuando corresponda, definir el tipo de estudio, añadir una descripción y seleccionar un archivo.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Registrar-Estudio.png" alt="Mock-up web del registro de estudio" width="1000">
  <img src="assets/MAX-Web-Registrar-Estudio.png" alt="Captura original del registro web de estudio" width="1000">
  <p><em>Registro de estudio: mock-up y captura de referencia.</em></p>
</div>

**Perfil del Médico**

El perfil agrupa datos de la cuenta, imagen, preferencias e información de sesión. También presenta accesos relacionados con la contraseña y el cierre de sesión.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Perfil-Medico.png" alt="Mock-up web del Perfil del Médico" width="1000">
  <img src="assets/MAX-Web-Perfil-Medico.png" alt="Captura original del Perfil del Médico" width="1000">
  <p><em>Perfil del Médico: mock-up y captura de referencia.</em></p>
</div>

**Cambiar contraseña**

La ventana solicita la contraseña actual, la nueva contraseña y su confirmación. Las instrucciones permiten reconocer las condiciones esperadas para la entrada.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Cambiar-Contrasena.png" alt="Mock-up web del cambio de contraseña" width="1000">
  <img src="assets/MAX-Web-Cambiar-Contrasena.png" alt="Captura original del cambio de contraseña web" width="1000">
  <p><em>Cambio de contraseña: mock-up y captura de referencia.</em></p>
</div>

**Configuración**

La pantalla presenta opciones de idioma, tema, tamaño de texto y notificaciones, además de información del sistema. La presencia visual de estos controles no verifica por sí sola su funcionamiento.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Configuracion.png" alt="Mock-up web del módulo Configuración" width="1000">
  <img src="assets/MAX-Web-Configuracion.png" alt="Captura original del módulo web Configuración" width="1000">
  <p><em>Configuración: mock-up y captura de referencia.</em></p>
</div>

**Administrador**

El módulo muestra controles para el límite de cuentas y un área de perfiles. El acceso efectivo a estas operaciones debe corresponder a los permisos definidos en la implementación.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Administrador.png" alt="Mock-up web del módulo Administrador" width="1000">
  <img src="assets/MAX-Web-Administrador.png" alt="Captura original del módulo web Administrador" width="1000">
  <p><em>Administrador: mock-up y captura de referencia.</em></p>
</div>

**Versión responsive**

Las siguientes propuestas adaptan Inicio y Pacientes a un navegador móvil. Conservan las funciones principales y reorganizan la presentación para un ancho reducido.

<div align="center">
  <img src="assets/MAX-Web-Mockup-Responsive-Inicio.png" alt="Mock-up responsive del inicio web para navegador móvil" width="380">
  <img src="assets/MAX-Web-Mockup-Responsive-Pacientes.png" alt="Mock-up responsive de pacientes web para navegador móvil" width="380">
  <p><em>Propuestas responsive de Inicio y Pacientes.</em></p>
</div>

### 4.6.4. Web Applications User Flow Diagrams

Los user flows presentan las decisiones y los resultados esperados para cada objetivo web. Utilizan los mock-ups para relacionar la lógica de interacción con las pantallas correspondientes.

Las rutas principales conducen al resultado esperado. Las alternativas consideran validaciones, ausencia de coincidencias, cancelaciones y retornos para corregir información.

| Código | Objetivo | Alternativas o condiciones consideradas |
| --- | --- | --- |
| W01 | Acceder al panel | Credenciales inválidas y corrección. |
| W02 | Crear cuenta | Campos incompletos o datos inválidos. |
| W03 | Registrar paciente | Corrección de información o cancelación. |
| W04 | Localizar paciente | Búsqueda sin coincidencias. |
| W05 | Eliminar paciente | Ausencia de coincidencias y cancelación de la confirmación. |
| W06 | Consultar citas | Ausencia de citas o resultados. |
| W07 | Registrar estudio | Revisión del paciente, datos y archivo requerido. |
| W08 | Localizar estudio | Modificación de filtros sin coincidencias. |
| W09 | Actualizar perfil | Corrección de datos. |
| W10 | Cambiar contraseña | Datos inválidos o confirmación no coincidente. |
| W11 | Ajustar preferencias | Selección o conservación de preferencias. |
| W12 | Gestionar límite de cuentas | Validación del valor propuesto. |
| W13 | Cerrar sesión | Retorno al acceso una vez finalizada la sesión. |

Los diagramas documentan la propuesta de interacción. Su validación funcional debe realizarse sobre el prototipo interactivo o la aplicación.

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W01.png" alt="User flow web W01 para acceder al panel" width="1000">
  <p><em>W01. Acceso al panel y validación de credenciales.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W02.png" alt="User flow web W02 para crear cuenta" width="1000">
  <p><em>W02. Creación de cuenta y corrección de datos.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W03.png" alt="User flow web W03 para registrar paciente" width="1000">
  <p><em>W03. Registro de paciente y alternativas de corrección o cancelación.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W04.png" alt="User flow web W04 para localizar paciente" width="1000">
  <p><em>W04. Búsqueda de pacientes y revisión de coincidencias.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W05.png" alt="User flow web W05 para eliminar paciente" width="1000">
  <p><em>W05. Búsqueda, selección y confirmación propuesta de eliminación.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W06.png" alt="User flow web W06 para consultar citas" width="1000">
  <p><em>W06. Consulta de agenda y estados sin resultados.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W07.png" alt="User flow web W07 para registrar estudio" width="1000">
  <p><em>W07. Registro de estudio y validación de información y archivo.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W08.png" alt="User flow web W08 para localizar estudio" width="1000">
  <p><em>W08. Búsqueda de estudios mediante filtros.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W09.png" alt="User flow web W09 para actualizar perfil" width="1000">
  <p><em>W09. Actualización del perfil y corrección de datos.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W10.png" alt="User flow web W10 para cambiar contraseña" width="1000">
  <p><em>W10. Cambio de contraseña y validaciones.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W11.png" alt="User flow web W11 para ajustar preferencias" width="1000">
  <p><em>W11. Ajuste de preferencias de presentación.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W12.png" alt="User flow web W12 para gestionar el límite de cuentas" width="1000">
  <p><em>W12. Gestión del límite de cuentas y validación del valor.</em></p>
</div>

<div align="center">
  <img src="assets/MAX-Web-UserFlow-W13.png" alt="User flow web W13 para cerrar sesión" width="1000">
  <p><em>W13. Cierre de sesión y retorno al acceso.</em></p>
</div>

## 4.7. Web Applications Prototyping

El prototipado web conecta las pantallas para representar los recorridos W01–W13. Permite revisar la continuidad entre acceso, navegación, formularios, validaciones y resultados esperados.

El mapa organiza los destinos principales y las operaciones asociadas a pacientes, consultas, estudios, perfil, configuración y administración.

<div align="center">
  <img src="assets/MAX-Web-Prototyping-Map.png" alt="Mapa de prototipado de la aplicación web MAX" width="1000">
  <p><em>Mapa visual de conexiones previstas para el prototipo web.</em></p>
</div>

La evaluación del prototipo interactivo deberá considerar:

- Acceso a los módulos y reconocimiento de la sección seleccionada.
- Continuidad de los formularios de registro.
- Comprensión de validaciones, estados vacíos y resultados.
- Cancelación de operaciones y retorno al contexto anterior.
- Confirmación de las acciones de eliminación.
- Uso de las propuestas responsive desde un navegador móvil.
- Finalización de sesión y retorno a la pantalla de acceso.

Las láminas constituyen la base visual para configurar estas interacciones en la herramienta de prototipado. No demuestran por sí solas persistencia de datos, permisos ni ejecución de operaciones.

**Estado de la evidencia:** mapa visual y diseños de pantallas disponibles. Pendientes de incorporar el enlace al prototipo interactivo para escritorio y navegador móvil, junto con el video de demostración en Microsoft Stream.
