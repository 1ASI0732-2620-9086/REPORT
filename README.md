<div align="center">
  <img src="assets/logo_upc.png" alt="Logo UPC" width="300">
  <br>
  <h3>Universidad Peruana de Ciencias Aplicadas</h3>
  <h4>Facultad de Ingeniería</h4>
  <h4>Carrera de Ingeniería de Software</h4>
  <br>
  <h4>Ciclo 2026-20</h4>
  <br>
  <h4>1ASI0732 - Diseño de Experimentos de Ingeniería de Software</h4>
  <h4>NRC: 2620</h4>
  <h4>Profesor: Julio Manuel Noriega Melendez</h4>
  <br>
  <h2>Informe de Trabajo Final</h2>
  <br>
  <h3>Startup: [Nuevo Nombre de la Startup]</h3>
  <h3>Producto: [Nuevo Nombre del Producto]</h3>
  <br>
  <h4>Integrantes:</h4>
  <ul style="list-style-type: none; padding: 0;">
    <li>U202311828 - Landauri Preciado, Stephano Mayrzon</li>
    <li>U202311842 - Quijandria Espinoza, Oscar Leonardo</li>
    <li>[Código 3] - [Apellidos, Nombres 3]</li>
  </ul>
  <br>
  <h4>Septiembre, 2026</h4>
</div>

---

## Registro de Versiones del Informe

| Versión | Fecha | Autor | Descripción de modificación |
|---------|-------|-------|-----------------------------|
| 1.0     | [Fecha] | [Autor] | Versión inicial del documento (Estructura base) |

---

## Project Report Collaboration Insights

URL del repositorio: `[URL del Repositorio de GitHub para el Informe]`

*(En esta sección se explicará cómo se han desarrollado las actividades de elaboración del informe y se presentarán capturas de los analíticos de colaboración y commits en GitHub).*

---

## Contenido

- [Registro de Versiones del Informe](#registro-de-versiones-del-informe)
- [Project Report Collaboration Insights](#project-report-collaboration-insights)
- [Contenido](#contenido)
- [Student Outcome](#student-outcome)
- [Capítulo I: Introducción](#capítulo-i-introducción)
  - [1.1. Startup Profile](#11-startup-profile)
    - [1.1.1. Descripción de la Startup](#111-descripción-de-la-startup)
    - [Misión](#misión)
    - [Visión](#visión)
    - [Valores](#valores)
    - [Objetivo General](#objetivo-general)
    - [Objetivos Específicos](#objetivos-específicos)
    - [1.1.2. Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
  - [1.2. Solution Profile](#12-solution-profile)
    - [1.2.1 Antecedentes y problemática](#121-antecedentes-y-problemática)
    - [Análisis 5W + 2H](#análisis-5w--2h)
    - [Referencias](#referencias)
    - [1.2.2 Lean UX Process](#122-lean-ux-process)
      - [1.2.2.1. Lean UX Problem Statements](#1221-lean-ux-problem-statements)
      - [1.2.2.2. Lean UX Assumptions](#1222-lean-ux-assumptions)
      - [1.2.2.3. Lean UX Hypothesis Statements](#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4. Lean UX Canvas](#1224-lean-ux-canvas)
  - [1.3. Segmentos objetivo](#13-segmentos-objetivo)
    - [Segmento 1: Médicos cirujanos](#segmento-1-médicos-cirujanos)
    - [Segmento 2: Pacientes](#segmento-2-pacientes)
- [Capítulo II: Requirements Elicitation & Analysis](#capítulo-ii-requirements-elicitation--analysis)
  - [2.1. Competidores](#21-competidores)
    - [2.1.1. Análisis competitivo](#211-análisis-competitivo)
    - [2.1.2. Estrategias y tácticas frente a competidores](#212-estrategias-y-tácticas-frente-a-competidores)
  - [2.2. Entrevistas](#22-entrevistas)
    - [2.2.1. Diseño de entrevistas](#221-diseño-de-entrevistas)
    - [Segmento 1: Médicos](#segmento-1-médicos)
    - [Segmento 2: Pacientes](#segmento-2-pacientes-1)
    - [2.2.2. Registro de entrevistas](#222-registro-de-entrevistas)
    - [Segmento 2: Pacientes](#segmento-2-pacientes-2)
      - [Entrevista 1](#entrevista-1)
      - [Entrevista 2](#entrevista-2)
    - [Segmento 1: Médicos](#segmento-1-médicos-1)
      - [Entrevista 1](#entrevista-1-1)
      - [Entrevista 2](#entrevista-2-1)
    - [2.2.3. Análisis de entrevistas](#223-análisis-de-entrevistas)
    - [Médicos](#médicos)
    - [Pacientes](#pacientes)
  - [2.3. Needfinding](#23-needfinding)
    - [2.3.1. User Personas](#231-user-personas)
    - [User Persona - Médico](#user-persona---médico)
    - [User Persona - Paciente](#user-persona---paciente)
    - [2.3.2. User Task Matrix](#232-user-task-matrix)
    - [2.3.3. User Journey Mapping](#233-user-journey-mapping)
    - [User Journey Mapping - Médico](#user-journey-mapping---médico)
    - [User Journey Mapping - Paciente](#user-journey-mapping---paciente)
    - [2.3.4. Empathy Mapping](#234-empathy-mapping)
    - [Empathy Mapping - Médico](#empathy-mapping---médico)
    - [Empathy Mapping - Paciente](#empathy-mapping---paciente)
    - [2.3.5. As-Is Scenario Mapping](#235-as-is-scenario-mapping)
    - [As-Is Scenario Mapping - Médico](#as-is-scenario-mapping---médico)
    - [As-Is Scenario Mapping - Paciente](#as-is-scenario-mapping---paciente)
  - [2.4. Ubiquitous Language](#24-ubiquitous-language)
- [Capítulo III: Requirements Specification](#capítulo-iii-requirements-specification)
  - [3.1. To-Be Scenario Mapping](#31-to-be-scenario-mapping)
  - [3.2. User Stories](#32-user-stories)
    - [Cuadro de Epics, User Stories y Technical Stories](#cuadro-de-epics-user-stories-y-technical-stories)
  - [EP-01: Gestión de Identidad y Acceso](#ep-01-gestión-de-identidad-y-acceso)
  - [EP-02: Gestión de Pacientes](#ep-02-gestión-de-pacientes)
  - [EP-03: Gestión de Placas y Estudios](#ep-03-gestión-de-placas-y-estudios)
  - [EP-04: Gestión de Consultas y Agenda Clínica](#ep-04-gestión-de-consultas-y-agenda-clínica)
  - [EP-05: Configuración y Preferencias del Sistema](#ep-05-configuración-y-preferencias-del-sistema)
  - [3.3. Product Backlog](#33-product-backlog)
    - [Distribución por entrega](#distribución-por-entrega)
    - [Distribución por Epic](#distribución-por-epic)
    - [Consideraciones sobre el orden](#consideraciones-sobre-el-orden)
  - [3.4. Impact Mapping](#34-impact-mapping)
    - [Business Goals SMART](#business-goals-smart)
    - [Actores considerados](#actores-considerados)
    - [Mapa de impacto](#mapa-de-impacto)
    - [Conclusión del Impact Mapping](#conclusión-del-impact-mapping)
- [Capítulo IV: Product Design](#capítulo-iv-product-design)
  - [4.1. Style Guidelines](#41-style-guidelines)
    - [4.1.1. General Style Guidelines](#411-general-style-guidelines)
    - [4.1.2. Web Style Guidelines](#412-web-style-guidelines)
    - [4.1.3. Mobile Style Guidelines](#413-mobile-style-guidelines)
      - [4.1.3.1. iOS Mobile Style Guidelines](#4131-ios-mobile-style-guidelines)
      - [4.1.3.2. Android Mobile Style Guidelines](#4132-android-mobile-style-guidelines)
  - [4.2. Information Architecture](#42-information-architecture)
    - [4.2.1. Organization Systems](#421-organization-systems)
    - [4.2.2. Labeling Systems](#422-labeling-systems)
    - [4.2.3. SEO Tags and Meta Tags](#423-seo-tags-and-meta-tags)
    - [4.2.4. Searching Systems](#424-searching-systems)
    - [4.2.5. Navigation Systems](#425-navigation-systems)
  - [4.3. Landing Page UI Design](#43-landing-page-ui-design)
    - [4.3.1. Landing Page Wireframe](#431-landing-page-wireframe)
    - [4.3.2. Landing Page Mock-up](#432-landing-page-mock-up)
  - [4.4. Mobile Applications UX/UI Design](#44-mobile-applications-uxui-design)
    - [4.4.1. Mobile Applications Wireframes](#441-mobile-applications-wireframes)
    - [4.4.2. Mobile Applications Wireflow Diagrams](#442-mobile-applications-wireflow-diagrams)
    - [4.4.3. Mobile Applications Mock-ups](#443-mobile-applications-mock-ups)
    - [4.4.4. Mobile Applications User Flow Diagrams](#444-mobile-applications-user-flow-diagrams)
  - [4.5. Mobile Applications Prototyping](#45-mobile-applications-prototyping)
    - [4.5.1. Android Mobile Applications Prototyping](#451-android-mobile-applications-prototyping)
    - [4.5.2. iOS Mobile Applications Prototyping](#452-ios-mobile-applications-prototyping)
  - [4.6. Web Applications UX/UI Design](#46-web-applications-uxui-design)
    - [4.6.1. Web Applications Wireframes](#461-web-applications-wireframes)
    - [4.6.2. Web Applications Wireflow Diagrams](#462-web-applications-wireflow-diagrams)
    - [4.6.3. Web Applications Mock-ups](#463-web-applications-mock-ups)
    - [4.6.4. Web Applications User Flow Diagrams](#464-web-applications-user-flow-diagrams)
  - [4.7. Web Applications Prototyping](#47-web-applications-prototyping)
    - [4.8. Domain-Driven Software Architecture](#48-domain-driven-software-architecture)
      - [4.8.1. Software Architecture Context Diagram](#481-software-architecture-context-diagram)
      - [4.8.2. Software Architecture Container Diagrams](#482-software-architecture-container-diagrams)
      - [4.8.3. Software Architecture Components Diagrams](#483-software-architecture-components-diagrams)
    - [4.9. Software Object-Oriented Design](#49-software-object-oriented-design)
      - [4.9.1. Class Diagrams](#491-class-diagrams)
      - [4.9.2. Class Dictionary](#492-class-dictionary)
    - [4.10. Database Design](#410-database-design)
      - [4.10.1. Relational/Non-Relational Database Diagrams](#4101-relationalnon-relational-database-diagrams)
- [Capítulo V: Product Implementation, Validation & Deployment](#capítulo-v-product-implementation-validation--deployment)
  - [5.1. Software Configuration Management](#51-software-configuration-management)
  - [Requirements Management](#requirements-management)
  - [Product UX/UI](#product-uxui)
  - [Software Development](#software-development)
  - [Software Documentation](#software-documentation)
    - [5.1.1. Software Development Environment Configuration](#511-software-development-environment-configuration)
    - [Landing Page](#landing-page)
    - [Backend](#backend)
    - [Base de Datos](#base-de-datos)
    - [Frontend Web Application](#frontend-web-application)
    - [Resumen del entorno de despliegue](#resumen-del-entorno-de-despliegue)
    - [5.1.2. Source Code Management](#512-source-code-management)
    - [Organización de repositorios](#organización-de-repositorios)
    - [Estrategia de Branching](#estrategia-de-branching)
    - [Gestión de commits](#gestión-de-commits)
    - [Integración y revisión de cambios](#integración-y-revisión-de-cambios)
    - [Relación entre Source Code Management y Deployment](#relación-entre-source-code-management-y-deployment)
    - [Trazabilidad del código fuente](#trazabilidad-del-código-fuente)
    - [5.1.3. Source Code Style Guide & Conventions](#513-source-code-style-guide--conventions)
    - [5.1.4. Software Deployment Configuration](#514-software-deployment-configuration)
    - [Deployment Architecture](#deployment-architecture)
    - [Landing Page Deployment](#landing-page-deployment)
    - [Frontend Deployment](#frontend-deployment)
    - [Backend Deployment](#backend-deployment)
    - [Database Deployment](#database-deployment)
    - [Deployment Workflow](#deployment-workflow)
    - [Environment Variables](#environment-variables)
    - [Deployment Summary](#deployment-summary)
    - [Production URLs](#production-urls)
  - [5.2. Product implementation & deployment](#52-product-implementation--deployment)
    - [5.2.1. Sprint 1](#521-sprint-1)
      - [5.2.1.1. Sprint Planning 1](#5211-sprint-planning-1)
      - [5.2.1.2. Aspect Leaders and Collaborators](#5212-aspect-leaders-and-collaborators)
      - [5.2.1.3. Sprint Backlog 1](#5213-sprint-backlog-1)
      - [5.2.1.4. Development Evidence for Sprint Review](#5214-development-evidence-for-sprint-review)
      - [5.2.1.5. Execution Evidence for Sprint Review](#5215-execution-evidence-for-sprint-review)
      - [5.2.1.6. Services Documentation Evidence for Sprint Review](#5216-services-documentation-evidence-for-sprint-review)
      - [5.2.1.7. Software Deployment Evidence for Sprint Review](#5217-software-deployment-evidence-for-sprint-review)
      - [5.2.1.8. Team Collaboration Insights during Sprint](#5218-team-collaboration-insights-during-sprint)
    - [5.2.2. Implemented Landing Page Evidence](#522-implemented-landing-page-evidence)
    - [5.2.3. Implemented Frontend-Web Application Evidence](#523-implemented-frontend-web-application-evidence)
    - [5.2.4. Implemented Native-Mobile Application Evidence](#524-implemented-native-mobile-application-evidence)
    - [5.2.5. Implemented RESTful API and/or Serverless Backend Evidence](#525-implemented-restful-api-andor-serverless-backend-evidence)
    - [5.2.6. RESTful API Documentation](#526-restful-api-documentation)
    - [5.2.7. Team Collaboration Insights](#527-team-collaboration-insights)
  - [5.3. Video About-the-Product](#53-video-about-the-product)
- [Conclusiones](#conclusiones)
  - [Conclusiones y recomendaciones](#conclusiones-y-recomendaciones)
  - [Video About-the-Team](#video-about-the-team)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)
  - [Anexo A. Videos de Exposiciones](#anexo-a-videos-de-exposiciones)

---

## Student Outcome
**ABET - EAC - Student Outcome 3**
**Criterio:** Capacidad de comunicarse efectivamente con un rango de audiencias.

El curso contribuye al cumplimiento del Student Outcome ABET. En el siguiente cuadro se describe las acciones realizadas y enunciados de conclusiones por parte del grupo, que permiten sustentar el haber alcanzado el logro.

| Criterio específico | Acciones realizadas | Conclusiones |
|---------------------|---------------------|--------------|
| **3.c1. Comunica oralmente sus ideas y/o resultados con objetividad a público de diferentes especialidades y niveles jerárquicos, en el marco del desarrollo de un proyecto en ingeniería de software.** | **Stephano Mayrzon Landauri**<br>AV1: Comunicó los avances y resultados correspondientes a los capítulos 1 y 2 y parte del capítulo 5, explicando la propuesta de MAX, la problemática identificada, los segmentos objetivo, el análisis competitivo, los resultados de las entrevistas, el Needfinding y aspectos relacionados con la gestión y configuración del proyecto.<br><br>**Oscar Leonardos Espinoza Quijandria**<br>AV1: Comunicó los aspectos técnicos relacionados con el despliegue de MAX, explicando la configuración y publicación de los diferentes componentes de la solución, incluyendo el Landing Page, Frontend, Backend y Base de Datos.<br><br>**Johnny Alexander Ojanama Abanto**<br>AV1: Comunicó los avances y resultados correspondientes al capítulo 3, explicando los requerimientos y especificaciones definidos para MAX y su relación con las funcionalidades planteadas para la solución. | Durante el AV1, el equipo fortaleció su capacidad para comunicar oralmente los avances y resultados del proyecto MAX de manera objetiva y organizada. Cada integrante presentó los aspectos correspondientes a su participación en el proyecto, permitiendo comunicar tanto elementos relacionados con la investigación y definición del producto como aspectos técnicos de requerimientos, desarrollo y despliegue. |
| **3.c2. Comunica en forma escrita ideas y/o resultados con objetividad a público de diferentes especialidades y niveles jerárquicos, en el marco del desarrollo de un proyecto de ingeniería de software.** | **Stephano Mayrzon Landauri**<br>AV1: Elaboró la documentación correspondiente a los capítulos 1 y 2 y parte del capítulo 5, incluyendo la definición de MAX, análisis de la problemática, Lean UX, segmentos objetivo, análisis competitivo, entrevistas, Needfinding y documentación relacionada con la gestión y configuración del proyecto.<br><br>**Oscar Leonardos Espinoza Quijandria**<br>AV1: Elaboró la documentación y evidencias relacionadas con la configuración y despliegue de los componentes de MAX, incluyendo el Landing Page, Frontend, Backend y Base de Datos.<br><br>**Johnny Alexander Ojanama Abanto**<br>AV1: Elaboró la documentación correspondiente al capítulo 3, estructurando los requerimientos y especificaciones de la solución de acuerdo con las necesidades identificadas para MAX. | Durante el AV1, el equipo desarrolló documentación técnica de manera clara, objetiva y estructurada. La distribución del trabajo permitió integrar en un mismo proyecto la investigación de usuarios, la definición de requerimientos y los aspectos técnicos de desarrollo y despliegue. El uso de Markdown y GitHub permitió mantener la información organizada y comprensible para diferentes tipos de audiencia. |

---

## Capítulo I: Introducción
### 1.1. Startup Profile
#### 1.1.1. Descripción de la Startup

Max es una startup tecnológica enfocada en mejorar la interacción entre médicos y pacientes mediante una plataforma digital. La solución busca centralizar la gestión de citas y documentos relacionados con la atención, como recetas, informes, resultados de exámenes y estudios médicos.

A través de la plataforma, los médicos podrán gestionar sus citas, pacientes y documentos, mientras que los pacientes podrán consultar sus citas y acceder de manera organizada a la información compartida por sus médicos.

#### Misión

Facilitar la interacción entre médicos y pacientes mediante una solución tecnológica que permita gestionar citas y documentación médica de manera organizada, accesible y segura.

#### Visión

Convertirse en una plataforma tecnológica reconocida por mejorar la experiencia y comunicación entre médicos y pacientes, ofreciendo soluciones innovadoras que faciliten el seguimiento de la atención médica.

#### Valores

Nuestros valores se basan en la **innovación**, buscando constantemente nuevas formas de mejorar la experiencia de médicos y pacientes mediante la tecnología; la **seguridad**, priorizando la protección de la información de los usuarios; la **confianza**, promoviendo una relación transparente entre médicos, pacientes y la plataforma; la **accesibilidad**, desarrollando una solución sencilla y fácil de utilizar; y la **responsabilidad**, considerando la sensibilidad de la información gestionada y el impacto que nuestra solución puede generar en sus usuarios.

#### Objetivo General

Desarrollar una plataforma digital que conecte a médicos y pacientes mediante la gestión centralizada de citas y documentación relacionada con la atención, facilitando el acceso y seguimiento de la información.

#### Objetivos Específicos

- Facilitar a los médicos la gestión de sus citas, pacientes y documentación.

- Permitir el intercambio organizado de recetas, informes, resultados y otros documentos entre médicos y pacientes.

- Facilitar a los pacientes la consulta de sus citas y documentación desde un único lugar.

- Implementar notificaciones que faciliten el seguimiento de citas y nueva información disponible.

- Incorporar mecanismos de autenticación y control de acceso para proteger la información gestionada por la plataforma.

- Recopilar métricas de uso que permitan evaluar funcionalidades y mejorar continuamente la experiencia de médicos y pacientes.

#### 1.1.2. Perfiles de integrantes del equipo

| Foto | Nombre completo | Código | Carrera | Habilidades técnicas y rol |
|:---:|---|---|---|---|
| <img src="assets/stephano_landauri.jpg" alt="Stephano Landauri Preciado" width="400"> | Stephano Mayrzon Landauri Preciado | U202311828 | Ingeniería de Software | Desarrollo Full Stack con React, TypeScript, JavaScript, Node.js y Express. Creación de APIs REST y manejo de SQLite, MySQL y MongoDB. Conocimientos en Git, GitHub, PWA, Capacitor, JWT y despliegue en Oracle Cloud. Aporta al análisis de las necesidades del usuario y promueve el trabajo colaborativo. |
| Por agregar | Johnny Alexander Ojanama Abanto | U20231F412 | Ingeniería de Software | Conocimientos en C++, MySQL, MongoDB y Python. Experiencia en desarrollo Frontend y Backend con tecnologías como Angular, Vue.js y Flutter. Conocimientos en DDD y su integración con Clean Architecture. Participa en la resolución de problemas y apoya al equipo ante contratiempos. |
| <img src="assets/oscar_espinoza.jpeg" alt="Oscar Leonardo Espinoza Quijandria" width="200"> | Oscar Leonardo Espinoza Quijandria | U202311842 | Ingeniería de Software | Conocimientos en programación orientada a objetos con C++, estructuras de datos y bases de datos SQL. Participación en el análisis de requerimientos, diseño de arquitectura con ADD, DDD, Clean Architecture y microservicios. Elaboración de diagramas y documentación técnica mediante Markdown, Git y GitHub. |

### 1.2. Solution Profile
#### 1.2.1 Antecedentes y problemática

En el Perú, la gestión de la información médica presenta dificultades debido a la fragmentación de los sistemas de salud y a la existencia de múltiples registros clínicos. Según Rojas-Mezarina, Cedamanos-Medina y Vargas-Herrera (2015), esta fragmentación puede ocasionar la pérdida de información valiosa del paciente al no contar con mecanismos adecuados para integrar sus diferentes historias clínicas. Asimismo, Huapaya-Huertas et al. (2021) destacan que la implementación de historias clínicas electrónicas permite mejorar la disponibilidad de la información y favorecer la continuidad de la atención.

Esta problemática evidencia la necesidad de soluciones digitales que faciliten la organización y disponibilidad de la información relacionada con la atención. Por ello, se propone una plataforma que conecte a médicos y pacientes, permitiendo gestionar citas y compartir de manera organizada recetas, informes, resultados de exámenes y otros documentos.

#### Análisis 5W + 2H

| Elemento | Descripción |
| --- | --- |
| **What? (¿Qué?)** | Fragmentación y dificultad para organizar y acceder a la información relacionada con la atención médica (Rojas-Mezarina et al., 2015). |
| **Why? (¿Por qué?)** | Debido a la existencia de diferentes registros y sistemas que dificultan integrar la información de un mismo paciente (Rojas-Mezarina et al., 2015). |
| **Who? (¿Quién?)** | Médicos y pacientes que necesitan consultar, gestionar o compartir información relacionada con la atención. |
| **Where? (¿Dónde?)** | En el contexto de los servicios de salud en el Perú (Rojas-Mezarina et al., 2015). |
| **When? (¿Cuándo?)** | Durante las consultas y el posterior seguimiento de la atención del paciente. |
| **How? (¿Cómo?)** | Mediante información distribuida en diferentes registros y documentos, dificultando su disponibilidad y continuidad (Huapaya-Huertas et al., 2021). |
| **How much? (¿Cuánto?)** | La fragmentación puede ocasionar pérdida de información relevante y afectar la continuidad de la atención (Rojas-Mezarina et al., 2015; Huapaya-Huertas et al., 2021). |

#### Referencias

Rojas-Mezarina, L., Cedamanos-Medina, C. A., & Vargas-Herrera, J. (2015). Registro nacional de historias clínicas electrónicas en Perú. *Revista Peruana de Medicina Experimental y Salud Pública, 32*(2), 395–396. 

Huapaya-Huertas, O., Palomino-Rojas, J., Calle-Texeira, C., Alvarez-Huiman, G., Montesinos-Segura, R., & Taype-Rondan, A. (2021). Experiencia del Complejo Hospitalario San Pablo (Perú) en la implementación de un sistema de historias clínicas electrónicas. *Anales de la Facultad de Medicina, 82*(4), 349–354. 

#### 1.2.2 Lean UX Process
##### 1.2.2.1. Lean UX Problem Statements

Los **médicos y pacientes** presentan dificultades para gestionar y acceder de manera organizada a la información relacionada con la atención médica. Por un lado, los médicos necesitan administrar sus citas y consultar o compartir documentos como recetas, informes y resultados de exámenes; por otro lado, los pacientes necesitan acceder fácilmente a sus citas y a la documentación proporcionada por sus médicos. La dispersión de esta información entre diferentes registros, documentos y medios digitales puede dificultar su consulta y el seguimiento de la atención.

**¿Cómo podríamos facilitar la interacción entre médicos y pacientes, permitiendo gestionar citas y acceder de manera organizada a la información relacionada con la atención médica desde un mismo entorno digital?**

##### 1.2.2.2. Lean UX Assumptions

**Business Assumptions**

- Creemos que los médicos necesitan una herramienta que les permita gestionar sus citas y la información de sus pacientes desde un mismo entorno.

- Creemos que los pacientes valorarán poder consultar sus citas, recetas, informes y resultados de manera organizada.

- Creemos que centralizar la interacción y documentación entre médicos y pacientes puede facilitar el seguimiento de la atención.

- Creemos que una plataforma web y móvil puede mejorar la accesibilidad a la información para ambos segmentos.

**User Assumptions**

- Creemos que los médicos tienen dificultades al gestionar información de sus pacientes mediante diferentes medios.

- Creemos que los pacientes tienen dificultades para mantener organizados sus documentos relacionados con la atención médica.

- Creemos que los pacientes necesitan acceder rápidamente a sus recetas, informes y resultados.

- Creemos que médicos y pacientes utilizarían una plataforma digital si esta es sencilla, accesible y segura.

- Creemos que los usuarios consideran importante recibir notificaciones sobre citas y nueva documentación disponible.

##### 1.2.2.3. Lean UX Hypothesis Statements

1. Creemos que centralizar las citas y documentos relacionados con la atención médica permitirá a médicos y pacientes acceder y gestionar su información de manera más organizada.

2. Creemos que enviar recordatorios de las próximas citas ayudará a los pacientes a realizar un mejor seguimiento de sus citas programadas.

3. Creemos que permitir a los pacientes consultar sus recetas, informes y resultados desde un único entorno facilitará el acceso a su información.

4. Creemos que permitir a los médicos compartir documentos directamente con sus pacientes facilitará el seguimiento de la atención.

5. Creemos que ofrecer una plataforma sencilla, accesible y organizada aumentará la disposición de médicos y pacientes a utilizarla.

##### 1.2.2.4. Lean UX Canvas

![Lean UX Canvas](assets/Lean_UX_Canvas.png)

### 1.3. Segmentos objetivo

#### Segmento 1: Médicos cirujanos

Este segmento está conformado por médicos cirujanos que atienden pacientes de manera presencial o virtual y que necesitan organizar sus citas, consultar información de sus pacientes y gestionar documentación relacionada con la atención.

Durante su actividad profesional, pueden generar y consultar recetas, informes médicos y otros documentos, además de recibir resultados de laboratorio, resonancias, estudios y archivos proporcionados por sus pacientes. La información puede encontrarse distribuida entre diferentes medios, dificultando su organización y consulta posterior.

MAX busca brindar a este segmento un entorno digital centralizado desde el cual puedan gestionar sus citas y pacientes, compartir documentación médica, recibir estudios o resultados y consultar información de atenciones anteriores.

**Principales necesidades:**

- Gestionar citas y disponibilidad de atención.

- Consultar información de sus pacientes.

- Generar y compartir recetas e informes médicos.

- Recibir resultados de laboratorio, resonancias y otros estudios.

- Consultar documentos relacionados con atenciones anteriores.

- Realizar seguimiento de los pacientes después de una consulta.

- Mantener organizada la información relacionada con cada atención.

- Contar con mecanismos de autenticación y control de acceso para proteger la información.

#### Segmento 2: Pacientes

Este segmento está conformado por personas que reciben atención médica y necesitan organizar sus citas y acceder a la documentación relacionada con sus atenciones.

Los pacientes pueden recibir recetas, informes, resultados de exámenes y otros documentos durante diferentes etapas de su atención. Asimismo, pueden necesitar compartir resultados de laboratorio, resonancias u otros estudios con sus médicos para continuar con su seguimiento.

MAX busca permitir que los pacientes consulten desde un mismo entorno sus citas y documentos, reciban recordatorios y compartan información con sus médicos de manera organizada.

**Principales necesidades:**

- Programar y consultar sus citas médicas.

- Recibir recordatorios de próximas citas.

- Consultar recetas e informes médicos.

- Acceder a resultados y estudios relacionados con sus atenciones.

- Consultar documentos de atenciones anteriores.

- Compartir resultados o estudios con su médico.

- Mantener organizada su documentación médica.

- Tener control sobre el acceso a su información.

---

## Capítulo II: Requirements Elicitation & Analysis
### 2.1. Competidores

Para identificar oportunidades de diferenciación de la solución se analizaron plataformas digitales que actualmente ofrecen servicios relacionados con la interacción entre médicos y pacientes. Se seleccionaron Doctoralia, Auna y SANNA debido a que presentan funcionalidades relacionadas con búsqueda de especialistas, gestión de citas, teleconsultas y acceso a información médica.

#### 2.1.1. Análisis competitivo

| Sección | Subcategoría | MAX | Doctoralia | Mi Auna | SANNA |
| --- | --- | --- | --- | --- | --- |
| **Perfil** | **Overview** | Plataforma digital orientada a conectar médicos y pacientes mediante la gestión de citas y la centralización de documentos relacionados con la atención, como recetas, informes, resultados de exámenes y estudios médicos. | Plataforma que conecta pacientes con profesionales de la salud, permitiendo buscar especialistas, revisar perfiles y opiniones, reservar citas y acceder a consultas online. | Plataforma digital del ecosistema Auna que permite a sus pacientes gestionar citas y acceder a diferentes servicios e información relacionada con su atención. | Plataforma perteneciente a la red SANNA que permite a los pacientes gestionar citas y acceder a servicios ofrecidos por sus establecimientos y profesionales. |
| **Ventaja competitiva** | **¿Qué valor ofrece a los clientes?** | Integra en un mismo entorno la gestión de citas y el intercambio organizado de documentación entre médicos y pacientes, incluyendo recetas, informes, resultados y estudios. | Facilita encontrar profesionales de diferentes especialidades, comparar perfiles y opiniones, reservar citas y comunicarse con especialistas. | Integra diferentes servicios de Auna en un mismo entorno, incluyendo citas, teleconsultas, recetas y resultados de laboratorio. | Facilita la gestión digital de citas dentro de la red SANNA y permite administrar la atención de familiares desde una misma cuenta. |
| **Perfil de Marketing** | **Mercado objetivo** | Médicos independientes o pertenecientes a pequeños consultorios y pacientes que necesitan gestionar citas y documentación relacionada con su atención. | Pacientes que buscan profesionales de la salud y médicos o especialistas que desean ofrecer sus servicios y gestionar citas mediante una plataforma digital. | Pacientes atendidos dentro de las clínicas, programas y servicios pertenecientes al ecosistema Auna. | Pacientes que utilizan los establecimientos, médicos y servicios pertenecientes a la red SANNA. |
| | **Estrategias de marketing** | Posicionamiento como plataforma sencilla para centralizar la relación médico-paciente, inicialmente enfocada en gestión de citas y documentación relacionada con la atención. | Posicionamiento como marketplace de profesionales de salud basado en disponibilidad, perfiles profesionales, opiniones de pacientes y facilidad para reservar citas. | Integración de servicios digitales con la red de establecimientos y programas de salud de Auna para mantener al paciente dentro de su ecosistema de atención. | Integración de la experiencia digital con los establecimientos y profesionales pertenecientes a la red SANNA. |
| **Perfil de Producto** | **Productos & Servicios** | Gestión de citas, agenda médica, perfiles de pacientes, recetas, informes, carga y consulta de resultados o estudios, repositorio de documentos, recordatorios y notificaciones. | Búsqueda de especialistas, perfiles profesionales, opiniones, reserva y gestión de citas, recordatorios, mensajería y consultas online. | Gestión de citas, historial de citas, teleconsultas, recetas, resultados de laboratorio, información de coberturas, sedes y pagos. | Agendamiento, pago y reprogramación de citas, búsqueda de médicos y gestión de familiares asociados a la cuenta. |
| | **Precios & Costos** | El MVP tendrá inicialmente acceso gratuito para médicos y pacientes con el objetivo de validar la propuesta. El modelo de monetización será evaluado posteriormente. | La búsqueda y reserva de citas no tiene costos añadidos para el paciente. El precio de las consultas depende del profesional y servicio seleccionado. | El acceso a Mi Auna funciona como parte del ecosistema de servicios de Auna; los costos dependen de las consultas, programas, coberturas y servicios contratados. | El acceso a la plataforma forma parte de los servicios digitales de SANNA; los costos dependen de las consultas y servicios médicos utilizados. |
| | **Canales de distribución (Web/Móvil)** | Landing Page, aplicación web para médicos y aplicación móvil para pacientes, de acuerdo con el alcance inicial del producto. | Plataforma web y aplicación móvil para pacientes, además de herramientas digitales destinadas a profesionales. | Plataforma web Mi Auna y aplicación móvil Auna. | Plataforma web de agendamiento y aplicación móvil SANNA. |
| **Análisis SWOT** | **Fortalezas** | Centralización de citas y documentos, intercambio de información entre médico y paciente, orientación tanto a médicos independientes como a pacientes y posibilidad de construir una experiencia específica para cada segmento. | Amplia cantidad de especialistas, sistema de opiniones, facilidad de reserva, recordatorios, consultas online y presencia consolidada en el mercado digital de salud. | Integración de citas, teleconsultas, recetas, resultados y otros servicios dentro de un ecosistema de salud establecido. | Integración con una red de establecimientos y profesionales, gestión digital de citas y posibilidad de administrar familiares. |
| | **Debilidades** | Producto nuevo sin una base inicial de médicos y pacientes. Su valor dependerá de conseguir participación de ambos segmentos y gestionar adecuadamente información sensible. | Su propuesta está principalmente orientada al descubrimiento de especialistas y gestión de consultas, por lo que la centralización longitudinal de documentos médicos entre diferentes profesionales no constituye su enfoque principal. | Su utilización está principalmente relacionada con pacientes y servicios pertenecientes al ecosistema Auna. | Su utilización está principalmente vinculada a profesionales, establecimientos y servicios pertenecientes a la red SANNA. |
| | **Oportunidades** | Incorporar médicos independientes y pequeños consultorios, validar nuevas funcionalidades mediante experimentos, mejorar el seguimiento posterior a las consultas e incorporar progresivamente nuevas herramientas de comunicación y gestión documental. | Ampliar herramientas digitales para profesionales y pacientes e integrar nuevas funcionalidades relacionadas con el seguimiento de la atención. | Continuar integrando servicios médicos digitales y ampliar la experiencia del paciente dentro de su ecosistema. | Ampliar los servicios disponibles digitalmente y mejorar la integración entre pacientes, profesionales y establecimientos de su red. |
| | **Amenazas** | Competencia de plataformas consolidadas, dificultad para generar una masa inicial de usuarios, requisitos de privacidad y seguridad de información sensible y posibilidad de que competidores incorporen funcionalidades similares. | Competencia de otras plataformas de salud y crecimiento de soluciones digitales ofrecidas directamente por clínicas y establecimientos médicos. | Competencia de otros grupos de salud y plataformas digitales independientes que permitan atenderse con profesionales de diferentes instituciones. | Competencia de otras redes privadas de salud y plataformas independientes con mayor variedad de profesionales y servicios digitales. |
#### 2.1.2. Estrategias y tácticas frente a competidores

A partir del análisis competitivo realizado, se desarrolla una matriz FODA y C.A.M.E. para establecer las estrategias que MAX puede aplicar frente a sus competidores. La matriz relaciona las fortalezas y debilidades internas de MAX con las oportunidades y amenazas identificadas en el mercado de plataformas digitales orientadas a la interacción entre médicos y pacientes.

| MATRIZ FODA y C.A.M.E. | Oportunidades: Crecimiento de los servicios digitales de salud, mayor adopción de herramientas para la gestión de citas y oportunidad de centralizar la interacción y documentación entre médicos y pacientes. | Amenazas: Competidores consolidados, plataformas propias de clínicas y redes de salud, requisitos relacionados con privacidad y seguridad de información sensible y aparición de funcionalidades similares. |
| --- | --- | --- |
| **Fortalezas:** Centralización de citas y documentos relacionados con la atención, intercambio de información entre médicos y pacientes, experiencia diferenciada para ambos segmentos y orientación inicial hacia médicos independientes y pacientes. | **Estrategia Ofensiva (F + O):** Aprovechar la centralización de citas y documentos para ofrecer una experiencia enfocada en la continuidad de la interacción entre médico y paciente. La orientación hacia médicos independientes permitirá ampliar progresivamente la adopción de MAX sin limitar la solución a una red clínica específica. | **Estrategia Defensiva (F + A):** Diferenciar MAX frente a Doctoralia, Mi Auna, SANNA y otras plataformas mediante la integración de gestión de citas, recetas, informes, resultados y otros documentos dentro de un mismo entorno. Asimismo, implementar mecanismos de autenticación, autorización y control de acceso que permitan proteger la información gestionada. |
| **Debilidades:** Bajo reconocimiento de marca, ausencia de una comunidad inicial de médicos y pacientes, producto nuevo y necesidad de generar confianza para que los usuarios gestionen información relacionada con su atención mediante la plataforma. | **Estrategia de Reorientación (D + O):** Concentrar inicialmente la adopción en médicos independientes y pacientes que necesiten organizar sus citas y documentos. Realizar entrevistas, pruebas de usabilidad y experimentos permitirá validar las funcionalidades de mayor valor antes de ampliar progresivamente el alcance de MAX. | **Estrategia de Supervivencia (D + A):** Limitar inicialmente el alcance a las funcionalidades esenciales de gestión de citas y documentación, evitando competir directamente con ecosistemas clínicos completos. Implementar controles de seguridad, gestión de permisos y prácticas de protección de información desde el MVP para fortalecer progresivamente la confianza de médicos y pacientes. |

### 2.2. Entrevistas

Las entrevistas permitirán comprender cómo médicos y pacientes gestionan actualmente sus citas y documentación relacionada con la atención. Asimismo, permitirán identificar problemas, necesidades, comportamientos y expectativas que puedan ser utilizados para validar los supuestos planteados durante el desarrollo de MAX.

Para la investigación se consideran los dos segmentos objetivo definidos previamente: médicos y pacientes.

#### 2.2.1. Diseño de entrevistas

Para cada segmento se elaboró un conjunto de diez preguntas. Las entrevistas buscan explorar experiencias reales relacionadas con la gestión de citas, organización de documentos, intercambio de información entre médicos y pacientes y seguimiento posterior a una consulta.

#### Segmento 1: Médicos

**Objetivo de la entrevista:** Comprender cómo los médicos gestionan actualmente sus citas, pacientes y documentación relacionada con la atención, identificar las principales dificultades que experimentan al compartir o consultar información y conocer qué factores considerarían importantes para utilizar una plataforma digital como MAX.

1. ¿Cómo organizas actualmente las citas y horarios de atención de tus pacientes?

2. ¿Qué herramientas o medios utilizas para gestionar tus citas y por qué los utilizas?

3. ¿Qué dificultades encuentras actualmente al gestionar tu agenda o las citas de tus pacientes?

4. ¿Cómo entregas normalmente recetas, informes u otros documentos después de una consulta?

5. ¿Cómo recibes resultados de laboratorio, resonancias u otros estudios realizados por tus pacientes?

6. Cuando necesitas consultar información o documentos de una atención anterior, ¿cómo los buscas actualmente?

7. ¿Qué dificultades has experimentado al organizar o encontrar documentos relacionados con tus pacientes?

8. ¿Cómo realizas actualmente el seguimiento de un paciente después de una consulta?

9. ¿Qué información o funcionalidades considerarías más importantes en una plataforma para gestionar citas y documentos de tus pacientes?

10. ¿Qué necesitarías conocer sobre una plataforma como MAX para confiar en ella y utilizarla para gestionar información relacionada con tus pacientes?

#### Segmento 2: Pacientes

**Objetivo de la entrevista:** Comprender cómo los pacientes gestionan actualmente sus citas y documentos relacionados con su atención, identificar dificultades al acceder o compartir esta información y conocer qué factores consideran importantes para utilizar una plataforma digital que centralice su interacción con el médico.

1. ¿Cómo programas normalmente una cita con un médico?

2. ¿Qué herramientas o medios utilizas actualmente para recordar y organizar tus citas médicas?

3. ¿Alguna vez has tenido alguna dificultad relacionada con una cita médica, como olvidarla, reprogramarla o encontrar la información necesaria?

4. ¿Cómo recibes y dónde guardas normalmente tus recetas, informes y otros documentos entregados por un médico?

5. ¿Alguna vez has tenido dificultades para encontrar una receta, informe o resultado cuando lo necesitabas? ¿Qué ocurrió?

6. ¿Cómo compartes actualmente resultados de laboratorio, resonancias u otros estudios con tu médico?

7. Después de una consulta, ¿cómo realizas el seguimiento de las indicaciones o documentos que te proporciona el médico?

8. ¿Qué información relacionada con tus citas o documentos te gustaría poder consultar desde una aplicación?

9. Si pudieras tener tus citas, recetas, informes y resultados en un mismo lugar, ¿qué funcionalidades considerarías más importantes?

10. ¿Qué necesitarías conocer sobre una plataforma como MAX para confiar en ella y utilizarla para gestionar información relacionada con tu atención?

#### 2.2.2. Registro de entrevistas

#### Segmento 2: Pacientes

##### Entrevista 1

| Campo | Información |
| --- | --- |
| **Nombre** | Fernanda Valderrama |
| **Edad** | 20 años |
| **Ocupación** | Estudiante universitaria |
| **Duración** | 00:00 - 06:07 |
| **Resumen** | Fernanda Valderrama, de 20 años, programa normalmente sus citas médicas mediante aplicaciones o páginas web y, cuando necesita conseguir una cita con mayor urgencia, realiza llamadas para consultar disponibilidad. Indicó que actualmente no utiliza ninguna herramienta para recordar sus citas, por lo que algunas veces las olvida o debe reprogramarlas cuando coinciden con actividades universitarias, llegando a esperar aproximadamente una semana para obtener una nueva cita. Respecto a su documentación médica, señaló que suele guardar las recetas junto con los medicamentos, mientras que los informes son revisados y posteriormente pueden terminar extraviándose. Los estudios médicos, como resonancias u otros documentos, son almacenados físicamente en su clóset y deben ser entregados presencialmente cuando un médico los solicita. Después de una consulta, realiza el seguimiento principalmente cumpliendo el tratamiento hasta finalizar los medicamentos. Manifestó interés en poder consultar recetas anteriores para conocer los medicamentos utilizados previamente y considera importante disponer de un buscador que permita localizar información mediante el nombre de un medicamento. También valoró que las recetas incluyan información específica sobre medicamentos, cantidades y horarios. Finalmente, señaló que la existencia de alianzas con las clínicas que frecuenta contribuiría a su disposición para utilizar una plataforma como MAX. |

**Entrevista 1:** [Link a la entrevista](https://youtu.be/Mw2_g3XfptE)

##### Entrevista 2

| Campo | Información |
| --- | --- |
| **Nombre** | Maricielo Bravo |
| **Edad** | 21 años |
| **Ocupación** | No especificada |
| **Duración** | 00:00 - 05:08 |
| **Resumen** | Maricielo Bravo, de 21 años, gestiona actualmente sus citas médicas mediante la aplicación de la Clínica Internacional, donde puede seleccionar al médico, la especialidad y el horario de atención. Para recordar sus citas, vincula la información con el calendario de su celular y recibe recordatorios; sin embargo, señaló que en algunas ocasiones la sincronización no funciona correctamente y que tiene dificultades para personalizar con cuánta anticipación desea recibir los avisos. Respecto a sus documentos médicos, indicó que los informes y resultados pueden visualizarse en la aplicación y también son enviados a su correo. Para realizar el seguimiento de análisis que demoran algunos días, recibe notificaciones mediante correo electrónico o WhatsApp cuando los resultados están disponibles. Considera importante poder consultar desde un mismo lugar su historial de citas, resultados organizados por especialidad, informes, radiografías e interconsultas, evitando tener que buscar información entre diferentes medios como WhatsApp y correo electrónico. También considera especialmente importantes los recordatorios configurables, prefiriendo recibir avisos varios días antes, un día antes, unas horas antes y aproximadamente treinta minutos antes de una cita. Asimismo, le gustaría recibir recordatorios sobre exámenes pendientes. Finalmente, para confiar en una plataforma como MAX considera fundamental que su información médica únicamente pueda ser visualizada por ella y por el médico que la atiende. También considera importante poder seleccionar qué documentos compartir con otros médicos, conocer quién puede acceder a sus datos y saber qué medidas de seguridad utiliza la plataforma para proteger su información. |

**Entrevista 2:** [Link a la entrevista](https://youtu.be/Q_GEiuq-wkU)

#### Segmento 1: Médicos

##### Entrevista 1

| Campo | Información |
| --- | --- |
| **Nombre** | Francesca Durand Alba |
| **Edad** | 25 años |
| **Ocupación** | Médica cirujana |
| **Duración** | 00:00 - 06:26 |
| **Resumen** | Francesca Durand Alba, médica cirujana de 25 años, organiza actualmente sus citas utilizando principalmente WhatsApp para coordinar con los pacientes y Google Calendar para registrar y organizar sus horarios. Señaló que una de las principales dificultades se presenta cuando existen cancelaciones, cambios o confirmaciones, debido a que la coordinación mediante WhatsApp dificulta visualizar rápidamente la disponibilidad y mantener organizada la agenda. Respecto a la documentación, explicó que las recetas e informes pueden entregarse físicamente durante una atención presencial o enviarse mediante WhatsApp cuando la consulta es virtual. Asimismo, recibe resultados de laboratorio, resonancias y otros estudios tanto físicamente como mediante fotografías, archivos PDF u otros documentos enviados por WhatsApp. Aunque dispone de una historia clínica virtual para consultar atenciones anteriores, los documentos complementarios pueden encontrarse distribuidos en diferentes chats y formatos, lo que dificulta localizarlos rápidamente. También señaló que algunos pacientes olvidan llevar sus resultados a las consultas. Considera importante que una plataforma permita realizar seguimiento del tratamiento, mantener la comunicación con el paciente y centralizar la historia clínica y los documentos en un solo lugar. Para confiar en una plataforma como MAX, considera fundamental conocer las medidas utilizadas para proteger la información, quién puede acceder a ella, cómo se realizan las copias de respaldo, cómo pueden recuperarse los datos y qué ocurre con la información si deja de utilizar el servicio. Además, considera importante que la plataforma sea fácil de utilizar y permita almacenar y adjuntar todos los documentos relacionados con cada paciente. |

**Entrevista 1:** [Link a la entrevista](https://youtu.be/C9Fik3RUqL4)

##### Entrevista 2

| Campo | Información |
| --- | --- |
| **Nombre** | Aixa Valle |
| **Edad** | 21 años |
| **Ocupación** | Doctora |
| **Duración** | 00:00 - 05:45 |
| **Resumen** | Aixa Valle, doctora de 21 años, organiza actualmente las citas de sus pacientes mediante una agenda, WhatsApp y Google Calendar. Utiliza principalmente WhatsApp para coordinar horarios debido a que es el medio de comunicación más utilizado por sus pacientes, mientras que Google Calendar le permite registrar las citas y visualizar su disponibilidad. Entre las principales dificultades identificó las cancelaciones y reprogramaciones, ya que debe revisar diferentes conversaciones y posteriormente actualizar su calendario. Respecto a la documentación, entrega recetas e indicaciones físicamente durante las consultas presenciales y también utiliza WhatsApp para compartir documentos digitales o gestionar atenciones virtuales. Los resultados de laboratorio, resonancias y otros estudios pueden ser entregados físicamente o enviados como fotografías y archivos PDF mediante WhatsApp, lo que puede dificultar encontrarlos posteriormente entre diferentes conversaciones. Indicó que la información de sus pacientes puede encontrarse distribuida entre sistemas, documentos físicos, archivos almacenados y WhatsApp, dificultando disponer de toda la información en un único lugar. Para realizar el seguimiento después de una consulta utiliza principalmente WhatsApp, mediante el cual los pacientes realizan consultas o envían resultados, y coordina nuevas citas cuando necesita volver a evaluarlos. Considera importante que una plataforma permita centralizar la agenda y la información de cada paciente, revisar citas, adjuntar recetas e informes, recibir resultados y estudios, consultar documentos anteriores, recibir notificaciones y recordatorios y facilitar el seguimiento. Finalmente, para confiar en una plataforma como MAX considera fundamental conocer cómo se protege la información de los pacientes, quién puede acceder a ella, cómo se almacenan los documentos y si existen copias de seguridad. También considera importante que la plataforma sea sencilla y permita ahorrar tiempo en la gestión de citas e información. |

**Entrevista 2:** [Link a la entrevista](https://youtu.be/j2yfDpQWgHI)

#### 2.2.3. Análisis de entrevistas
A partir de las entrevistas realizadas a los segmentos objetivo de MAX, se identificaron patrones relacionados con la gestión de citas, la organización y acceso a documentos médicos, los canales utilizados para intercambiar información, los recordatorios y la seguridad de los datos. Los resultados se analizaron de manera independiente para los segmentos de médicos y pacientes.

#### Médicos

Las entrevistas realizadas a **Francesca Durand Alba y Aixa Valle** muestran que ambas utilizan diferentes herramientas para gestionar sus actividades diarias. Las dos entrevistadas utilizan **WhatsApp para comunicarse y coordinar con sus pacientes**, mientras que **Google Calendar es utilizado para organizar y registrar sus citas**.

Uno de los principales problemas identificados es la **dispersión de la información**. Ambas médicas indicaron que reciben documentos como resultados de laboratorio, resonancias, fotografías o archivos PDF mediante WhatsApp, además de manejar información mediante documentos físicos u otros sistemas. Esta situación puede dificultar la búsqueda de información de atenciones anteriores y obliga a consultar diferentes medios para localizar los documentos de un paciente.

También se identificaron dificultades relacionadas con la **gestión de cambios, cancelaciones y reprogramaciones de citas**, debido a que parte de estas coordinaciones se realiza mediante conversaciones de WhatsApp y posteriormente debe actualizarse la agenda.

Respecto al seguimiento posterior a una consulta, las entrevistadas utilizan principalmente la comunicación directa con el paciente para resolver dudas, recibir resultados y coordinar nuevas evaluaciones. Ambas consideran importante disponer de una plataforma que permita **centralizar las citas y documentos de cada paciente**.

Finalmente, la **seguridad de la información** representa un aspecto fundamental para ambas entrevistadas. Entre los elementos mencionados se encuentran conocer quién puede acceder a los datos, cómo se almacenan los documentos, la existencia de copias de seguridad y las medidas utilizadas para proteger la información médica.

![Hallazgos principales - Médicos](assets/Hallazgos_Medicos.png)

#### Pacientes

Las entrevistas realizadas a **Fernanda Valderrama y Maricielo Bravo** muestran diferentes formas de gestionar las citas y la documentación médica. Fernanda indicó que programa sus citas mediante aplicaciones o páginas web, pero no utiliza una herramienta específica para recordarlas, lo que ha ocasionado que algunas veces olvide una cita. Maricielo, por otro lado, utiliza la aplicación de la Clínica Internacional y sincroniza sus citas con el calendario de su celular, aunque ha experimentado problemas con la configuración y sincronización de los recordatorios.

En relación con la documentación, ambas entrevistas evidencian la importancia de poder **consultar información médica de manera organizada**. Fernanda señaló que suele conservar las recetas junto con sus medicamentos y que algunos informes terminan extraviándose, mientras que Maricielo puede acceder a parte de su información mediante la aplicación de su clínica y su correo electrónico, aunque también debe consultar diferentes canales.

Las dos entrevistadas manifestaron interés en disponer de sus **citas y documentos médicos en un mismo lugar**. Entre las funcionalidades mencionadas se encuentran consultar recetas anteriores, resultados, informes, radiografías e historial de citas, además de contar con mecanismos que faciliten la búsqueda de información.

Los **recordatorios** también representan una oportunidad relevante. Fernanda indicó que algunas veces olvida sus citas debido a que no las registra, mientras que Maricielo manifestó interés en configurar avisos con diferentes niveles de anticipación y recibir recordatorios sobre exámenes pendientes.

Finalmente, ambas entrevistadas mencionaron elementos relacionados con la **confianza en la plataforma**. Fernanda valoró que MAX pudiera mantener alianzas con las clínicas que utiliza, mientras que Maricielo destacó la necesidad de proteger su información médica, controlar quién puede acceder a ella y decidir qué documentos compartir con otros médicos.

En conjunto, los resultados muestran que MAX puede enfocarse en **centralizar citas y documentación médica, facilitar la búsqueda de información y mejorar la gestión de recordatorios**, considerando además mecanismos de privacidad y control de acceso.

![Hallazgos principales - Pacientes](assets/Hallazgos_Pacientes.png)

### 2.3. Needfinding
#### 2.3.1. User Personas
#### User Persona - Médico

A partir de los segmentos objetivo definidos para MAX, se desarrollarán dos User Personas que representen a los principales tipos de usuarios de la solución. Los perfiles definitivos serán elaborados a partir de los patrones identificados durante las entrevistas.

![User Persona - Médico](assets/user_medico.png)

#### User Persona - Paciente

Este User Persona representa a pacientes que realizan consultas médicas y necesitan gestionar sus citas y mantener organizada la documentación relacionada con su atención. Sus principales necesidades se relacionan con el acceso a recetas, informes, resultados y recordatorios, así como con la posibilidad de compartir información con sus médicos.

![User Persona - Paciente](assets/User_Persona_Paciente.png)

#### 2.3.2. User Task Matrix

La User Task Matrix permite identificar y comparar las principales actividades realizadas por médicos y pacientes relacionadas con la gestión de citas y documentación. Para cada tarea se considera la frecuencia con la que se realiza y su nivel de importancia para cada segmento.

| Tarea del usuario | Médico - Frecuencia | Médico - Importancia | Paciente - Frecuencia | Paciente - Importancia |
| --- | --- | --- | --- | --- |
| Consultar próximas citas | Alta | Alta | Media | Alta |
| Gestionar una cita | Alta | Alta | Media | Alta |
| Gestionar agenda | Alta | Alta | No aplica | No aplica |
| Consultar información relacionada con una atención | Alta | Alta | Media | Alta |
| Generar una receta | Alta | Alta | No aplica | No aplica |
| Consultar una receta | Media | Alta | Media | Alta |
| Generar un informe | Media | Alta | No aplica | No aplica |
| Consultar un informe | Media | Alta | Media | Alta |
| Subir resultados o estudios | Baja | Media | Media | Alta |
| Revisar resultados o estudios | Alta | Alta | Media | Alta |
| Compartir documentos | Alta | Alta | Media | Alta |
| Consultar documentos anteriores | Alta | Alta | Media | Alta |
| Recibir recordatorios de citas | Media | Media | Media | Alta |
| Consultar notificaciones | Media | Media | Media | Media |

A partir de la matriz se observa que ambos segmentos comparten actividades relacionadas con la gestión de citas, consulta de documentos y acceso a información relacionada con la atención. Sin embargo, las responsabilidades de cada usuario son diferentes.

El médico presenta una mayor frecuencia en actividades relacionadas con la administración de la agenda, generación de recetas e informes y revisión de resultados. Por otro lado, el paciente presenta una mayor necesidad de consultar documentos, recibir recordatorios y compartir resultados obtenidos después de una consulta.

Los valores definitivos de frecuencia e importancia deberán ser revisados después de analizar las entrevistas realizadas a ambos segmentos.

#### 2.3.3. User Journey Mapping


En esta sección se presenta el recorrido que realizan los principales usuarios de MAX, considerando los dos segmentos definidos: médicos y pacientes. El recorrido inicia con la programación de una cita y continúa con la preparación previa a la consulta, la realización de la atención, la gestión de los documentos generados y el seguimiento posterior.

Este análisis permite identificar las acciones, objetivos, pensamientos, dificultades y emociones que experimenta cada segmento durante las diferentes etapas de la atención. A partir de estos hallazgos, se pueden reconocer oportunidades para que MAX facilite la gestión de citas, centralice la documentación y mejore la interacción entre médicos y pacientes.

#### User Journey Mapping - Médico

El recorrido del médico comienza con la organización de sus citas y continúa con la revisión de la información disponible antes de atender al paciente. Durante la consulta, el médico evalúa al paciente y registra las indicaciones correspondientes. Posteriormente, genera o comparte documentos como recetas e informes y, finalmente, realiza el seguimiento mediante la revisión de resultados, estudios u otra información proporcionada por el paciente.

![User Journey Mapping - Médico](assets/User_Journey_Medico.png)

#### User Journey Mapping - Paciente

El recorrido del paciente comienza cuando necesita programar una cita con un médico. Antes de la consulta, organiza la información y documentos que podría necesitar. Durante la atención recibe las indicaciones correspondientes y, posteriormente, debe gestionar recetas, informes, resultados u otros documentos. Finalmente, realiza el seguimiento de su atención, pudiendo compartir nuevos resultados o estudios con su médico.

![User Journey Mapping - Paciente](assets/User_Journey_Paciente.png)

#### 2.3.4. Empathy Mapping

#### Empathy Mapping - Médico

![Empathy Mapping - Médico](assets/emp_médico.png)

#### Empathy Mapping - Paciente

![Empathy Mapping - Paciente](assets/Empathy_Mapping_Paciente.png)

#### 2.3.5. As-Is Scenario Mapping

En esta sección se presenta el As-Is Scenario Mapping de los dos segmentos objetivo de MAX: médicos y pacientes. Este análisis permite comprender cómo ambos usuarios realizan actualmente las actividades relacionadas con la gestión de citas, consultas y documentación médica sin utilizar MAX. A partir de este proceso se identifican las acciones que realizan, sus principales pensamientos y las emociones que experimentan durante cada etapa.

#### As-Is Scenario Mapping - Médico

El escenario actual del médico representa el proceso que realiza desde la organización de sus citas hasta el seguimiento posterior de sus pacientes. Actualmente, estas actividades pueden involucrar diferentes herramientas y medios para gestionar la agenda, consultar información, entregar documentos y recibir resultados.

![As-Is Scenario Mapping - Médico](assets/As_Is_Medico.png)

#### As-Is Scenario Mapping - Paciente

El escenario actual del paciente representa el proceso que realiza desde que necesita programar una cita hasta el seguimiento posterior a la consulta. Durante este recorrido puede utilizar diferentes medios para coordinar citas, conservar recetas e informes y compartir resultados con su médico.

![As-Is Scenario Mapping - Paciente](assets/As_Is_Paciente.png)

### 2.4. Ubiquitous Language



El Ubiquitous Language de MAX establece un vocabulario común para describir los principales conceptos del dominio de la solución. Su propósito es mantener una terminología consistente entre el equipo de desarrollo, los stakeholders, la documentación, los modelos de dominio y la implementación del software, reduciendo ambigüedades durante el desarrollo del proyecto.

| Término | Definición |
| --- | --- |
| **Usuario (User)** | Persona registrada en MAX que interactúa con la plataforma según los permisos asociados a su rol. |
| **Médico (Doctor)** | Profesional de la salud registrado en MAX que gestiona citas, pacientes y documentación relacionada con la atención. |
| **Paciente (Patient)** | Usuario que recibe atención de un médico y utiliza MAX para gestionar citas y consultar o compartir documentación. |
| **Rol (Role)** | Clasificación asignada a un usuario que determina las funcionalidades y recursos a los que puede acceder dentro de MAX. |
| **Perfil médico (Doctor Profile)** | Información profesional asociada a un médico registrado en MAX. |
| **Perfil del paciente (Patient Profile)** | Información asociada a un paciente registrado en MAX. |
| **Cita (Appointment)** | Encuentro programado entre un médico y un paciente para una fecha y hora determinadas. |
| **Estado de cita (Appointment Status)** | Situación actual de una cita dentro de su ciclo de gestión, como pendiente, confirmada, completada o cancelada. |
| **Agenda médica (Doctor Schedule)** | Conjunto de horarios y citas asociados a un médico. |
| **Disponibilidad (Availability)** | Periodos de tiempo definidos por el médico en los que puede programarse una cita. |
| **Atención (Medical Encounter)** | Interacción entre un médico y un paciente asociada a una cita realizada. |
| **Documento médico (Medical Document)** | Archivo relacionado con una atención que puede ser almacenado y consultado mediante MAX. |
| **Receta (Prescription)** | Documento generado por el médico que contiene las prescripciones o indicaciones correspondientes a una atención. |
| **Informe médico (Medical Report)** | Documento elaborado por el médico con información relacionada con una atención realizada. |
| **Resultado (Medical Result)** | Documento que contiene información obtenida a partir de un examen o estudio realizado al paciente. |
| **Estudio médico (Medical Study)** | Examen o procedimiento cuyos resultados pueden ser registrados o compartidos mediante MAX. |
| **Repositorio de documentos (Document Repository)** | Espacio de MAX utilizado para almacenar y organizar documentos relacionados con un paciente. |
| **Carga de documento (Document Upload)** | Proceso mediante el cual un usuario incorpora un documento autorizado a MAX. |
| **Compartir documento (Document Sharing)** | Acción mediante la cual un documento se pone a disposición de un usuario autorizado. |
| **Acceso a documento (Document Access)** | Permiso que permite a un usuario autorizado visualizar o consultar un documento disponible en MAX. |
| **Historial de citas (Appointment History)** | Registro de citas anteriores asociadas a un usuario. |
| **Notificación (Notification)** | Aviso generado por MAX para comunicar al usuario información relacionada con una cita, documento u otro evento relevante. |
| **Recordatorio de cita (Appointment Reminder)** | Notificación enviada antes de una cita programada. |
| **Seguimiento (Follow-up)** | Actividades posteriores a una atención destinadas a continuar la interacción entre médico y paciente. |
| **Autenticación (Authentication)** | Proceso mediante el cual MAX verifica la identidad de un usuario. |
| **Autorización (Authorization)** | Proceso mediante el cual MAX determina las acciones y recursos a los que puede acceder un usuario autenticado. |
| **Consentimiento (Consent)** | Autorización otorgada por el usuario para determinadas acciones relacionadas con el acceso y gestión de su información dentro del alcance definido por MAX. |

---

## Capítulo III: Requirements Specification
### 3.1. To-Be Scenario Mapping

El To-Be Scenario Mapping del paciente representa la experiencia propuesta al utilizar MAX mediante cinco fases: buscar y programar una cita, preparar información, asistir a la consulta, gestionar documentos y realizar el seguimiento. Las filas Doing, Thinking y Feeling describen las acciones, pensamientos y emociones esperadas durante este recorrido. La propuesta busca centralizar las citas y la documentación médica, facilitar la consulta de recetas y resultados, y reducir la dependencia de medios dispersos. Con ello, se espera que el paciente experimente mayor confianza, tranquilidad y control sobre la organización de su información.

<div align="center">
  <img src="assets/To-be.png" alt="To-Be Scenario Mapping del paciente utilizando MAX" width="1000">
  <p><em>To-Be Scenario Mapping: experiencia propuesta del paciente con MAX.</em></p>
</div>

### 3.2. User Stories
Esta sección presenta el conjunto de Epics, User Stories y Technical Stories definidos para MAX. Su elaboración parte de la evidencia recogida en el capítulo anterior: las tareas identificadas en la User Task Matrix, los puntos de fricción de los User Journey Maps, los problemas y oportunidades del Event Storming y el vocabulario fijado en el Ubiquitous Language.

Las User Stories expresan necesidades funcionales desde la perspectiva de los usuarios finales, es decir, los médicos de consultorio y el personal de salud. Las Technical Stories expresan las necesidades técnicas que sostienen esas funcionalidades, principalmente la seguridad de la plataforma, los recursos del RESTful API y la gestión del almacenamiento de archivos.

Los criterios de aceptación se redactan en formato Gherkin, con la estructura Given – When – Then. Se mantienen en tiempo presente y tercera persona, se evita referirse a detalles específicos de la interfaz gráfica y cada condición se formula de manera comprobable. Los Epics no incluyen criterios de aceptación, ya que funcionan como agrupadores: la verificación se realiza sobre las historias que contienen.

| Epic ID | Nombre del Epic | Alcance |
| :--- | :--- | :--- |
| **EP-01** | Gestión de Identidad y Acceso | Autenticación de usuarios, registro de nuevas cuentas médicas, cierre de sesión seguro y administración del perfil básico del profesional. |
| **EP-02** | Gestión de Pacientes | Registro, visualización estructurada, edición, búsqueda y eliminación lógica de la información personal y médica de los pacientes. |
| **EP-03** | Gestión de Placas y Estudios | Carga, almacenamiento, filtrado, visualización y organización de archivos médicos adjuntos (radiografías y documentos PDF) vinculados a cada paciente. |
#### Cuadro de Epics, User Stories y Technical Stories

## EP-01: Gestión de Identidad y Acceso
| Epic / Story ID | Título | Descripción | Criterios de Aceptación | Relacionado con (Epic ID) |
|---|---|---|---|---|
| **EP-01** | **Gestión de Identidad y Acceso** | Como médico, quiero iniciar sesión, registrar mi cuenta y administrar mi perfil para acceder de forma segura a la plataforma MAX. | — | — |
| **US-01** | Iniciar sesión en la plataforma | Como médico, quiero iniciar sesión con mi correo y contraseña para acceder a mi panel clínico. | **Given** que el médico ingresa sus credenciales en el cuadro "Iniciar sesión", **When** hace clic en el botón "Ingresar", **Then** el sistema lo redirige al panel de Inicio (Dashboard). <br><br> **Given** que ingresa una contraseña incorrecta, **When** intenta iniciar sesión, **Then** el sistema no permite el acceso. | EP-01 |
| **US-02** | Crear una nueva cuenta médica | Como profesional, quiero registrar una cuenta ingresando mis datos en el formulario interno para utilizar MAX. | **Given** que el usuario completa Nombres, Apellidos, Correo y confirma su contraseña, **When** hace clic en "Registrarme", **Then** el sistema crea la cuenta médica. | EP-01 |
| **US-03** | Cerrar sesión de forma segura | Como médico, quiero cerrar mi sesión desde mi perfil para proteger los datos de mi consultorio. | **Given** que el médico se encuentra en la vista "Perfil del Médico", **When** hace clic en el botón rojo "Cerrar sesión", **Then** el sistema lo redirige al Login. | EP-01 |
| **US-04** | Visualizar resumen en Dashboard | Como médico, quiero ver los indicadores de mi consultorio al ingresar para tener un control rápido. | **Given** que el médico accede a "Inicio", **When** la vista carga, **Then** el sistema muestra las tarjetas de "Número de pacientes" (activos/total) y "Últimos estudios subidos". | EP-01 |
| **US-05** | Editar perfil básico | Como médico, quiero actualizar mis datos básicos para mantener mi información al día. | **Given** que el médico modifica su Nombre, Apellido o Email en la tarjeta "Mi perfil", **When** hace clic en "Guardar cambios", **Then** el sistema actualiza su información. | EP-01 |
| **TS-01** | Autenticación y seguridad JWT | Como desarrollador, quiero implementar seguridad basada en JSON Web Tokens (JWT) para proteger las rutas de la aplicación. | **Given** que el frontend solicita cargar el listado de pacientes, **When** envía un token JWT válido, **Then** el servidor retorna HTTP 200 y los datos. | EP-01 |
| **TS-02** | Cifrado de contraseñas | Como desarrollador, quiero asegurar que las contraseñas se guarden encriptadas mediante bcrypt. | **Given** que un nuevo usuario se registra, **When** el backend procesa la petición, **Then** almacena únicamente el hash de la contraseña en la base de datos. | EP-01 |

## EP-02: Gestión de Pacientes

| Epic / Story ID | Título | Descripción | Criterios de Aceptación | Relacionado con (Epic ID) |
|---|---|---|---|---|
| **EP-02** | **Gestión de Pacientes** | Como médico, quiero registrar, visualizar y administrar la información de mis pacientes para mantener un control organizado de sus expedientes. | — | — |
| **US-06** | Registrar un nuevo paciente | Como médico, quiero registrar a un paciente ingresando su información personal y médica. | **Given** que el médico hace clic en "Registrar Paciente", **When** completa el modal de Información personal y médica (Alergias, Riesgo, Diagnóstico) y guarda, **Then** el sistema crea el expediente. | EP-02 |
| **US-07** | Consultar el listado en tarjetas | Como médico, quiero ver a mis pacientes en tarjetas independientes para visualizar sus datos básicos rápidamente. | **Given** que el médico accede a "Pacientes", **When** la vista carga, **Then** el sistema muestra tarjetas con el Nombre, DNI, Edad y estado (Activo) de cada paciente. | EP-02 |
| **US-08** | Buscar pacientes por DNI o Nombre | Como médico, quiero localizar rápidamente a mis pacientes usando los campos de búsqueda superiores. | **Given** que el médico escribe en los inputs "Buscar por nombre" o "Buscar por DNI", **When** existen coincidencias, **Then** el listado de tarjetas se filtra en tiempo real. | EP-02 |
| **US-09** | Visualizar detalle estático | Como médico, quiero consultar la información de un paciente en una vista de solo lectura para revisar antecedentes. | **Given** que el médico hace clic en el botón "Ver" de una tarjeta, **When** se abre el modal "Detalle del paciente", **Then** el sistema muestra la información inhabilitada para edición. | EP-02 |
| **US-10** | Editar información del paciente | Como médico, quiero actualizar los datos de un paciente usando el mismo formulario de registro. | **Given** que el médico selecciona "Editar", **When** modifica campos en el modal "Editar paciente" y guarda, **Then** la tarjeta del paciente se actualiza en el listado. | EP-02 |
| **US-11** | Eliminar un paciente del sistema | Como médico, quiero eliminar un paciente validando la acción mediante su nombre o documento. | **Given** que el médico selecciona el botón rojo "Eliminar paciente", **When** el modal solicita buscar por Nombre o DNI para confirmar, **Then** el sistema valida la entrada antes de permitir el borrado. | EP-02 |
| **TS-03** | Carga de pacientes | Como desarrollador, quiero implementar paginación en el backend para no saturar la respuesta del servidor en la vista de tarjetas. | **Given** que el médico tiene una gran base de pacientes, **When** solicita la vista "Pacientes", **Then** el backend retorna el listado en bloques optimizados. | EP-02 |

## EP-03: Gestión de Placas y Estudios

| Epic / Story ID | Título | Descripción | Criterios de Aceptación | Relacionado con (Epic ID) |
|---|---|---|---|---|
| **EP-03** | **Gestión de Placas y Estudios** | Como médico, quiero cargar, visualizar y organizar archivos médicos adjuntos (radiografías y documentos PDF) vinculados a cada paciente. | — | — |
| **US-12** | Adjuntar nueva placa o estudio | Como médico, quiero subir archivos médicos indicando el paciente y el tipo de documento. | **Given** que el médico selecciona "Adjuntar estudio", **When** elige al paciente, el tipo de estudio, agrega una descripción y sube el archivo, **Then** el sistema lo registra. | EP-03 |
| **US-13** | Buscar placas por paciente o fecha | Como médico, quiero filtrar el repositorio buscando por DNI/Nombre o por una fecha específica. | **Given** que el médico ingresa datos en los inputs "Buscar por nombre o DNI" o "Fecha (dd/mm/aaaa)", **When** presiona enter, **Then** el sistema filtra las tarjetas de estudios. | EP-03 |
| **US-14** | Identificar formato del estudio (Etiquetas) | Como médico, quiero ver visualmente si un estudio adjunto es una placa radiográfica o un documento PDF. | **Given** que el médico revisa la sección Estudios, **When** visualiza las tarjetas, **Then** el sistema muestra una etiqueta indicadora (ej. "RX" o "PDF médico") en la esquina superior derecha. | EP-03 |
| **US-15** | Visualizar archivo adjunto | Como médico, quiero abrir el archivo del estudio haciendo clic en su botón de acción. | **Given** que un estudio tiene un archivo subido, **When** el médico hace clic en el botón "Ver", **Then** el sistema despliega el documento (PDF o Imagen) para su lectura. | EP-03 |
| **TS-04** | Almacenamiento seguro de archivos | Como desarrollador, quiero implementar un repositorio para guardar los binarios de las placas. | **Given** que el frontend envía un archivo (`.pdf`, `.png`, `.jpg`), **When** el backend lo procesa, **Then** almacena el archivo y guarda su ruta referencial en la base de datos. | EP-03 |
| **TS-05** | Validación de Tipos | Como desarrollador, quiero verificar desde el backend que los archivos subidos sean formatos válidos. | **Given** que un usuario intenta subir un formato no permitido, **When** el backend evalúa el tipo, **Then** rechaza la carga devolviendo un error. | EP-03 |

## EP-04: Gestión de Consultas y Agenda Clínica

| Epic / Story ID | Título | Descripción | Criterios de Aceptación | Relacionado con |
|---|---|---|---|---|
| **US-16** | Programar una nueva cita | Como médico, quiero agendar una consulta futura asignando una fecha, hora y seleccionando al paciente. | **Given** que el médico selecciona la opción de programar cita, **When** ingresa la fecha, hora y paciente, y guarda, **Then** el sistema registra la cita como pendiente en la agenda. | EP-04 |
| **US-17** | Validar disponibilidad de horario | Como médico, quiero que el sistema me avise si intento agendar una cita en un horario ya ocupado. | **Given** que el médico selecciona una fecha y hora, **When** el bloque de tiempo ya está ocupado por otra cita, **Then** el sistema deshabilita el botón de guardado y muestra una advertencia de cruce. | EP-04 |
| **US-18** | Cancelar una cita programada | Como médico, quiero eliminar o cancelar una cita si el paciente avisa que no asistirá. | **Given** que el médico selecciona una cita pendiente en la agenda, **When** hace clic en "Cancelar" y confirma, **Then** la cita cambia a estado cancelado y libera el horario. | EP-04 |
| **US-19** | Registrar atención clínica | Como médico, quiero ingresar las notas clínicas (anamnesis, diagnóstico) para documentar formalmente el acto médico. | **Given** que el médico inicia el registro de una consulta, **When** completa los campos de texto con el detalle clínico y guarda, **Then** el sistema guarda el expediente de la atención de forma permanente. | EP-04 |
| **US-20** | Vincular atención a una cita previa | Como médico, quiero asociar mi registro clínico a una cita previamente agendada para cerrar el ciclo de atención. | **Given** que el médico registra una atención, **When** selecciona una cita pendiente del menú "Consulta asociada", **Then** el sistema vincula ambos registros y marca la cita original como "Completada". | EP-04 |
| **US-21** | Consultar historial de atenciones | Como médico, quiero revisar las consultas pasadas de un paciente para recordar su diagnóstico o tratamiento previo. | **Given** que el médico accede a la pestaña "Consultas", **When** busca a un paciente específico, **Then** el sistema lista todas las atenciones previas ordenadas de la más reciente a la más antigua. | EP-04 |
| **US-22** | Editar notas de una consulta | Como médico, quiero modificar las notas de una consulta pasada si olvidé agregar un detalle importante. | **Given** que el médico visualiza una consulta previa, **When** selecciona editar, modifica el texto y guarda los cambios, **Then** el sistema actualiza la base de datos y registra la fecha de última modificación. | EP-04 |
| **TS-06** | Integridad transaccional de citas | Como desarrollador, quiero usar transacciones ACID al vincular una atención clínica con una cita para evitar inconsistencias. | **Given** que el backend recibe la petición de completar una cita al registrar una atención, **When** procesa la orden, **Then** actualiza el estado de la cita y guarda el registro clínico en una única transacción de base de datos. | EP-04 |
| **TS-07** | Optimización de agenda por rangos | Como desarrollador, quiero que el endpoint de citas filtre los registros por fecha para no sobrecargar el frontend. | **Given** que el sistema solicita cargar la agenda, **When** el frontend envía un rango de fechas (inicio y fin), **Then** el backend retorna exclusivamente las citas que coinciden con ese periodo temporal. | EP-04 |

## EP-05: Configuración y Preferencias del Sistema

| Epic / Story ID | Título | Descripción | Criterios de Aceptación | Relacionado con |
|---|---|---|---|---|
| **US-23** | Cambiar el idioma de la plataforma | Como médico, quiero cambiar el idioma de la interfaz para utilizar la plataforma en mi idioma de preferencia. | **Given** que el médico se encuentra en la vista de Configuración, **When** alterna el toggle de Idioma entre "ES" y "EN", **Then** todos los textos del sistema se traducen de inmediato. | EP-05 |
| **US-24** | Configurar tema visual | Como médico, quiero poder alternar entre tema claro y oscuro para reducir la fatiga visual. | **Given** que el médico revisa la sección Preferencias, **When** cambia el selector de Tema a "Oscuro", **Then** la interfaz invierte sus colores de fondo y texto globalmente. | EP-05 |
| **US-25** | Ajustar tamaño de texto | Como médico, quiero poder aumentar la tipografía del sistema para facilitar la lectura de los expedientes. | **Given** que el médico está en la vista Configuración, **When** cambia el toggle de Tamaño de texto a "Grande", **Then** la escala tipográfica de toda la plataforma aumenta. | EP-05 |
| **US-26** | Gestionar notificaciones | Como médico, quiero activar o desactivar las notificaciones para evitar distracciones durante las consultas. | **Given** que el médico revisa sus preferencias, **When** desactiva el switch de "Notificaciones", **Then** el sistema silencia temporalmente las alertas emergentes. | EP-05 |
| **US-27** | Consultar versión y estado del sistema | Como médico, quiero verificar la versión actual del software para asegurarme de tener las últimas actualizaciones. | **Given** que el médico accede a Configuración, **When** revisa la tarjeta "Sistema", **Then** el sistema muestra campos de solo lectura con la Versión (ej. MAX 1.0.0) y el Estado (Operativo). | EP-05 |
| **TS-08** | Persistencia de preferencias del usuario | Como desarrollador, quiero guardar la configuración visual del usuario para que se mantenga intacta cuando vuelva a iniciar sesión. | **Given** que el médico cambia su idioma o tema, **When** la aplicación registra el evento, **Then** el sistema actualiza las variables en el LocalStorage y las sincroniza con el backend. | EP-05 |

### 3.3. Product Backlog

El Product Backlog ordena las User Stories y Technical Stories definidas para la primera y segunda entrega de la plataforma MAX. El orden responde al plan lógico de construcción del producto: primero la infraestructura de seguridad e identidad, luego el núcleo transaccional (expedientes de pacientes), el soporte para archivos adjuntos, seguido por el sistema de agendamiento clínico y, por último, la personalización de preferencias.

La estimación se expresa en Story Points siguiendo la sucesión de Fibonacci (1, 2, 3, 5, 8). El valor representa el esfuerzo relativo considerando complejidad técnica, incertidumbre y volumen de trabajo, y no una cantidad exacta de horas.

| Orden | Entrega | Story ID | Título | Descripción | Story Points |
|---:|---|---|---|---|---:|
| 1 | Entrega 1 | TS-01 | Autenticación y seguridad JWT | Como desarrollador, quiero implementar seguridad basada en JSON Web Tokens. | 5 |
| 2 | Entrega 1 | TS-02 | Cifrado de contraseñas | Como desarrollador, quiero asegurar que las contraseñas se guarden encriptadas. | 2 |
| 3 | Entrega 1 | US-02 | Crear una nueva cuenta médica | Como profesional, quiero registrar una cuenta ingresando mis datos personales. | 3 |
| 4 | Entrega 1 | US-01 | Iniciar sesión en la plataforma | Como médico, quiero iniciar sesión con mi correo y contraseña. | 3 |
| 5 | Entrega 1 | US-03 | Cerrar sesión de forma segura | Como médico, quiero cerrar mi sesión para proteger la confidencialidad. | 1 |
| 6 | Entrega 1 | US-05 | Editar perfil básico | Como médico, quiero actualizar mi nombre y correo. | 2 |
| 7 | Entrega 1 | US-06 | Registrar un nuevo paciente | Como médico, quiero registrar a un paciente ingresando su información base. | 5 |
| 8 | Entrega 1 | US-07 | Consultar el listado en tarjetas | Como médico, quiero ver a mis pacientes en tarjetas independientes. | 3 |
| 9 | Entrega 1 | TS-03 | Paginación / Carga diferida | Como desarrollador, quiero implementar paginación en el backend. | 5 |
| 10 | Entrega 1 | US-08 | Buscar pacientes por DNI o Nombre | Como médico, quiero localizar rápidamente a mis pacientes. | 3 |
| 11 | Entrega 1 | US-09 | Visualizar detalle estático | Como médico, quiero consultar la información de un paciente sin habilitar edición. | 2 |
| 12 | Entrega 1 | US-10 | Editar información del paciente | Como médico, quiero actualizar los datos de un paciente. | 3 |
| 13 | Entrega 1 | US-11 | Eliminar un paciente del sistema | Como médico, quiero eliminar un paciente validando la acción mediante su nombre. | 2 |
| 14 | Entrega 1 | US-04 | Visualizar resumen en Dashboard | Como médico, quiero ver los indicadores de mi consultorio al ingresar. | 3 |
| 15 | Entrega 1 | TS-04 | Almacenamiento seguro de archivos | Como desarrollador, quiero implementar un repositorio para los binarios de placas. | 5 |
| 16 | Entrega 1 | TS-05 | Validación de Tipos | Como desarrollador, quiero verificar que los archivos subidos sean formatos válidos. | 2 |
| 17 | Entrega 1 | US-12 | Adjuntar nueva placa o estudio | Como médico, quiero subir archivos médicos indicando el paciente. | 5 |
| 18 | Entrega 1 | US-13 | Buscar placas por paciente o fecha | Como médico, quiero filtrar el repositorio buscando por DNI/Nombre o fecha. | 3 |
| 19 | Entrega 1 | US-14 | Identificar formato del estudio | Como médico, quiero ver visualmente si un estudio adjunto es RX o PDF. | 2 |
| 20 | Entrega 1 | US-15 | Visualizar archivo adjunto | Como médico, quiero abrir el archivo del estudio haciendo clic en su botón. | 3 |
| 21 | Entrega 2 | TS-07 | Optimización de agenda por rangos | Como desarrollador, quiero que el endpoint de citas filtre los registros por fecha. | 5 |
| 22 | Entrega 2 | TS-06 | Integridad transaccional de citas | Como desarrollador, quiero usar transacciones ACID al vincular atenciones. | 3 |
| 23 | Entrega 2 | US-16 | Programar una nueva cita | Como médico, quiero agendar una consulta futura asignando una fecha y paciente. | 5 |
| 24 | Entrega 2 | US-17 | Validar disponibilidad de horario | Como médico, quiero que el sistema me avise si hay un cruce de horarios en agenda. | 3 |
| 25 | Entrega 2 | US-18 | Cancelar una cita programada | Como médico, quiero eliminar o cancelar una cita si el paciente no asiste. | 2 |
| 26 | Entrega 2 | US-19 | Registrar atención clínica | Como médico, quiero ingresar las notas clínicas (anamnesis, diagnóstico). | 5 |
| 27 | Entrega 2 | US-20 | Vincular atención a cita previa | Como médico, quiero asociar mi registro clínico a una cita previamente agendada. | 3 |
| 28 | Entrega 2 | US-21 | Consultar historial de atenciones | Como médico, quiero revisar las consultas pasadas de un paciente específico. | 3 |
| 29 | Entrega 2 | US-22 | Editar notas de una consulta | Como médico, quiero modificar las notas de una consulta pasada. | 2 |
| 30 | Entrega 2 | TS-08 | Persistencia de preferencias | Como desarrollador, quiero guardar la configuración visual del usuario (LocalStorage/BD). | 3 |
| 31 | Entrega 2 | US-23 | Cambiar idioma de la plataforma | Como médico, quiero cambiar el idioma de la interfaz a mi preferencia. | 3 |
| 32 | Entrega 2 | US-24 | Configurar tema visual | Como médico, quiero alternar entre tema claro y oscuro para reducir fatiga visual. | 3 |
| 33 | Entrega 2 | US-25 | Ajustar tamaño de texto | Como médico, quiero aumentar la tipografía del sistema para facilitar la lectura. | 2 |
| 34 | Entrega 2 | US-26 | Gestionar notificaciones | Como médico, quiero activar o desactivar alertas para evitar distracciones. | 2 |
| 35 | Entrega 2 | US-27 | Consultar versión y estado | Como médico, quiero verificar la versión actual del software y estado operativo. | 1 |

#### Distribución por entrega

| Entrega | Alcance | Historias | Story Points |
|---|---|---:|---:|
| **Entrega 1** | Configuración de seguridad, gestión integral de pacientes y almacenamiento de estudios adjuntos. | 20 | 62 |
| **Entrega 2** | Gestión de agenda médica, registro de atenciones clínicas y configuración de preferencias del sistema. | 15 | 45 |
| **Total** | — | **35** | **107** |

#### Distribución por Epic

| Epic | Historias | Story Points |
|---|---:|---:|
| EP-01 Gestión de Identidad y Acceso | 7 | 19 |
| EP-02 Gestión de Pacientes | 7 | 23 |
| EP-03 Gestión de Placas y Estudios | 6 | 20 |
| EP-04 Gestión de Consultas y Agenda Clínica | 9 | 31 |
| EP-05 Configuración y Preferencias del Sistema | 6 | 14 |
| **Total** | **35** | **107** |

#### Consideraciones sobre el orden

La secuencia del Product Backlog para esta primera entrega obedece a las dependencias técnicas y de negocio. Se abordan íntegramente las bases del sistema (TS-01 y TS-02) antes de desarrollar las interfaces de usuario de acceso. 

A continuación, se desarrolla el núcleo transaccional, ya que el sistema requiere usuarios autenticados para asignarles la autoría de los registros. Asimismo, la historia US-04 se relega hacia el final de este bloque debido a que requiere la existencia previa de pacientes para mostrar las métricas correctamente.

Finalmente, la sección de placas y estudios se construye al final del ciclo porque la entidad "Estudio" depende obligatoriamente de la existencia de la entidad "Paciente" para poder ser registrada y vinculada en el repositorio.

Para la **Entrega 2**, el orden prioriza la infraestructura backend de la agenda (TS-07 y TS-06) para garantizar que las validaciones lógicas y transacciones funcionen correctamente antes de exponer las interfaces. Luego, se desarrollan las historias de programación de citas y registro de atención médica (EP-04). Por último, las historias de configuración y preferencias (EP-05) se abordan al cierre del ciclo, ya que representan mejoras de usabilidad y personalización visual que no bloquean el flujo clínico principal.

### 3.4. Impact Mapping

El Impact Mapping conecta los objetivos de negocio de MAX con los actores capaces de contribuir a ellos, los cambios de comportamiento que se espera provocar, los entregables digitales que los harían posibles y las User Stories que los materializan. Su utilidad radica en verificar que cada historia del backlog persigue un objetivo declarado: si una historia no puede rastrearse hasta un Business Goal, se considera fuera del alcance del MVP.

El artefacto responde a cuatro preguntas encadenadas:

| Elemento | Pregunta que responde |
|---|---|
| **Business Goal** | ¿Qué objetivo de negocio se busca alcanzar? |
| **Actor** | ¿Quién puede contribuir a alcanzarlo? |
| **Impact** | ¿Qué debería hacer ese actor, de forma distinta a hoy, para contribuir? |
| **Deliverable** | ¿Qué se puede construir para provocar ese cambio de comportamiento? |

#### Business Goals SMART

Los objetivos se formulan bajo criterios SMART (específicos, medibles, alcanzables, relevantes y acotados en el tiempo). Los plazos se definen respecto a la liberación de las entregas de la plataforma.

| ID | Business Goal |
|---|---|
| **BG-01** | Garantizar que el **100%** de los accesos a la información de los pacientes se realice mediante sesiones autenticadas y cifradas durante la fase de despliegue inicial. |
| **BG-02** | Lograr que los médicos participantes registren digitalmente los expedientes base de al menos **50 pacientes** sin recurrir a formatos de papel durante el primer mes de uso. |
| **BG-03** | Reducir en un **50%** el tiempo que el médico invierte en localizar radiografías y estudios pasados, utilizando la búsqueda digital por DNI, en un plazo de **2 meses**. |
| **BG-04** | Lograr que el **80%** de las atenciones médicas se programen y documenten a través del módulo de agenda de la plataforma durante el tercer mes de uso, eliminando por completo los cruces de horarios. |
| **BG-05** | Incrementar la comodidad de uso de la plataforma, logrando que al menos el **60%** de los médicos personalicen la interfaz (tema, idioma o texto) en sus primeras dos semanas, reduciendo la fatiga visual. |

#### Actores considerados

| Actor | Rol respecto de los objetivos |
|---|---|
| **Médico de consultorio** | Es el usuario central de la plataforma. Produce la información (registra pacientes, agenda citas, documenta atenciones y sube placas) y la consume. Su adopción determina si el sistema contiene datos centralizados y si se abandona el uso de medios físicos. |

#### Mapa de impacto

| Business Goal | Actor | Impact (cambio de comportamiento esperado) | Deliverable | User Stories |
|---|---|---|---|---|
| **BG-01** | Médico de consultorio | Autentica su identidad antes de consultar cualquier dato y cierra su sesión al terminar. | Módulo de autenticación segura (Login/Logout) y cifrado de credenciales. | US-01, US-02, US-03, TS-01, TS-02 |
| **BG-01** | Médico de consultorio | Mantiene sus datos de contacto e identidad actualizados en el sistema. | Gestión de perfil de usuario. | US-05 |
| **BG-02** | Médico de consultorio | Crea el expediente del paciente directamente en la plataforma en lugar de usar fichas físicas. | Formulario de registro de pacientes y almacenamiento centralizado. | US-06, US-09, US-10, US-11 |
| **BG-02** | Médico de consultorio | Consulta su volumen total de atención y la lista de pacientes desde un entorno digital. | Dashboard de métricas, listado en tarjetas y paginación. | US-04, US-07, TS-03 |
| **BG-02** | Médico de consultorio | Localiza el expediente de un paciente específico de manera instantánea. | Buscador en tiempo real por DNI o Nombre. | US-08 |
| **BG-03** | Médico de consultorio | Almacena las placas y resultados médicos en un repositorio digital seguro en la nube. | Módulo de carga de archivos con validación de formatos. | US-12, US-14, TS-04, TS-05 |
| **BG-03** | Médico de consultorio | Visualiza y filtra los estudios directamente en pantalla sin buscar en carpetas físicas. | Buscador de estudios y previsualizador integrado de PDF/RX. | US-13, US-15 |
| **BG-04** | Médico de consultorio | Gestiona su disponibilidad de tiempo y programa citas apoyándose en validaciones automáticas. | Módulo de agenda con prevención de colisiones de horarios. | US-16, US-17, US-18, TS-06, TS-07 |
| **BG-04** | Médico de consultorio | Documenta la atención y vincula el registro clínico directamente con la cita y el paciente. | Registro de consultas e historial clínico estructurado. | US-19, US-20, US-21, US-22 |
| **BG-05** | Médico de consultorio | Adapta la plataforma a sus necesidades visuales para trabajar de manera más cómoda. | Panel de configuración de preferencias y sistema. | US-23, US-24, US-25, US-26, US-27, TS-08 |

#### Conclusión del Impact Mapping

El mapa evidencia que los objetivos de MAX dependen de una adopción progresiva por parte del médico de consultorio. El primer cambio (BG-01) es un requisito de seguridad habilitante. El segundo cambio (BG-02) representa la carga inicial de datos maestros. El tercer y cuarto cambio (BG-03 y BG-04) consolidan el valor transaccional de la herramienta al centralizar el flujo de trabajo diario: agendar pacientes, atenderlos y revisar sus exámenes de manera integral. Finalmente, el quinto cambio (BG-05) busca la retención a largo plazo mediante la ergonomía digital.

Esta dependencia justifica la priorización reflejada en el Product Backlog: la infraestructura de identidad debe construirse primero, seguida por la gestión de expedientes y estudios , para finalmente habilitar las interacciones de agenda diaria y la configuración de experiencia de usuario.


<img src="assets/ImpactMapping.png" alt="Impact Mapping" width="900">

---

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

### 4.8. Domain-Driven Software Architecture
#### 4.8.1. Software Architecture Context Diagram
#### 4.8.2. Software Architecture Container Diagrams
#### 4.8.3. Software Architecture Components Diagrams
### 4.9. Software Object-Oriented Design
#### 4.9.1. Class Diagrams
#### 4.9.2. Class Dictionary
### 4.10. Database Design
#### 4.10.1. Relational/Non-Relational Database Diagrams

---

## Capítulo V: Product Implementation, Validation & Deployment
### 5.1. Software Configuration Management
### Requirements Management

- **Discord y WhatsApp:** Estas plataformas fueron esenciales para la comunicación interna del equipo, siendo WhatsApp especialmente útil por su facilidad para gestionar grupos de trabajo.

- **Trello:** Se utilizó para planificar y dar seguimiento al avance del proyecto mediante tableros que representaban el backlog del producto y otras tareas organizativas.

### Product UX/UI

- **Figma:** Herramienta principal para el diseño de wireframes y prototipos, tanto en versiones de escritorio como móviles.

- **Miro:** Se utilizó como apoyo en la creación de los Scenario Mapping para ambos segmentos objetivo considerados en el desarrollo del proyecto.

### Software Development

- **Visual Studio Code:** Editor principal utilizado para el desarrollo y programación del landing page.

- **GitHub y Git Bash:** Herramientas empleadas para el control de versiones y el desarrollo colaborativo del repositorio del proyecto.

- **HTML y CSS:** Lenguajes fundamentales utilizados para la estructura (HTML) y el diseño visual (CSS) del landing page.

### Software Documentation

- **Google Drive:** Plataforma utilizada para el almacenamiento compartido de documentación e informes colaborativos.

- **Google Meet y Zoom:** Google Meet fue utilizado principalmente para las reuniones virtuales del equipo, mientras que Zoom se empleó para las grabaciones de entrevistas y presentaciones relacionadas con el desarrollo del proyecto.

- **Lucidchart:** Herramienta utilizada para la creación de diagramas de flujo y modelado visual del sistema, incluyendo diagramas de clases.


- **Vertabelo:** Herramienta empleada para el diseño de la base de datos y la elaboración de diagramas lógicos.
- 
#### 5.1.1. Software Development Environment Configuration

Para el desarrollo de MAX se configuraron diferentes entornos y servicios que permiten gestionar el código fuente, desplegar los componentes de la solución y mantener disponible la infraestructura necesaria para su funcionamiento. La arquitectura de despliegue considera de manera independiente el Landing Page, Frontend, Backend y Base de Datos.

El equipo utiliza **GitHub** como plataforma principal para el almacenamiento del código fuente y el control de versiones. Los diferentes componentes de la solución se encuentran organizados en repositorios independientes, permitiendo administrar de manera separada el desarrollo y despliegue de cada aplicación.

#### Landing Page

El Landing Page de MAX se encuentra alojado en un repositorio de GitHub y desplegado mediante **GitHub Pages**. La configuración utiliza la rama `main` como fuente de publicación, permitiendo que los cambios integrados en esta rama puedan reflejarse posteriormente en la versión publicada del sitio.

El despliegue mediante GitHub Pages permite disponer de una versión pública del Landing Page sin necesidad de administrar un servidor web independiente.

![Deployment Landing Page](assets/dep_landi.jpeg)

#### Backend

El Backend de MAX se encuentra desplegado mediante **Railway**. El servicio está conectado con el repositorio correspondiente en GitHub, permitiendo desplegar la aplicación a partir del código fuente del proyecto.

Railway proporciona el entorno necesario para mantener disponible el servicio Backend y permite consultar información relacionada con los deployments, variables de entorno, métricas y registros de ejecución.

En la configuración mostrada, el servicio `MAX_DEV_BACK` se encuentra desplegado correctamente en el ambiente de producción.

![Deployment Backend](assets/dep_back.jpeg)

#### Base de Datos

La base de datos utilizada por MAX se encuentra desplegada mediante **Railway** utilizando **MySQL**. Este servicio se encuentra conectado con el Backend, permitiendo almacenar y consultar la información necesaria para el funcionamiento de la plataforma.

La instancia contiene las diferentes tablas utilizadas por el sistema, entre las que se encuentran `app_settings`, `citas`, `consultas`, `estudios`, `pacientes` y `usuarios`.

La separación entre el servicio Backend y la instancia MySQL permite mantener diferenciadas la lógica de negocio y la persistencia de los datos dentro del entorno desplegado.

![Deployment Database](assets/dep_db.jpeg)

#### Frontend Web Application

El Frontend de MAX se encuentra desplegado mediante **Cloudflare Workers & Pages**. El proyecto está conectado con su repositorio de GitHub y utiliza la rama `main` para realizar los deployments correspondientes al ambiente de producción.

La plataforma mantiene un historial de los diferentes despliegues realizados y permite verificar el estado de cada versión publicada. De esta manera, los cambios incorporados al Frontend pueden ser desplegados y posteriormente validados en el ambiente de producción.

![Deployment Frontend](assets/dep_front.jpeg)

#### Resumen del entorno de despliegue

| Componente | Tecnología / Servicio | Función |
| --- | --- | --- |
| **Control de versiones** | GitHub | Administración de repositorios, ramas y versiones del código fuente. |
| **Landing Page** | GitHub Pages | Publicación y alojamiento del Landing Page de MAX. |
| **Frontend** | Cloudflare Workers & Pages | Despliegue y alojamiento de la aplicación web. |
| **Backend** | Railway | Ejecución y despliegue del servicio Backend. |
| **Base de Datos** | MySQL en Railway | Persistencia y administración de los datos utilizados por MAX. |
| **Entorno de desarrollo** | Visual Studio Code | Desarrollo y edición del código fuente de los componentes del proyecto. |

#### 5.1.2. Source Code Management

La gestión del código fuente de **MAX** se realiza mediante **Git** como sistema de control de versiones y **GitHub** como plataforma para el almacenamiento de los repositorios y el trabajo colaborativo. Esta configuración permite mantener un historial de los cambios realizados, separar el desarrollo de los diferentes componentes de la solución y controlar la integración de nuevas funcionalidades.

MAX mantiene sus principales componentes en repositorios independientes, permitiendo que cada aplicación pueda evolucionar y desplegarse de manera separada.

#### Organización de repositorios

| Repositorio | Descripción |
| --- | --- |
| **REPORT** | Contiene la documentación, capítulos y evidencias correspondientes al desarrollo del proyecto. |
| **LANDING-PAGE** | Contiene el código fuente del Landing Page de MAX. |
| **FRONT** | Contiene el código fuente de la aplicación web utilizada por los usuarios de MAX. |
| **BACK** | Contiene el código fuente correspondiente al Backend y los servicios necesarios para procesar las operaciones de la plataforma. |
| **MOBILE** | Contiene el código fuente correspondiente a la aplicación móvil de MAX. |

Esta separación permite administrar de manera independiente la documentación, presentación del producto, interfaz web, lógica del servidor y aplicación móvil.

#### Estrategia de Branching

Para organizar el desarrollo colaborativo se utiliza una estrategia basada en **GitFlow**, evitando realizar el desarrollo de nuevas funcionalidades directamente sobre la rama estable.

Las principales ramas consideradas son:

- **`main`:** contiene las versiones estables e integradas del proyecto y funciona como referencia para los despliegues de producción.

- **`develop`:** concentra los cambios provenientes de las diferentes funcionalidades antes de su integración hacia `main`.

- **`feature/*`:** ramas destinadas al desarrollo de funcionalidades, componentes o secciones específicas del proyecto.

El flujo de integración utilizado puede representarse de la siguiente manera:

```text

feature/*

    │

    ▼

 develop

    │

    ▼

  main

```

Cada nueva funcionalidad puede desarrollarse inicialmente en una rama `feature/*`. Una vez terminada y revisada, sus cambios pueden integrarse a `develop`. Posteriormente, cuando el conjunto de cambios se encuentra preparado para formar parte de una versión estable, se integra a `main`.

En el repositorio de documentación, por ejemplo, se pueden utilizar ramas específicas para trabajar los diferentes capítulos:

```text

feature/report-chapter-1

feature/report-chapter-2

feature/report-chapter-3

feature/report-chapter-4

feature/report-chapter-5

```

Esto permite que los integrantes trabajen sobre diferentes partes del proyecto sin modificar directamente el contenido estable.

#### Gestión de commits

Los cambios realizados en el código y documentación son registrados mediante **commits**, permitiendo mantener la trazabilidad de la evolución del proyecto.

Para facilitar la comprensión del historial se considera el uso de **Conventional Commits**, utilizando prefijos que permitan identificar el propósito principal de cada cambio.

| Convención | Propósito |
| --- | --- |
| `feat:` | Incorporación de una nueva funcionalidad. |
| `fix:` | Corrección de errores. |
| `docs:` | Modificaciones relacionadas con documentación. |
| `refactor:` | Reestructuración del código sin incorporar una nueva funcionalidad. |
| `test:` | Incorporación o modificación de pruebas. |
| `chore:` | Cambios de mantenimiento, configuración u otras tareas técnicas. |

Algunos ejemplos de mensajes de commit aplicables al proyecto son:

```text
feat: add appointment management
feat: support multipart study uploads
fix: correct patient document upload
docs: update chapter 5 documentation
refactor: improve appointment service
test: add appointment unit tests

```

De esta manera, el historial del repositorio permite identificar con mayor facilidad qué tipo de modificación fue realizada.

#### Integración y revisión de cambios

GitHub permite centralizar el trabajo realizado por los diferentes integrantes del equipo. Los cambios desarrollados localmente son enviados a sus respectivas ramas remotas y posteriormente pueden integrarse mediante **Pull Requests**.

Los Pull Requests permiten revisar las modificaciones antes de incorporarlas a una rama principal, identificar posibles conflictos y mantener evidencia de las integraciones realizadas durante el desarrollo.

El flujo general de gestión del código fuente es:

1. Crear o seleccionar una rama `feature/*`.

2. Realizar los cambios correspondientes.

3. Registrar los cambios mediante commits.

4. Publicar la rama en GitHub.

5. Crear un Pull Request hacia `develop`.

6. Revisar e integrar los cambios.

7. Integrar posteriormente `develop` hacia `main` cuando corresponda a una versión estable.

#### Relación entre Source Code Management y Deployment

Los repositorios almacenados en GitHub también funcionan como fuente para los diferentes servicios utilizados durante el despliegue de MAX.
| Componente | Repositorio | Servicio de despliegue |
| --- | --- | --- |
| **Landing Page** | LANDING-PAGE | GitHub Pages |
| **Frontend Web** | FRONT | Cloudflare Workers & Pages |
| **Backend** | BACK | Railway |
| **Aplicación móvil** | MOBILE | Repositorio de código fuente |
| **Documentación** | REPORT | GitHub |

En los componentes desplegados, la rama `main` representa el código utilizado como referencia para el ambiente de producción. De esta manera, existe una relación entre el control de versiones y los deployments de la solución.

Por ejemplo, el Landing Page publicado mediante GitHub Pages utiliza el código almacenado en la rama `main`, mientras que el Frontend desplegado mediante Cloudflare y el Backend desplegado mediante Railway se encuentran vinculados con sus respectivos repositorios de GitHub.

#### Trazabilidad del código fuente

El uso conjunto de Git y GitHub permite mantener trazabilidad sobre la evolución de MAX. A través del historial del repositorio es posible identificar los commits realizados, las ramas utilizadas para cada funcionalidad, los integrantes responsables de los cambios y las integraciones realizadas.

Esta estrategia permite mantener organizado el desarrollo de los diferentes componentes de MAX y conservar un registro de la evolución del producto durante las distintas etapas del proyecto.

#### 5.1.3. Source Code Style Guide & Conventions
#### 5.1.4. Software Deployment Configuration



La configuración de despliegue de **MAX** permite publicar y mantener disponibles los principales componentes de la solución en servicios independientes. Esta estrategia separa el Landing Page, Frontend Web, Backend y Base de Datos, permitiendo que cada componente sea desplegado y administrado según sus requerimientos.

Los repositorios almacenados en **GitHub** constituyen la fuente principal del código utilizado para los despliegues. Para los componentes publicados se utiliza la rama `main` como referencia de las versiones destinadas al ambiente de producción.

#### Deployment Architecture

La configuración general de despliegue de MAX se organiza de la siguiente manera:

```text

                         GitHub

                            │

          ┌─────────────────┼─────────────────┐

          │                 │                 │

          ▼                 ▼                 ▼

    LANDING-PAGE           FRONT             BACK

          │                 │                 │

          ▼                 ▼                 ▼

   GitHub Pages      Cloudflare Pages      Railway

          │                 │                 │

          ▼                 ▼                 ▼

    Landing Page       Web Application     REST API

                                              │

                                              ▼

                                         MySQL Database

                                            Railway

```

De esta manera, cada componente mantiene un proceso de despliegue independiente, mientras que el Frontend y Backend permanecen integrados para proporcionar las funcionalidades de la plataforma.

#### Landing Page Deployment

El **Landing Page** se encuentra desplegado mediante **GitHub Pages** a partir del repositorio `LANDING-PAGE`.

La configuración utiliza la rama `main` y el directorio raíz del repositorio como fuente de publicación. Esto permite que la versión estable almacenada en GitHub pueda ser utilizada para mantener disponible el sitio público de MAX.

**Plataforma:** GitHub Pages  

**Ambiente:** Production  

**Branch:** `main`  

**URL:** [MAX Landing Page](https://1asi0732-2620-9086.github.io/LANDING-PAGE/)

![Deployment Landing Page](assets/dep_landi.jpeg)

#### Frontend Deployment

El **Frontend Web** se encuentra desplegado mediante **Cloudflare Workers & Pages**. El proyecto está conectado con su correspondiente repositorio de GitHub y utiliza la rama `main` para los deployments de producción.

Cuando se integra una versión destinada a producción, Cloudflare realiza el proceso necesario para construir y publicar la aplicación. La plataforma también mantiene un historial de deployments que permite consultar las versiones desplegadas y verificar su estado.

**Plataforma:** Cloudflare Workers & Pages  

**Ambiente:** Production  

**Branch:** `main`  

**URL:** [MAX Web Application](https://max-dev-front.pages.dev/auth)

![Deployment Frontend](assets/dep_front.jpeg)

#### Backend Deployment

El **Backend** se encuentra desplegado mediante **Railway** bajo el servicio `MAX_DEV_BACK`. El servicio se encuentra conectado con el repositorio correspondiente de GitHub y permite ejecutar el Backend en el ambiente de producción.

Railway proporciona las opciones necesarias para administrar el deployment, variables de entorno, métricas y logs de ejecución del servicio.

Las variables de entorno permiten mantener separada del código fuente la configuración necesaria para el funcionamiento del Backend, incluyendo información relacionada con la conexión a servicios externos y a la Base de Datos.

**Plataforma:** Railway  

**Servicio:** `MAX_DEV_BACK`  

**Ambiente:** Production  

**URL:** [MAX Backend](https://maxdevback-production.up.railway.app)

![Deployment Backend](assets/dep_back.jpeg)

#### Database Deployment

MAX utiliza **MySQL** como sistema de gestión de Base de Datos. La instancia se encuentra desplegada mediante **Railway** y es utilizada por el Backend para realizar las operaciones de persistencia requeridas por la plataforma.

La Base de Datos no funciona como un componente público de la aplicación. El acceso se realiza desde el Backend mediante la configuración correspondiente del entorno.

Entre las tablas disponibles actualmente se encuentran:

- `app_settings`

- `citas`

- `consultas`

- `estudios`

- `pacientes`

- `usuarios`

Las credenciales y parámetros necesarios para establecer la conexión con la Base de Datos deben mantenerse mediante variables de entorno y no directamente dentro del código fuente.

**Motor:** MySQL  

**Plataforma:** Railway  

**Ambiente:** Production  

**Acceso:** Interno mediante el Backend

![Deployment Database](assets/dep_db.jpeg)

#### Deployment Workflow

El flujo general utilizado para desplegar los componentes de MAX parte del código fuente administrado mediante Git y GitHub.

```text

Desarrollo local

      │

      ▼

feature/*

      │

      ▼

develop

      │

      ▼

main

      │

      ├──────────────► GitHub Pages

      │                  Landing Page

      │

      ├──────────────► Cloudflare Pages

      │                  Frontend

      │

      └──────────────► Railway

                         Backend

                            │

                            ▼

                      MySQL - Railway

```

Las funcionalidades son desarrolladas inicialmente en ramas `feature/*` y posteriormente integradas a `develop`. Una vez que los cambios corresponden a una versión estable, pueden ser integrados a `main`, rama utilizada como referencia para los componentes desplegados en producción.

#### Environment Variables

Las configuraciones que pueden variar entre ambientes o que contienen información sensible deben mantenerse mediante **variables de entorno**.

Entre estas configuraciones pueden encontrarse:

```text

Database connection

Database user

Database password

API configuration

Authentication configuration

External service credentials

```

Las credenciales no deben almacenarse directamente dentro del repositorio de GitHub.

Railway permite administrar las variables necesarias para el Backend y la Base de Datos desde la configuración del proyecto, manteniendo estos valores separados del código fuente.

#### Deployment Summary

| Componente | Plataforma | Branch / Fuente | Ambiente | Estado |
| --- | --- | --- | --- | --- |
| **Landing Page** | GitHub Pages | `main` | Production | Desplegado |
| **Frontend Web** | Cloudflare Workers & Pages | `main` | Production | Desplegado |
| **Backend** | Railway | Repositorio BACK | Production | Desplegado |
| **Base de Datos** | MySQL / Railway | Backend / Variables de entorno | Production | Desplegado |

#### Production URLs

| Componente | URL |
| --- | --- |
| **Landing Page** | [https://1asi0732-2620-9086.github.io/LANDING-PAGE/](https://1asi0732-2620-9086.github.io/LANDING-PAGE/) |
| **Frontend Web** | [https://max-dev-front.pages.dev/auth](https://max-dev-front.pages.dev/auth) |
| **Backend** | [https://maxdevback-production.up.railway.app](https://maxdevback-production.up.railway.app) |

La configuración implementada permite que los principales componentes de MAX se mantengan desplegados de manera independiente, conservando la integración necesaria entre el Frontend, Backend y Base de Datos. Asimismo, el uso de GitHub como fuente del código facilita mantener una relación entre las versiones desarrolladas y las versiones publicadas en los diferentes servicios de despliegue.

### 5.2. Product implementation & deployment
#### 5.2.1. Sprint 1
##### 5.2.1.1. Sprint Planning 1

| Campo | Detalle |
|---|---|
| **Sprint #** | Sprint 1 |
| **Date** | 2026-08-25 |
| **Time** | 09:00 PM |
| **Location** | Reunión virtual mediante Discord |
| **Prepared By** | Oscar Espinoza |
| **Attendees (to planning meeting)** | Stephano Mayrzon Landauri, Oscar Leonardos Espinoza Quijandria y Johnny Alexander Ojanama Abanto |
| **Sprint N°1 Review Summary** | Al tratarse del primer sprint del proyecto MAX, no existe una revisión de un sprint anterior. |
| **Sprint N°1 Retrospective Summary** | Al ser el primer sprint del proyecto, no se cuenta con una retrospectiva previa. La retroalimentación y las oportunidades de mejora serán evaluadas al cierre del Sprint 1. |
| **Sprint Goal & User Stories** | Para el Sprint 1 se seleccionaron las 20 historias correspondientes a la Primera Entrega del Product Backlog de MAX, relacionadas con la configuración de seguridad, gestión integral de pacientes y almacenamiento de estudios adjuntos. |
| **Sprint N°1 Goal** | **Our focus is on** implementing the first delivery of MAX, including security configuration, patient management, and storage of attached medical studies. **We believe it delivers** the functional foundation required for doctors to securely manage their patients and associated medical information. **This will be confirmed when** the 20 User Stories and Technical Stories selected for the sprint are implemented and available for review. |
| **Sprint N°1 Velocity** | **62 Story Points** |
| **Sum of Story Points** | **62 Story Points** |

##### 5.2.1.2. Aspect Leaders and Collaborators

| Team Member | Autenticación y Seguridad | Gestión de Pacientes | Dashboard | Estudios Médicos | Landing Page | Frontend Web | Backend / API | Documentación |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Stephano Mayrzon Landauri** | C | C | C | C | L | C | C | L |
| **Oscar Leonardos Espinoza Quijandria** | L | C | C | C | C | C | L | C |
| **Johnny Alexander Ojanama Abanto** | C | L | L | L | C | L | C | C |

##### 5.2.1.3. Sprint Backlog 1

| User Story Id | Título | Task Id | Título | Descripción | Estimación (hrs) | Asignado a | Estado |
|---|---|---|---|---|---:|---|---|
| TS-01 | Autenticación y seguridad JWT | T01 | Configurar seguridad JWT | Implementar la generación y validación de tokens JWT en el backend. | 4 | Oscar Espinoza | Done |
| TS-01 | Autenticación y seguridad JWT | T02 | Proteger endpoints | Configurar el acceso autenticado a los endpoints protegidos de MAX. | 3 | Oscar Espinoza | Done |
| TS-02 | Cifrado de contraseñas | T03 | Implementar cifrado | Configurar el mecanismo de cifrado para almacenar las contraseñas de manera segura. | 3 | Oscar Espinoza | Done |
| US-02 | Crear una nueva cuenta médica | T04 | Crear formulario de registro | Implementar la interfaz para registrar una nueva cuenta médica. | 3 | Johnny Ojanama | Done |
| US-02 | Crear una nueva cuenta médica | T05 | Integrar registro con backend | Conectar el formulario de registro con el servicio correspondiente de la API. | 3 | Oscar Espinoza | Done |
| US-01 | Iniciar sesión en la plataforma | T06 | Crear interfaz de login | Implementar la pantalla de inicio de sesión de MAX. | 3 | Johnny Ojanama | Done |
| US-01 | Iniciar sesión en la plataforma | T07 | Integrar autenticación | Conectar el login con el sistema de autenticación JWT. | 3 | Oscar Espinoza | Done |
| US-03 | Cerrar sesión de forma segura | T08 | Implementar cierre de sesión | Eliminar la sesión activa y redirigir al usuario hacia la pantalla de acceso. | 2 | Johnny Ojanama | Done |
| US-05 | Editar perfil básico | T09 | Implementar edición de perfil | Permitir al médico modificar su nombre y correo desde su perfil. | 3 | Johnny Ojanama | Done |
| US-05 | Editar perfil básico | T10 | Actualizar información | Conectar la edición del perfil con el servicio de actualización del backend. | 2 | Oscar Espinoza | Done |
| US-06 | Registrar un nuevo paciente | T11 | Crear formulario de paciente | Diseñar e implementar el formulario para registrar los datos de un paciente. | 4 | Johnny Ojanama | Done |
| US-06 | Registrar un nuevo paciente | T12 | Implementar registro de paciente | Crear la operación necesaria en el backend para almacenar nuevos pacientes. | 4 | Oscar Espinoza | Done |
| US-07 | Consultar el listado en tarjetas | T13 | Diseñar tarjetas de pacientes | Implementar la visualización de pacientes mediante tarjetas independientes. | 4 | Johnny Ojanama | Done |
| TS-03 | Paginación / Carga diferida | T14 | Implementar paginación | Incorporar paginación en el backend para optimizar la consulta de pacientes. | 4 | Oscar Espinoza | Done |
| TS-03 | Paginación / Carga diferida | T15 | Integrar carga paginada | Conectar la paginación del backend con el listado mostrado en el frontend. | 3 | Johnny Ojanama | Done |
| US-08 | Buscar pacientes por DNI o Nombre | T16 | Implementar buscador | Crear el componente de búsqueda de pacientes por DNI o nombre. | 3 | Johnny Ojanama | Done |
| US-08 | Buscar pacientes por DNI o Nombre | T17 | Implementar filtros de búsqueda | Integrar los criterios de búsqueda con la consulta de pacientes. | 3 | Oscar Espinoza | Done |
| US-09 | Visualizar detalle estático | T18 | Crear vista de detalle | Implementar la pantalla de información detallada del paciente en modo de solo lectura. | 3 | Johnny Ojanama | Done |
| US-10 | Editar información del paciente | T19 | Crear edición de paciente | Habilitar el formulario para modificar los datos registrados de un paciente. | 4 | Johnny Ojanama | Done |
| US-10 | Editar información del paciente | T20 | Actualizar paciente en backend | Implementar la operación de actualización de información del paciente. | 3 | Oscar Espinoza | Done |
| US-11 | Eliminar un paciente del sistema | T21 | Implementar confirmación de eliminación | Crear el flujo de confirmación mediante el nombre del paciente antes de eliminarlo. | 3 | Johnny Ojanama | Done |
| US-11 | Eliminar un paciente del sistema | T22 | Implementar eliminación | Crear la operación del backend para eliminar el registro seleccionado. | 2 | Oscar Espinoza | Done |
| US-04 | Visualizar resumen en Dashboard | T23 | Diseñar Dashboard | Implementar la interfaz principal con los indicadores del consultorio. | 4 | Johnny Ojanama | Done |
| US-04 | Visualizar resumen en Dashboard | T24 | Integrar indicadores | Obtener y presentar en el Dashboard los datos registrados en MAX. | 3 | Johnny Ojanama | Done |
| TS-04 | Almacenamiento seguro de archivos | T25 | Implementar almacenamiento | Configurar el mecanismo utilizado para almacenar archivos médicos adjuntos. | 5 | Oscar Espinoza | Done |
| TS-04 | Almacenamiento seguro de archivos | T26 | Vincular archivos con pacientes | Relacionar cada archivo almacenado con el paciente correspondiente. | 3 | Oscar Espinoza | Done |
| TS-05 | Validación de Tipos | T27 | Validar formatos de archivos | Implementar validaciones para aceptar únicamente los formatos de archivos permitidos. | 3 | Oscar Espinoza | Done |
| US-12 | Adjuntar nueva placa o estudio | T28 | Crear formulario de carga | Implementar la interfaz para seleccionar el paciente y adjuntar un estudio médico. | 4 | Johnny Ojanama | Done |
| US-12 | Adjuntar nueva placa o estudio | T29 | Integrar carga de archivos | Conectar el formulario con el servicio de almacenamiento de estudios. | 4 | Oscar Espinoza | Done |
| US-13 | Buscar placas por paciente o fecha | T30 | Crear filtros de estudios | Implementar filtros por DNI, nombre del paciente y fecha. | 3 | Johnny Ojanama | Done |
| US-13 | Buscar placas por paciente o fecha | T31 | Integrar búsqueda de estudios | Conectar los filtros con la consulta de estudios almacenados. | 3 | Oscar Espinoza | Done |
| US-14 | Identificar formato del estudio | T32 | Mostrar tipo de archivo | Incorporar indicadores visuales para diferenciar los formatos de los estudios adjuntos. | 2 | Johnny Ojanama | Done |
| US-15 | Visualizar archivo adjunto | T33 | Implementar apertura de archivos | Permitir abrir el archivo asociado a un estudio desde la interfaz de MAX. | 3 | Johnny Ojanama | Done |
| US-15 | Visualizar archivo adjunto | T34 | Validar acceso al archivo | Verificar que el archivo solicitado pueda ser recuperado correctamente desde el backend. | 2 | Oscar Espinoza | Done |

##### 5.2.1.4. Development Evidence for Sprint Review

Durante el Sprint 1, el equipo realizó la implementación de los primeros componentes de MAX en los repositorios correspondientes al producto. El desarrollo fue registrado mediante commits en GitHub, permitiendo mantener evidencia de los cambios realizados y de la evolución de los diferentes componentes de la solución.

A continuación, se presentan algunos de los principales commits asociados al desarrollo realizado durante esta primera entrega.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on |
|---|---|---|---|---|---|
| LANDING-PAGE | main | `e70c713` | Primera versión de la landing page | Implementación inicial de la Landing Page de MAX. | 2026-09-17 |
| LANDING-PAGE | main | `120d36b` | Create CNAME | Configuración inicial del dominio para la publicación de la Landing Page. | 2026-09-17 |
| LANDING-PAGE | main | `e7352a7` | Delete CNAME | Ajuste de la configuración utilizada para la publicación de la Landing Page. | 2026-09-17 |
| FRONT | main | `63ed173` | Primera versión del frontend de MAX | Incorporación de la primera versión funcional del Frontend Web de MAX. | 2026-09-17 |
| MOBILE | main | `601fc35` | Primera versión de la aplicación móvil de MAX | Incorporación de la primera versión de la aplicación móvil del producto MAX. | 2026-09-17 |

##### 5.2.1.5. Execution Evidence for Sprint Review
##### 5.2.1.6. Services Documentation Evidence for Sprint Review
##### 5.2.1.7. Software Deployment Evidence for Sprint Review
##### 5.2.1.8. Team Collaboration Insights during Sprint
*(Nota: Repetir esta estructura para Sprint 2, 3, y 4 según corresponda cada hito de evaluación)*
#### 5.2.2. Implemented Landing Page Evidence
#### 5.2.3. Implemented Frontend-Web Application Evidence
#### 5.2.4. Implemented Native-Mobile Application Evidence
#### 5.2.5. Implemented RESTful API and/or Serverless Backend Evidence
#### 5.2.6. RESTful API Documentation
#### 5.2.7. Team Collaboration Insights
### 5.3. Video About-the-Product

---

## Conclusiones
### Conclusiones y recomendaciones
### Video About-the-Team

---

## Bibliografía

---

## Anexos
### Anexo A. Videos de Exposiciones
*(Incluir de forma progresiva el título e hipervínculo al video de Exposición en Microsoft Stream para cada entrega AV1, TB1, AV2, TB2).*
