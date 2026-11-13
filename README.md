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
| TB1 | 16/09/2026 | Stephano Mayrzon Landauri Preciado<br>Oscar Leonardo Espinoza Quijandria<br>Johnny Alexander Ojanama Abanto | Primera entrega del informe de MAX. Desarrollo de los capítulos I al IV: presentación de la startup y de la solución, análisis de la problemática, investigación de usuarios, definición de requerimientos, historias de usuario, Product Backlog y diseño del producto. |
| TP1 | 07/10/2026 | Stephano Mayrzon Landauri Preciado<br>Oscar Leonardo Espinoza Quijandria<br>Johnny Alexander Ojanama Abanto | Actualización del informe para el Trabajo Parcial. Incorporación y consolidación de los capítulos V, VI y VII: implementación de los componentes de MAX, documentación de pruebas y validación, configuración de integración continua y recopilación de evidencias de GitHub Actions. Actualización del índice, del Student Outcome y de la documentación sobre las prácticas de entrega y despliegue. |

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
- [Capítulo VI: Product Verification & Validation](#capítulo-vi-product-verification--validation)
  - [6.1. Testing Suites & Validation](#61-testing-suites--validation)
    - [6.1.1. Core Entities Unit Tests](#611-core-entities-unit-tests)
      - [6.1.1.1. IAM](#6111-iam)
        - [6.1.1.1.1. Backend](#61111-backend)
        - [6.1.1.1.2. iOS](#61112-ios)
        - [6.1.1.1.3. Android](#61113-android)
        - [6.1.1.1.4. Web](#61114-web)
        - [6.1.1.1.5. Resumen agregado de IAM](#61115-resumen-agregado-de-iam)
      - [6.1.1.2. Patients](#6112-patients)
        - [6.1.1.2.1. Backend](#61121-backend)
        - [6.1.1.2.2. iOS](#61122-ios)
        - [6.1.1.2.3. Android](#61123-android)
        - [6.1.1.2.4. Web](#61124-web)
        - [6.1.1.2.5. Resumen agregado de Patients](#61125-resumen-agregado-de-patients)
      - [6.1.1.3. Studies](#6113-studies)
        - [6.1.1.3.1. Backend](#61131-backend)
        - [6.1.1.3.2. iOS](#61132-ios)
        - [6.1.1.3.3. Android](#61133-android)
        - [6.1.1.3.4. Web](#61134-web)
        - [6.1.1.3.5. Resumen agregado de Studies](#61135-resumen-agregado-de-studies)
      - [6.1.1.4. Pruebas complementarias de la landing y del cliente móvil](#6114-pruebas-complementarias-de-la-landing-y-del-cliente-móvil)
      - [6.1.1.5. Resumen consolidado de unidades y componentes](#6115-resumen-consolidado-de-unidades-y-componentes)
    - [6.1.2. Core Integration Tests](#612-core-integration-tests)
      - [6.1.2.1. Integración de IAM](#6121-integración-de-iam)
      - [6.1.2.2. Integración de Patients](#6122-integración-de-patients)
      - [6.1.2.3. Integración de Studies](#6123-integración-de-studies)
      - [6.1.2.4. Comandos de ejecución](#6124-comandos-de-ejecución)
      - [6.1.2.5. Evidencias de ejecución](#6125-evidencias-de-ejecución)
    - [6.1.3. Core Behavior-Driven Development](#613-core-behavior-driven-development)
      - [6.1.3.1. IAM](#6131-iam)
      - [6.1.3.2. Patients](#6132-patients)
      - [6.1.3.3. Studies](#6133-studies)
      - [6.1.3.4. Trazabilidad](#6134-trazabilidad)
    - [6.1.4. Core System Tests](#614-core-system-tests)
      - [6.1.4.1. Aplicación web](#6141-aplicación-web)
      - [6.1.4.2. Aplicación Android](#6142-aplicación-android)
      - [6.1.4.3. Aplicación iOS](#6143-aplicación-ios)
- [Capítulo VII: DevOps Practices](#capítulo-vii-devops-practices)
  - [7.1. Continuous Integration](#71-continuous-integration)
    - [7.1.1. Tools and Practices](#711-tools-and-practices)
    - [7.1.2. Build & Test Suite Pipeline Components](#712-build--test-suite-pipeline-components)
  - [7.2. Continuous Delivery](#72-continuous-delivery)
    - [7.2.1. Tools and Practices](#721-tools-and-practices)
    - [7.2.2. Stages Deployment Pipeline Components](#722-stages-deployment-pipeline-components)
  - [7.3. Continuous Deployment](#73-continuous-deployment)
    - [7.3.1. Tools and Practices](#731-tools-and-practices)
    - [7.3.2. Production Deployment Pipeline Components](#732-production-deployment-pipeline-components)
  - [7.4. Continuous Monitoring](#74-continuous-monitoring)
    - [7.4.1. Tools and Practices](#741-tools-and-practices)
    - [7.4.2. Monitoring Pipeline Components](#742-monitoring-pipeline-components)
    - [7.4.3. Alerting Pipeline Components](#743-alerting-pipeline-components)
    - [7.4.4. Notification Pipeline Components](#744-notification-pipeline-components)
- [Capítulo VIII: Experiment-Driven Development](#capítulo-viii-experiment-driven-development)
  - [8.1. Experiment Planning](#81-experiment-planning)
    - [8.1.1. As-Is Summary.](#811-as-is-summary)
    - [8.1.2. Raw Material: Assumptions, Knowledge Gaps, Ideas, Claims.](#812-raw-material-assumptions-knowledge-gaps-ideas-claims)
    - [8.1.3. Experiment-Ready Questions.](#813-experiment-ready-questions)
    - [8.1.4. Question Backlog.](#814-question-backlog)
    - [8.1.5. Experiment Cards.](#815-experiment-cards)
  - [8.2. Experiment Design](#82-experiment-design)
    - [8.2.1. Hypotheses.](#821-hypotheses)
    - [8.2.2. Domain Business Metrics](#822-domain-business-metrics)
    - [8.2.3. Measures.](#823-measures)
    - [8.2.4. Conditions.](#824-conditions)
    - [8.2.5. Scale Calculations and Decisions.](#825-scale-calculations-and-decisions)
    - [8.2.6. Methods Selection.](#826-methods-selection)
    - [8.2.7. Data Analytics: Goals, KPIs and Metrics Selection.](#827-data-analytics-goals-kpis-and-metrics-selection)
    - [8.2.8. Web and Mobile Tracking Plan.](#828-web-and-mobile-tracking-plan)
  - [8.3. Experimentation](#83-experimentation)
    - [8.3.1. To-Be User Stories.](#831-to-be-user-stories)
    - [8.3.2. To-Be Product Backlog](#832-to-be-product-backlog)
- [Conclusiones](#conclusiones)
  - [Conclusiones y recomendaciones](#conclusiones-y-recomendaciones)
  - [Video About-the-Team](#video-about-the-team)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)
  - [Anexo A. Videos de Exposiciones](#anexo-a-videos-de-exposiciones)

---

## Student Outcome

El desarrollo del proyecto MAX contribuye al Student Outcome 3, relacionado con la capacidad de comunicarse eficazmente con diferentes audiencias. A continuación, se describen las acciones realizadas por los integrantes durante AV1 y TP, así como las conclusiones correspondientes a cada criterio.

| Criterio específico | Acciones realizadas | Conclusiones |
|---|---|---|
| **3.c1. Comunica oralmente sus ideas y/o resultados con objetividad a público de diferentes especialidades y niveles jerárquicos, en el marco del desarrollo de un proyecto en ingeniería de software.** | **Stephano Mayrzon Landauri Preciado**<br><br>**AV1:** Comunicó los avances y resultados correspondientes a los capítulos 1 y 2 y parte del capítulo 5, explicando la propuesta de MAX, la problemática identificada, los segmentos objetivo, el análisis competitivo, los resultados de las entrevistas, el Needfinding y aspectos relacionados con la gestión y configuración del proyecto.<br><br>**TP:** Explicó los avances de MAX y su relación con las necesidades de los usuarios, presentando las funcionalidades desarrolladas y el valor de la solución. Organizó la información para que la audiencia comprendiera la evolución del producto y los resultados de esta entrega.<br><br>**AV2:** Preparó la comunicación de los resultados correspondientes al apartado 6.2, Static Testing & Verification, explicando los estándares y convenciones de codificación, el análisis de calidad y seguridad del código, y las revisiones técnicas realizadas sobre los componentes de MAX. Organizó las evidencias de análisis estático, auditorías de dependencias y verificaciones mediante GitHub, diferenciando los resultados comprobados de las actividades pendientes.<br><br>**Oscar Leonardo Espinoza Quijandria**<br><br>**AV1:** Comunicó los aspectos técnicos relacionados con el despliegue de MAX, explicando la configuración y publicación de los diferentes componentes de la solución, incluyendo el Landing Page, Frontend, Backend y Base de Datos.<br><br>**TP:** Explicó la integración de los componentes de MAX, las pruebas realizadas y el funcionamiento de los flujos de integración continua. Presentó las evidencias de ejecución y sus resultados, diferenciando las validaciones efectuadas de las actividades de entrega y despliegue aún pendientes.<br><br>**AV2:** Preparó la exposición del capítulo VIII, Experiment-Driven Development, explicando el proceso de planificación y diseño de experimentos mediante el análisis As-Is, la identificación de premisas, preguntas de experimentación, hipótesis, métricas, condiciones y métodos de evaluación. Asimismo, organizó la presentación de las historias de usuario y el Product Backlog To-Be, relacionando las oportunidades de mejora con los objetivos y necesidades identificadas para MAX.<br><br>**Johnny Alexander Ojanama Abanto**<br><br>**AV1:** Comunicó los avances y resultados correspondientes al capítulo 3, explicando los requerimientos y especificaciones definidos para MAX y su relación con las funcionalidades planteadas para la solución.<br><br>**TP:** Explicó la relación entre los requerimientos, las historias de usuario y las funcionalidades implementadas. Presentó los avances de validación del producto y la forma en que los resultados obtenidos permiten revisar el cumplimiento del alcance de esta entrega.<br><br>**AV2:** Pendiente de incorporar las actividades de comunicación oral correspondientes a su participación en este avance. | **AV1:** El equipo fortaleció su capacidad para comunicar oralmente los avances y resultados del proyecto MAX de manera objetiva y organizada. Cada integrante presentó los aspectos correspondientes a su participación en el proyecto, permitiendo comunicar tanto elementos relacionados con la investigación y definición del producto como aspectos técnicos de requerimientos, desarrollo y despliegue.<br><br>**TP:** El equipo fortaleció la presentación de resultados mediante explicaciones apoyadas en demostraciones, capturas y reportes de pruebas. La distribución de temas permitió relacionar el valor del producto con su implementación y validación, utilizando un lenguaje comprensible para audiencias técnicas y no técnicas y señalando el alcance de las evidencias presentadas.<br><br>**AV2:** El equipo fortaleció la organización y comunicación de los avances relacionados con la calidad del software y el desarrollo dirigido por experimentos. La preparación de explicaciones sobre análisis estático, seguridad, planificación experimental, hipótesis y mejoras propuestas permitió relacionar los aspectos técnicos con las necesidades de los usuarios. Asimismo, se priorizó una comunicación objetiva, diferenciando las evidencias verificadas de las propuestas y actividades pendientes, para facilitar la comprensión del proyecto por parte de públicos técnicos y no técnicos. |
| **3.c2. Comunica en forma escrita ideas y/o resultados con objetividad a público de diferentes especialidades y niveles jerárquicos, en el marco del desarrollo de un proyecto de ingeniería de software.** | **Stephano Mayrzon Landauri Preciado**<br><br>**AV1:** Elaboró la documentación correspondiente a los capítulos 1 y 2 y parte del capítulo 5, incluyendo la definición de MAX, análisis de la problemática, Lean UX, segmentos objetivo, análisis competitivo, entrevistas, Needfinding y documentación relacionada con la gestión y configuración del proyecto.<br><br>**TP:** Contribuyó a la actualización y organización del informe, relacionando la propuesta del producto con los avances de implementación. Revisó la claridad de las descripciones, la estructura del contenido y la presentación de las evidencias correspondientes a esta entrega.<br><br>**AV2:** Desarrolló la documentación del apartado 6.2, Static Testing & Verification, incluyendo 6.2.1 Static Code Analysis, 6.2.1.1 Coding Standard & Code Conventions, 6.2.1.2 Code Quality & Code Security y 6.2.2 Reviews. Organizó la información sobre convenciones de programación, herramientas de análisis estático, controles de seguridad, auditorías de dependencias y mecanismos de revisión de código. Incorporó tablas de evaluación, hallazgos, conclusiones y referencias a evidencias de los repositorios de MAX, manteniendo la distinción entre las verificaciones realizadas y aquellas pendientes.<br><br>**Oscar Leonardo Espinoza Quijandria**<br><br>**AV1:** Elaboró la documentación y evidencias relacionadas con la configuración y despliegue de los componentes de MAX, incluyendo el Landing Page, Frontend, Backend y Base de Datos.<br><br>**TP:** Documentó la configuración técnica, las pruebas y las prácticas de integración continua de MAX. Organizó capturas, reportes y referencias a las ejecuciones de GitHub Actions para respaldar los resultados, precisando los entornos utilizados y las actividades que permanecen pendientes.<br><br>**AV2:** Desarrolló la documentación del capítulo VIII, Experiment-Driven Development, abarcando la planificación de experimentos (8.1), el resumen As-Is, Raw Material, Experiment-Ready Questions, Question Backlog y Experiment Cards. Asimismo, elaboró el diseño experimental (8.2), incluyendo hipótesis, métricas de negocio, medidas, condiciones, cálculos de escala, selección de métodos, objetivos de analítica, KPIs y el Web and Mobile Tracking Plan. Finalmente, desarrolló la sección de Experimentation (8.3), estructurando las To-Be User Stories y el To-Be Product Backlog para organizar y priorizar las mejoras propuestas de MAX. La documentación relaciona las necesidades de los usuarios con las hipótesis, los criterios de evaluación y la evolución planificada del producto.<br><br>**Johnny Alexander Ojanama Abanto**<br><br>**AV1:** Elaboró la documentación correspondiente al capítulo 3, estructurando los requerimientos y especificaciones de la solución de acuerdo con las necesidades identificadas para MAX.<br><br>**TP:** Contribuyó a documentar la relación entre las historias de usuario, las funcionalidades implementadas y los criterios de validación. Revisó la consistencia de los requerimientos y colaboró en la organización de los resultados y conclusiones de esta entrega.<br><br>**AV2:** Pendiente de incorporar las actividades de documentación correspondientes a su participación en este avance. | **AV1:** El equipo desarrolló documentación técnica de manera clara, objetiva y estructurada. La distribución del trabajo permitió integrar en un mismo proyecto la investigación de usuarios, la definición de requerimientos y los aspectos técnicos de desarrollo y despliegue. El uso de Markdown y GitHub permitió mantener la información organizada y comprensible para diferentes tipos de audiencia.<br><br>**TP:** El equipo consolidó un informe que vincula los requerimientos con la implementación, las pruebas y las prácticas DevOps. La actualización del índice y el registro de versiones facilitó el seguimiento de los cambios, mientras que la incorporación de evidencias permitió sustentar los resultados y distinguir los avances comprobados de las tareas pendientes.<br><br>**AV2:** El equipo amplió la documentación de MAX mediante el desarrollo de apartados relacionados con la verificación estática del software y el desarrollo dirigido por experimentos. Se organizaron los estándares de codificación, los análisis de calidad y seguridad, las revisiones técnicas, las premisas, las hipótesis, las métricas y las propuestas de mejora del producto. La integración de tablas, criterios de evaluación, referencias técnicas e historias de usuario To-Be permitió mantener una documentación estructurada, objetiva y trazable, facilitando la comprensión de los avances y estableciendo una base para la validación y evolución continua de MAX. |


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

Durante el Sprint 1 se realizaron pruebas de ejecución de las funcionalidades implementadas para comprobar el correcto funcionamiento de los componentes desarrollados en MAX.

Las siguientes evidencias muestran la ejecución de las principales funcionalidades correspondientes a la Primera Entrega, incluyendo el acceso a la plataforma, la visualización del Dashboard, la gestión de pacientes y la administración de estudios médicos.

##### Inicio de sesión

La plataforma permite al médico ingresar mediante sus credenciales para acceder a las funcionalidades disponibles en MAX.

![Inicio de sesión de MAX](assets/sprint1-login.jpeg)

##### Dashboard principal

Después de iniciar sesión, el médico puede acceder al Dashboard principal, desde donde puede visualizar información general y acceder a los diferentes módulos de la plataforma.

![Dashboard de MAX](assets/sprint1-dashboard.jpeg)

##### Gestión de pacientes

MAX permite visualizar los pacientes registrados y acceder a las funcionalidades relacionadas con su gestión.

![Listado de pacientes](assets/sprint1-pacientes.jpeg)

Asimismo, el médico puede registrar nuevos pacientes mediante el formulario correspondiente.

![Registro de paciente](assets/sprint1-registro-paciente.jpeg)

##### Búsqueda y detalle de pacientes

El sistema permite buscar pacientes mediante los criterios implementados y consultar la información correspondiente al paciente seleccionado.

![Detalle del paciente](assets/sprint1-detalle-paciente.jpeg)

##### Gestión de estudios médicos

El módulo de estudios permite asociar archivos médicos a los pacientes registrados y posteriormente consultar los estudios almacenados.

![Registro de estudio médico](assets/sprint1-registro-estudio.jpeg)

![Listado de estudios médicos](assets/sprint1-estudios.jpeg)

Estas evidencias permiten comprobar la ejecución de las principales funcionalidades desarrolladas durante el Sprint 1 y demostrar el avance funcional alcanzado en la Primera Entrega de MAX.

##### 5.2.1.6. Services Documentation Evidence for Sprint Review

Durante el Sprint 1 se implementaron los servicios necesarios para soportar las principales funcionalidades correspondientes a la Primera Entrega de MAX. Estos servicios permiten la comunicación entre el Frontend Web y el Backend de la plataforma, gestionando las operaciones relacionadas con autenticación, usuarios, pacientes y estudios médicos.

La documentación de los servicios permite identificar y verificar las operaciones disponibles en la API, así como los métodos HTTP, parámetros, estructuras de datos y respuestas utilizadas durante la comunicación entre los componentes de MAX.

##### Servicios de autenticación

Los servicios de autenticación permiten gestionar el acceso de los médicos a la plataforma. Durante esta primera entrega se implementaron las operaciones necesarias para el registro e inicio de sesión, utilizando mecanismos de autenticación para proteger el acceso a los recursos de MAX.

![Servicios de autenticación](assets/sprint1-api-auth.jpeg)

##### Servicios de pacientes

Los servicios relacionados con pacientes permiten realizar las operaciones necesarias para registrar, consultar, buscar, actualizar y eliminar la información de los pacientes asociados al médico.

Estos servicios constituyen una parte central de la Primera Entrega, debido a que permiten gestionar la información necesaria para posteriormente relacionar citas, consultas y estudios médicos con cada paciente.

![Servicios de pacientes](assets/sprint1-api-pacientes.jpeg)

##### Servicios de estudios médicos

Los servicios de estudios permiten gestionar los archivos médicos asociados a los pacientes. A través de estos servicios, la plataforma puede registrar y consultar estudios, así como relacionarlos con el paciente correspondiente.

![Servicios de estudios médicos](assets/sprint1-api-estudios.jpeg)

##### Verificación de los servicios

Durante el Sprint Review se verificó la disponibilidad y funcionamiento de los servicios implementados mediante solicitudes realizadas a la API. Esta validación permitió comprobar la comunicación entre el Frontend Web y el Backend y verificar que las operaciones necesarias para la Primera Entrega estuvieran disponibles.

![Ejecución de servicios de la API](assets/sprint1-api-ejecucion.jpeg)

Las evidencias presentadas muestran la documentación y ejecución de los servicios utilizados durante el Sprint 1, proporcionando trazabilidad entre las funcionalidades implementadas en el Frontend Web y las operaciones disponibles en el Backend de MAX.

##### 5.2.1.7. Software Deployment Evidence for Sprint Review

Durante el Sprint 1 se realizaron actividades de despliegue de los principales componentes de MAX con el objetivo de disponer de versiones accesibles de la solución y comprobar la integración entre los diferentes componentes desarrollados.

Para el despliegue se utilizaron diferentes servicios según las necesidades de cada componente de la arquitectura. La Landing Page fue publicada mediante GitHub Pages, el Frontend Web mediante Cloudflare Pages y el Backend junto con la base de datos MySQL mediante Railway.

##### Landing Page Deployment

La Landing Page de MAX fue desplegada utilizando **GitHub Pages**, permitiendo disponer de una versión pública del sitio informativo del producto.

**Deployment URL:**  
https://1asi0732-2620-9086.github.io/LANDING-PAGE/

![Landing Page Deployment](assets/dep_landi.jpeg)

##### Frontend Web Application Deployment

El Frontend Web de MAX fue desplegado mediante **Cloudflare Pages**, permitiendo acceder a la aplicación desde un entorno web publicado.

**Deployment URL:**  
https://max-dev-front.pages.dev/auth

![Frontend Web Deployment](assets/dep_front.jpeg)

##### Backend Deployment

El Backend de MAX fue desplegado mediante **Railway**, proporcionando el entorno necesario para ejecutar los servicios utilizados por el Frontend Web.

**Deployment URL:**  
https://maxdevback-production.up.railway.app

![Backend Deployment](assets/dep_back.jpeg)

##### Database Deployment

La base de datos **MySQL** utilizada por MAX se encuentra alojada en Railway y conectada con el servicio Backend.

La instancia contiene las estructuras de datos necesarias para almacenar la información gestionada por la plataforma, incluyendo usuarios, pacientes, citas, consultas, estudios y configuraciones de la aplicación.

A diferencia de los componentes web, la base de datos no dispone de una URL pública destinada al usuario final, debido a que su acceso se realiza desde el Backend mediante la configuración correspondiente del entorno.

![Database Deployment](assets/dep_db.jpeg)

##### Deployment Architecture

La arquitectura de despliegue utilizada durante el desarrollo de MAX puede representarse mediante el siguiente flujo:

**Usuario → Landing Page / Frontend Web → Backend → MySQL**

De esta manera, el usuario accede a las interfaces publicadas de MAX, mientras que el Frontend Web consume los servicios proporcionados por el Backend y este se comunica con la base de datos MySQL para gestionar la persistencia de la información.

Las evidencias presentadas permiten comprobar que los principales componentes desarrollados para MAX cuentan con entornos de despliegue que permiten validar su funcionamiento e integración durante el Sprint Review.

##### 5.2.1.8. Team Collaboration Insights during Sprint
![Team Collaboration Insights](assets/Inside.png)

*(Nota: Repetir esta estructura para Sprint 2, 3, y 4 según corresponda cada hito de evaluación)*

### 5.2.2. Implemented Landing Page Evidence

La Landing Page de MAX fue implementada con el objetivo de presentar la propuesta de valor del producto y brindar información sobre las principales características de la plataforma dirigida a médicos cirujanos y pacientes.

La página permite a los usuarios conocer el propósito de MAX, sus principales funcionalidades, valores y medios de contacto.

La Landing Page se encuentra desplegada mediante **GitHub Pages** y puede ser consultada públicamente mediante el siguiente enlace:

**Landing Page:**  
https://1asi0732-2620-9086.github.io/LANDING-PAGE/

#### Página principal

La sección principal presenta MAX y permite al usuario identificar rápidamente el propósito de la plataforma.

![Landing Page - Inicio](assets/landing-page-home.png)

#### Sección Nosotros

Esta sección presenta información sobre MAX y el propósito de la solución, permitiendo que los visitantes comprendan la propuesta del producto.

![Landing Page - Nosotros](assets/landing-page-nosotros.png)

#### Sección de Funcionalidades

Esta sección presenta las principales funcionalidades ofrecidas por MAX para facilitar la interacción entre médicos cirujanos y pacientes.

![Landing Page - Funcionalidades](assets/landing-page-funcionalidades.png)

#### Sección de Valores

Esta sección presenta los principales valores considerados para el desarrollo de MAX: innovación, seguridad, confianza, accesibilidad y responsabilidad.

![Landing Page - Valores](assets/landing-page-valores.png)

#### Sección de Contacto

Finalmente, la Landing Page cuenta con una sección de contacto que proporciona información para comunicarse con el equipo responsable de MAX.

![Landing Page - Contacto](assets/landing-page-contacto.png)

Las evidencias presentadas demuestran la implementación y publicación de la Landing Page de MAX, proporcionando a los usuarios un punto inicial para conocer la propuesta de valor y las principales características del producto.


### 5.2.3. Implemented Frontend-Web Application Evidence

La aplicación Frontend Web de MAX fue implementada para proporcionar a los médicos cirujanos una interfaz desde la cual puedan acceder a las principales funcionalidades de la plataforma.

El Frontend Web permite interactuar con los servicios proporcionados por el Backend de MAX y gestionar la información disponible en la plataforma.

La aplicación se encuentra desplegada mediante **Cloudflare Pages** y puede ser consultada mediante el siguiente enlace:

**Frontend Web:**  
https://max-dev-front.pages.dev/auth

#### Autenticación

La aplicación cuenta con una interfaz de autenticación que permite al usuario ingresar a MAX utilizando sus credenciales.

![Frontend Web - Login](assets/sprint1-login.jpeg)

#### Dashboard

Después de iniciar sesión, el usuario puede acceder al Dashboard principal de MAX, desde donde puede visualizar información general y acceder a los diferentes módulos disponibles.

![Frontend Web - Dashboard](assets/sprint1-dashboard.jpeg)

#### Gestión de pacientes

El módulo de pacientes permite visualizar y gestionar la información de los pacientes registrados en la plataforma.

![Frontend Web - Pacientes](assets/sprint1-pacientes.jpeg)

#### Registro de pacientes

La aplicación permite registrar nuevos pacientes mediante un formulario destinado al ingreso de su información.

![Frontend Web - Registro de Paciente](assets/sprint1-registro-paciente.jpeg)

#### Detalle del paciente

El médico puede acceder al detalle de un paciente para consultar la información registrada y las opciones disponibles relacionadas con su gestión.

![Frontend Web - Detalle de Paciente](assets/sprint1-detalle-paciente.jpeg)

#### Gestión de estudios médicos

MAX permite gestionar estudios médicos asociados a los pacientes, facilitando el almacenamiento y consulta de los archivos registrados en la plataforma.

![Frontend Web - Estudios Médicos](assets/sprint1-estudios.jpeg)

Las evidencias presentadas permiten comprobar la implementación de las principales interfaces del Frontend Web de MAX y su integración con las funcionalidades desarrolladas para el producto.


### 5.2.4. Implemented Native-Mobile Application Evidence

MAX cuenta con una aplicación móvil orientada a facilitar el acceso de los pacientes a las funcionalidades disponibles desde dispositivos móviles.

La aplicación móvil constituye uno de los componentes de la solución MAX y busca proporcionar una experiencia adaptada a este tipo de dispositivos, permitiendo consultar información relacionada con la atención médica desde una interfaz accesible.

#### Inicio de sesión

La aplicación móvil dispone de una interfaz de autenticación mediante la cual el usuario puede ingresar utilizando sus credenciales.

![Mobile - Login](assets/mobile-login.png)

#### Pantalla principal

Después de autenticarse, el usuario puede acceder a la pantalla principal de la aplicación y consultar las funcionalidades disponibles.

![Mobile - Inicio](assets/mobile-home.png)

#### Gestión de citas

La aplicación móvil permite acceder a la información relacionada con las citas del usuario, facilitando su consulta desde un dispositivo móvil.

![Mobile - Citas](assets/mobile-citas.png)

#### Documentación médica

Desde la aplicación, el paciente puede acceder a la información y documentación médica que se encuentre disponible dentro de MAX.

![Mobile - Documentos](assets/mobile-documentos.png)

### 5.2.5. Implemented RESTful API and/or Serverless Backend Evidence

El Backend de MAX proporciona los servicios necesarios para gestionar la lógica de negocio y permitir la comunicación entre las aplicaciones cliente y la información almacenada en la base de datos.

El Backend se encuentra desplegado mediante **Railway** y se comunica con una base de datos **MySQL** utilizada para la persistencia de la información de la plataforma.

**Backend:**  
https://maxdevback-production.up.railway.app

#### Backend desplegado

El servicio Backend de MAX se encuentra publicado en Railway, proporcionando el entorno de ejecución necesario para los servicios utilizados por la plataforma.

![Backend - Railway](assets/dep_back.jpeg)

#### Servicios de autenticación

El Backend proporciona servicios relacionados con los procesos de autenticación y control de acceso a la plataforma.

![Backend - Authentication](assets/sprint1-api-auth.jpeg)

#### Servicios de pacientes

Los servicios relacionados con pacientes permiten realizar las operaciones necesarias para registrar, consultar, actualizar y gestionar la información de los pacientes.

![Backend - Pacientes](assets/sprint1-api-pacientes.jpeg)

#### Servicios de estudios médicos

El Backend proporciona servicios para gestionar los estudios médicos asociados a los pacientes y permitir su utilización desde las aplicaciones cliente.

![Backend - Estudios](assets/sprint1-api-estudios.jpeg)

#### Persistencia de información

La información gestionada por los servicios del Backend es almacenada en una base de datos **MySQL** desplegada en Railway.

Entre las estructuras disponibles se encuentran tablas relacionadas con usuarios, pacientes, citas, consultas, estudios y configuraciones de la aplicación.

![Backend - Base de Datos](assets/dep_db.jpeg)

Las evidencias presentadas permiten comprobar la implementación del Backend de MAX, su despliegue y su integración con la base de datos utilizada para la persistencia de la información.


### 5.2.6. RESTful API Documentation

La API de MAX permite la comunicación entre las aplicaciones cliente y el Backend mediante servicios orientados a gestionar los diferentes recursos utilizados por la plataforma.

La documentación de la API permite identificar las operaciones disponibles, métodos HTTP, parámetros, estructuras de solicitud y respuestas proporcionadas por los servicios.

#### Documentación general de la API

La documentación proporciona una vista general de los servicios disponibles en el Backend de MAX.

![API Documentation - General](assets/api-documentation.jpeg)

#### Authentication API

Los servicios de autenticación permiten gestionar el acceso de los usuarios a MAX y las operaciones relacionadas con la autenticación de la plataforma.

![API Documentation - Authentication](assets/sprint1-api-auth.jpeg)

#### Patients API

Los servicios correspondientes a pacientes permiten realizar las operaciones necesarias para administrar la información de los pacientes registrados en MAX.

![API Documentation - Patients](assets/sprint1-api-pacientes.jpeg)

#### Medical Studies API

Los servicios relacionados con estudios médicos permiten gestionar la información y los archivos asociados a los pacientes.

![API Documentation - Studies](assets/sprint1-api-estudios.jpeg)

#### Ejecución de servicios

La documentación de la API permite comprobar el funcionamiento de los servicios mediante la ejecución de solicitudes y la visualización de las respuestas proporcionadas por el Backend.

![API Documentation - Execution](assets/sprint1-api-ejecucion.jpeg)

La documentación de la API proporciona una referencia técnica de los servicios implementados en MAX y facilita la comprensión de la comunicación entre el Frontend Web, la aplicación móvil y el Backend.


### 5.2.7. Team Collaboration Insights

Durante el desarrollo de MAX, el equipo trabajó de manera colaborativa en los diferentes componentes que conforman la solución, incluyendo la Landing Page, el Frontend Web, la aplicación móvil, el Backend y la documentación del proyecto.

Para la gestión del código fuente se utilizó **GitHub**, permitiendo mantener repositorios independientes para los diferentes componentes del producto y registrar los cambios realizados durante el proceso de desarrollo.

La coordinación del equipo se realizó principalmente mediante reuniones virtuales en **Discord**, donde los integrantes revisaron avances, distribuyeron actividades y discutieron los inconvenientes encontrados durante la implementación.

La utilización de la matriz **Leadership and Collaboration Matrix (LACX)** permitió establecer líderes y colaboradores para los principales aspectos del proyecto, facilitando la distribución de responsabilidades entre los integrantes del equipo.

Durante el desarrollo también se identificó la importancia de mantener una comunicación constante entre los responsables del Frontend y Backend, debido a que la correcta integración de ambos componentes depende de la disponibilidad y estructura de los servicios proporcionados por la API.

Asimismo, el uso de repositorios en GitHub permitió mantener trazabilidad sobre los cambios realizados y facilitó la integración progresiva de los diferentes componentes desarrollados.

Como resultado del trabajo realizado, el equipo logró avanzar en la implementación e integración de los principales componentes de MAX, obteniendo una solución compuesta por una Landing Page, una aplicación Frontend Web, una aplicación móvil, un Backend y una base de datos para la persistencia de la información.

La experiencia obtenida durante las diferentes iteraciones permitió identificar oportunidades de mejora relacionadas con la coordinación del equipo, la integración continua de componentes, el seguimiento de actividades y la validación temprana de las funcionalidades desarrolladas.

El siguiente video presenta MAX, su propuesta de valor, las principales funcionalidades de la plataforma y la forma en que facilita la interacción entre médicos cirujanos y pacientes.

[▶️ Ver Video About-the-Product de MAX](https://youtu.be/QQunga5vDYM)
---


# MAX — Product Verification & Validation y DevOps Practices

Fecha de validación: **07/10/2026, America/Lima (UTC−05:00)**. Entorno: **LOCAL AISLADO**, datos sintéticos. No se modificó la BD de producción, no se hicieron commits/push y no se publicaron nuevas versiones.

Este documento integra los resultados de la entrega de evidencias del 7 de octubre de 2026. Sus rutas están preparadas para ubicar el Markdown en la raíz del repositorio del informe, junto con `assets/` y `docs/`. Se conserva la distinción entre pruebas locales, configuración preparada y observaciones de servicios publicados.

**Alcance de esta revisión:** se contrastaron los recuentos con los XML, JSON y logs recibidos y se revisaron las imágenes. No se volvieron a ejecutar las aplicaciones ni se accedió a los dashboards remotos. Los archivos fuente de pruebas, scripts y workflows se citan por su ubicación en los repositorios del equipo; no están incluidos en los ZIP de evidencias recibidos.

**Estado de la entrega:** hay validaciones locales documentadas. No se acredita ejecución remota de los nuevos workflows, un ambiente de staging ni un nuevo despliegue clínico a producción. El paquete conserva los reportes y capturas originales; los binarios JAR/APK y bundles de aplicación se mantienen en la entrega original de Codex.

## Stack, arquitectura y versiones comprobadas

| Componente | Stack y arquitectura observados | Versión base evaluada |
|---|---|---|
| Backend | Monolito Spring Boot, contextos `auth`, `admin`, `pacientes`, `citas`, `consultas`, `estudios`; capas application/domain/infrastructure/interfaces; JPA, autenticación mediante cookie HttpOnly y control de sesiones | Java 21.0.10, Boot 4.0.8, Maven Wrapper 3.9.12; `17e93c08b92cad83fdb4ea232b06c21eb70c260f` + cambios locales |
| BD local | MySQL nativo con datadir independiente, puerto 33307. Flyway valida V1–V11. H2 complementa las pruebas HTTP | MySQL servidor 8.0.45; Flyway 11.14.1; H2 2.4.240 |
| Web clínica | Angular standalone, organización por contextos, componentes/fachadas/servicios/stores/clientes; `/api` mediante proxy | Angular 21.2.23, CLI/build 21.2.24, CDK 21.2.14, TS 5.9.3; `63ed173284647024a7612d5a1cf8f8b0290eff35` + cambios locales |
| Android | Flutter/Dart; `AppController` coordina operaciones, modelos y `MaxApi`; Dio y almacenamiento seguro para cookies | Flutter 3.41.9, Dart 3.11.5, Dio 5.11.1, app 1.0.0+1; `601fc357b9522e8782f8eae3498c7b98c6638673` + cambios locales |
| Landing local | React, componentes/secciones y reglas de formulario públicas. No envía citas a un servicio | React 19.2.8, Vite 8.3.1, TS 6.0.2, oxlint 1.81.0; `e2396fe467b47ea3659802a99d334e13436d2573` + cambios locales |
| Landing académica remota | HTML estático publicado en GitHub Pages; repositorio distinto de la landing React local | `1ASI0732-2620-9086/LANDING-PAGE`, historial de ejecuciones del 17/09/2026 |
| Informe | README consultado sin editar el remoto; contiene US/TS reales en 3.2 y llega hasta capítulo V | `REPORT`, commit `9892066480a9fac7fe0dc75f2878700266f0f517` |

La versión probada **incluye cambios sin commit**: no atribuir las pruebas nuevas únicamente al SHA base. [Estado de fuentes](docs/evidencias/reportes/source-state-final.json) registra las rutas y el estado Git; [inventario de archivos](docs/evidencias/reportes/changed-files.json) identifica las modificaciones concretas. Se recomienda una rama por proyecto antes de integrar esta entrega; no se cambió la rama actual.

Flujo implementado: Angular y Flutter → misma API Spring → MySQL; la web usa `/api` y un proxy, el emulador usa `http://10.0.2.2:18080/api`. Configuración: `MAX_FRONT/MAX/proxy.evidence.json`, `MAX_MOBILE/lib/core/config/app_config.dart` y `scripts/Start-MaxTestApi.ps1`. No se conectó Flutter directamente con MySQL.

IAM, Patients y Studies son **áreas funcionales del informe**, no nombres nuevos de paquetes. Consultas/citas se conservaron y se comprobaron en pruebas relacionadas con el historial. El futuro portal del paciente no está implementado ni se acredita aquí. No se creó una arquitectura de microservicios ni se dockerizó el backend o la BD.

# Capítulo VI: Product Verification & Validation

## 6.1. Testing Suites & Validation

La verificación y validación de MAX comprende pruebas unitarias y de componentes, integración con base de datos, escenarios Behavior-Driven Development (BDD) y recorridos de sistema. Esta entrega, correspondiente al **7 de octubre de 2026**, incorpora las ejecuciones aprobadas de GitHub Actions y conserva, como antecedente separado, la validación local del cliente Android.

El sistema utiliza Angular y Flutter como clientes de una API Spring Boot, que persiste la información en MySQL. IAM, Patients y Studies identifican las áreas funcionales evaluadas. Los entornos de integración utilizan datos sintéticos y una API de pruebas; los resultados no corresponden a operaciones sobre información clínica de producción.

| Suite | Alcance | Ejecutadas | Aprobadas | Fallidas | Omitidas | Evidencia |
|---|---|---:|---:|---:|---:|---|
| Backend JUnit | 26 unitarias y 37 de integración/contexto, con H2, MySQL y migraciones | 63 | 63 | 0 | 0 | [MAX Backend CI](https://github.com/PersonalProjects5443/MAX_DEV_BACK/actions/runs/37694651919); XML Surefire de la integración remota |
| Web Vitest | Validadores, stores, servicios y clientes HTTP con transporte sustituido | 24 | 24 | 0 | 0 | [MAX Web CI](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/actions/runs/37694826162), `web-vitest.json` |
| Flutter | Unidades y componentes con API o transporte sustituido | 22 | 22 | 0 | 0 | [MAX Android CI](https://github.com/1ASI0732-2620-9086/MOBILE/actions/runs/37694655470), `android-unit.jsonl` |
| Landing académica HTML | Contratos de HTML, navegación, recursos y HTTP local | 7 | 7 | 0 | 0 | [MAX Academic Landing CI](https://github.com/1ASI0732-2620-9086/LANDING-PAGE/actions/runs/37694657336), `landing-tests.json` |
| Playwright con API sustituida | Tres casos de navegador en escritorio y viewport móvil | 6 | 6 | 0 | 0 | `browser-mocked.json` del CI web |
| BDD con API y MySQL reales | Nueve escenarios HTTP sobre un entorno aislado dentro del runner | 9 escenarios | 9 | 0 | 0 | [Integración web](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/actions/runs/37701471163), `web/reports/bdd.json` |
| Sistema web con API y MySQL reales | Recorrido completo desde la UI, en escritorio y viewport móvil | 2 recorridos | 2 | 0 | 0 | `web/reports/system-web.json` del artefacto de integración |
| Sistema Android, validación local previa | Aplicación Flutter en emulador Android 14 con API y MySQL de pruebas | 1 recorrido | 1 | 0 | 0 | `android-system-evidence-final.log` de la entrega local |
| iOS | Sin plataforma iOS activa en la entrega evaluada | No aplica | — | — | — | Alcance del repositorio móvil |

Los **72 casos unitarios o de componentes clínicos** corresponden a 26 de backend, 24 de web y 22 de Flutter. Las 37 pruebas de integración/contexto completan los 63 casos JUnit del backend. Las siete comprobaciones de la landing, los seis casos de navegador con API sustituida, BDD y los recorridos de sistema se presentan por separado para evitar duplicidades. La repetición de JUnit en el workflow de integración no añade casos diferentes al total de 63.

La landing académica HTML de `1ASI0732-2620-9086/LANDING-PAGE` es distinta de la landing React `PersonalProjects5443/LANDING-PAGE-MAX`, revisada previamente de forma local. Los siete resultados remotos corresponden exclusivamente a la primera. No se midió cobertura de código, por lo que estos recuentos no representan un porcentaje de cobertura.

## 6.1.1. Core Entities Unit Tests

Herramientas: backend JUnit Jupiter 6.0.3/Mockito 5.20.0; web Vitest 4.1.11 con Angular TestBed/HttpTestingController y jsdom; Android `flutter_test` del SDK 3.41.9. Arrange–Act–Assert se refleja en configuración de dependencias, operación y aserciones. Los clientes HTTP que usan dobles se clasifican como pruebas de unidad/componente, no como integración contra una API real.

Los IDs UT de este documento identifican evidencia, no historias nuevas. Cada caso conserva su nombre original y resultado. Los validadores de búsqueda y `ClinicalDataService` se contabilizan una sola vez en Patients por coordinar sus listados; también prestan servicio a otras pantallas.

### 6.1.1.1. IAM

#### 6.1.1.1.1. Backend

Unidades: **AuthService; AvatarValidator; PasswordPolicy**. Archivos: `AuthServiceUnitTest.java, AvatarValidatorUnitTest.java, shared/security/PasswordPolicyTest.java`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MAX_DEV_BACK/src/test/java/com/max/maxbackend/contexts/auth/application/AuthServiceUnitTest.java`.

Fragmento real:

```java
  @Test void rejectsUnknownAccountWithoutIssuingSession() {
    when(users.findByEmail("missing@example.test")).thenReturn(Optional.empty());
    assertThatThrownBy(() -> service.login(new LoginRequest("missing@example.test", "wrong"))).isInstanceOf(ApiException.class).hasMessage("Invalid credentials");
    verifyNoInteractions(tokens, passwords);
  }
  @Test void rejectsWrongPasswordWithoutChangingUserOrSession() {
    when(users.findByEmail(user.email())).thenReturn(Optional.of(user));
    when(passwords.matches("wrong", "hash")).thenReturn(false);
    assertThatThrownBy(() -> service.login(new LoginRequest(user.email(), "wrong"))).isInstanceOf(ApiException.class);
    verify(users, never()).save(any());
    verifyNoInteractions(tokens);
  }
  @Test void loginNormalizesEmailAndPreservesIdentityAndCreatedAt() {
    when(users.findByEmail(user.email())).thenReturn(Optional.of(user));
    when(passwords.matches("correct", "hash")).thenReturn(true);
    when(users.save(any())).thenAnswer(call -> call.getArgument(0));
    when(tokens.generateToken(7L, user.email(), "MEDICO")).thenReturn("synthetic-session");
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-IAM-Backend-01 | AuthServiceUnitTest | duplicateRegistrationDoesNotHashOrSave | Correo duplicado: conflicto; no calcular hash ni guardar. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-02 | AuthServiceUnitTest | wrongCurrentPasswordDoesNotRevokeSessions | Contraseña actual incorrecta: rechazo sin revocar sesiones. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-03 | AuthServiceUnitTest | rejectsUnknownAccountWithoutIssuingSession | Cuenta desconocida: 401 y ninguna sesión nueva. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-04 | AuthServiceUnitTest | loginNormalizesEmailAndPreservesIdentityAndCreatedAt | Correo normalizado; conservar ID y createdAt al acceder. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-05 | AuthServiceUnitTest | rejectsWrongPasswordWithoutChangingUserOrSession | Contraseña incorrecta: 401 sin modificar usuario ni sesión. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-06 | AvatarValidatorUnitTest | rejectsInvalidBase64UnsupportedTypeAndOversize | Rechazar avatar inválido, tipo no permitido y exceso de 5 MiB. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-07 | AvatarValidatorUnitTest | acceptsPngSignatureAndRejectsMimeMismatch | Aceptar PNG válido y rechazar MIME incompatible con contenido. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-08 | AvatarValidatorUnitTest | historicalUnchangedValueIsPreserved | Conservar la referencia histórica de avatar sin alteración. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-09 | AvatarValidatorUnitTest | emptyValueRemovesAvatar | Valor vacío elimina la referencia del avatar. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-10 | PasswordPolicyTest | acceptsTheCompletePolicy | Aceptar más de ocho caracteres, mayúscula, número y signo. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Backend-11 | PasswordPolicyTest | rejectsEveryMissingRequirement | Rechazar cada requisito faltante de contraseña. | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `./mvnw -B verify`, desde la raíz de `MAX_DEV_BACK`, con el entorno MySQL de pruebas configurado. Reportes: XML y TXT de Surefire en los artefactos de Actions.

#### 6.1.1.1.2. iOS

**No aplica:** no hay implementación iOS activa. No se generó imagen iOS ni se reutilizaron resultados Android.

#### 6.1.1.1.3. Android

Unidades: **AppController; MaxValidators.password; API sustituida**. Archivos: `test/iam_test.dart; test/validators_test.dart`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MOBILE/test/iam_test.dart`.

Fragmento real:

```dart
    test('rechaza correo inválido y exige correo al registrarse', () {
      expect(MaxValidators.email('bad', required: true), isNotNull);
      expect(MaxValidators.email('', required: true), isNotNull);
      expect(MaxValidators.email('ana@example.test', required: true), isNull);
    });
    test('credenciales inválidas no crean identidad autenticada', () async {
      final api = FakeApi()..loginError = const ApiException('Credenciales incorrectas', statusCode: 401);
      final controller = AppController(api: api);
      expect(await controller.login('ana@example.test', 'wrong'), contains('incorrectas'));
      expect(controller.isAuthenticated, isFalse);
      expect(controller.actionLoading, isFalse);
      controller.dispose();
    });
    test('login y logout limpian datos e identidad', () async {
      final api = FakeApi()..records = [syntheticPatient];
      final controller = AppController(api: api);
      expect(await controller.login('ana@example.test', 'synthetic'), isNull);
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-IAM-Android-01 | iam_test.dart | IAM rechaza correo inválido y exige correo al registrarse | IAM rechaza correo inválido y exige correo al registrarse | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Android-02 | iam_test.dart | IAM credenciales inválidas no crean identidad autenticada | IAM credenciales inválidas no crean identidad autenticada | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Android-03 | iam_test.dart | IAM login y logout limpian datos e identidad | IAM login y logout limpian datos e identidad | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Android-04 | iam_test.dart | IAM contraseña actual incorrecta conserva la sesión | IAM contraseña actual incorrecta conserva la sesión | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Android-05 | validators_test.dart | seguridad de contraseña exige longitud, mayúscula, número y signo | seguridad de contraseña exige longitud, mayúscula, número y signo | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `flutter test --reporter=json`, desde la raíz de `MOBILE`. Reporte: `android-unit.jsonl` en el artefacto `android-reports-<SHA>`.

#### 6.1.1.1.4. Web

Unidades: **AuthStore; validación de contraseña y confirmación**. Archivos: `contexts/usuarios/application/auth-store.spec.ts; core/validation/password.validation.spec.ts`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MAX_DEV_FRONT/src/app/contexts/usuarios/application/auth-store.spec.ts`.

Fragmento real:

```typescript
  it('elimina credenciales antiguas sin borrar preferencias ajenas a la sesión', () => {
    localStorage.setItem('max_users', '[{"token":"legacy"}]');
    localStorage.setItem('max_access_token', 'legacy-token');
    localStorage.setItem('language', 'es');

    clearLegacyAuthStorage();

    expect(localStorage.getItem('max_users')).toBeNull();
    expect(localStorage.getItem('max_access_token')).toBeNull();
    expect(localStorage.getItem('language')).toBe('es');
  });
});
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-IAM-Web-01 | app/core/validation/password.validation.spec.ts | accepts a password with more than eight characters, uppercase, number and sign | accepts a password with more than eight characters, uppercase, number and sign | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Web-02 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: clave#123 | rejects a password that does not satisfy the full policy: clave#123 | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Web-03 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: Clave#abc | rejects a password that does not satisfy the full policy: Clave#abc | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Web-04 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: Clave1234 | rejects a password that does not satisfy the full policy: Clave1234 | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Web-05 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: Cla#1234 | rejects a password that does not satisfy the full policy: Cla#1234 | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Web-06 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: Clave #123 | rejects a password that does not satisfy the full policy: Clave #123 | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Web-07 | app/core/validation/password.validation.spec.ts | detects different confirmation values | detects different confirmation values | Caso aprobado en el reporte automatizado | Aprobada |
| UT-IAM-Web-08 | app/contexts/usuarios/application/auth-store.spec.ts | elimina credenciales antiguas sin borrar preferencias ajenas a la sesión | elimina credenciales antiguas sin borrar preferencias ajenas a la sesión | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `npm run test:ci`, desde la raíz de `MAX_DEV_FRONT`. Reporte: `web-vitest.json` en el artefacto `web-reports-<SHA>`.

#### 6.1.1.1.5. Resumen agregado de IAM

| Plataforma | Ejecutadas | Aprobadas | Fallidas | Omitidas | Evidencia |
|---|---:|---:|---:|---:|---|
| Backend | 11 | 11 | 0 | 0 | `JUnit XML / Surefire` |
| Android | 5 | 5 | 0 | 0 | `android-unit.jsonl` |
| Web | 8 | 8 | 0 | 0 | `web-vitest.json` |
| iOS | No aplica | — | — | — | Sin implementación |

### 6.1.1.2. Patients

#### 6.1.1.2.1. Backend

Unidades: **PacienteService y validación Bean Validation**. Archivos: `contexts/pacientes/application/PacienteServiceUnitTest.java`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MAX_DEV_BACK/src/test/java/com/max/maxbackend/contexts/pacientes/application/PacienteServiceUnitTest.java`.

Fragmento real:

```java
  @Test void updateKeepsPathIdentityAndAuthenticatedOwner() {
    when(patients.findByIdAndOwnerUserId(10L, 7L)).thenReturn(Optional.of(patient()));
    when(patients.save(any())).thenAnswer(call -> call.getArgument(0));
    var saved = service.update(7L, 10L, request(PATIENT_JSON.replace("\"version\":0", "\"id\":999,\"version\":0")));
    assertThat(saved.id()).isEqualTo(10L);
    assertThat(saved.ownerUserId()).isEqualTo(7L);
  }
  @Test void missingRecordCannotBeUpdated() {
    when(patients.findByIdAndOwnerUserId(99L, 7L)).thenReturn(Optional.empty());
    assertThatThrownBy(() -> service.update(7L, 99L, request(PATIENT_JSON))).isInstanceOf(ResourceNotFoundException.class);
    verify(patients, never()).save(any());
  }
  @Test void staleVersionCannotOverwrite() {
    when(patients.findByIdAndOwnerUserId(10L, 7L)).thenReturn(Optional.of(patient()));
    assertThatThrownBy(() -> service.update(7L, 10L, request(PATIENT_JSON.replace("\"version\":0", "\"version\":4")))).isInstanceOf(ApiException.class);
    verify(patients, never()).save(any());
  }
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Patients-Backend-01 | PacienteServiceUnitTest | missingRecordCannotBeUpdated | ID inexistente: rechazar actualización sin guardar. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Backend-02 | PacienteServiceUnitTest | validatesRequiredNamesDniEmailAndPhone | Validar nombres obligatorios y formatos DNI, correo y teléfono. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Backend-03 | PacienteServiceUnitTest | invalidBirthDateIsRejectedBeforeSave | Rechazar fecha inválida/futura antes de guardar. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Backend-04 | PacienteServiceUnitTest | emptyCollectionIsAnEmptyResult | Listado vacío devuelve una colección vacía. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Backend-05 | PacienteServiceUnitTest | staleVersionCannotOverwrite | Versión antigua: conflicto; no sobrescribir datos. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Backend-06 | PacienteServiceUnitTest | updateKeepsPathIdentityAndAuthenticatedOwner | Conservar ID de la ruta y propietario autenticado. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Backend-07 | PacienteServiceUnitTest | creationUsesAuthenticatedOwnerAndNormalizesOptionalFields | Asignar propietario autenticado y normalizar campos opcionales. | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `./mvnw -B verify`, desde la raíz de `MAX_DEV_BACK`, con el entorno MySQL de pruebas configurado. Reportes: XML y TXT de Surefire en los artefactos de Actions.

#### 6.1.1.2.2. iOS

**No aplica:** no hay implementación iOS activa. No se generó imagen iOS ni se reutilizaron resultados Android.

#### 6.1.1.2.3. Android

Unidades: **Patient, AppController y MaxValidators**. Archivos: `test/patients_test.dart; test/models_test.dart; test/validators_test.dart`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MOBILE/test/patients_test.dart`.

Fragmento real:

```dart
    test('nombres y DNI se normalizan sin cambiar identidad o versión', () {
      final patient = Patient.fromJson({'id': 10, 'firstName': ' Ana ', 'lastName': ' Prueba ', 'dni': ' 87654321 ', 'version': 3});
      final json = patient.toJson();
      expect(json['id'], 10);
      expect(json['version'], 3);
      expect(json['firstName'], 'Ana');
      expect(json['dni'], '87654321');
    });
    test('registro inexistente y listado vacío mantienen estado vacío', () {
      final controller = AppController(api: FakeApi());
      expect(controller.patientById(99), isNull);
      expect(controller.patients, isEmpty);
      controller.dispose();
    });
    test('un fallo de persistencia no agrega pacientes ficticios', () async {
      final api = FakeApi()..saveError = const ApiException('Fallo de red', statusCode: 503);
      final controller = AppController(api: api)..user = syntheticUser;
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Patients-Android-01 | models_test.dart | paciente conserva contrato JSON del backend | paciente conserva contrato JSON del backend | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Android-02 | patients_test.dart | Patients nombres y DNI se normalizan sin cambiar identidad o versión | Patients nombres y DNI se normalizan sin cambiar identidad o versión | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Android-03 | patients_test.dart | Patients registro inexistente y listado vacío mantienen estado vacío | Patients registro inexistente y listado vacío mantienen estado vacío | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Android-04 | patients_test.dart | Patients un fallo de persistencia no agrega pacientes ficticios | Patients un fallo de persistencia no agrega pacientes ficticios | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Android-05 | patients_test.dart | Patients bloquea doble envío mientras la operación está pendiente | Patients bloquea doble envío mientras la operación está pendiente | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Android-06 | patients_test.dart | Patients descarta pacientes recibidos después del logout | Patients descarta pacientes recibidos después del logout | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Android-07 | validators_test.dart | validaciones de paciente DNI acepta exactamente ocho dígitos | validaciones de paciente DNI acepta exactamente ocho dígitos | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Android-08 | validators_test.dart | validaciones de paciente nombres no aceptan números ni signos arbitrarios | validaciones de paciente nombres no aceptan números ni signos arbitrarios | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Android-09 | validators_test.dart | validaciones de paciente teléfono acepta entre siete y quince dígitos | validaciones de paciente teléfono acepta entre siete y quince dígitos | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `flutter test --reporter=json`, desde la raíz de `MOBILE`. Reporte: `android-unit.jsonl` en el artefacto `android-reports-<SHA>`.

#### 6.1.1.2.4. Web

Unidades: **PacientesStore; campos y búsquedas; ClinicalDataService**. Archivos: `contexts/pacientes/application/*.spec.ts; core/validation/search-input.validation.spec.ts; core/state/clinical-data.service.spec.ts`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MAX_DEV_FRONT/src/app/core/state/clinical-data.service.spec.ts`.

Fragmento real:

```typescript
  it('descarta la respuesta de la sesión anterior después de reset', async () => {
    const pending = new Subject<any[]>();
    const { service, patientsStore } = setup(pending);
    const load = service.ensureLoaded();
    service.reset();
    pending.next([{ id: 99, name: 'Anterior' }]); pending.complete();
    await load;
    expect(patientsStore.pacientes()).toEqual([]);
    expect(patientsStore.loadState()).toBe('pending');
  });
  it('expone fallo de pacientes y permite que otros módulos terminen', async () => {
    const { service, patientsStore, studiesStore } = setup(throwError(() => new Error('Synthetic')));
    await service.ensureLoaded();
    expect(patientsStore.loadState()).toBe('error');
    expect(patientsStore.error()).toContain('pacientes');
    expect(studiesStore.loadState()).toBe('loaded');
  });
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Patients-Web-01 | app/core/state/clinical-data.service.spec.ts | reutiliza la carga pendiente y evita llamadas duplicadas | reutiliza la carga pendiente y evita llamadas duplicadas | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-02 | app/core/state/clinical-data.service.spec.ts | descarta la respuesta de la sesión anterior después de reset | descarta la respuesta de la sesión anterior después de reset | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-03 | app/core/state/clinical-data.service.spec.ts | expone fallo de pacientes y permite que otros módulos terminen | expone fallo de pacientes y permite que otros módulos terminen | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-04 | app/core/validation/search-input.validation.spec.ts | allows only letters and spaces in name searches | allows only letters and spaces in name searches | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-05 | app/core/validation/search-input.validation.spec.ts | allows at most eight digits in DNI searches | allows at most eight digits in DNI searches | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-06 | app/core/validation/search-input.validation.spec.ts | allows letters, digits and spaces in combined searches | allows letters, digits and spaces in combined searches | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-07 | app/contexts/pacientes/application/pacientes.store.spec.ts | expone estados explícitos y elimina los datos al cambiar de sesión | expone estados explícitos y elimina los datos al cambiar de sesión | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-08 | app/contexts/pacientes/application/patient-input.validation.spec.ts | keeps only letters and spaces in names | keeps only letters and spaces in names | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-09 | app/contexts/pacientes/application/patient-input.validation.spec.ts | keeps only the allowed amount of digits | keeps only the allowed amount of digits | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Patients-Web-10 | app/contexts/pacientes/application/patient-input.validation.spec.ts | accepts only real, non-future birth dates within 120 years | accepts only real, non-future birth dates within 120 years | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `npm run test:ci`, desde la raíz de `MAX_DEV_FRONT`. Reporte: `web-vitest.json` en el artefacto `web-reports-<SHA>`.

#### 6.1.1.2.5. Resumen agregado de Patients

| Plataforma | Ejecutadas | Aprobadas | Fallidas | Omitidas | Evidencia |
|---|---:|---:|---:|---:|---|
| Backend | 7 | 7 | 0 | 0 | `JUnit XML / Surefire` |
| Android | 9 | 9 | 0 | 0 | `android-unit.jsonl` |
| Web | 10 | 10 | 0 | 0 | `web-vitest.json` |
| iOS | No aplica | — | — | — | Sin implementación |

### 6.1.1.3. Studies

#### 6.1.1.3.1. Backend

Unidades: **EstudioService, FileUpload y contrato de almacenamiento**. Archivos: `contexts/estudios/application/EstudioServiceUnitTest.java`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MAX_DEV_BACK/src/test/java/com/max/maxbackend/contexts/estudios/application/EstudioServiceUnitTest.java`.

Fragmento real:

```java
  @Test void storageFailureDoesNotSaveStudyMetadata() {
    ownPatient();
    when(storage.isConfigured()).thenReturn(true);
    when(storage.uploadObject(anyString(), anyString(), any(), anyLong())).thenThrow(new ApiException(org.springframework.http.HttpStatus.BAD_GATEWAY, "Synthetic failure"));
    assertThatThrownBy(() -> upload("test.pdf", "application/pdf", pdf.length, new ByteArrayInputStream(pdf))).hasMessage("Synthetic failure");
    verify(studies, never()).save(any());
    verify(lifecycle, never()).markLinked(any());
  }
  @Test void unauthorizedAccessNeverSignsOrDeletesAnObject() {
    when(studies.findByIdAndOwnerUserId(55L, 7L)).thenReturn(Optional.empty());
    assertThatThrownBy(() -> service.accessUrl(7L, 55L)).isInstanceOf(ResourceNotFoundException.class);
    assertThatThrownBy(() -> service.delete(7L, 55L)).isInstanceOf(ResourceNotFoundException.class);
    verifyNoInteractions(storage, lifecycle);
  }
  @Test void createCannotAdoptAnArbitraryObjectKey() {
    ownPatient();
    var request = new EstudioUpsertRequest(null, 10L, null, EstudioTipo.PDF, "", "2026-10-07T10:00:00", "test.pdf", "application/pdf", "url", "another-owner/key.pdf", null, null);
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Studies-Backend-01 | EstudioServiceUnitTest | rejectsOversizeBeforeReadingContent | Rechazar más de 20 MiB antes de leer el contenido. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Backend-02 | EstudioServiceUnitTest | nonexistentOrForeignPatientNeverUploads | Paciente ajeno/inexistente: no ejecutar carga del objeto. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Backend-03 | EstudioServiceUnitTest | acceptsExactly20MiBAndGeneratesServerOwnedKey | Aceptar exactamente 20 MiB; generar clave desde servidor. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Backend-04 | EstudioServiceUnitTest | createCannotAdoptAnArbitraryObjectKey | Rechazar claves arbitrarias al crear un estudio. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Backend-05 | EstudioServiceUnitTest | rejectsUnsupportedExtensionAndForgedContent | Rechazar extensión no admitida y firma de contenido inválida. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Backend-06 | EstudioServiceUnitTest | storageFailureDoesNotSaveStudyMetadata | Fallo de almacenamiento: no guardar metadatos ficticios. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Backend-07 | EstudioServiceUnitTest | localStoragePreservesBytesAndMetadata | Conservar bytes, paciente y metadatos en modo embebido. | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Backend-08 | EstudioServiceUnitTest | unauthorizedAccessNeverSignsOrDeletesAnObject | Acceso ajeno: no firmar ni eliminar objetos. | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `./mvnw -B verify`, desde la raíz de `MAX_DEV_BACK`, con el entorno MySQL de pruebas configurado. Reportes: XML y TXT de Surefire en los artefactos de Actions.

#### 6.1.1.3.2. iOS

**No aplica:** no hay implementación iOS activa. No se generó imagen iOS ni se reutilizaron resultados Android.

#### 6.1.1.3.3. Android

Unidades: **Study, MaxApi.uploadStudy, AppController y StudyImage**. Archivos: `test/studies_test.dart; test/study_transport_test.dart; test/study_viewer_test.dart`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MOBILE/test/study_transport_test.dart`.

Fragmento real:

```dart
    test('multipart conserva el día y el contrato de fecha/hora: ${entry.key}', () async {
      final dio = Dio(BaseOptions(baseUrl: 'http://localhost:18080/api'));
      final api = MaxApi(ApiClient(dio: dio));
      FormData? sent;
      dio.interceptors.add(InterceptorsWrapper(onRequest: (request, handler) {
        sent = request.data as FormData;
        handler.resolve(Response(requestOptions: request, statusCode: 201, data: {
          'id': 1, 'pacienteId': 10, 'tipo': 'PDF', 'fecha': entry.value,
        }));
      }));
      final study = await api.uploadStudy(patientId: 10, type: 'PDF', date: entry.key,
        description: 'Documento sintético', fileName: 'synthetic.pdf',
        bytes: Uint8List.fromList('%PDF-1.7\n%%EOF'.codeUnits));
      expect(sent!.fields.singleWhere((field) => field.key == 'fecha').value, entry.value);
      expect(sent!.fields.singleWhere((field) => field.key == 'pacienteId').value, '10');
      expect(study.patientId, 10);
      expect(sent!.files.single.value.contentType.toString(), 'application/pdf');
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Studies-Android-01 | studies_test.dart | Studies conserva relaciones y metadatos del contrato JSON | Studies conserva relaciones y metadatos del contrato JSON | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Android-02 | studies_test.dart | Studies identifica imágenes y PDF histórico por extensión | Studies identifica imágenes y PDF histórico por extensión | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Android-03 | studies_test.dart | Studies informa archivos fallidos y reintenta sin duplicar atención | Studies informa archivos fallidos y reintenta sin duplicar atención | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Android-04 | study_transport_test.dart | multipart conserva el día y el contrato de fecha/hora: 2026-10-07 | multipart conserva el día y el contrato de fecha/hora: 2026-10-07 | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Android-05 | study_transport_test.dart | multipart conserva el día y el contrato de fecha/hora: 2026-10-07T16:45:00 | multipart conserva el día y el contrato de fecha/hora: 2026-10-07T16:45:00 | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Android-06 | study_viewer_test.dart | la imagen histórica embebida usa bytes y conserva el visor | la imagen histórica embebida usa bytes y conserva el visor | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Android-07 | study_viewer_test.dart | referencia embebida no imagen muestra un error accionable | referencia embebida no imagen muestra un error accionable | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `flutter test --reporter=json`, desde la raíz de `MOBILE`. Reporte: `android-unit.jsonl` en el artefacto `android-reports-<SHA>`.

#### 6.1.1.3.4. Web

Unidades: **EstudiosStore y EstudiosApiClient**. Archivos: `contexts/estudios/application/estudios.store.spec.ts; contexts/estudios/infrastructure/estudios.api-client.spec.ts`; raíz de pruebas backend `MAX_DEV_BACK/src/test/java/com/max/maxbackend/`, web `MAX_DEV_FRONT/src/app/`, Android `MOBILE/`. El archivo completo representativo es `MAX_DEV_FRONT/src/app/contexts/estudios/infrastructure/estudios.api-client.spec.ts`.

Fragmento real:

```typescript
  it('propaga un fallo HTTP sin devolver un estudio ficticio', () => {
    let errorStatus = 0;
    client.findAll().subscribe({ next: () => { throw new Error('No debe simular éxito'); }, error: error => errorStatus = error.status });
    http.expectOne('/api/estudios').flush({}, { status: 503, statusText: 'Unavailable' });
    expect(errorStatus).toBe(503);
  });
  it('solicita una URL vigente al abrir un estudio', () => {
    let url = '';
    client.accessUrl(42).subscribe(result => url = result.url);
    http.expectOne('/api/estudios/42/access-url').flush({ url: 'https://example.test/current', expiresAt: '2026-10-07T11:00:00Z' });
    expect(url).toBe('https://example.test/current');
  });
});
```

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Studies-Web-01 | app/contexts/estudios/application/estudios.store.spec.ts | conserva el error y los datos sin simular un guardado | conserva el error y los datos sin simular un guardado | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Web-02 | app/contexts/estudios/application/estudios.store.spec.ts | revoca URLs temporales y vacía datos al cerrar sesión | revoca URLs temporales y vacía datos al cerrar sesión | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Web-03 | app/contexts/estudios/application/estudios.store.spec.ts | elimina únicamente los estudios del paciente seleccionado | elimina únicamente los estudios del paciente seleccionado | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Web-04 | app/contexts/estudios/infrastructure/estudios.api-client.spec.ts | envía un multipart asociado al paciente sin inventar consulta | envía un multipart asociado al paciente sin inventar consulta | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Web-05 | app/contexts/estudios/infrastructure/estudios.api-client.spec.ts | propaga un fallo HTTP sin devolver un estudio ficticio | propaga un fallo HTTP sin devolver un estudio ficticio | Caso aprobado en el reporte automatizado | Aprobada |
| UT-Studies-Web-06 | app/contexts/estudios/infrastructure/estudios.api-client.spec.ts | solicita una URL vigente al abrir un estudio | solicita una URL vigente al abrir un estudio | Caso aprobado en el reporte automatizado | Aprobada |

Comando: `npm run test:ci`, desde la raíz de `MAX_DEV_FRONT`. Reporte: `web-vitest.json` en el artefacto `web-reports-<SHA>`.

#### 6.1.1.3.5. Resumen agregado de Studies

| Plataforma | Ejecutadas | Aprobadas | Fallidas | Omitidas | Evidencia |
|---|---:|---:|---:|---:|---|
| Backend | 8 | 8 | 0 | 0 | `JUnit XML / Surefire` |
| Android | 7 | 7 | 0 | 0 | `android-unit.jsonl` |
| Web | 6 | 6 | 0 | 0 | `web-vitest.json` |
| iOS | No aplica | — | — | — | Sin implementación |

### 6.1.1.4. Pruebas complementarias de la landing y del cliente móvil

La landing académica utiliza una suite Python de siete comprobaciones. El reporte `landing-tests.json` registra **7 ejecutadas, 7 aprobadas, 0 fallos, 0 errores y 0 omitidas**.

| Comprobación | Resultado esperado | Estado |
|---|---|---|
| Enlaces de entrada a MAX | Mantener un destino de autenticación consistente | Aprobada |
| Referencias externas | Utilizar HTTPS | Aprobada |
| Referencias locales | Resolver los recursos dentro del sitio | Aprobada |
| Fragmentos de navegación | Apuntar a identificadores existentes | Aprobada |
| Identificadores de sección | No presentar duplicados | Aprobada |
| Documento principal | Declarar español, título y viewport móvil | Aprobada |
| HTTP local con prefijo de proyecto | Servir la entrada y sus recursos bajo el prefijo esperado | Aprobada |

Estas comprobaciones verifican el sitio estático y su servicio HTTP local; no prueban una conexión con el backend ni el funcionamiento de los servicios externos enlazados. Las seis pruebas de fechas de la landing React pertenecen a la validación local previa y no se suman a esta suite académica.

![Siete comprobaciones aprobadas de la landing académica en GitHub Actions](assets/MAX-CI-Landing-Pruebas.png)

*Figura 6.1. El comando `python3 scripts/test_ci.py` finaliza con siete pruebas y resultado OK.*

La suite Flutter incorpora además el caso `perfil administrativo usa id como userId compatible`. Se contabiliza como una comprobación de modelo complementaria, sin atribuirle la validación de un recorrido administrativo completo.

### 6.1.1.5. Resumen consolidado de unidades y componentes

| Área funcional | Backend | Web | Flutter/Dart | Total aprobado |
|---|---:|---:|---:|---:|
| IAM | 11 | 8 | 5 | 24 |
| Patients | 7 | 10 | 9 | 26 |
| Studies | 8 | 6 | 7 | 21 |
| Modelo administrativo complementario | 0 | 0 | 1 | 1 |
| **Total** | **26** | **24** | **22** | **72** |

Los reportes JSON permiten comprobar los recuentos completos aunque las capturas de consola no enumeren todos los casos. En Flutter se excluyen los eventos internos de carga de suites del conteo de pruebas funcionales.

![Ejecución de Vitest en MAX Web CI](assets/MAX-CI-Web-Pruebas.png)

*Figura 6.2. Paso `npm run test:ci`. El archivo `web-vitest.json` del artefacto confirma 24 pruebas aprobadas.*

![Finalización correcta de las pruebas Flutter en Actions](assets/MAX-CI-Mobile-Pruebas.png)

*Figura 6.3. El reporte `android-unit.jsonl` confirma 22 pruebas aprobadas; el evento final comunica el éxito de la ejecución.*

## 6.1.2. Core Integration Tests

Límites reales: servidor HTTP Spring y seguridad, repositorios JPA y BD; MySQL nativo en esquemas efímeros por suite, además de H2. No hay Testcontainers ni Docker. El workflow prepara MySQL nativo en el runner para ejecutar los contratos contra una base de datos real. `MySqlWorkflowIntegrationTest` hereda los 16 contratos HTTP existentes y añade bcrypt persistido; `MySqlMigrationIntegrationTest` ejecuta tres pruebas de esquema. Los esquemas creados por estas clases se eliminan al finalizar. BDD y sistema utilizan una instancia de pruebas independiente dentro del runner.

El total de integración/contexto del backend es **37**: 19 casos de IAM, 12 de Patients, 2 de Studies, 3 de migraciones MySQL y 1 de inicio del contexto de aplicación. Los últimos cuatro son comprobaciones compartidas y no se duplican dentro de las áreas funcionales.

### 6.1.2.1. Integración de IAM

19 casos JUnit: nueve contratos con H2 y los mismos nueve con MySQL, más el caso MySQL de bcrypt. Registro/cookie, CSRF, contraseñas débiles, logout, revocación por cambio de contraseña, contraseña actual incorrecta, avatar y limitación de acceso. El bcrypt se leyó desde `usuarios.password_hash`, se comprobó que no contiene texto plano y se verificaron claves correcta/incorrecta con el encoder real. Los casos HTTP de credenciales correctas/incorrectas también están en BDD y no se suman nuevamente a JUnit.

Archivos: `AuthIntegrationTest.java`, `MySqlWorkflowIntegrationTest.java`. Los resultados por caso se registran en los XML de Surefire.

### 6.1.2.2. Integración de Patients

12 casos JUnit (seis H2 y seis MySQL): alta con historial atómica/idempotente, validaciones, versiones, cascadas, atención/cita/ultimaConsulta y desvinculación de consulta al eliminar una cita. BDD complementa creación/listado/edición e ID ajeno. El recorrido web demuestra búsqueda por DNI desde la UI y lectura posterior real.

No se afirma que la API implemente un endpoint separado de búsqueda: Angular/Flutter filtran sus listados autorizados. El caso BDD localiza el DNI en el listado; no acredita por sí solo el buscador visual.

### 6.1.2.3. Integración de Studies

Dos casos JUnit (uno H2 y uno MySQL) comprueban el aislamiento de registros y acceso al archivo entre perfiles. Los tres escenarios BDD de Estudios complementan multipart PDF, recuperación exacta de bytes, extensión prohibida y paciente inexistente. El recorrido web carga PNG y comprueba `naturalWidth=480`; la validación local previa de Android utilizó el cliente nativo para cargar y el visor UI para mostrarlo. La prueba unitaria de fallo de almacenamiento comprueba que no se persisten metadatos cuando el doble de R2 falla.

**R2 no fue integrado realmente:** proveedor `none`, archivo embebido en BD. El límite de 20 MiB se probó a nivel unitario; no se realizó un multipart real de ese tamaño. No se acredita recuperación ante un fallo real de red de R2, permisos del bucket, procesador de eliminaciones ni reintentos físicos. Hace falta un bucket de prueba y credenciales limitadas, sin usar el bucket clínico.

### 6.1.2.4. Comandos de ejecución

Cada comando se ejecuta en la raíz del repositorio correspondiente. La reproducción de las pruebas reales requiere configurar previamente el entorno aislado que utiliza el workflow; instalar dependencias por sí solo no inicia la API ni MySQL.

| Repositorio | Comando | Propósito y condición |
|---|---|---|
| Backend | `./mvnw -B verify` | Ejecutar JUnit y construir el JAR; requiere las variables MySQL del entorno de pruebas |
| Frontend | `npm ci` y `npm run test:ci` | Instalar desde el lockfile y ejecutar Vitest |
| Frontend | `npm run test:e2e` | Ejecutar seis casos Playwright con API sustituida; requiere Chromium |
| Frontend | `npm run test:bdd` | Ejecutar escenarios contra la API y MySQL reales de pruebas |
| Frontend | `npm run test:system` | Ejecutar el recorrido UI con Angular, API y MySQL de pruebas |
| Mobile | `flutter pub get --enforce-lockfile` y `flutter test --reporter=json` | Instalar dependencias y ejecutar las 22 pruebas Flutter |
| Landing académica | `python3 scripts/test_ci.py` | Ejecutar las siete comprobaciones de HTML y HTTP local |

La suite backend utiliza `MAX_TEST_MYSQL_URL`, `MAX_TEST_MYSQL_USER` y `MAX_TEST_MYSQL_PASSWORD`. La integración web prepara la API en loopback, puerto **18080**, y la web en el puerto **14200**. Los valores concretos se establecen en el entorno de pruebas, sin utilizar credenciales ni destinos de producción. La configuración reproducible se encuentra en [el CI del backend](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/ci/max-tests-actions/.github/workflows/ci.yml) y [el workflow de integración web](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/ci/max-tests-actions/.github/workflows/integration.yml).

### 6.1.2.5. Evidencias de ejecución

Las siguientes capturas proceden de la ejecución real de GitHub Actions. El resultado se contrasta con los reportes XML de Surefire, que también están incluidos en el artefacto del workflow de integración web.

| Clase JUnit | Casos aprobados | Clasificación |
|---|---:|---|
| `AuthServiceUnitTest` | 5 | Unidad |
| `AvatarValidatorUnitTest` | 4 | Unidad |
| `PasswordPolicyTest` | 2 | Unidad |
| `PacienteServiceUnitTest` | 7 | Unidad |
| `EstudioServiceUnitTest` | 8 | Unidad |
| `AuthIntegrationTest` | 16 | Integración con H2 |
| `MySqlWorkflowIntegrationTest` | 17 | Integración con MySQL |
| `MySqlMigrationIntegrationTest` | 3 | Migraciones MySQL |
| `MaxBackendApplicationTests` | 1 | Inicio del contexto |
| **Total** | **63** | **0 fallos, 0 errores, 0 omitidas** |

![Inicio del entorno H2 durante las pruebas del backend](assets/MAX-CI-Backend-Entorno.png)

*Figura 6.4. Preparación del contexto de aplicación y del entorno H2 utilizado por la suite de integración.*

![Contratos HTTP y migraciones MySQL en Actions](assets/MAX-CI-Backend-Integracion.png)

*Figura 6.5. La ejecución muestra los contratos de integración y la validación de once migraciones Flyway; once migraciones no equivalen a once casos JUnit adicionales.*

![Resumen JUnit con 63 pruebas aprobadas](assets/MAX-CI-Backend-Pruebas.png)

*Figura 6.6. Maven finaliza con `Tests run: 63`, sin fallos, errores ni pruebas omitidas, y `BUILD SUCCESS`.*

## 6.1.3. Core Behavior-Driven Development

Herramientas: Cucumber y Playwright APIRequestContext. Archivos del frontend: `cucumber.cjs`, `bdd/run.cjs`, `bdd/features/*.feature` y `bdd/steps/max.steps.cjs`. Los pasos llaman endpoints reales, preparan cuentas y pacientes sintéticos, inicializan CSRF y comprueban las respuestas y los datos persistidos. La ejecución remota aprobada utiliza la API y MySQL del mismo runner.

### 6.1.3.1. IAM

`bdd/features/iam.feature`: credenciales válidas/identidad, credenciales incorrectas y login sin CSRF. Tres escenarios aprobados. US-01 se acredita a nivel HTTP; la redirección visual es un criterio de UI separado.

**Escenarios registrados en el reporte**

El siguiente bloque reconstruye de forma legible los nombres, etiquetas y pasos de `bdd.json`. El archivo `.feature` original debe consultarse en el repositorio indicado; no se presenta esta transcripción como una copia íntegra de ese archivo.

```gherkin
Feature: IAM - acceso a MAX

  @US-01
  Scenario: Credenciales válidas permiten consultar la identidad
    Given una cuenta médica registrada
    When inicio sesión con la contraseña correcta
    Then recibo estado HTTP 200
    And puedo consultar mi identidad

  @US-01
  Scenario: Credenciales incorrectas son rechazadas
    Given una cuenta médica registrada
    When inicio sesión con una contraseña incorrecta
    Then recibo estado HTTP 401

  @security-csrf
  Scenario: Login sin CSRF es rechazado
    Given una cuenta médica registrada
    When envío login sin token CSRF
    Then recibo estado HTTP 403
```

**Definiciones de pasos**

El reporte identifica implementaciones en `MAX_DEV_FRONT/bdd/steps/max.steps.cjs`. Los pasos preparan cuentas o pacientes sintéticos, ejecutan solicitudes HTTP y comprueban códigos de respuesta y datos posteriores. Las implementaciones se consultan en [la rama evaluada del frontend](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/tree/ci/max-tests-actions/bdd).

Evidencia: `web/reports/bdd.json` y `web/reports/bdd.html` del artefacto de integración; captura consolidada en 6.1.3.4.

### 6.1.3.2. Patients

`bdd/features/patients.feature`: registrar/listar por DNI, editar/reconsultar y rechazo de ID ajeno. Tres escenarios aprobados. Los escenarios llevan tags de las historias verificadas; solo se acredita la parte HTTP, no todo el modal o búsqueda visual.

**Escenarios registrados en el reporte**

El siguiente bloque reconstruye de forma legible los nombres, etiquetas y pasos de `bdd.json`. El archivo `.feature` original debe consultarse en el repositorio indicado; no se presenta esta transcripción como una copia íntegra de ese archivo.

```gherkin
Feature: Patients - persistencia de pacientes

  @US-06 @US-08 @US-09
  Scenario: Registrar y consultar un paciente
    Given una cuenta médica registrada
    When registro un paciente con datos válidos
    Then recibo estado HTTP 201
    And el listado contiene al paciente con su DNI

  @US-10
  Scenario: Editar mantiene identidad y datos actualizados
    Given un paciente registrado por mi cuenta
    When actualizo sus observaciones con la versión vigente
    Then recibo estado HTTP 200
    And una nueva consulta conserva el ID y las observaciones

  @security-owner
  Scenario: Otra cuenta no puede modificar mi paciente
    Given un paciente registrado por otra cuenta
    When intento modificar ese paciente
    Then recibo estado HTTP 404
```

**Definiciones de pasos**

El reporte identifica implementaciones en `MAX_DEV_FRONT/bdd/steps/max.steps.cjs`. Los pasos preparan cuentas o pacientes sintéticos, ejecutan solicitudes HTTP y comprueban códigos de respuesta y datos posteriores. Las implementaciones se consultan en [la rama evaluada del frontend](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/tree/ci/max-tests-actions/bdd).

Evidencia: `web/reports/bdd.json` y `web/reports/bdd.html` del artefacto de integración; captura consolidada en 6.1.3.4.

### 6.1.3.3. Studies

`bdd/features/studies.feature`: cargar/recuperar PDF permitido, rechazar `.exe` sin persistir estudio y rechazar paciente inexistente. Tres escenarios aprobados.

Comando: `npm run test:bdd`, desde la raíz del frontend, con la API y MySQL de pruebas activos. La ejecución remota confirma **9 escenarios aprobados**. El log indica «50 steps»; el JSON distingue **32 pasos Given/When/Then/And y 18 hooks Before/After**, todos aprobados. Los hooks preparan y limpian el entorno y no representan comportamientos adicionales. Reportes: `web/reports/bdd.html` y `web/reports/bdd.json`.

**Escenarios registrados en el reporte**

El siguiente bloque reconstruye de forma legible los nombres, etiquetas y pasos de `bdd.json`. El archivo `.feature` original debe consultarse en el repositorio indicado; no se presenta esta transcripción como una copia íntegra de ese archivo.

```gherkin
Feature: Studies - documentos del paciente

  @US-12 @US-15 @TS-04
  Scenario: Adjuntar y recuperar un PDF permitido
    Given un paciente registrado por mi cuenta
    When adjunto un PDF sintético válido
    Then recibo estado HTTP 201
    And puedo recuperar exactamente los bytes del estudio

  @TS-05
  Scenario: Rechazar extensión no admitida
    Given un paciente registrado por mi cuenta
    When adjunto un archivo con extensión exe
    Then recibo estado HTTP 400
    And ningún estudio fue persistido

  @study-association
  Scenario: Rechazar paciente inexistente
    Given una cuenta médica registrada
    When adjunto un PDF a un paciente inexistente
    Then recibo estado HTTP 404
```

**Definiciones de pasos**

El reporte identifica implementaciones en `MAX_DEV_FRONT/bdd/steps/max.steps.cjs`. Los pasos preparan cuentas o pacientes sintéticos, ejecutan solicitudes HTTP y comprueban códigos de respuesta y datos posteriores. Las implementaciones se consultan en [la rama evaluada del frontend](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/tree/ci/max-tests-actions/bdd).

Evidencia: `web/reports/bdd.json` y `web/reports/bdd.html` del artefacto de integración; captura consolidada en 6.1.3.4.

### 6.1.3.4. Trazabilidad

Identificadores comprobados en [REPORT, sección 3.2](https://github.com/1ASI0732-2620-9086/REPORT/blob/9892066480a9fac7fe0dc75f2878700266f0f517/README.md#32-user-stories). Snapshot original: `REPORT-README-referencia.md`; metadatos: `report-reference.json`. Las condiciones de seguridad adicionales vienen del alcance solicitado y no se les inventó una historia US.

| Historia o requisito | Escenario/caso | Archivo | Plataforma/límite | Resultado y cobertura parcial | Evidencia |
|---|---|---|---|---|---|
| US-01 | Acceso correcto e incorrecto | `iam.feature` | HTTP API/MySQL | Aprobado: identidad/401; redirección de login no acreditada por este BDD | `bdd.json`, BDD IAM PNG |
| US-02 | Crear cuenta | Given de las nueve features; recorrido UI | Web/Android + API/MySQL | Registro real aprobado; no todos los errores posibles | `system-web.json`, Android log |
| US-03 | Logout | Integración y recorridos completos | HTTP/Web/Android | Revocación y retorno al acceso aprobados | Surefire y PNG sistema |
| TS-01 | Credencial JWT transportada en cookie | Cookie /me/CSRF; sin JWT en JSON/localStorage | Backend/Web | Aprobado: cookie HttpOnly; sin token en JSON/localStorage en los casos evaluados | IAM integración y sistema web |
| TS-02 | Bcrypt persistido | `registeredPasswordIsPersistedAsBcryptInsteadOfPlaintext` | Aplicación/JPA/MySQL | Hash real distinto del texto plano, matches correcto/incorrecto | XML MySqlWorkflowIntegrationTest |
| US-06/US-09 | Registrar y consultar paciente | `patients.feature`; UI | HTTP/Web/Android | Persistencia/lectura aprobadas; modal completo en web/native | Patients BDD y sistema |
| US-08 | Buscar por DNI/nombre | Listado por DNI BDD; filtro DNI UI web | HTTP y UI web | DNI aprobado; búsqueda visual por nombre no recorrida end-to-end | Patients BDD; web trace |
| US-10 | Editar paciente | Editar/reconsultar | HTTP/Web/Android | ID y observaciones conservados | BDD Patients; sistema |
| US-12/US-15 | Adjuntar/visualizar | PDF BDD; PNG UI web/native | API/BD, visor UI | Aprobado en almacenamiento embebido; PDF externo y picker nativo pendientes | Studies BDD; visores PNG |
| TS-04 | Archivo y referencia | Recuperar bytes exactos | API/MySQL | Aprobado en el runner; integración R2 no acreditada | BDD Studies |
| TS-05 | Formatos | Rechazo .exe y firma/MIME unitarios | API + unidades | Aprobado para casos enumerados | BDD Studies; UT Studies |
| Aislamiento por propietario (alcance) | Cuenta ajena / archivo ajeno | Patients feature + HTTP integración | API/MySQL/H2 | Rechazo aprobado | Surefire, BDD Patients |
| CSRF (alcance) | Login sin token | IAM feature | API/MySQL | 403 aprobado | BDD IAM |
| Asociación válida (alcance) | Paciente inexistente | Studies feature | API/MySQL | 404 sin estudio aprobado | BDD Studies |

US-19/US-20 tienen comprobaciones HTTP de atención/cita; no se acredita aquí todo su recorrido UI ni la historia US-17 de cruces de horario. Las pruebas no cubren automáticamente todos los criterios de una historia solo por llevar su tag.

![BDD y Playwright con API y MySQL reales aprobados en GitHub Actions](assets/MAX-CI-Web-BDD-Playwright-Integracion.png)

*Figura 6.7. El workflow remoto registra nueve escenarios BDD y dos recorridos Playwright aprobados. El detalle de los pasos BDD se interpreta según el JSON, distinguiendo los hooks.*

## 6.1.4. Core System Tests

### 6.1.4.1. Aplicación web

`MAX_DEV_FRONT/e2e-system/clinical-workflow.spec.ts`, con configuración `playwright.system.config.ts`. El workflow de integración ejecuta los proyectos **desktop-chromium** y **mobile-web-chromium** contra Angular, la API Spring Boot y MySQL reales dentro del runner. Ambos recorridos aprobaron. El viewport móvil constituye una prueba de la aplicación web y no de Flutter nativo.

| ID | Acción | Esperado | Obtenido | Estado |
|---|---|---|---|---|
| SYS-W-01 | Registro desde formulario | Cookie y acceso a Inicio | `/inicio`; cookie HttpOnly | Aprobado en ambos viewports |
| SYS-W-02 | Alta de paciente con historial | Paciente/cita/consulta persistidos | 201; un registro de cada relación | Aprobado |
| SYS-W-03 | Buscar DNI y consultar | Tarjeta correcta y datos del modal | DNI esperado en vista | Aprobado |
| SYS-W-04 | Editar observaciones y recargar | Nueva lectura conserva ID/cambio | API y pantalla vuelven a cargar | Aprobado |
| SYS-W-05 | Entrada directa a Estudios | Dependencias y listado cargados | Pantalla protegida disponible | Aprobado |
| SYS-W-06 | Adjuntar PNG y visualizar | Archivo persistido y decodificado | 480px naturalWidth y mismos bytes en access-url | Aprobado |
| SYS-W-07 | Logout y ruta protegida | Acceso rechazado sin sesión | `/auth`; API 401; sin token en localStorage | Aprobado |

Estos IDs representan pasos de **un recorrido por viewport**, por lo que el total es de dos recorridos de sistema. Los archivos sintéticos no contienen información clínica real. El artefacto de integración conserva `web/reports/system-web.json` y `web/reports/system-web-html/index.html`; el JSON registra dos aprobados y ningún resultado omitido, inesperado o inestable.

**Pruebas de navegador con API sustituida**

El CI básico también ejecuta seis pruebas Playwright: acceso sin credenciales en `localStorage`, rechazo de contraseña débil y recarga de una ruta clínica protegida, cada caso en escritorio y viewport móvil. Se utiliza `page.route` para sustituir las respuestas de la API. Esta suite comprueba el comportamiento del frontend; los dos recorridos anteriores son los que verifican la integración real con backend y MySQL.

![Seis pruebas de navegador aprobadas con API sustituida](assets/MAX-CI-Web-Playwright.png)

*Figura 6.8. Resultado Playwright del CI web básico: seis casos aprobados. Su alcance se diferencia del workflow de integración real.*

### 6.1.4.2. Aplicación Android

**Validación local previa:** se ejecutó Flutter `integration_test` en `Medium_Phone`, modelo `sdk_gphone64_x86_64`, Android **14/API 34**, serial `emulator-5554`. Resolución física informada 1080×2400 y override 1080×1920. App `com.max.max_mobile` **1.0.0+1**. Se construyó e instaló un APK instrumental de `integration_test/max_system_test.dart`; el recorrido usa `MaxApp` real, cookies en almacenamiento seguro y API local `10.0.2.2:18080/api`.

| ID | Acción | Esperado | Obtenido | Estado |
|---|---|---|---|---|
| SYS-A-01 | Registro y navegación Pacientes | Usuario real, estado vacío | NavigationBar y “Sin resultados” | Aprobado |
| SYS-A-02 | Modal de alta y calendario | Datos válidos e historial | API devuelve paciente creado | Aprobado |
| SYS-A-03 | Editar y leer nuevamente | Observación persistida | Consulta API confirma valor | Aprobado |
| SYS-A-04 | Carga con MaxApi del cliente nativo | Multipart y fecha compatibles | Estudio asociado al paciente | Aprobado; no automatiza picker del SO |
| SYS-A-05 | Listado y visor desde la UI | PNG decodificado | Imagen visible, sin error del visor | Aprobado |
| SYS-A-06 | Logout | Pantalla acceso; /me rechazado | Ingresar visible y ApiException | Aprobado |

Es **un recorrido funcional**. Flutter anuncia `+2` por incluir `tearDownAll`; no se cuentan dos recorridos. No acredita teléfono físico, PDF en app externa, instalación release firmada, selector de archivos del sistema operativo ni R2 real. Reportes: `android-system-evidence-final.log`, `android-system-response.json`, `android-environment.json`. Esta evidencia pertenece al paquete local previo. Las 26 capturas actuales de Actions no incluyen el recorrido del emulador. El CI Android remoto confirma las 22 pruebas, el análisis estático y la construcción del APK debug; no ejecuta este recorrido nativo.

### 6.1.4.3. Aplicación iOS

**No aplica al estado del repositorio:** no existe plataforma iOS activa. No se construyó, simuló ni capturó iOS. Para habilitar ese alcance posteriormente se necesitan implementación/plataforma iOS, macOS/Xcode y un simulador/dispositivo; los resultados Android no se sustituyen por iOS.


# Capítulo VII: DevOps Practices

## 7.1. Continuous Integration

La integración continua de MAX se documenta mediante configuraciones locales de construcción y pruebas para los cuatro proyectos. Se verificaron comandos locales y la sintaxis de los workflows. La ejecución de esos workflows en GitHub Actions todavía no está acreditada; por ello se distingue entre configuración preparada y automatización remota ejecutada.

### 7.1.1. Tools and Practices

| Categoría | Herramienta/version | Uso concreto | Evidencia |
|---|---|---|---|
| Versionado | Git; cuatro repositorios locales en main | SHA base + cambios locales; sin publicación | `source-state-final.json`, `changed-files.json` |
| Automatización | GitHub Actions, configuración nueva local | PR/push main/manual; reportes always; candidatos condicionados | Nueve YAML bajo `.github/workflows/` |
| Construcción backend | Java 21, Maven 3.9.12 Wrapper, Boot 4.0.8 | `verify`, JAR ejecutable | `backend-final-isolated.log` |
| Construcción web | Node 24.13.1, npm 10.9.3 configurado, Angular CLI 21.2.24 | Lockfile, bundle/browser y proxy | `web-build.log` |
| Construcción Android | Flutter 3.41.9/Java21/Gradle del proyecto | Analyze, unidades, APK debug interno | `android-analysis-final.log`, `android-build-internal.log` |
| Pruebas | JUnit6/Mockito5; Vitest4; Playwright1.55; Cucumber13; flutter_test | Unidades e integración locales reales según cada suite | XML/JSON/logs originales |
| Análisis de workflows | actionlint 1.7.11, binario oficial con checksum comprobado | Sintaxis y expresiones GitHub; shellcheck/pyflakes desactivados por no estar instalados | `workflows-actionlint.log/json` |
| Reportes | Surefire, JSON/HTML/eventos; Pillow para PNG | Preservar originales y renderizar tablas identificadas | `render_max_evidence.py`, PNG y fuentes |
| Artefactos | JAR, browser/functions, dist y APK debug | SHA-256 e identificación del código | `docs/evidencias/artefactos/manifest.json` |
| Dependencias | package-lock/pubspec.lock/Maven BOM | Instalar desde lock; registrar auditoría | `web-audit-*.json`, `web-audit-run.log` |

Las Actions se fijaron al SHA consultado de checkout v5, setup-node v6, setup-java v5, upload-artifact v4 y flutter-action v2. Fuentes y SHAs: `actions-pins.json`, [documentación de herramientas](docs/pipelines/README.md).

La auditoría detectó **7 avisos totales (5 high, 2 critical)** y **1 high en dependencias de ejecución**, Angular Router GHSA-ff3f-86qr-9cv3. El advisory se refiere a SSR; la aplicación inspeccionada es cliente Angular y no se demostró explotación. Revisar aplicabilidad y parches antes de promover; no se ejecutó `npm audit fix --force` ni se actualizaron dependencias fuera del objetivo de pruebas. El gate configurado de auditoría fallaría con este lockfile. [Advisory original](https://github.com/advisories/GHSA-ff3f-86qr-9cv3).

Ramas/PR: el trabajo siguió en main local, no se integró a remoto. Protección de rama, revisiones obligatorias y requerimientos de checks remotos **no verificados**. Configurar esos controles requiere acceso al repositorio; un YAML por sí solo no configura la protección de main.
<p align="center">
  <img src="assets/MAX-CI-Tools-Practices.png" alt="Resumen de herramientas y configuración de CI revisadas localmente." width="1000">
</p>

<p align="center"><em>Figura 25. Resumen de herramientas y configuración de CI revisadas localmente.</em></p>

### 7.1.2. Build & Test Suite Pipeline Components

| Workflow local | Eventos/jobs | Comprobaciones y artefactos | Estado |
|---|---|---|---|
| `MAX_BACK/max-backend/.github/workflows/ci.yml` | PR/push main/manual → verify | MySQL nativo del runner; Maven verify; guard de pruebas MySQL no omitidas; Surefire always; JAR+SHA | actionlint aprobado; comandos locales aprobados; Actions pendiente |
| `MAX_FRONT/MAX/.github/workflows/ci.yml` | PR/push main/manual → verify | npm ci, test:ci, build, Playwright con API sustituida, audit; browser+functions+SHA | actionlint aprobado; auditoría local fallida; Actions pendiente |
| `MAX_MOBILE/.github/workflows/ci.yml` | PR/push main/manual → verify | lock, analyze, flutter test JSON, APK debug interno+SHA; sin emulador remoto | actionlint/comandos locales aprobados; Actions pendiente |
| `MAX_LANDING/.github/workflows/ci.yml` | PR/push main/manual → verify | React local: npm ci/lint/test/build; sitio+SHA | actionlint/comandos locales aprobados; Actions pendiente |
| `MAX_FRONT/MAX/.github/workflows/integration.yml` | Solo manual; SHA backend | token de lectura limitado; checkout backend; verify; API/MySQL del runner; BDD/UI real; reportes always | actionlint aprobado; equivalente local aprobado; requiere secreto de acceso |

Los cuatro CI básicos tienen timeout, permisos `contents:read` y cancelación de ejecuciones supersedidas. Un comando fallido impide pasos posteriores de candidato; los reportes se suben incluso ante fallo. El workflow manual de integración conserva también logs backend y capturas UI. Los candidatos no contienen credenciales de producción. La shell local usó npm 11.8.0; packageManager y el CI preparado fijan npm 10.9.3. Las versiones originales constan en `reportes/tool-versions.json`. El build web pasó con tres avisos de presupuesto CSS, conservados en el log; no se modificaron esos estilos.

Ejecuciones remotas consultadas: MOBILE y REPORT no tenían runs; los back/front devolvieron 404 en la consulta pública sin autenticación (no prueba que no tengan workflows). La landing académica tiene runs históricos de Pages, descritos en 7.3; no ejecutaron estas suites ni pertenecen a la landing React local. No existe ID de Actions para los YAML nuevos porque no se publicaron. **No se generó `MAX-CI-Resultados.png` como si hubiera una ejecución remota clínica.**
<p align="center">
  <img src="assets/MAX-CI-Pipeline.png" alt="Diagrama de la configuración de CI preparada; no acredita ejecución remota." width="1000">
</p>

<p align="center"><em>Figura 26. Diagrama de la configuración de CI preparada; no acredita ejecución remota.</em></p>

## 7.2. Continuous Delivery

La entrega continua se encuentra en fase de preparación de candidatos identificables. Se empaquetaron artefactos locales y se describió cómo recuperar una construcción validada conservando su versión y sus sumas de comprobación. No se acredita despliegue en staging ni promoción remota de una versión.

### 7.2.1. Tools and Practices

Artefactos internos locales en `docs/evidencias/artefactos/`: `backend-local.jar`, `web-browser/`, `web-functions/`, `landing-react/` y `android-interno-debug.apk`. `manifest.json` registra tamaños y SHA-256. El JAR de la API evaluada tiene SHA **2198991ECE94BA42FF59BED26026CE90AE51EFFC92B548C2906B9803CA24A422**, con health UP. La fuente web fue recorrida con servidor de desarrollo; no se afirma verificación del Service Worker del bundle de producción. El APK normal debug construido al final es distinto del APK instrumental utilizado por el recorrido; no es una release firmada ni se presenta como publicación móvil validada.

No se encontró staging confirmado en configuración/documentación ni fue proporcionada una URL. Los resultados corresponden a Windows/MySQL/API/emulador locales. Ambiente clínico previsto: Pages/Railway/R2; configuración separada mediante variables, no secretos guardados. Falta canal de distribución de Android y credenciales de firma/canal de pruebas. iOS no aplica.
<p align="center">
  <img src="assets/MAX-Delivery-Tools-Practices.png" alt="Configuración de entrega y límites de la validación local." width="1000">
</p>

<p align="center"><em>Figura 27. Configuración de entrega y límites de la validación local.</em></p>

### 7.2.2. Stages Deployment Pipeline Components

Se añadieron cuatro `.github/workflows/delivery.yml`. Solo manual: recibe `ci_run_id`; exige run completado y success de `ci.yml`, main y evento push/manual; recupera el candidato del mismo SHA; verifica `commit.txt` y `SHA256SUMS`; conserva el JSON del run y el candidato. No reconstruye ni despliega, no usa `pull_request_target`, permisos limitados a lectura de código/Actions. Sin staging, la etapa remota permanece pendiente.

La versión local fue iniciada con `Start-MaxTestApi.ps1`, validada con health/BDD/UI y empaquetada con `Package-MaxLocalCandidate.ps1`. El manifest declara **no elegible para producción**: auditoría y validaciones externas pendientes. No se ejecutó delivery en Actions ni se presentó aprobación/transferencia a staging.
<p align="center">
  <img src="assets/MAX-Delivery-Pipeline.png" alt="Diagrama de preparación de candidatos; sin despliegue de staging acreditado." width="1000">
</p>

<p align="center"><em>Figura 28. Diagrama de preparación de candidatos; sin despliegue de staging acreditado.</em></p>

<p align="center">
  <img src="assets/MAX-Delivery-Local-Validacion.png" alt="Reporte de la validación local del candidato; no es evidencia de staging." width="1000">
</p>

<p align="center"><em>Figura 29. Reporte de la validación local del candidato; no es evidencia de staging.</em></p>

`MAX-Delivery-Staging.png` no se generó: no hay un despliegue de staging comprobado. Para continuar, proporcionar URL/ubicación de staging, permisos limitados y configuración protegida; usar una copia restaurada y bucket de prueba, sin modificar producción.

## 7.3. Continuous Deployment

El despliegue continuo clínico no queda demostrado con la entrega recibida. La evidencia remota disponible corresponde a ejecuciones históricas de la landing académica y a lecturas de disponibilidad. Estas observaciones se conservan como antecedentes, diferenciadas de una publicación nueva del backend, de la aplicación web o de Android.

### 7.3.1. Tools and Practices

Aplicación clínica: Cloudflare Pages, Railway/MySQL y R2 son los destinos descritos por el proyecto. El proxy Pages real está en `MAX_FRONT/MAX/functions/api/[[path]].ts`, destino fijo `MAX_API_ORIGIN`, cookies y `Set-Cookie`, con `MAX_PROXY_SECRET` opcional compartido con backend. Variables backend: `MYSQLHOST`, `MYSQLPORT`, `MYSQLDATABASE`, `MYSQLUSER`, `MYSQLPASSWORD`, `MAX_JWT_SECRET`, `MAX_JWT_EXPIRATION_MINUTES`, `MAX_CORS_ALLOWED_ORIGINS`, `MAX_PROXY_SECRET` y `MAX_R2_*` según README/configuración. Configurar valores en la plataforma; no incluir secretos en el informe.

Los disparadores/branch seleccionada, checks antes de publicar, aprobaciones y revisión activa de Pages/Railway **no pudieron verificarse en sus dashboards**. No se afirma despliegue continuo clínico. Esta entrega configura **CI y preparación manual de candidatos**; no publica automáticamente en producción. El historial de GitHub Pages acredita una automatización anterior de la landing estática académica, no del backend/Angular/Flutter.
<p align="center">
  <img src="assets/MAX-Deployment-Tools-Practices.png" alt="Revisión de configuración de publicación; sin nuevo despliegue clínico." width="1000">
</p>

<p align="center"><em>Figura 30. Revisión de configuración de publicación; sin nuevo despliegue clínico.</em></p>

### 7.3.2. Production Deployment Pipeline Components

Evidencia histórica real: [run Pages 35287404692](https://github.com/1ASI0732-2620-9086/LANDING-PAGE/actions/runs/35287404692), `pages build and deployment`, success, **17/09/2026 23:33:56 UTC**, SHA `e7352a7e834445a174568f22c5d54217ebcc5c48`. JSON original del run/listado y jobs: `landing-academic-actions.json`, `landing-academic-actions-jobs.json`. Hubo otro run success y uno cancelled; no se ocultaron. El workflow dinámico de Pages demuestra esa ejecución, pero sin acceso a settings no se verifica aquí qué aprobación/evento regula futuras publicaciones.

Lecturas del 07/10/2026 15:31:40 America/Lima: landing académica HTTP 200 con título MAX HealthTech; Railway `/actuator/health` HTTP 200 y UP. No se verificó el SHA activo de ninguno. Estas lecturas no acreditan funcionamiento clínico completo, integración Cloudflare/Railway ni publicación de los cambios locales. Fuente original: `remote-health-readonly.json`.
<p align="center">
  <img src="assets/MAX-Production-Pipeline.png" alt="Reporte de ejecuciones históricas de la landing académica en GitHub Pages." width="1000">
</p>

<p align="center"><em>Figura 31. Reporte de ejecuciones históricas de la landing académica en GitHub Pages.</em></p>

<p align="center">
  <img src="assets/MAX-Production-Validacion.png" alt="Lecturas HTTP y health registradas; no verifican la versión activa ni el flujo clínico completo." width="1000">
</p>

<p align="center"><em>Figura 32. Lecturas HTTP y health registradas; no verifican la versión activa ni el flujo clínico completo.</em></p>

Secuencia preparada para revisión (sin ejecutar): candidato aprobado → copia protegida/backup y ensayo de restauración → preflight/migraciones compatibles → backend y proxy → Angular → verificaciones sintéticas autorizadas → registrar versiones y reabrir. Antes de cualquier publicación nueva se necesita autorización explícita, destinos y acceso a controles remotos.

Recuperación documentada en `docs/pipelines/README.md`: restablecer aplicaciones a una versión compatible previa, conservar ampliaciones de esquema y no restaurar un backup antiguo sobre nuevas escrituras. No se ensayó rollback en producción ni se eliminó contenido de R2. Ninguna automatización nueva de producción se activó.

## 7.4. Continuous Monitoring

MAX incorpora una implementación de monitoreo externo de la landing académica, el frontend web y el endpoint de salud del backend. El objetivo es observar disponibilidad HTTP, contenido esperado y tiempo de respuesta, detectar incidentes y registrar su recuperación. El código, las pruebas y las evidencias de esta sección se publicaron en la rama **`feature/report-chapter-7`** de REPORT.

**Estado al 12/11/2026:** [ejecución remota 43329875776 aprobada](https://github.com/1ASI0732-2620-9086/REPORT/actions/runs/43329875776), sobre el commit `9e81225054ca93351fe6541cdc39777109b2b37e`. Pasaron 34 pruebas; los tres destinos respondieron correctamente; el simulacro abrió y cerró automáticamente la [incidencia #2](https://github.com/1ASI0732-2620-9086/REPORT/issues/2), asignada a `Carbocnito5443`. Se comprobó el aviso en el buzón de GitHub y el destinatario aportó las capturas del correo recibido. Con la integración en `main`, el workflow incorpora la programación cada 15 minutos. Las evidencias citadas aquí corresponden a las ejecuciones por `push` y no acreditan por sí solas un historial continuo de disponibilidad.

### 7.4.1. Tools and Practices

| Herramienta o práctica | Aplicación en MAX | Estado acreditado |
|---|---|---|
| Spring Boot Actuator | Consulta de lectura a `/actuator/health`; se exige HTTP 200 y estado `UP` | Endpoint publicado consultado correctamente |
| Python y biblioteca estándar | Solicitudes HTTP, validación de respuestas, medición de duración y reportes JSON/Markdown | Ejecutados localmente y en el runner; sin dependencias adicionales |
| GitHub Actions | Workflow de monitoreo separado de los pipelines de construcción y despliegue | Jobs `monitor` y `exercise` aprobados; YAML validado con actionlint |
| GitHub Issues | Apertura de un incidente por servicio y cierre al observar recuperación | Alta y cierre automáticos de la incidencia #2 comprobados |
| Responsable de alertas | `Carbocnito5443`, configurable con la variable de Actions `MONITORING_ASSIGNEE` | Asignación y aviso en GitHub comprobados; correo recibido evidenciado con capturas |
| Artefactos de Actions | Conservación de resultados por ejecución e intento durante 30 días | Dos artefactos descargados; SHA-256 contrastados con GitHub |
| Pruebas automatizadas | Casos de fallo, recuperación, latencia, respuestas inválidas, reintentos y aislamiento de incidentes | 34 pruebas aprobadas localmente y en GitHub Actions |

La configuración de destinos y umbrales se encuentra en [`monitoring/targets.json`](monitoring/targets.json). El monitor solo realiza solicitudes GET sin iniciar sesión ni acceder a expedientes, archivos o datos clínicos.

| Componente | URL supervisada | Criterio de respuesta válida |
|---|---|---|
| Landing académica | `https://1asi0732-2620-9086.github.io/LANDING-PAGE/` | HTTP 200, HTML y título `MAX HealthTech` |
| Frontend Angular | `https://max-dev-front.pages.dev/auth` | HTTP 200, HTML y elemento `app-root` |
| Backend Spring Boot | `https://maxdevback-production.up.railway.app/actuator/health` | HTTP 200, JSON y `status: UP` |

La aplicación Flutter comparte la dependencia del backend. Este monitoreo observa esa API; no acredita sesiones móviles, navegación, fallos internos, consumo de recursos ni estabilidad del APK. Tampoco acredita funcionamiento clínico completo, disponibilidad de R2 o la versión de código activa en producción.

### 7.4.2. Monitoring Pipeline Components

El workflow publicado está en [`.github/workflows/monitoring.yml`](.github/workflows/monitoring.yml) y utiliza [`monitoring/check_services.py`](monitoring/check_services.py). Sus componentes son:

1. **Disparador:** publicación de cambios del monitor en `feature/report-chapter-7`, ejecución manual o programación cada 15 minutos, en los minutos 7, 22, 37 y 52.
2. **Verificación del monitor:** pruebas automatizadas antes de consultar los servicios.
3. **Recolección:** GET HTTPS a los destinos configurados, con tiempo máximo de espera de 15 segundos por intento y validación de certificado TLS.
4. **Validación:** comprobación de código HTTP, tipo de contenido, marca HTML o estado de Actuator. Se rechazan respuestas incompletas y redirecciones a otro origen.
5. **Clasificación:** `healthy`, `degraded` o `down`, conservando cada intento y su fecha UTC, duración, código HTTP y motivo.
6. **Registro:** generación de `report.json` y `report.md`; sincronización de incidentes; conservación de artefactos y resumen del job. Los fallos o degradaciones dejan el workflow en estado fallido después de conservar los resultados.

**Restricción de activación:** GitHub ejecuta los eventos `schedule` únicamente desde la rama predeterminada y puede retrasarlos. Las ejecuciones históricas acreditadas se dispararon por `push` a `feature/report-chapter-7`. Tras la integración en `main`, el archivo queda en la rama predeterminada con horario configurado para los minutos 7, 22, 37 y 52 de cada hora. La evidencia de una ejecución programada debe identificarse por su evento `schedule`; no se atribuye esa condición a los runs históricos por `push`. [Fuente: eventos de GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

La muestra real obtenida desde el runner el **12/11/2026 a las 18:33:48–18:33:49, America/Lima** registró:

| Servicio | HTTP | Tiempo observado | Resultado |
|---|---|---|---|
| Landing académica | 200 | 189.07 ms | HTML y título esperado |
| Frontend Angular | 200 | 426.23 ms | HTML y `app-root` |
| Backend Spring Boot | 200 | 138.19 ms | JSON con `status: UP` |

Fuente original del artefacto: [JSON de comprobación](docs/evidencias/monitoring/github-43329875776/production/report.json) y [reporte legible](docs/evidencias/monitoring/github-43329875776/production/report.md). Son muestras puntuales, no porcentajes de disponibilidad ni medidas de un SLA. Los archivos contienen estados y tiempos, sin cuerpos HTML, credenciales ni información clínica.

![Resumen real de GitHub Actions con los jobs monitor y exercise aprobados, resultados HTTP y artefactos](assets/MAX-Monitoring-Resultado-GitHub.png)

*Figura 33. Captura original de la ejecución 43329875776: ambos jobs aprobados, los tres servicios saludables y los artefactos de monitoreo y simulacro con sus digest.*

### 7.4.3. Alerting Pipeline Components

Las reglas iniciales, ajustables en `targets.json`, son decisiones operativas para esta implementación:

| Condición | Tratamiento |
|---|---|
| Respuesta válida y duración de hasta 3000 ms | Servicio `healthy`; termina la comprobación del servicio |
| HTTP 200 y contenido válido, con duración mayor a 3000 ms | Intento `degraded`; se reintenta antes de registrar incidente |
| Error HTTP, timeout, conexión fallida, JSON inválido, salud diferente de `UP`, HTML inesperado o respuesta incompleta | Intento `down`; se reintenta |
| Ninguno de los tres intentos alcanza `healthy` | Incidente del servicio con el último estado observado; espera de dos segundos entre intentos |
| Ya existe un incidente abierto para ese servicio y ámbito | Se reutiliza; no se crean incidencias ni avisos repetidos por cada comprobación |
| Una comprobación posterior alcanza `healthy` | Se registra la recuperación y se cierra el incidente correspondiente |

La gestión se implementa en [`monitoring/sync_incidents.py`](monitoring/sync_incidents.py). Los incidentes se identifican por servicio y ámbito. Un resultado de simulacro no cierra incidentes de producción; un servicio no observado tampoco se declara recuperado. El sincronizador conserva las respuestas de escritura de la API durante el proceso para tolerar listados que todavía no muestran cambios recientes y exige confirmación de `state: closed`. Las pruebas cubren estas condiciones y el rechazo de la API: un error de envío o cierre no se presenta como entrega confirmada.

El [simulacro remoto](docs/evidencias/monitoring/github-43329875776/drill/exercise.json), ejecutado mediante [`monitoring/exercise.py`](monitoring/exercise.py), utilizó un servidor HTTP real en `127.0.0.1` dentro del runner de GitHub Actions:

| Fase | Respuesta observada | Intentos | Resultado |
|---|---|---|---|
| Estado inicial | HTTP 200 y `UP` | 1 | `healthy`; no se crea incidente |
| Fallo controlado | HTTP 503 | 3 | `opened`; incidencia #2 creada y asignada |
| Recuperación | HTTP 200 y `UP` | 1 | `recovered`; la misma incidencia se cierra |

El fallo ocurrió únicamente en el servidor de prueba; no se provocó una caída de los servicios publicados. La incidencia #2 se abrió a las **18:33:46** y se cerró a las **18:33:47, America/Lima**. Se verificó su estado final mediante una consulta directa a GitHub, además del reporte del workflow.

La [primera ejecución](docs/evidencias/monitoring/github-43329041988/README.md) quedó conservada como antecedente: aunque Actions mostraba `success`, la verificación posterior encontró la incidencia #1 abierta. Se corrigió el manejo del listado y se endureció el simulacro para exigir apertura y cierre; #1 se cerró como limpieza operativa y no forma parte de la evidencia de recuperación automática aprobada.

### 7.4.4. Notification Pipeline Components

El canal implementado es **GitHub Issues**, con asignación a **`Carbocnito5443`**, configurable mediante **`MONITORING_ASSIGNEE`**. La cuenta personal y su asignabilidad se verificaron antes de publicar; la incidencia real confirma la asignación. El workflow utiliza `GITHUB_TOKEN` con permisos `contents: read` e `issues: write`; el token solo se entrega al paso que gestiona incidentes. No requiere guardar credenciales de correo ni exponer información clínica.

El aviso incluye servicio, ámbito, estado, código HTTP, duración, motivo, número de intentos, fecha UTC y enlace a la ejecución. Una recuperación actualiza y cierra esa misma incidencia. El simulacro remoto utiliza una incidencia independiente identificada como **`[SIMULACRO]`**, con su ID asociado a la ejecución y al intento.

Las respuestas exitosas de la API acreditan la creación y el cierre y conservan la URL en `notifications.json`. El script comprueba que GitHub haya asignado realmente el responsable solicitado; una asignación ignorada se registra como fallo. También se consultaron las notificaciones del destinatario para este repositorio: se observó el hilo correspondiente a la incidencia #2 con motivo `assign`. La [verificación del canal](docs/evidencias/monitoring/github-43329875776/notification-verification.json) conserva ese resultado sin publicar identificadores privados del buzón ni su estado de lectura. Las capturas originales aportadas por el destinatario evidencian además la recepción de los correos de detección, recuperación, asignación y cierre. Los registros `email_receipt: not_verified` dentro de los artefactos originales describen el estado conocido por el script antes de que el usuario aportara estas capturas. [Fuente sobre las preferencias de entrega: configuración de notificaciones de GitHub](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications).

![Correo recibido de github-actions con detección HTTP 503 del simulacro y recuperación HTTP 200 de la incidencia 2](assets/MAX-Monitoring-Correo-Incidente.png)

*Figura 34. Correo recibido para la incidencia #2: fallo controlado HTTP 503 tras tres intentos y recuperación HTTP 200. El servicio mostrado es el endpoint del simulacro en el runner, no una caída de producción.*

![Correos recibidos con asignación de la incidencia 2 a Carbocnito5443 y cierre como completada](assets/MAX-Monitoring-Correo-Asignacion-Cierre.png)

*Figura 35. Correos que confirman la asignación de la incidencia #2 a Carbocnito5443 y su cierre como completada. Las tres capturas se conservaron sin modificaciones; sus hashes están en el [registro de capturas](docs/evidencias/monitoring/github-43329875776/screenshots.json).*

**Evidencia actual:** [apertura](docs/evidencias/monitoring/github-43329875776/drill/02-failure/notifications.json), [cierre](docs/evidencias/monitoring/github-43329875776/drill/03-recovery/notifications.json), [estado e historial de la incidencia](docs/evidencias/monitoring/github-43329875776/issue-events.json), [log de las 34 pruebas ejecutadas en Actions](docs/evidencias/monitoring/github-43329875776/remote-tests.log) y [resumen de verificación](docs/evidencias/monitoring/github-43329875776/verification.json). Los ZIP originales se descargaron y sus SHA-256 se contrastaron con los publicados por GitHub. La [validación local final](docs/evidencias/monitoring/final-local-validation-2026-11-12/validation.json) acredita las mismas 34 pruebas antes de publicar la corrección. La carpeta `2026-11-12/` conserva la fase previa local, cuyos registros `not_dispatched` describen únicamente esa fase.

Comandos de reproducción desde la raíz de REPORT, con Python 3.12 o posterior:

```powershell
python -m unittest discover -s monitoring -p "test_*.py" -v
python monitoring/check_services.py --config monitoring/targets.json
python monitoring/exercise.py --output monitoring-results/drill
python monitoring/sync_incidents.py --report monitoring-results/production/report.json --scope production --output monitoring-results/production
```

El último comando, sin `--apply`, registra que no se despacharon notificaciones y no consulta ni modifica GitHub. El [índice de evidencias](docs/evidencias/monitoring/README.md) distingue la fase local, el primer intento y la ejecución remota aprobada. El workflow se integró en `main` y conserva las ejecuciones históricas por `push` como evidencia. La programación está configurada en la rama predeterminada; cada ejecución posterior debe verificarse por su evento y resultado.

## Defectos encontrados y correcciones verificadas

| Hallazgo | Tipo | Corrección/estado | Archivo y evidencia |
|---|---|---|---|
| Estudio Flutter enviaba fecha sin hora; API devolvía Invalid date/time | Producto, dentro del flujo probado | Añadir T00:00:00 únicamente a yyyy-MM-dd; conservar fechas ya completas | `lib/data/max_api.dart`; regression red 1 fallo/1 pass, green 2 pass; recorrido nativo aprobado |
| Visor Flutter usaba Image.network para data URI | Producto, lectura histórica/local | Image.memory para data:image; conservar HTTP network y error visible para referencia inválida | `lib/features/shared/study_viewer.dart`; `test/study_viewer_test.dart`; intento3 fallido y final aprobado |
| Puerto web 14200 no incluido en CORS de entorno de prueba | Configuración de prueba | CORS local explícito, sin ampliar producción | `scripts/Start-MaxTestApi.ps1`; intento1 web 403, final aprobado |
| Selector DNI Android encontraba búsqueda y modal | Automatización | Seleccionar campo del modal (último visible) | `integration_test/max_system_test.dart`; intento1 Too many elements |
| Test usaba texto “Registrar estudio”; botón real “Adjuntar estudio” | Automatización | Selector corregido; UI sin cambios | Web intento2 vs final |
| Host Angular del visor no tiene caja visible; modal hijo sí | Automatización | Aserción sobre modal real y naturalWidth | Web intento3 vs final |
| Repetir suite MySQL reutilizaba DNI de pruebas | Aislamiento de pruebas | Crear esquema UUID por ejecución y eliminar solo ese esquema guardado | `MySqlWorkflowIntegrationTest.java`; ejecución fallida 5, final 63/63 |
| Surefire conserva XML antiguos | Recopilación de evidencia | Copiar solo clases nombradas por log final; total corroborado en log | `Collect-MaxEvidence.ps1`; final 63, no sumar archivo obsoleto |
| Capturas Android se perdían al reemplazar reportData | Automatización/evidencia | Conservar campos existentes y screenshots | `integration_test/max_system_test.dart`; dos capturas reales del run final |
| Auditoría Angular | Dependencias, pendiente de revisión | 1 high de ejecución/7 total; applicability SSR por revisar; sin force update | JSON/log audit; CI de candidatos bloqueará con este lockfile |

Los intentos fallidos están conservados y no forman parte del total final aprobado: `web-system-attempt1/2/3`, logs Android attempts 1/2/3, `backend-final.log` y `backend-final-failed-surefire/`. No hubo cambios visuales, renombre de paquetes, endpoints ni reglas clínicas; las dos correcciones de producto adaptan transporte/visor a contratos existentes.

## Pendientes y datos necesarios

Los archivos fuente de las pruebas, los nueve workflows y los scripts PowerShell mencionados permanecen en el workspace del equipo; no se incluyeron en `docs.zip` ni en `assets.zip`. Para permitir la reproducción, deben conservarse en los repositorios correspondientes y enlazarse desde el informe. Los reportes por sí solos no sustituyen esos archivos.

No hay implementación iOS activa en la entrega inspeccionada. Esta constatación describe el alcance técnico disponible; no sustituye los requisitos de diseño o implementación que correspondan según el enunciado y el alcance acordado del proyecto.

| Pendiente | Qué hace falta | Estado verificable |
|---|---|---|
| Staging clínico | URL/ubicación confirmada, configuración y permisos limitados | Bloqueado externamente; validación local completada |
| Actions remoto nuevo | Autorizar publicación de los cambios; acceso a repo/Actions y MAX_BACKEND_READ_TOKEN para integración web | Workflows locales y actionlint aprobados; sin run nuevo |
| Gates/PR | Configurar protección de main/checks/revisiones con acceso al repositorio | No verificado |
| R2 integración | Bucket de pruebas, credenciales limitadas e inventario sintético | No ejecutado; no tocar bucket real |
| Copia real para migración | Backup protegido/restaurable y entorno aislado autorizado | Se probó legacy sintético; no copia clínica real |
| Android release/dispositivo | Keystore/canal de pruebas y dispositivo físico | Emulador y debug local aprobados; release/distribución pendientes |
| Picker/PDF/escenarios restantes | Automatización del selector del SO, lector PDF disponible y casos ampliados | Parcial, explicitado en 6.1.4 |
| Auditoría | Revisar avisos/aplicabilidad, autorizar parche compatible y repetir gates | Fallo audit conservado |
| Publicación clínica | Acceso a dashboards, destino, SHA candidato, respaldo/recuperación y autorización expresa | No se realizó despliegue |
| iOS | Nueva plataforma/configuración, macOS/Xcode si se decide soportar | No aplica al producto actual |

## Archivos modificados y cómo comprobarlos

Inventario preciso en `reportes/changed-files.json`. Backend: pruebas nuevas y workflows; código principal conservado. Web: tres specs nuevos, BDD, recorridos UI, proxies/config de pruebas, scripts/dependencia Cucumber/lock y workflows. Flutter: cinco suites nuevas + fake API, integración/driver, SDK integration_test, dos correcciones pequeñas y workflows. Landing React: prueba de fecha, script test y workflows. Raíz: scripts, documentos, reportes y assets. No se cambió el remoto de landing ni se sobrescribió el README remoto de REPORT.

Además de los comandos anteriores:

```powershell
Push-Location MAX_LANDING
npm.cmd test
npm.cmd run lint
npm.cmd run build
Pop-Location
# Verificación estática (requiere actionlint instalado):
$flows=Get-ChildItem MAX_BACK\max-backend\.github\workflows,MAX_FRONT\MAX\.github\workflows,MAX_MOBILE\.github\workflows,MAX_LANDING\.github\workflows -Filter *.yml
actionlint -shellcheck= -pyflakes= @($flows.FullName)
# Auditoría actual: el fallo queda visible, no significa que las pruebas funcionales fallen.
Push-Location MAX_FRONT\MAX
npm.cmd audit --omit=dev
Pop-Location
```

## Inventario de imágenes y ubicación en el informe

Cada PNG de resultados se identifica como reporte renderizado; cada diagrama como configuración. Ninguno sustituye una ejecución que no ocurrió. Las fuentes están en `reportes/` y los archivos UI provienen de Playwright/Flutter.

| Apartado | Evidencia requerida | Archivo | Fuente | Estado | Pendiente |
|---|---|---|---|---|---|
| 6.1.1.1.1 | Unidades IAM/Backend | `assets/MAX-UT-IAM-Backend.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.1.1.2 | Unidades IAM/iOS | `assets/MAX-UT-IAM-iOS.png` | Sin plataforma iOS | No aplica; no generada | Decidir soporte iOS |
| 6.1.1.1.3 | Unidades IAM/Android | `assets/MAX-UT-IAM-Android.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.1.1.4 | Unidades IAM/Web | `assets/MAX-UT-IAM-Web.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.1.2.1 | Unidades Patients/Backend | `assets/MAX-UT-Patients-Backend.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.1.2.2 | Unidades Patients/iOS | `assets/MAX-UT-Patients-iOS.png` | Sin plataforma iOS | No aplica; no generada | Decidir soporte iOS |
| 6.1.1.2.3 | Unidades Patients/Android | `assets/MAX-UT-Patients-Android.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.1.2.4 | Unidades Patients/Web | `assets/MAX-UT-Patients-Web.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.1.3.1 | Unidades Studies/Backend | `assets/MAX-UT-Studies-Backend.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.1.3.2 | Unidades Studies/iOS | `assets/MAX-UT-Studies-iOS.png` | Sin plataforma iOS | No aplica; no generada | Decidir soporte iOS |
| 6.1.1.3.3 | Unidades Studies/Android | `assets/MAX-UT-Studies-Android.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.1.3.4 | Unidades Studies/Web | `assets/MAX-UT-Studies-Web.png` | XML/JSON/eventos reales | Generada | — |
| 6.1.2.1 | MAX-IT-IAM | `assets/MAX-IT-IAM.png` | docs/evidencias/reportes/backend-final-surefire/ | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.2.2 | MAX-IT-Patients | `assets/MAX-IT-Patients.png` | docs/evidencias/reportes/backend-final-surefire/ | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.2.3 | MAX-IT-Studies | `assets/MAX-IT-Studies.png` | docs/evidencias/reportes/backend-final-surefire/ | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.2.5 | MAX-IT-Ejecucion-Backend | `assets/MAX-IT-Ejecucion-Backend.png` | docs/evidencias/reportes/backend-final-isolated.log | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.2.5 | MAX-IT-Ejecucion-Web | `assets/MAX-IT-Ejecucion-Web.png` | bdd.json; system-web.json; bdd-final.log; web-system-final.log | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.3.1 | MAX-BDD-IAM-Resultados | `assets/MAX-BDD-IAM-Resultados.png` | docs/evidencias/reportes/bdd.json | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.3.2 | MAX-BDD-Patients-Resultados | `assets/MAX-BDD-Patients-Resultados.png` | docs/evidencias/reportes/bdd.json | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.3.3 | MAX-BDD-Studies-Resultados | `assets/MAX-BDD-Studies-Resultados.png` | docs/evidencias/reportes/bdd.json | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.4.1 | MAX-System-Web-Resultados | `assets/MAX-System-Web-Resultados.png` | docs/evidencias/reportes/system-web.json; system-web-artifacts/ | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.4.1 | MAX-System-Web-Recorrido | `assets/MAX-System-Web-Recorrido.png` | Playwright/Flutter captura de UI | Captura real UI | — |
| 6.1.4.1 | MAX-System-Web-Mobile-Recorrido | `assets/MAX-System-Web-Mobile-Recorrido.png` | Playwright/Flutter captura de UI | Captura real UI | — |
| 6.1.4.2 | MAX-System-Android-Resultados | `assets/MAX-System-Android-Resultados.png` | android-system-evidence-final.log; android-system-response.json; android-environment.json | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |
| 6.1.4.2 | MAX-System-Android-Recorrido | `assets/MAX-System-Android-Recorrido.png` | Playwright/Flutter captura de UI | Captura real UI | — |
| 6.1.4.2 | MAX-System-Android-Estudio | `assets/MAX-System-Android-Estudio.png` | Playwright/Flutter captura de UI | Captura real UI | — |
| 6.1.4.3 | MAX-System-iOS-Resultados | `assets/MAX-System-iOS-Resultados.png` | Sin ejecución/plataforma | No generada | iOS no aplica |
| 7.1.1 | MAX-CI-Tools-Practices | `assets/MAX-CI-Tools-Practices.png` | workflows-actionlint.log; actions-pins.json; web-audit-production.json; archivos CI locales | CONFIGURACIÓN PREPARADA · NO EJECUCIÓN REMOTA | — |
| 7.1.2 | MAX-CI-Pipeline | `assets/MAX-CI-Pipeline.png` | MAX_BACK/max-backend/.github/workflows/ci.yml; MAX_BACK/max-backend/.github/workflows/delivery.yml; MAX_FRONT/MAX/.github/workflows/ci.yml; MAX_FRONT/MAX/.github/workflows/delivery.yml; MAX_FRONT/MAX/.github/workflows/integration.yml; MAX_LANDING/.github/workflows/ci.yml; MAX_LANDING/.github/workflows/delivery.yml; MAX_MOBILE/.github/workflows/ci.yml; MAX_MOBILE/.github/workflows/delivery.yml | DIAGRAMA DE CONFIGURACIÓN · ACTIONS SIN EJECUTAR | — |
| 7.1.2 | MAX-CI-Resultados | `assets/MAX-CI-Resultados.png` | Sin ejecución/plataforma | No generada | Publicar y ejecutar CI con autorización |
| 7.2.1 | MAX-Delivery-Tools-Practices | `assets/MAX-Delivery-Tools-Practices.png` | docs/pipelines/README.md; delivery.yml; local-candidate.json | CONFIGURACIÓN REVISADA · VALIDACIÓN LOCAL | — |
| 7.2.2 | MAX-Delivery-Pipeline | `assets/MAX-Delivery-Pipeline.png` | Los cuatro .github/workflows/delivery.yml; docs/pipelines/README.md | DIAGRAMA DE CONFIGURACIÓN · SIN DESPLIEGUE | — |
| 7.2.2 | MAX-Delivery-Local-Validacion | `assets/MAX-Delivery-Local-Validacion.png` | local-candidate.json; bdd-final.log; web-system-final.log; android-system-evidence-final.log | REPORTE RENDERIZADO · CANDIDATO LOCAL REAL | — |
| 7.2.2 | MAX-Delivery-Staging | `assets/MAX-Delivery-Staging.png` | Sin ejecución/plataforma | No generada | Staging confirmado |
| 7.3.1 | MAX-Deployment-Tools-Practices | `assets/MAX-Deployment-Tools-Practices.png` | docs/pipelines/README.md; Functions API; landing-academic-actions.json | REVISIÓN DE CONFIGURACIÓN · SIN PUBLICACIÓN NUEVA | — |
| 7.3.2 | MAX-Production-Pipeline | `assets/MAX-Production-Pipeline.png` | landing-academic-actions.json; landing-academic-actions-jobs.json | REPORTE RENDERIZADO · EJECUCIONES REMOTAS HISTÓRICAS | — |
| 7.3.2 | MAX-Production-Validacion | `assets/MAX-Production-Validacion.png` | docs/evidencias/reportes/remote-health-readonly.json | REPORTE RENDERIZADO · SOLO HTTP / HEALTH | — |
| 6.1 complementario | MAX-UT-Landing-Web | `assets/MAX-UT-Landing-Web.png` | docs/evidencias/reportes/landing-unit.log | REPORTE RENDERIZADO · VALIDACIÓN LOCAL | — |

# Capítulo VIII: Experiment-Driven Development

Este capítulo presenta la planificación y el diseño de experimentos para evaluar mejoras de MAX. Se parte de las necesidades de organización de citas y documentos médicos identificadas en los capítulos anteriores, y se transforma esa información en preguntas, hipótesis, métricas y procedimientos de evaluación.

**Estado del trabajo:** los experimentos están diseñados, pero todavía no se han ejecutado. Las variantes de interfaz, la instrumentación, el reclutamiento y las mediciones descritas son propuestas para una etapa posterior. Los umbrales, las dispersiones y los tamaños de muestra son parámetros de planificación; no representan resultados observados ni usuarios ya disponibles.

## 8.1. Experiment Planning

La planificación busca determinar qué necesita aprender el equipo antes de invertir en cambios del producto. El proceso relaciona el estado actual, las suposiciones y las brechas de conocimiento con preguntas priorizadas y tarjetas de experimento. Se seleccionan tres preguntas sobre búsqueda de estudios, gestión de citas y legibilidad, manteniendo trazabilidad con los objetivos de negocio de MAX.

### 8.1.1. As-Is Summary.

MAX es una plataforma orientada a centralizar la gestión de pacientes, citas, consultas y documentación relacionada con la atención. La documentación del proyecto considera a médicos y pacientes como segmentos objetivo. En el producto revisado, las funciones operativas se concentran en la gestión realizada por el personal médico.

| Dimensión | Estado identificado | Implicación para la experimentación |
|---|---|---|
| Problema de origen | Las entrevistas documentadas describen citas y archivos distribuidos entre distintos medios, dificultades de búsqueda y cambios de agenda | La evaluación debe observar tareas concretas de localización y gestión, además de opiniones |
| Aplicación web | Frontend Angular con autenticación, pacientes, estudios, consultas, agenda y preferencias de interfaz | Permite definir una condición de referencia para los flujos de búsqueda y citas |
| Backend | API Spring Boot con control de acceso y validaciones del dominio | Las variantes deben conservar las reglas de seguridad y de agenda; no se modifica el backend como factor experimental |
| Aplicación móvil | Cliente Flutter para Android que consume la API de MAX | Permite estudiar tareas de lectura e interacción en una pantalla móvil |
| Roles revisados | El enum `UserRole` declara `ADMIN`, `MEDICO` y `ASISTENTE` | No se presupone que exista un portal autenticado de pacientes; los experimentos seleccionados se dirigen a médicos |
| Evidencia técnica | El capítulo VII acredita pruebas automatizadas y un monitoreo remoto de disponibilidad con simulacro de incidente | Esa evidencia apoya la preparación técnica, pero no mide ahorro de tiempo, facilidad de uso ni adopción |
| Evidencia de comportamiento | No se dispone de una línea base experimental para los tiempos y tasas definidos en este capítulo | Se necesita un piloto antes de fijar definitivamente la escala y ejecutar comparaciones confirmatorias |

Las entrevistas del informe aportan indicios cualitativos sobre la dispersión de documentos y la gestión de citas. No se utilizan como estimación representativa de tasas de éxito, tiempos medios o disposición de todos los usuarios. Asimismo, los avisos de monitoreo del capítulo VII no constituyen evidencia de recordatorios clínicos enviados a pacientes.

Las referencias de partida son el [informe As-Is, capítulos I a V](https://github.com/1ASI0732-2620-9086/REPORT/blob/706ede0c60d1bc2f0bc7db6b6319172633ac2c14/README.md), el [enum de roles del backend](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/ci/max-tests-actions/src/main/java/com/max/maxbackend/contexts/auth/domain/UserRole.java) y la [evidencia de monitoreo del capítulo VII](https://github.com/1ASI0732-2620-9086/REPORT/blob/ead7c059f151ed35c69abeca1e778633979bc182/README.md#74-continuous-monitoring).

### 8.1.2. Raw Material: Assumptions, Knowledge Gaps, Ideas, Claims.

El material inicial se clasifica según su naturaleza. Una idea describe una posible solución; una suposición expresa una creencia; una brecha identifica información desconocida; una afirmación debe conservar su fuente y distinguir una meta de un resultado.

#### Assumptions

| ID | Suposición del equipo | Fundamento inicial | Riesgo de equivocarse |
|---|---|---|---|
| A-01 | Un flujo de búsqueda centrado en el paciente permitirá localizar el estudio correcto con menor esfuerzo | Problema de dispersión de documentos descrito en las entrevistas | Invertir en una mejora que no reduzca el trabajo de consulta |
| A-02 | Un flujo guiado de programación y reprogramación facilitará completar cambios de agenda correctamente | Dificultades de coordinación y actualización de citas documentadas | Introducir pasos que aumenten el tiempo o generen confusión |
| A-03 | Facilitar la configuración de legibilidad en Android mejorará la ejecución de tareas de lectura e interacción | Necesidad de una plataforma sencilla y preferencias de interfaz existentes | Confundir el uso de ajustes con una mejora real de la experiencia |
| A-04 | Los beneficios observados en una tarea pueden variar según experiencia y plataforma | Diferencias entre uso web y móvil | Generalizar resultados de una plataforma o perfil a todos los usuarios |

#### Knowledge Gaps

| ID | Brecha de conocimiento | Información necesaria |
|---|---|---|
| KG-01 | No se conoce el tiempo ni la tasa de acierto al localizar estudios en el flujo actual | Tiempos por participante, errores y tareas completadas |
| KG-02 | No se conocen los puntos de dificultad al programar y reprogramar citas | Secuencia de interacción, conflictos detectados y solicitudes de ayuda |
| KG-03 | No se ha medido el efecto de los ajustes de legibilidad sobre tareas móviles | Comparación de tareas equivalentes y facilidad percibida |
| KG-04 | No se ha acreditado un flujo autenticado de acceso directo para pacientes | Definición y validación futura de ese flujo, sus permisos y su alcance |
| KG-05 | No se ha acreditado instrumentación de eventos de comportamiento para estos experimentos | Comprobación de captura, duración, deduplicación y correspondencia con resultados correctos |

#### Ideas

| ID | Propuesta para explorar | Premisa que debe probarse |
|---|---|---|
| I-01 | Prototipo de búsqueda con recorrido focalizado: localizar paciente, identificar estudio y abrirlo | A-01; la organización propuesta debe reducir tiempo sin aumentar errores |
| I-02 | Prototipo de agenda con pasos de selección, disponibilidad y resumen previo a la confirmación | A-02; la guía debe ayudar sin eliminar controles ni añadir carga innecesaria |
| I-03 | Prototipo de configuración guiada de legibilidad, con previsualización en Android | A-03; el ajuste debe aportar utilidad al realizar tareas, no solo generar interacciones |

Estas ideas son variantes experimentales por preparar. No describen funcionalidades nuevas ya implementadas ni implican que el flujo actual carezca de búsqueda, validaciones de citas o preferencias.

#### Claims

| ID | Afirmación o meta de partida | Fuente y estado |
|---|---|---|
| C-01 | Reducir en 50% el tiempo de localización de estudios mediante búsqueda digital en dos meses | BG-03 del informe: meta de negocio, no resultado medido |
| C-02 | Alcanzar 80% de atenciones programadas y documentadas mediante la agenda durante el tercer mes y eliminar cruces | BG-04: objetivo de adopción e integridad, pendiente de evaluación de campo |
| C-03 | Conseguir que 60% de los médicos personalicen la interfaz durante sus primeras dos semanas | BG-05: meta de adopción de preferencias, no demuestra por sí misma mayor facilidad de uso |
| C-04 | La plataforma cuenta con evidencia de pruebas y de disponibilidad HTTP | Capítulo VII: hecho técnico acreditado con el alcance allí descrito; no prueba las metas C-01 a C-03 |

Los objetivos se conservan como contexto de negocio. Los experimentos siguientes comparan el software actual con variantes propuestas; no equivalen a evaluar todo el cambio desde el trabajo en papel, la adopción mensual o la utilización sostenida durante dos semanas.

### 8.1.3. Experiment-Ready Questions.

Las preguntas basadas en creencias permiten contrastar una expectativa. Las exploratorias buscan comprender dificultades o requisitos todavía desconocidos, sin imponer una respuesta esperada.

| ID | Tipo | Pregunta preparada | Por qué interesa responderla |
|---|---|---|---|
| ERQ-01 | Basada en creencia | ¿El recorrido focalizado de búsqueda reduce al menos 30 segundos el tiempo penalizado de localización, frente al flujo actual en web, conservando el acierto? | Determinar si I-01 aporta eficiencia a la consulta de estudios y contribuye a BG-03 |
| ERQ-02 | Basada en creencia | ¿El flujo guiado de agenda reduce al menos 40 segundos el tiempo penalizado de completar programación y reprogramación, manteniendo las validaciones? | Evaluar una mejora del trabajo administrativo relacionada con BG-04 |
| ERQ-03 | Basada en creencia | ¿La configuración guiada de legibilidad reduce al menos 30 segundos el tiempo penalizado de una batería de tareas en Android, sin reducir su resolución correcta? | Evaluar el beneficio funcional de I-03, relacionado con BG-05 |
| ERQ-04 | Exploratoria | ¿En qué pasos y por qué se solicita ayuda o se abandona una tarea de agenda? | Explicar los resultados de ERQ-02 y orientar iteraciones |
| ERQ-05 | Exploratoria | ¿Qué ajustes y dificultades de lectura consideran relevantes los médicos durante las tareas móviles? | Explicar los resultados de ERQ-03 sin interpretar cada cambio de ajuste como éxito |
| ERQ-06 | Exploratoria | ¿Qué condiciones de acceso y control necesitarían los pacientes para consultar documentación en un flujo específico? | Reducir KG-04 antes de plantear experimentos sobre un portal no acreditado |

Los valores de 30 y 40 segundos son diferencias mínimas propuestas para planificar; se revisarán con el piloto y con el equipo antes de la fase confirmatoria. No se presentan como ahorros ya obtenidos.

Para ERQ-01, las preguntas de contexto delimitan el experimento: **quién**, médicos; **qué**, localizar y abrir un estudio sintético correcto; **dónde**, web en entorno de prueba; **cuándo**, durante una tarea con límite de 180 segundos; **por qué**, reducir la carga de búsqueda; **cómo**, comparando A y B con casos equivalentes. La misma delimitación se aplica a las otras preguntas seleccionadas.

### 8.1.4. Question Backlog.

Se mantiene un backlog amplio de seis preguntas y uno profundo con las tres preguntas que tienen Experiment Cards. El backlog contiene preguntas de investigación, no una lista de funcionalidades por implementar.

La priorización utiliza puntuaciones de 1 a 5: **C**, confianza en la creencia actual; **R**, riesgo de tomar una decisión equivocada; **I**, impacto de la respuesta; y **J**, interés del equipo y los interesados. Una confianza alta reduce la incertidumbre pendiente. Se propone:

```text
Prioridad calculada P = (6 - C) + R + I + J
```

Se ordena por P descendente. En caso de empate se prioriza el mayor riesgo; si persiste, el ID menor. Las puntuaciones son juicios iniciales del equipo y deben revisarse con nueva evidencia; no son mediciones de usuarios.

| Orden | Pregunta | C | R | I | J | P | Estado propuesto |
|---|---|---|---|---|---|---|---|
| 1 | ERQ-01 | 2 | 5 | 5 | 5 | 19 | Diseñada; pendiente de prototipo, instrumentación y piloto |
| 2 | ERQ-02 | 2 | 5 | 5 | 4 | 18 | Diseñada; pendiente de piloto |
| 3 | ERQ-03 | 1 | 4 | 4 | 5 | 18 | Diseñada; pendiente de piloto |
| 4 | ERQ-04 | 2 | 4 | 4 | 3 | 15 | Exploración secundaria dentro de EXP-02 |
| 5 | ERQ-06 | 1 | 4 | 4 | 2 | 15 | Investigación futura del flujo de pacientes; fuera de los experimentos seleccionados |
| 6 | ERQ-05 | 2 | 3 | 3 | 3 | 13 | Exploración secundaria dentro de EXP-03 |

| Backlog profundo | Experimento | Relación con el negocio | Plataforma principal |
|---|---|---|---|
| ERQ-01 | EXP-01 | BG-03: eficiencia en localización de estudios | Web |
| ERQ-02 | EXP-02 | BG-04: gestión correcta de agenda | Web |
| ERQ-03 | EXP-03 | BG-05: utilidad de la personalización | Android |

### 8.1.5. Experiment Cards.

Cada tarjeta contiene un frente con pregunta, motivación, hipótesis y la intervención mínima útil; el reverso define medidas, condiciones y escala. Las métricas M-01 a M-10 se definen de manera única en 8.2.2. Sus referencias en las tarjetas no crean métricas adicionales.

#### Experiment Card EXP-01: Localización de estudios

**Frente**

| Campo | Definición |
|---|---|
| Pregunta | ERQ-01 |
| Por qué | A-01 y KG-01; contribuir a la eficiencia de consulta de BG-03 |
| Hipótesis de trabajo | H-01: la variante B reducirá al menos 30 segundos la media de M-01 respecto de A |
| Intervención mínima útil | Prototipo de recorrido focalizado para localizar paciente, identificar estudio y abrirlo; mismas funciones y datos que el flujo de referencia |
| Segmento y plataforma | Médicos cirujanos; aplicación web de prueba |

**Reverso**

| Campo | Definición |
|---|---|
| Condiciones | A: recorrido actual congelado para el estudio. B: prototipo I-01. Casos sintéticos equivalentes y orden A/B contrabalanceado |
| Medida principal | M-01, tiempo penalizado de búsqueda; diferencia media A menos B |
| Medidas complementarias | M-02, M-05, M-08 y M-09; calidad de captura M-10 |
| Tarea y límite | Localizar y abrir el estudio indicado de un paciente sintético; 180 segundos por condición |
| Escala | Piloto con 8 médicos; planificación provisional de 48 pares válidos para la fase confirmatoria, sujeta al recálculo de 8.2.5 |
| Regla de decisión | Aplicar 8.2.7: evidencia de reducción, estimación puntual de al menos 30 segundos y cumplimiento de los controles de acierto y captura |
| Control de riesgo | Un estudio de otro paciente es error crítico, no una búsqueda exitosa; se conserva el control de acceso |
| Estado | Diseño pendiente de ejecución; no existen resultados experimentales |

#### Experiment Card EXP-02: Gestión de citas

**Frente**

| Campo | Definición |
|---|---|
| Pregunta | ERQ-02; ERQ-04 como exploración secundaria |
| Por qué | A-02 y KG-02; contribuir a la gestión de agenda de BG-04 |
| Hipótesis de trabajo | H-02: la variante B reducirá al menos 40 segundos la media de M-03 respecto de A |
| Intervención mínima útil | Prototipo I-02 con selección, revisión de disponibilidad y resumen de confirmación, conservando las mismas reglas del servidor |
| Segmento y plataforma | Médicos cirujanos; aplicación web de prueba |

**Reverso**

| Campo | Definición |
|---|---|
| Condiciones | A: formulario y recorrido actual. B: recorrido guiado. Mismo calendario sintético, restricciones y oportunidades equivalentes de completar la tarea |
| Medida principal | M-03, tiempo penalizado de una batería de programación y reprogramación |
| Medidas complementarias | M-04, M-05, M-08 y M-09; calidad de captura M-10 |
| Tarea y límite | Programar una cita y reprogramar otra, eligiendo horarios válidos; límite conjunto de 240 segundos por condición |
| Escala | Piloto con 8 médicos; planificación provisional de 48 pares válidos, según 8.2.5 |
| Regla de decisión | Aplicar 8.2.7 con diferencia puntual de al menos 40 segundos y controles de corrección de agenda |
| Control de riesgo | Las dos variantes rechazan cruces de horario. No se desactiva una validación para favorecer al tratamiento ni se modifican citas reales |
| Estado | Diseño pendiente de ejecución; no acredita adopción del módulo ni ausencia de errores en producción |

#### Experiment Card EXP-03: Legibilidad en Android

**Frente**

| Campo | Definición |
|---|---|
| Pregunta | ERQ-03; ERQ-05 como exploración secundaria |
| Por qué | A-03 y KG-03; estudiar utilidad de la personalización relacionada con BG-05 |
| Hipótesis de trabajo | H-03: la variante B reducirá al menos 30 segundos la media de M-06 respecto de A |
| Intervención mínima útil | Prototipo I-03 que facilita elegir y previsualizar ajustes de legibilidad antes de realizar las tareas |
| Segmento y plataforma | Médicos cirujanos; cliente Android de prueba |

**Reverso**

| Campo | Definición |
|---|---|
| Condiciones | A: acceso actual a preferencias. B: configuración guiada. Mismo dispositivo, contenido, servicios y acceso a los ajustes necesarios |
| Medida principal | M-06, tiempo penalizado de la batería móvil |
| Medidas complementarias | M-07, M-05, M-08 y M-09; calidad de captura M-10 |
| Tarea y límite | Configurar los ajustes que se consideren necesarios y luego localizar una cita, interpretar metadatos de un documento sintético y encontrar la acción indicada para abrirlo; límite conjunto de 360 segundos, incluido el tiempo de configuración |
| Escala | Piloto con 8 médicos; planificación provisional de 48 pares válidos, según 8.2.5 |
| Regla de decisión | Aplicar 8.2.7 con diferencia puntual de al menos 30 segundos y controles de resolución correcta |
| Control de riesgo | Las ayudas de accesibilidad habituales permanecen disponibles en A y B. No se exige utilizar una configuración incómoda para generar contraste |
| Estado | Diseño pendiente de ejecución; no se infiere reducción de fatiga física ni adopción durante dos semanas |

## 8.2. Experiment Design

El diseño establece cómo obtener evidencia útil para las tres preguntas seleccionadas. Define de antemano los resultados principales, los controles, la escala, las reglas de análisis y el seguimiento mínimo. Cualquier cambio relevante debe registrarse antes de la fase confirmatoria, con su motivo y versión del protocolo.

### 8.2.1. Hypotheses.

Para cada experimento se define una diferencia individual `d = tiempo penalizado en A - tiempo penalizado en B`. Un valor positivo favorece a B. La unidad estadística es el participante con un par de condiciones, no cada clic, evento o tarea de una misma persona.

| ID | Hipótesis de trabajo, medible y refutable | Hipótesis nula | Alternativa estadística |
|---|---|---|---|
| H-01 | I-01 reducirá la media de M-01 al menos 30 segundos, manteniendo el acierto de búsqueda | H0-01: la media de las diferencias de M-01 es cero | H1-01: la media de las diferencias de M-01 es distinta de cero |
| H-02 | I-02 reducirá la media de M-03 al menos 40 segundos, manteniendo la corrección de las citas | H0-02: la media de las diferencias de M-03 es cero | H1-02: la media de las diferencias de M-03 es distinta de cero |
| H-03 | I-03 reducirá la media de M-06 al menos 30 segundos, manteniendo la resolución de tareas móviles | H0-03: la media de las diferencias de M-06 es cero | H1-03: la media de las diferencias de M-06 es distinta de cero |

Se propone un contraste bilateral para detectar también deterioro. Los 30 o 40 segundos expresan el efecto mínimo de interés para planificar y decidir, no el valor de las hipótesis nulas. Una diferencia estadísticamente significativa menor que ese umbral no basta para recomendar la variante. Una diferencia negativa sería evidencia desfavorable a B.

Las hipótesis se someten a contraste; no se declaran verdaderas por anticipado. No rechazar H0 tampoco demuestra equivalencia entre las variantes. Las preguntas ERQ-04 a ERQ-06 son exploratorias y no reciben una hipótesis causal artificial.

### 8.2.2. Domain Business Metrics

Este catálogo es la referencia de todas las métricas de las tarjetas. Las metas son propuestas operativas para el diseño; las líneas base todavía deben medirse. Los porcentajes usan denominadores explícitos y se informan como no calculables cuando el denominador es cero.

Se define una **condición** como el bloque completo de tareas que un participante realiza con A o B en un experimento. Una ejecución sin ayuda, completada correctamente y dentro del límite obtiene su tiempo real. Un bloque no resuelto, con error crítico, ayuda, abandono voluntario de la tarea o vencimiento del tiempo recibe el límite de la tarjeta como tiempo penalizado. Las equivocaciones recuperables o validaciones rechazadas no implican por sí mismas un fallo: el cronómetro continúa y se verifica el resultado final. La ayuda se proporciona cuando se solicita; la penalización analítica no impide asistir al participante. Los fallos de captura se tratan como datos faltantes, no como tareas rápidas ni como resultados exitosos. Un intento válido significa medible y autorizado, no necesariamente exitoso.

| ID | Métrica y fórmula | Unidad | Recolección propuesta | Meta de diseño |
|---|---|---|---|---|
| M-01 | Tiempo penalizado de búsqueda: media de `t_busqueda`, con `t_busqueda = duración real` si cumple la tarea o `180` en otro caso válido | Segundos por participante y condición | Inicio, final y verificación del estudio correcto | Diferencia media A menos B de al menos 30 segundos |
| M-02 | Acierto de búsqueda: `participantes que abren el estudio correcto sin ayuda y dentro del límite / participantes con intento válido × 100` | Porcentaje por condición | Confirmación de visualización y rúbrica del observador | B al menos 90% y sin caída observada frente a A |
| M-03 | Tiempo penalizado de agenda: media del tiempo conjunto de programar y reprogramar; se asignan `240` segundos si no se completa correctamente y sin ayuda | Segundos por participante y condición | Inicio del bloque, confirmaciones y rúbrica | Diferencia media A menos B de al menos 40 segundos |
| M-04 | Resolución de agenda: `participantes que completan correctamente las dos acciones sin ayuda y dentro del límite / participantes con intento válido × 100` | Porcentaje por condición | Estado final de citas sintéticas y rúbrica | B al menos 90% y sin caída observada frente a A |
| M-05 | Errores críticos: `participantes con al menos un error crítico / participantes con intento válido × 100` | Porcentaje por experimento y condición | Rúbrica: documento de otro paciente, paciente incorrecto o fecha/horario incorrecto aceptado como correcto | Cero errores críticos observados; cualquier caso obliga a revisar la variante |
| M-06 | Tiempo penalizado de batería móvil: media de la duración total de configuración y tres tareas; se asignan `360` segundos si no se completan correctamente y sin ayuda | Segundos por participante y condición | Inicio antes de configurar y final de batería, con rúbrica de las tres tareas | Diferencia media A menos B de al menos 30 segundos |
| M-07 | Resolución móvil: media de `tareas móviles correctas sin ayuda / 3 × 100`, calculada primero para cada participante | Porcentaje por participante y condición | Rúbrica de las tres tareas | B al menos 90% y sin caída observada frente a A |
| M-08 | Necesidad de ayuda: `participantes que solicitan o reciben ayuda para el bloque / participantes con intento válido × 100` | Porcentaje por experimento y condición | Marca de ayuda del observador | Referencia descriptiva: como máximo 20% en B |
| M-09 | Facilidad percibida: mediana y distribución de respuestas a «¿Qué tan fácil fue completar estas tareas?», de 1, muy difícil, a 7, muy fácil | Escala ordinal de 1 a 7 | Pregunta del equipo al finalizar cada condición | Referencia descriptiva: mediana de al menos 5 en B |
| M-10 | Calidad de captura: `bloques realizados con registro completo, válido y deduplicado / bloques realizados que debían registrarse × 100` | Porcentaje por condición | Validación del registro y contraste con la hoja del observador | Al menos 95% antes de interpretar resultados |

M-01 y M-02 contribuyen a estudiar BG-03; M-03 a M-05, la operación de agenda de BG-04; y M-06 a M-09, la utilidad de preferencias asociada con BG-05. M-10 protege la validez de la medición. M-09 es una pregunta propia del equipo, no un instrumento SUS o NPS validado.

Estos estudios no miden directamente el ahorro frente al papel, el porcentaje de atenciones de un consultorio ni la personalización voluntaria durante dos semanas. Por tanto, sus resultados no bastarán para declarar cumplidas las metas completas BG-03, BG-04 y BG-05.

### 8.2.3. Measures.

| Experimento | Resultado principal predefinido | Resultados secundarios | Evidencia cualitativa |
|---|---|---|---|
| EXP-01 | Diferencia pareada de M-01 | M-02, M-05, M-08 y M-09 | Estrategia de búsqueda y motivos de confusión |
| EXP-02 | Diferencia pareada de M-03 | M-04, M-05, M-08 y M-09 | Pasos difíciles, interpretación de disponibilidad y motivos de ayuda; ERQ-04 |
| EXP-03 | Diferencia pareada de M-06 | M-07, M-05, M-08 y M-09 | Ajustes útiles y barreras percibidas; ERQ-05 |

M-10 se verificará en los tres experimentos. Los tiempos son medidas de razón, los aciertos y errores son resultados dicotómicos, y M-09 es una medida ordinal. Las explicaciones de los participantes se analizarán mediante temas, sin convertir una opinión aislada en una tasa generalizable.

Se propone una hoja de observación con código de participante, experimento, caso, variante, orden, resultado, duración, ayuda y error crítico. El registro automático deberá coincidir con la rúbrica; una respuesta HTTP 200, por sí sola, no demuestra que se haya abierto el documento o modificado la cita correctos.

El cronómetro empieza al presentar la instrucción y habilitar la tarea. Termina cuando se cumplen todos sus criterios, se declara el abandono o vence el límite. Los casos incluyen búsqueda, lectura y decisiones del usuario; no se interpretarán como latencia del backend. Las notas cualitativas se limitarán a dificultades de interacción y se evitará registrar información identificable o clínica.

### 8.2.4. Conditions.

#### Población y entorno

Los experimentos seleccionados se dirigirán a médicos cirujanos que gestionen citas o consulten documentación en su actividad profesional. El reclutamiento y la disponibilidad de participantes están pendientes. No se sustituirá esta población por integrantes del equipo para afirmar resultados sobre médicos; el equipo podrá participar únicamente en comprobaciones técnicas de los instrumentos.

El reclutamiento propuesto es por conveniencia, no una muestra probabilística de los médicos del país. Las conclusiones quedarán limitadas al perfil participante, las tareas y el entorno evaluados; la asignación del orden A/B no elimina ese límite de generalización.

Se utilizarán cuentas y registros sintéticos en un entorno aislado. El ambiente experimental todavía debe habilitarse. Si el piloto utiliza prototipos interactivos, A y B deberán tener la misma fidelidad funcional y los resultados se identificarán como evaluación de prototipos, no como desempeño integral del producto desplegado.

| Experimento | Control A | Tratamiento B | Elementos que deben permanecer constantes |
|---|---|---|---|
| EXP-01 | Recorrido actual de búsqueda, congelado en una versión identificada | Prototipo I-01 de recorrido focalizado | Funciones disponibles, cantidad y complejidad de documentos, dispositivo, conexión y backend |
| EXP-02 | Recorrido actual de programación y reprogramación | Prototipo I-02 con pasos y resumen | Reglas de agenda, horarios válidos y ocupados, contenido de las tareas, dispositivo y backend |
| EXP-03 | Acceso actual a ajustes de apariencia | Prototipo I-03 de configuración guiada y previsualización | Teléfono Android, contenido, condiciones de lectura, ayudas habituales y servicios |

#### Asignación y control de interferencias

Cada participante probará A y B del mismo experimento: diseño pareado con orden AB o BA asignado aleatoriamente y equilibrado. Se utilizarán dos conjuntos de casos equivalentes; también se alternará su asociación con la variante para no confundir una interfaz con un caso más sencillo. Habrá una práctica no puntuada y las mismas instrucciones para todos.

Los casos de agenda utilizarán estados aislados y equivalentes, sin que las acciones en A modifiquen los horarios que encontrará B u otro participante. En EXP-03 se partirá de la misma configuración inicial segura y aceptada por cada participante, manteniendo sus ayudas habituales. El cronómetro incluirá cualquier ajuste realizado dentro de la condición; no se excluirá el costo de configurar B.

Los tres experimentos son estudios diferentes. Si participa una misma cohorte, se realizarán en sesiones separadas por al menos 24 horas, con casos distintos y orden de experimentos contrabalanceado. No se expondrá simultáneamente a una persona a dos experimentos sobre el mismo flujo. La comparación confirmatoria será web para EXP-01 y EXP-02, y Android para EXP-03; otras plataformas serán futuras réplicas, no datos intercambiables dentro de una misma comparación.

El contrabalanceo reduce la influencia del orden, pero no elimina todo aprendizaje ni las expectativas sobre una interfaz nueva. El participante reconocerá qué recorrido utiliza; esta limitación y el efecto del entorno moderado deberán constar al interpretar los resultados.

#### Participación, exclusiones y protección

- La participación será voluntaria, con explicación del registro y posibilidad de retirarse. La actividad evaluará interacción administrativa, no decisiones de diagnóstico o tratamiento.
- Se excluirán de la muestra confirmatoria quienes diseñaron las variantes, participaron en su piloto o no cumplan el perfil. La exclusión no dependerá de si el resultado favorece a A o B.
- No se utilizarán pacientes, documentos, citas ni archivos clínicos reales. Las validaciones de seguridad y disponibilidad se conservarán en las dos variantes.
- Se mantendrán disponibles las ayudas de accesibilidad habituales. Una dificultad no justifica negar ayuda; se registra M-08 y el resultado correspondiente de la tarea.
- Se registrarán por separado fallos de instrumentación, interrupciones externas y retiros de consentimiento. Un fallo funcional de la variante es resultado del experimento y no se elimina como si fuera un problema de captura.
- Los registros de personas que retiren su consentimiento se tratarán conforme a lo explicado y acordado antes de participar. No se conservarán datos individuales contra esa decisión para completar artificialmente la muestra.

### 8.2.5. Scale Calculations and Decisions.

La escala depende de la variabilidad, la diferencia de interés y el riesgo de error aceptable. Como no existe todavía una línea base experimental, se separan un piloto de factibilidad y una fase confirmatoria condicionada a sus resultados y al reclutamiento.

#### Parámetros y cálculo inicial

Se propone una potencia de planificación de 80% por comparación principal y un error de tipo I familiar de 5% para las tres comparaciones. Se aplica Bonferroni: `alfa_individual = 0.05 / 3 = 0.016667`. Los intervalos de cada comparación principal tendrán un nivel aproximado de 98.33%, para una cobertura conjunta de al menos 95% bajo los supuestos del análisis. Este ajuste se fija antes de observar resultados. [Fundamento: método de Bonferroni, NIST](https://www.itl.nist.gov/div898/handbook/prc/section4/prc473.htm).

Para una primera aproximación sobre las diferencias pareadas se utilizará:

```text
n_z = techo[(z_(1-alfa_individual/2) + z_(potencia))² × (sigma_d / MDE)²]
```

`sigma_d` es la desviación estándar de las diferencias de cada participante, no la de todos los clics ni la de una condición aislada. La fórmula normal supone una dispersión conocida o aproximada; cuando se estima con un piloto, corresponde revisar la escala con la distribución t u otro procedimiento coherente con el método final. [Fundamento: tamaños de muestra, NIST](https://www.itl.nist.gov/div898/handbook/prc/section2/prc222.htm).

| Experimento | MDE propuesto | `sigma_d` supuesto, no medido | Cálculo normal inicial | Objetivo operativo provisional |
|---|---|---|---|---|
| EXP-01 | 30 segundos de M-01 | 60 segundos | `techo[(2.39398 + 0.84162)² × (60/30)²] = 42` pares | 48 pares válidos |
| EXP-02 | 40 segundos de M-03 | 80 segundos | `techo[(2.39398 + 0.84162)² × (80/40)²] = 42` pares | 48 pares válidos |
| EXP-03 | 30 segundos de M-06 | 60 segundos | `techo[(2.39398 + 0.84162)² × (60/30)²] = 42` pares | 48 pares válidos |

Las dispersiones de 60 y 80 segundos son supuestos ilustrativos del equipo, no estimaciones del producto. Los 48 pares añaden margen al cálculo normal inicial y facilitan contrabalancear el orden, pero **no garantizan por sí solos una potencia real de 80%**. El piloto debe permitir recalcular la escala y comprobar que el MDE tiene sentido frente a los tiempos y límites de cada tarea.

El cálculo inicial es reproducible con la biblioteca estándar de Python:

```python
from math import ceil
from statistics import NormalDist

alfa_individual = 0.05 / 3
potencia = 0.80
normal = NormalDist()
z_alfa = normal.inv_cdf(1 - alfa_individual / 2)
z_potencia = normal.inv_cdf(potencia)

for experimento, mde, sigma_d in [
    ("EXP-01", 30, 60),
    ("EXP-02", 40, 80),
    ("EXP-03", 30, 60),
]:
    pares = ceil((z_alfa + z_potencia) ** 2 * (sigma_d / mde) ** 2)
    print(experimento, pares)  # 42 pares en cada supuesto inicial
```

#### Decisiones de escala y factibilidad

| Etapa | Escala propuesta | Decisión prevista |
|---|---|---|
| Comprobación técnica | Equipo del proyecto, sin incorporarlo a la muestra de médicos | Verificar casos, rúbrica, eventos y asignación de variantes |
| Piloto | 8 médicos, que pueden participar en los tres estudios en sesiones separadas | Estimar dispersión, revisar límites, dificultad de casos y calidad de captura; resultados descriptivos |
| Confirmación | 48 pares válidos por experimento, sujetos al recálculo | Contrastar la métrica principal con la corrección definida; no contar eventos o subtareas como personas distintas |
| Reclutamiento | Hasta 60 médicos nuevos como presupuesto inicial: `techo(48 / 0.80)` | El 20% de pérdida es una reserva supuesta, no una tasa observada ni garantía de completar la muestra |
| Restricción de recursos | Si no se consigue la escala recalculada o falla la captura | Reportar el estudio como piloto o inconcluso; no afirmar potencia ni beneficios confirmados |

Los participantes del piloto no se sumarán a la fase confirmatoria. Si se utiliza la misma cohorte confirmatoria para los tres experimentos, 48 personas pueden aportar hasta 48 pares a cada estudio, no 144 personas independientes. Se propone distribuir los seis órdenes posibles de los experimentos entre ocho personas cada uno y equilibrar AB/BA dentro de cada comparación. El equilibrio final se revisará si hay retiros.

El protocolo, los MDE, los límites, la escala recalculada y el análisis deben congelarse después del piloto y antes de la confirmación. Se fijarán una ventana de reclutamiento y un máximo de participantes; no se revisarán valores p repetidamente para decidir cuándo detenerse. El calendario tentativo es de cuatro semanas después de preparar las variantes y confirmar participantes; no constituye una fecha de ejecución cumplida. La disponibilidad de médicos y del entorno es una condición de inicio pendiente.

### 8.2.6. Methods Selection.

Se seleccionan procedimientos que permitan responder las preguntas con el menor cambio útil y sin intervenir en atención real.

| Experimento o pregunta | Método | Justificación y límite |
|---|---|---|
| EXP-01 | Comparación pareada y contrabalanceada de tareas web | Cada médico actúa como referencia de sí mismo; los casos equivalentes reducen el efecto del aprendizaje |
| EXP-02 | Comparación pareada de dos recorridos de agenda | Permite observar tiempo y corrección con las mismas validaciones; no altera citas de producción |
| EXP-03 | Comparación pareada de tareas en Android | Observa el efecto funcional de la configuración guiada; no mide salud visual ni retención de dos semanas |
| ERQ-04 y ERQ-05 | Observación moderada y entrevista breve posterior a la tarea | Explica dificultades; durante la medición no se introduce una entrevista que modifique el tiempo |
| ERQ-06 | Investigación futura con pacientes y prototipos de acceso | Requiere definir primero el flujo y sus permisos; no utiliza los datos de médicos como sustituto |

El análisis principal propuesto compara la media de las diferencias pareadas de M-01, M-03 y M-06. Si el piloto respalda una aproximación razonable para esas diferencias, se predefinirá una prueba t pareada y su intervalo. No se exige que los tiempos originales de cada variante sean normales. [Fundamento: observaciones pareadas, NIST](https://www.itl.nist.gov/div898/handbook/prc/section3/prc311.htm).

Si el piloto muestra asimetría severa, demasiadas observaciones en el límite o una medición inestable, se revisarán el instrumento, el método y la escala antes de la confirmación. No se cambiará a otra prueba después de ver qué resultado produce significancia. Un cambio de estimando, como pasar de una media a una mediana, requiere actualizar hipótesis, tarjeta y cálculo de muestra.

Las tasas de éxito, errores y ayuda se informarán descriptivamente con sus numeradores, denominadores e intervalos cuando sea posible. No se afirmará no inferioridad estadística a partir de que dos porcentajes observados sean parecidos. M-09 se resumirá como escala ordinal y las notas se agruparán en temas; no se interpretará un aumento porcentual de una puntuación ordinal como un ahorro de negocio.

### 8.2.7. Data Analytics: Goals, KPIs and Metrics Selection.

Los indicadores se seleccionan por su relación con las tareas y los objetivos de negocio. Los clics, aperturas de ajustes o respuestas HTTP no se utilizarán por sí solos como prueba de valor para el usuario.

| Objetivo analítico | Trazabilidad | KPI principal | Controles e información complementaria |
|---|---|---|---|
| G-01: reducir la carga de localizar estudios correctos | BG-03 → ERQ-01 → EXP-01 → H-01 | Diferencia pareada de M-01 | M-02, M-05, M-08, M-09 y M-10 |
| G-02: facilitar programación y reprogramación correctas | BG-04 → ERQ-02 → EXP-02 → H-02 | Diferencia pareada de M-03 | M-04, M-05, M-08, M-09 y M-10; ERQ-04 explica dificultades |
| G-03: mejorar la ejecución de tareas móviles mediante legibilidad | BG-05 → ERQ-03 → EXP-03 → H-03 | Diferencia pareada de M-06 | M-07, M-05, M-08, M-09 y M-10; ERQ-05 explica preferencias |

El conjunto analítico tendrá una fila por participante, experimento y condición, con vínculo al caso y versión del instrumento. Primero se validarán esquema, duplicados y rúbrica; luego se formarán los pares A/B. Los intentos fallidos con registro válido permanecen mediante el tiempo penalizado. Los pares incompletos por captura fallida o retiro se contarán y explicarán como pérdidas, sin asignarles un tiempo cero ni ocultarlos.

Se publicarán el tamaño válido por estudio, el reparto de orden AB/BA, las diferencias estimadas, sus intervalos y las tasas complementarias. Los análisis por experiencia o plataforma no predefinidos serán exploratorios. Las tres métricas principales conservarán `alfa_individual = 0.016667`; no se probarán distintos cortes de participantes hasta obtener un resultado favorable.

| Situación observada al ejecutar | Decisión prevista |
|---|---|
| Muestra válida suficiente, M-10 al menos 95% en ambas condiciones, diferencia favorable con intervalo ajustado por encima de cero y estimación puntual que alcanza el MDE | Considerar la variante como candidata, si también cumple los controles de resolución y no presenta errores críticos |
| Diferencia favorable con evidencia estadística, pero estimación puntual menor al MDE | Reconocer una señal de mejora insuficiente para el umbral práctico propuesto; no declarar el beneficio esperado |
| Velocidad mejor, pero caída observada de M-02, M-04 o M-07, o presencia de errores críticos M-05 | No recomendar la variante sin corregir y volver a evaluar el problema |
| Intervalo compatible con ausencia de diferencia o muestra inferior a la recalculada | Informar resultado inconcluso o de piloto; no afirmar que las variantes son equivalentes |
| Captura incompleta o no confiable | Corregir la instrumentación y repetir la medición necesaria; no interpretar el problema técnico como comportamiento del usuario |

Los umbrales de acierto, ayuda y facilidad son controles operativos propuestos, no demostraciones de una tasa poblacional mínima. Un intervalo favorable frente a cero junto con una estimación que alcance el MDE tampoco demuestra que el efecto poblacional sea al menos ese MDE. La decisión debe expresar esa diferencia y sus límites.

### 8.2.8. Web and Mobile Tracking Plan.

El tracking se propone para las variantes web Angular y Android Flutter en un entorno de prueba. Su implementación y validación están pendientes; no se afirma que ya exista un SDK de analítica, un recolector publicado o eventos de negocio almacenados. El piloto puede comenzar con una hoja de observación estructurada; antes de la confirmación se necesita un mecanismo homogéneo y validado para A y B.

#### Esquema común propuesto

| Campo | Tipo y regla |
|---|---|
| `schema_version`, `event_name` | Versión del esquema y nombre de una lista permitida en `snake_case` |
| `event_id` | Identificador aleatorio para deduplicar un evento |
| `experiment_id`, `variant` | EXP-01, EXP-02 o EXP-03; variante A o B |
| `participant_code`, `session_id` | Código seudónimo del estudio y sesión aleatoria; no corresponden al ID de una cuenta clínica |
| `task_id`, `case_version` | Tarea y conjunto sintético asignado; sin identificadores de pacientes reales |
| `platform`, `environment`, `build_sha` | `web` o `android`; `experiment_test`; versión de la variante evaluada |
| `occurred_at_utc`, `consent_version` | Fecha UTC para ordenar y auditar; versión del consentimiento aplicable |
| Propiedades de resultado | Solo las necesarias según evento: duración numérica no negativa, resultado, ayuda y categoría de error de una lista permitida |

Los eventos comparten significado entre plataformas. La inclusión de Android en el esquema permite futuras réplicas de EXP-01 y EXP-02; no autoriza mezclar esas observaciones con sus comparaciones web principales.

#### Eventos y correspondencia con métricas

| Evento propuesto | Momento de captura | Propiedades específicas mínimas | Uso |
|---|---|---|---|
| `experiment_assigned` | Asignación documentada de variante, orden y caso | `sequence` AB/BA, código del caso sintético | Formar pares y auditar balance; M-10 |
| `task_started` | Presentación de instrucción y habilitación de la tarea o batería | Tipo de tarea y límite del protocolo | Inicio de M-01, M-03 y M-06 |
| `patient_lookup_started` | Inicio del recorrido de búsqueda | Ningún texto de búsqueda | Diagnóstico de EXP-01 |
| `study_view_confirmed` | Visor preparado y resultado contrastado con el caso sintético | `target_correct`, booleano validado por rúbrica | M-01 y M-02 |
| `appointment_flow_started` | Inicio de programación o reprogramación | `action_type`, de lista permitida | Diagnóstico de EXP-02 |
| `appointment_change_confirmed` | Confirmación visible del cambio y verificación del caso | `action_type`, `target_correct` | M-03 y M-04; no basta el código HTTP |
| `appointment_conflict_detected` | Rechazo de un horario ocupado del escenario sintético | Categoría de conflicto permitida | Interpretar errores y comprobar las reglas de agenda |
| `appearance_settings_opened` | Apertura de ajustes dentro de la tarea | Sin preferencias personales adicionales | Diagnóstico de EXP-03; no es KPI de éxito |
| `appearance_preview_applied` | Aplicación o previsualización de un ajuste experimental | Categoría de ajuste prevista en el protocolo | Relacionar intervención y tareas de EXP-03 |
| `assistance_recorded` | Solicitud o intervención de ayuda del moderador | Paso de la tarea y origen `requested` o `provided`, de listas permitidas | M-08 y asignación del tiempo penalizado |
| `critical_error_observed` | Registro del observador según rúbrica | Categoría de error, sin contenido clínico | M-05 |
| `task_finished` | Éxito, fallo, cancelación de tarea o vencimiento del límite | `duration_ms`, `outcome`, `assisted`, `critical_error`, cantidad de tareas correctas cuando corresponda | M-01 a M-08; conciliación con la rúbrica |
| `ease_answered` | Respuesta posterior a cada condición | `score`, entero de 1 a 7 | M-09 |

M-10 se calcula al verificar el conjunto completo, no a partir de un evento aislado. Los eventos de diagnóstico explican la secuencia y no introducen métricas de negocio adicionales a las del catálogo.

#### Recolección y calidad

La duración se obtendrá de un reloj monotónico dentro de la misma sesión, evitando restar relojes del navegador, teléfono y servidor. Los timestamps UTC se usarán para trazabilidad, no para sustituir esa medición. Una pausa, reinicio o cierre que impida reconstruir la duración se marcará para revisión; la ausencia de un evento no se interpretará automáticamente como abandono del usuario.

En el piloto se contrastarán los eventos con la observación. El protocolo de captura deberá detectar IDs duplicados, terminales faltantes, variantes incompatibles, duraciones negativas o incoherentes y resultados que no coincidan con el caso sintético. Si una tarea excede el plazo, se conserva como resultado válido con su tiempo penalizado al límite; no se elimina para mejorar el promedio. La misma transformación se aplicará a A y B. Se conservarán las causas de exclusión y las pérdidas por experimento antes de calcular sus indicadores.

El almacenamiento propuesto es un registro estructurado JSON o CSV del estudio, separado de los datos clínicos y accesible solo al equipo autorizado. Su ubicación y mecanismo de transferencia deberán definirse antes de instrumentar; este plan no crea endpoints, modifica bases de datos ni configura servicios externos.

#### Minimización y uso de la evidencia

No se incluirán nombres, DNI, correos, teléfonos, direcciones IP, identificadores de dispositivos o pacientes reales, términos de búsqueda, contenido de documentos, notas médicas, nombres de archivos, URL firmadas, cookies, JWT ni texto libre en los eventos. Un código seudónimo sigue requiriendo protección; no se presentará como anonimización irreversible.

La participación y el registro deben explicarse antes de comenzar. Se propone conservar los registros seudonimizados hasta 30 días después del cierre de la entrega, según lo acordado con los participantes, y luego conservar únicamente agregados que no permitan reidentificación. Las notas cualitativas se redactarán sin datos identificables; no se grabarán pantallas o voces por defecto. Cualquier vínculo necesario para administrar el consentimiento se mantendrá separado del registro de eventos.

Los entregables previstos son el protocolo versionado, los diccionarios de métricas y eventos, la hoja de observación, los registros seudonimizados, el informe de calidad y el análisis agregado. Se generarán durante la ejecución posterior; en esta sección se documenta su diseño, no se presentan datos recogidos ni conclusiones experimentales.

## 8.3. Experimentation

La experimentación propuesta materializa las intervenciones mínimas de EXP-01, EXP-02 y EXP-03 mediante variantes To-Be y requisitos verificables. Se mantienen las preguntas, hipótesis, métricas y condiciones de 8.1 y 8.2. El objetivo es preparar una comparación controlada del producto actual con alternativas concretas, y posteriormente recoger evidencia para decidir sobre su incorporación.

**Estado de la experimentación:** las variantes, la instrumentación y las sesiones con participantes de EXP-01 a EXP-03 continúan pendientes. En cambio, 8.3.1 y 8.3.2 catalogan funcionalidades ya implementadas en el código revisado de MAX, con énfasis en web de escritorio, landing y backend. Ese catálogo no demuestra beneficios experimentales, reclutamiento ni mediciones, y no sustituye la evidencia de pruebas y disponibilidad del capítulo VII.

#### Experimentos y variables

La variable independiente es el recorrido asignado, A o B. Cada médico probará ambas condiciones del mismo experimento, con orden AB/BA y casos equivalentes contrabalanceados. Esta comparación dentro de un estudio no implica exponerlo simultáneamente a estudios distintos sobre el mismo flujo.

| Experimento | Control A | Tratamiento B previsto | Variable dependiente principal | Controles complementarios |
|---|---|---|---|---|
| EXP-01 | Recorrido actual de localización y consulta de estudios en web | Recorrido focalizado que conserva el contexto del paciente y del estudio | Diferencia pareada de M-01 | M-02, M-05, M-08, M-09 y M-10 |
| EXP-02 | Recorrido actual de programación y reprogramación en web | Recorrido guiado con revisión de disponibilidad y confirmación del cambio | Diferencia pareada de M-03 | M-04, M-05, M-08, M-09 y M-10 |
| EXP-03 | Acceso actual a preferencias en Android | Configuración guiada de legibilidad con previsualización | Diferencia pareada de M-06 | M-07, M-05, M-08, M-09 y M-10 |

Las variables controladas incluyen la plataforma principal, el dispositivo, los servicios, la dificultad de los casos, las instrucciones y las reglas de acceso. Los casos de agenda se aíslan entre condiciones y participantes. En Android se parte de la configuración inicial segura acordada, conservando las ayudas habituales. Se registrarán orden, versión del caso y versión del producto para interpretar posibles efectos de aprendizaje o de configuración.

#### Escenarios y procedimiento previsto

| Caso del protocolo | Actividad | Verificación y límite |
|---|---|---|
| CE-01 | Localizar un paciente sintético, identificar el estudio solicitado y abrirlo | La rúbrica verifica paciente y documento correctos; 180 segundos por condición |
| CE-02 | Programar una cita sintética y reprogramar otra a horarios permitidos | Se verifican ambas acciones, ausencia de duplicación y conservación de las restricciones; 240 segundos por condición |
| CE-03 | Configurar los ajustes necesarios y realizar las tres tareas móviles de 8.1.5 | Se verifica cada tarea y se incluye el tiempo de configuración; 360 segundos por condición |

Los identificadores CE-01 a CE-03 nombran escenarios del protocolo, no pacientes ni registros existentes. Sus conjuntos equivalentes y respuestas esperadas deben definirse y versionarse antes del piloto.

1. Resolver los spikes de viabilidad y medición; documentar qué contratos y capacidades existentes permiten preparar cada variante. Cualquier necesidad de modificar una API o esquema se explicita para revisión antes de implementar.
2. Preparar A y B con versiones identificables, la misma fidelidad funcional y casos sintéticos aislados. La validación de horarios y el control de acceso permanecen en ambas condiciones.
3. Verificar que la instrumentación y la hoja de observación representen las métricas de 8.2.2, distinguiendo un fallo de tarea de un fallo de captura.
4. Confirmar elegibilidad y consentimiento, asignar el código seudónimo, el orden y los casos. La función de moderador pertenece al estudio; no crea un rol de autorización nuevo en MAX.
5. Realizar la práctica no puntuada y presentar la primera condición con instrucciones uniformes. Registrar inicio, resultado, ayuda y errores según la rúbrica.
6. Restablecer el estado aislado correspondiente y ejecutar la segunda condición con un caso equivalente. Mantener las ayudas habituales y evitar que las acciones de A alteren los datos que encontrará B.
7. Recoger de forma opcional la facilidad percibida después de cada condición y las observaciones cualitativas previstas, sin registrar información clínica real.
8. Revisar pares, pérdidas, registros duplicados y M-10. Aplicar las reglas de tiempos penalizados, sin eliminar errores funcionales para mejorar el promedio.
9. Ejecutar primero el piloto propuesto con 8 médicos; revisar instrumentos y recalcular la escala antes de congelar el protocolo confirmatorio. Los 48 pares válidos son un objetivo provisional de planificación, no una muestra reunida. La confirmación y sus decisiones seguirán 8.2.5 a 8.2.7.

La ejecución solo podrá declararse acreditada cuando existan versiones de las variantes, casos, consentimiento, registros válidos y resultados de sesiones. En esta etapa se documentan esos requisitos; no se presentan participantes ficticios ni resultados esperados como observaciones reales.

### 8.3.1. To-Be User Stories.

Este catálogo recoge **28 historias funcionales y 7 historias técnicas respaldadas por capacidades presentes en el código de MAX**. El foco es la aplicación web de escritorio, la landing académica y el backend con sus controles de seguridad. La aplicación móvil comparte parte de esos servicios, pero no se amplía aquí con historias exclusivas.

La denominación To-Be conserva la estructura del informe: los criterios describen el comportamiento objetivo de las funcionalidades que ya se encuentran implementadas en las versiones revisadas. El catálogo sustituye el listado anterior de intervenciones e instrumentos propuestos, por lo que se reorganizan sus identificadores `US-TB` y `TS-TB`. La valoración experimental, el tracking de comportamiento, los spikes y las variantes guiadas todavía no implementadas no se contabilizan como historias terminadas.

Las épicas EP-01 a EP-05 conservan sus nombres. Se utiliza el agrupador documental **EP-LP: Landing Page de MAX** para incorporar la landing ya presentada en los capítulos IV y V, sin modificar las épicas ni las historias del capítulo III. Las prioridades coinciden con el orden de 8.3.2. Los criterios mantienen la estructura Dado–Cuando–Entonces y se vinculan al código de respaldo.

**Estado del catálogo:** implementado en el código revisado. Esta constatación no equivale a una nueva ejecución de pruebas, a comprobar todos los escenarios en producción ni a haber realizado los experimentos de 8.1 y 8.2. Las referencias fijan las versiones consultadas para que el alcance sea revisable.

#### Fuentes de implementación

| Referencia | Área | Código de respaldo |
|---|---|---|
| `S-IAM` | Acceso y sesión | [auth-forms.facade.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/usuarios/application/auth-forms.facade.ts); [auth-session.service.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/usuarios/application/auth-session.service.ts); [AuthService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/auth/application/AuthService.java); [AuthController.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/auth/api/AuthController.java) |
| `S-PERFIL` | Perfil médico | [profile.facade.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/usuarios/application/profile.facade.ts); [AuthService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/auth/application/AuthService.java) |
| `S-ADMIN` | Administración | [admin.facade.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/admin/application/admin.facade.ts); [AdminService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/admin/application/AdminService.java); [ProfileLimitService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/auth/application/ProfileLimitService.java) |
| `S-INICIO` | Dashboard | [dashboard.facade.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/inicio/application/dashboard.facade.ts) |
| `S-PACIENTES` | Pacientes | [pacientes.facade.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/pacientes/application/pacientes.facade.ts); [pacientes-application.service.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/pacientes/application/pacientes-application.service.ts); [PacienteService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/pacientes/application/PacienteService.java); [ClinicalWorkflowService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/consultas/application/ClinicalWorkflowService.java) |
| `S-ESTUDIOS` | Estudios | [estudios.facade.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/estudios/application/estudios.facade.ts); [consultas.component.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/features/consultas/consultas.component.ts); [EstudioService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/estudios/application/EstudioService.java) |
| `S-VISOR` | Visor web | [estudios.component.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/features/estudios/estudios.component.ts); [study-viewer.component.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/shared/ui/study-viewer/study-viewer.component.ts); [study-viewer.component.html](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/shared/ui/study-viewer/study-viewer.component.html); [EstudioService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/estudios/application/EstudioService.java) |
| `S-AGENDA` | Agenda | [agenda.facade.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/consultas/agenda/application/agenda.facade.ts); [CitaService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/citas/application/CitaService.java) |
| `S-CONSULTAS` | Atenciones e historial | [consultas.facade.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/consultas/clinicas/application/consultas.facade.ts); [consultas-application.service.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/contexts/consultas/clinicas/application/consultas-application.service.ts); [ClinicalWorkflowService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/consultas/application/ClinicalWorkflowService.java); [ConsultaService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/consultas/application/ConsultaService.java) |
| `S-PREFERENCIAS` | Preferencias web | [configuracion.component.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/features/configuracion/configuracion.component.ts); [settings.service.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/core/settings/settings.service.ts); [i18n.service.ts](https://github.com/PersonalProjects5443/MAX_DEV_FRONT/blob/e8e395ce4784d2fa166f49acbca0c8e673688842/src/app/core/i18n/i18n.service.ts) |
| `S-LANDING` | Landing académica | [index.html](https://github.com/1ASI0732-2620-9086/LANDING-PAGE/blob/a4aeab2ab48dade34d2aed0cce153285cc462d63/index.html) |
| `S-SEGURIDAD` | Sesiones, credenciales y seguridad web | [JwtTokenService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/shared/security/JwtTokenService.java); [SessionCookieService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/shared/security/SessionCookieService.java); [SecurityConfig.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/shared/security/SecurityConfig.java) |
| `S-LIMITADOR` | Control de intentos | [AccessLimiter.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/shared/security/AccessLimiter.java); [AuthController.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/auth/api/AuthController.java) |
| `S-INTEGRIDAD` | Propietario, versiones y operaciones compuestas | [SecurityConfig.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/shared/security/SecurityConfig.java); [RecordValidation.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/shared/api/RecordValidation.java); [IdempotentOperations.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/shared/api/IdempotentOperations.java); [PacienteService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/pacientes/application/PacienteService.java); [ClinicalWorkflowService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/consultas/application/ClinicalWorkflowService.java) |
| `S-STORAGE` | Archivos y ciclo de almacenamiento | [EstudioService.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/estudios/application/EstudioService.java); [EstudioStorageLifecycle.java](https://github.com/PersonalProjects5443/MAX_DEV_BACK/blob/c789ac5f65248d5e24838fb12c9046e3b4666332/src/main/java/com/max/maxbackend/contexts/estudios/application/EstudioStorageLifecycle.java) |

Se utiliza exclusivamente la landing académica `1ASI0732-2620-9086/LANDING-PAGE`, cuyo `index.html` contiene las secciones de MAX y los enlaces al frontend. No se mezclan sus historias con la landing React de otro repositorio.

#### Cuadro de Epics, User Stories y Technical Stories

| Story ID | User | Priority | Epic | Title | Description | Acceptance Criteria |
|---|---|---|---|---|---|---|
| EP-01 | Médico y administrador | — | EP-01 | Gestión de Identidad y Acceso | Acceso, perfil, resumen del consultorio y administración de perfiles | US-TB-01, US-TB-02, US-TB-03, US-TB-04, US-TB-05, US-TB-06, US-TB-07, US-TB-08, US-TB-09 |
| US-TB-01 | Médico o administrador | 1 | EP-01 | Iniciar sesión en MAX | Como usuario registrado, deseo iniciar sesión con mi correo y contraseña, para acceder al área correspondiente a mi perfil | [CA-01.1 a CA-01.3](#us-tb-01-iniciar-sesión-en-max) |
| US-TB-02 | Profesional médico | 2 | EP-01 | Registrar una cuenta médica | Como profesional médico, deseo registrar mi cuenta con mis datos y credenciales, para utilizar MAX | [CA-02.1 a CA-02.3](#us-tb-02-registrar-una-cuenta-médica) |
| US-TB-03 | Usuario autenticado | 3 | EP-01 | Cerrar sesión de forma segura | Como usuario autenticado, deseo cerrar mi sesión, para finalizar el acceso desde el navegador | [CA-03.1 a CA-03.3](#us-tb-03-cerrar-sesión-de-forma-segura) |
| US-TB-04 | Médico | 4 | EP-01 | Consultar y actualizar el perfil médico | Como médico, deseo consultar y actualizar mis datos de perfil y fotografía, para mantener correcta mi identificación en MAX | [CA-04.1 a CA-04.3](#us-tb-04-consultar-y-actualizar-el-perfil-médico) |
| US-TB-05 | Médico | 5 | EP-01 | Cambiar la contraseña | Como médico, deseo cambiar mi contraseña comprobando la actual, para actualizar mis credenciales de acceso | [CA-05.1 a CA-05.3](#us-tb-05-cambiar-la-contraseña) |
| US-TB-06 | Médico | 6 | EP-01 | Consultar el resumen del consultorio | Como médico, deseo consultar el dashboard con pacientes, estudios, atenciones y próximas citas, para revisar la actividad de mi espacio | [CA-06.1 a CA-06.3](#us-tb-06-consultar-el-resumen-del-consultorio) |
| US-TB-07 | Administrador | 7 | EP-01 | Consultar perfiles y configurar su límite | Como administrador, deseo consultar los perfiles y configurar el límite de cuentas médicas, para controlar el cupo de MAX | [CA-07.1 a CA-07.3](#us-tb-07-consultar-perfiles-y-configurar-su-límite) |
| US-TB-08 | Administrador | 8 | EP-01 | Ingresar al contexto de un perfil médico | Como administrador, deseo ingresar al contexto de un perfil médico registrado, para acceder a su espacio mediante la operación administrativa existente | [CA-08.1 a CA-08.3](#us-tb-08-ingresar-al-contexto-de-un-perfil-médico) |
| US-TB-09 | Administrador | 9 | EP-01 | Eliminar un perfil con confirmación explícita | Como administrador, deseo confirmar la eliminación de un perfil y sus datos asociados, para gestionar una baja con conocimiento de su alcance | [CA-09.1 a CA-09.3](#us-tb-09-eliminar-un-perfil-con-confirmación-explícita) |
| EP-02 | Médico | — | EP-02 | Gestión de Pacientes | Registro, localización, consulta, actualización y eliminación de pacientes | US-TB-10, US-TB-11, US-TB-12, US-TB-13, US-TB-14 |
| US-TB-10 | Médico | 10 | EP-02 | Registrar un paciente con historial inicial | Como médico, deseo registrar los datos personales y médicos de un paciente, para crear su expediente con el historial inicial que genera MAX | [CA-10.1 a CA-10.3](#us-tb-10-registrar-un-paciente-con-historial-inicial) |
| US-TB-11 | Médico | 11 | EP-02 | Consultar y buscar pacientes por nombre o DNI | Como médico, deseo consultar mis pacientes y filtrarlos por nombre o DNI, para localizar su expediente | [CA-11.1 a CA-11.3](#us-tb-11-consultar-y-buscar-pacientes-por-nombre-o-dni) |
| US-TB-12 | Médico | 12 | EP-02 | Consultar el detalle del paciente sin editarlo | Como médico, deseo abrir la información de un paciente en modo de consulta, para revisar su expediente sin modificarlo | [CA-12.1 a CA-12.3](#us-tb-12-consultar-el-detalle-del-paciente-sin-editarlo) |
| US-TB-13 | Médico | 13 | EP-02 | Editar la información personal y médica del paciente | Como médico, deseo actualizar los datos personales, antecedentes, alergias, diagnóstico y riesgo del paciente, para mantener su expediente al día | [CA-13.1 a CA-13.3](#us-tb-13-editar-la-información-personal-y-médica-del-paciente) |
| US-TB-14 | Médico | 14 | EP-02 | Eliminar un paciente con confirmación | Como médico, deseo confirmar la eliminación de un paciente y conocer que alcanza a sus registros asociados, para evitar una baja involuntaria | [CA-14.1 a CA-14.3](#us-tb-14-eliminar-un-paciente-con-confirmación) |
| EP-03 | Médico | — | EP-03 | Gestión de Placas y Estudios | Carga, organización, consulta y eliminación de estudios clínicos | US-TB-15, US-TB-16, US-TB-17, US-TB-18 |
| US-TB-15 | Médico | 15 | EP-03 | Adjuntar un estudio al paciente y a su consulta | Como médico, deseo cargar un estudio indicando paciente y, cuando corresponda, una consulta de ese paciente, para centralizar su documentación clínica | [CA-15.1 a CA-15.3](#us-tb-15-adjuntar-un-estudio-al-paciente-y-a-su-consulta) |
| US-TB-16 | Médico | 16 | EP-03 | Buscar e identificar estudios por paciente y fecha | Como médico, deseo filtrar los estudios por paciente y fecha e identificar su tipo, para localizar el documento necesario | [CA-16.1 a CA-16.3](#us-tb-16-buscar-e-identificar-estudios-por-paciente-y-fecha) |
| US-TB-17 | Médico | 17 | EP-03 | Abrir y explorar un estudio autorizado en la web | Como médico, deseo abrir un PDF o explorar la imagen de un estudio autorizado, para revisar su contenido desde la web | [CA-17.1 a CA-17.3](#us-tb-17-abrir-y-explorar-un-estudio-autorizado-en-la-web) |
| US-TB-18 | Médico | 18 | EP-03 | Eliminar un estudio desde la consulta | Como médico, deseo eliminar un estudio asociado que ya no corresponda, para mantener organizada la documentación de la consulta | [CA-18.1 a CA-18.3](#us-tb-18-eliminar-un-estudio-desde-la-consulta) |
| EP-04 | Médico | — | EP-04 | Gestión de Consultas y Agenda Clínica | Citas, atenciones, historial y documentación asociada | US-TB-19, US-TB-20, US-TB-21, US-TB-22, US-TB-23, US-TB-24 |
| US-TB-19 | Médico | 19 | EP-04 | Consultar las citas de un paciente | Como médico, deseo consultar las citas y sus estados por paciente, para revisar su agenda registrada | [CA-19.1 a CA-19.3](#us-tb-19-consultar-las-citas-de-un-paciente) |
| US-TB-20 | Médico | 20 | EP-04 | Programar una cita futura | Como médico, deseo registrar una cita futura con paciente, fecha, motivo y notas, para organizar su atención | [CA-20.1 a CA-20.3](#us-tb-20-programar-una-cita-futura) |
| US-TB-21 | Médico | 21 | EP-04 | Editar la fecha, motivo y notas de una cita | Como médico, deseo editar la fecha, motivo y notas de una cita existente, para actualizar la agenda conservando su identidad | [CA-21.1 a CA-21.3](#us-tb-21-editar-la-fecha-motivo-y-notas-de-una-cita) |
| US-TB-22 | Médico | 22 | EP-04 | Eliminar una cita registrada | Como médico, deseo eliminar una cita de la agenda mediante la acción disponible, para retirar ese registro | [CA-22.1 a CA-22.3](#us-tb-22-eliminar-una-cita-registrada) |
| US-TB-23 | Médico | 23 | EP-04 | Registrar una atención clínica y sus adjuntos | Como médico, deseo registrar una atención con sus notas y archivos, con o sin cita previa, para documentar la atención del paciente | [CA-23.1 a CA-23.3](#us-tb-23-registrar-una-atención-clínica-y-sus-adjuntos) |
| US-TB-24 | Médico | 24 | EP-04 | Consultar el historial y editar una atención | Como médico, deseo revisar el historial del paciente y corregir las notas de una atención, para recuperar y actualizar su información clínica | [CA-24.1 a CA-24.3](#us-tb-24-consultar-el-historial-y-editar-una-atención) |
| EP-05 | Médico | — | EP-05 | Configuración y Preferencias del Sistema | Idioma, tema, tamaño de texto y preferencia local de notificaciones | US-TB-25 |
| US-TB-25 | Médico | 25 | EP-05 | Configurar las preferencias de la interfaz web | Como médico, deseo configurar idioma, tema, tamaño de texto y preferencia de notificaciones, para adaptar el uso de MAX en el navegador | [CA-25.1 a CA-25.3](#us-tb-25-configurar-las-preferencias-de-la-interfaz-web) |
| EP-LP | Visitante | — | EP-LP | Landing Page de MAX | Información pública, navegación de escritorio e ingreso a la aplicación | US-TB-26, US-TB-27, US-TB-28 |
| US-TB-26 | Visitante | 26 | EP-LP | Conocer la propuesta y las funcionalidades de MAX | Como visitante, deseo consultar la presentación, funcionalidades, misión, visión y valores de MAX, para conocer la propuesta del proyecto | [CA-26.1 a CA-26.3](#us-tb-26-conocer-la-propuesta-y-las-funcionalidades-de-max) |
| US-TB-27 | Visitante | 27 | EP-LP | Navegar por las secciones de la landing | Como visitante, deseo utilizar la navegación de la landing, para acceder a sus secciones informativas | [CA-27.1 a CA-27.3](#us-tb-27-navegar-por-las-secciones-de-la-landing) |
| US-TB-28 | Visitante | 28 | EP-LP | Ingresar a la aplicación desde la landing | Como visitante, deseo acceder al inicio de sesión desde las llamadas a la acción de la landing, para comenzar a utilizar MAX | [CA-28.1 a CA-28.3](#us-tb-28-ingresar-a-la-aplicación-desde-la-landing) |
| TS-TB-01 | Developer | 29 | Transversal: EP-01 | Proteger las credenciales y la sesión web | Como desarrollador, deseo almacenar hashes bcrypt y gestionar sesiones web con JWT y cookies protegidas, para controlar el acceso a MAX | [CA-T01.1 a CA-T01.3](#ts-tb-01-proteger-las-credenciales-y-la-sesión-web) |
| TS-TB-02 | Developer | 30 | Transversal: EP-01 | Aplicar protección CSRF y configuración CORS | Como desarrollador, deseo aplicar la protección CSRF y la política de orígenes configurada, para controlar las solicitudes web a la API | [CA-T02.1 a CA-T02.3](#ts-tb-02-aplicar-protección-csrf-y-configuración-cors) |
| TS-TB-03 | Developer | 31 | Transversal: EP-01 | Limitar intentos de acceso y registro | Como desarrollador, deseo aplicar el limitador de intentos por cuenta e IP, para restringir solicitudes repetidas de autenticación | [CA-T03.1 a CA-T03.3](#ts-tb-03-limitar-intentos-de-acceso-y-registro) |
| TS-TB-04 | Developer | 32 | Transversal: EP-01, EP-02, EP-03 y EP-04 | Aplicar permisos, aislamiento y control de versiones | Como desarrollador, deseo filtrar por propietario, restringir la administración y comprobar versiones, para proteger los registros de MAX | [CA-T04.1 a CA-T04.3](#ts-tb-04-aplicar-permisos-aislamiento-y-control-de-versiones) |
| TS-TB-05 | Developer | 33 | Transversal: EP-02 y EP-04 | Procesar las operaciones clínicas compuestas con idempotencia | Como desarrollador, deseo procesar el alta con historial y la atención mediante una clave idempotente, para controlar la repetición de esas operaciones | [CA-T05.1 a CA-T05.3](#ts-tb-05-procesar-las-operaciones-clínicas-compuestas-con-idempotencia) |
| TS-TB-06 | Developer | 34 | Transversal: EP-03 y EP-04 | Validar y gestionar los archivos clínicos | Como desarrollador, deseo validar los archivos y gestionar sus URLs de acceso y limpieza, para mantener los adjuntos asociados a los estudios autorizados | [CA-T06.1 a CA-T06.3](#ts-tb-06-validar-y-gestionar-los-archivos-clínicos) |
| TS-TB-07 | Developer | 35 | Transversal: EP-05 | Persistir las preferencias visuales y de notificaciones localmente | Como desarrollador, deseo conservar tema, tamaño de texto y preferencia de notificaciones en el navegador, para recuperarlos al iniciar MAX | [CA-T07.1 a CA-T07.3](#ts-tb-07-persistir-las-preferencias-visuales-y-de-notificaciones-localmente) |

#### US-TB-01. Iniciar sesión en MAX

**Relación As-Is:** US-01. **Respaldo implementado:** `S-IAM`; `AuthService.login; AuthSessionService.initializeSession`.

- **CA-01.1, acceso válido:** **Dado** que existe una cuenta registrada, **cuando** el usuario envía sus credenciales válidas, **entonces** se establece la sesión y se accede al área permitida para su perfil.
- **CA-01.2, credenciales incorrectas:** **Dado** que la contraseña no corresponde a la cuenta, **cuando** el usuario intenta ingresar, **entonces** el backend rechaza las credenciales y no crea una sesión autenticada.
- **CA-01.3, sesión vigente:** **Dado** que el navegador mantiene una sesión válida, **cuando** se vuelve a abrir la aplicación web, **entonces** se comprueba el usuario mediante la API y se recupera su contexto; si la sesión es rechazada, se limpia el estado local.

#### US-TB-02. Registrar una cuenta médica

**Relación As-Is:** US-02. **Respaldo implementado:** `S-IAM`; `AuthService.register; ProfileLimitService.canCreateProfile`.

- **CA-02.1, registro válido:** **Dado** que hay cupo disponible y el correo no está registrado, **cuando** el profesional envía los datos válidos del formulario, **entonces** se crea una cuenta con rol MEDICO y se establece su sesión.
- **CA-02.2, correo repetido:** **Dado** que el correo ya pertenece a una cuenta, **cuando** se solicita registrar otra cuenta con el mismo correo normalizado, **entonces** el sistema rechaza el registro sin crear un segundo usuario.
- **CA-02.3, límite alcanzado:** **Dado** que se ha alcanzado el límite de perfiles médicos configurado, **cuando** se solicita un nuevo registro, **entonces** el backend rechaza la creación y conserva los perfiles existentes.

#### US-TB-03. Cerrar sesión de forma segura

**Relación As-Is:** US-03. **Respaldo implementado:** `S-IAM`; `AuthSessionService.logout; AuthController.logout`.

- **CA-03.1, cierre confirmado:** **Dado** que existe una sesión activa y el backend responde, **cuando** el usuario cierra sesión, **entonces** el backend revoca el token recibido, elimina la cookie y el cliente limpia su estado.
- **CA-03.2, fallo de red:** **Dado** que el backend no responde durante el cierre, **cuando** finaliza el intento de cerrar sesión, **entonces** el cliente limpia igualmente su sesión y sus datos clínicos locales sin afirmar que recibió confirmación del servidor.
- **CA-03.3, otras pestañas:** **Dado** que hay otra pestaña suscrita a los eventos de sesión, **cuando** se publica el evento de cierre, **entonces** esa pestaña elimina su contexto autenticado y vuelve al acceso.

#### US-TB-04. Consultar y actualizar el perfil médico

**Relación As-Is:** US-05. **Respaldo implementado:** `S-PERFIL`; `ProfileFacade.saveProfile; handleAvatarChange; AuthService.updateProfile`.

- **CA-04.1, datos personales:** **Dado** que el médico modifica sus nombres o apellidos con valores válidos, **cuando** guarda el perfil y el servicio confirma, **entonces** se actualiza el usuario mostrado en la sesión.
- **CA-04.2, cambio de correo:** **Dado** que se solicita un correo distinto del actual, **cuando** el backend valida la actualización, **entonces** exige la contraseña actual correcta y un correo que no pertenezca a otro usuario.
- **CA-04.3, fotografía:** **Dado** que se selecciona una imagen JPEG o PNG no vacía de hasta 5 MiB, **cuando** se guarda el perfil, **entonces** se envía la fotografía seleccionada; el formulario rechaza tipos y tamaños no permitidos.

#### US-TB-05. Cambiar la contraseña

**Relación As-Is:** Complementa EP-01 y TS-02. **Respaldo implementado:** `S-PERFIL`; `ProfileFacade.changePassword; AuthService.changePassword`.

- **CA-05.1, cambio válido:** **Dado** que la contraseña actual es correcta y la nueva cumple las validaciones, **cuando** el médico confirma el cambio, **entonces** se guarda su nuevo hash y se renueva la sesión emitida para la operación.
- **CA-05.2, confirmación diferente:** **Dado** que la nueva contraseña y su confirmación son distintas, **cuando** se intenta confirmar el formulario web, **entonces** se muestra el error y no se envía el cambio.
- **CA-05.3, credencial actual incorrecta:** **Dado** que la contraseña actual no corresponde a la cuenta, **cuando** el backend procesa la solicitud, **entonces** se rechaza el cambio y no se reemplaza el hash.

#### US-TB-06. Consultar el resumen del consultorio

**Relación As-Is:** US-04. **Respaldo implementado:** `S-INICIO`; `DashboardFacade.totalPacientes; activePacientesCount; latestEstudios; recentConsultas; upcomingCitas`.

- **CA-06.1, indicadores:** **Dado** que se han cargado los datos clínicos de la sesión, **cuando** se muestra Inicio, **entonces** se calculan los pacientes totales y activos del conjunto cargado.
- **CA-06.2, actividad y agenda:** **Dado** que existen estudios, atenciones y citas programadas futuras, **cuando** se construye el resumen, **entonces** se muestran los listados recientes y las citas futuras ordenadas según sus fechas.
- **CA-06.3, carga fallida:** **Dado** que algún conjunto clínico informa un error de carga, **cuando** termina la inicialización del dashboard, **entonces** se activa el estado de fallo de carga en lugar de acreditar una carga correcta.

#### US-TB-07. Consultar perfiles y configurar su límite

**Relación As-Is:** Capacidad administrativa existente de EP-01. **Respaldo implementado:** `S-ADMIN`; `AdminFacade.loadPanel; saveProfileLimit; AdminService.listProfiles; ProfileLimitService`.

- **CA-07.1, listado válido:** **Dado** que el administrador abre su panel, **cuando** se cargan los perfiles y el límite, **entonces** se muestran los perfiles no administrativos y el cupo utilizado y configurado.
- **CA-07.2, límite válido:** **Dado** que el administrador introduce un máximo permitido y el servicio confirma, **cuando** se guarda el nuevo límite, **entonces** el panel presenta el valor confirmado y el registro médico aplica ese cupo.
- **CA-07.3, valor inválido:** **Dado** que se introduce en el formulario web un máximo inferior a 1 o superior a 10000, **cuando** se intenta guardar, **entonces** se impide enviar el cambio.

#### US-TB-08. Ingresar al contexto de un perfil médico

**Relación As-Is:** Capacidad administrativa existente de EP-01. **Respaldo implementado:** `S-ADMIN`; `AdminFacade.enterProfile; AdminService.impersonateProfile`.

- **CA-08.1, cambio válido:** **Dado** que el administrador selecciona un perfil no administrativo existente, **cuando** el servicio confirma el cambio de contexto, **entonces** se acepta la sesión de ese perfil y se navega a Inicio.
- **CA-08.2, perfil no permitido:** **Dado** que el perfil de destino es administrativo, **cuando** se solicita el cambio mediante el servicio, **entonces** el backend rechaza la operación.
- **CA-08.3, solicitud fallida:** **Dado** que el cambio de perfil no se confirma, **cuando** el panel recibe el error, **entonces** muestra el fallo sin aceptar una nueva sesión.

#### US-TB-09. Eliminar un perfil con confirmación explícita

**Relación As-Is:** Capacidad administrativa existente de EP-01. **Respaldo implementado:** `S-ADMIN`; `AdminFacade.canDeleteSelectedProfile; deleteSelectedProfile; AdminService.deleteProfile`.

- **CA-09.1, confirmación completa:** **Dado** que se selecciona un perfil no administrativo, **cuando** coinciden su correo, la frase ELIMINAR TODO y la aceptación del alcance, **entonces** la web permite solicitar la eliminación y recarga el panel tras confirmación.
- **CA-09.2, confirmación incompleta:** **Dado** que falta alguna de las confirmaciones del formulario web, **cuando** se intenta confirmar la baja, **entonces** no se envía la solicitud de eliminación.
- **CA-09.3, alcance existente:** **Dado** que el backend acepta la eliminación del perfil, **cuando** procesa sus dependencias, **entonces** elimina sus estudios, consultas, citas y pacientes, y encola la limpieza de archivos asociados; no modifica el perfil administrador.

#### US-TB-10. Registrar un paciente con historial inicial

**Relación As-Is:** US-06. **Respaldo implementado:** `S-PACIENTES`; `PacientesFacade.savePaciente; PacientesApplicationService.createWithHistory; ClinicalWorkflowService.register`.

- **CA-10.1, registro completo:** **Dado** que el formulario contiene los datos válidos del paciente, **cuando** se confirma el registro, **entonces** el backend crea el paciente, una cita REALIZADA de registro inicial y una consulta asociada.
- **CA-10.2, formulario inválido:** **Dado** que faltan campos requeridos o no se cumplen sus validaciones, **cuando** se intenta guardar, **entonces** el formulario indica los campos inválidos y no inicia el registro.
- **CA-10.3, confirmación del servicio:** **Dado** que el servicio confirma el registro compuesto, **cuando** se actualiza la interfaz, **entonces** se incorporan las entidades devueltas, se limpian los filtros y se cierra el formulario.

#### US-TB-11. Consultar y buscar pacientes por nombre o DNI

**Relación As-Is:** US-07 y US-08. **Respaldo implementado:** `S-PACIENTES`; `PacientesFacade.filteredPacientes; updateSearchName; updateSearchDni; PacientesComponent`.

- **CA-11.1, tarjetas:** **Dado** que existen pacientes en el conjunto autorizado, **cuando** se abre Pacientes, **entonces** se muestran las tarjetas con sus datos y acciones disponibles.
- **CA-11.2, búsqueda combinada:** **Dado** que se introducen nombre y DNI, **cuando** se aplican los filtros, **entonces** solo se mantienen los pacientes que cumplen ambos criterios.
- **CA-11.3, sin filtros:** **Dado** que se vacían los campos de búsqueda, **cuando** se recalcula la lista, **entonces** se vuelve a mostrar el conjunto de pacientes cargado.

#### US-TB-12. Consultar el detalle del paciente sin editarlo

**Relación As-Is:** US-09. **Respaldo implementado:** `S-PACIENTES`; `PacientesFacade.openView; prepareForm`.

- **CA-12.1, detalle:** **Dado** que se selecciona Ver en un paciente del listado, **cuando** se abre el formulario en modo de consulta, **entonces** se cargan los datos del paciente seleccionado.
- **CA-12.2, solo lectura:** **Dado** que el formulario está en modo view, **cuando** se consulta su contenido, **entonces** sus controles permanecen deshabilitados para edición.
- **CA-12.3, cierre:** **Dado** que se ha abierto el detalle sin editar, **cuando** se cierra el formulario, **entonces** no se envía una actualización del paciente.

#### US-TB-13. Editar la información personal y médica del paciente

**Relación As-Is:** US-10. **Respaldo implementado:** `S-PACIENTES`; `PacientesFacade.openEdit; savePaciente; PacienteService.update`.

- **CA-13.1, edición válida:** **Dado** que se abre un paciente en modo de edición, **cuando** se guardan datos válidos con su versión vigente, **entonces** se actualiza ese paciente y se conserva su identidad.
- **CA-13.2, fechas inválidas:** **Dado** que la fecha de nacimiento está en el futuro o fuera del rango permitido, **cuando** la solicitud se valida en el backend, **entonces** se rechaza la actualización.
- **CA-13.3, versión desactualizada:** **Dado** que otro cambio ha modificado la versión del paciente, **cuando** se envía la edición con una versión anterior, **entonces** el backend devuelve conflicto en vez de sobrescribir el registro vigente.

#### US-TB-14. Eliminar un paciente con confirmación

**Relación As-Is:** US-11. **Respaldo implementado:** `S-PACIENTES`; `PacientesFacade.confirmDelete; PacienteService.delete`.

- **CA-14.1, confirmación válida:** **Dado** que se ha seleccionado el paciente de destino, **cuando** se introduce la frase ELIMINAR PACIENTE y el servicio confirma, **entonces** se completa su eliminación y se cierra la confirmación.
- **CA-14.2, frase incorrecta:** **Dado** que la frase introducida no coincide con la requerida, **cuando** se intenta confirmar desde la web, **entonces** se muestra el error y no se envía el borrado.
- **CA-14.3, alcance del borrado:** **Dado** que el backend elimina un paciente del propietario autenticado, **cuando** procesa sus relaciones, **entonces** también elimina sus citas, consultas y estudios, encolando la limpieza de archivos; se trata de eliminación física, no de archivado lógico.

#### US-TB-15. Adjuntar un estudio al paciente y a su consulta

**Relación As-Is:** US-12. **Respaldo implementado:** `S-ESTUDIOS`; `EstudiosFacade.saveEstudio; consultOptions; EstudioService.create; validateRelations`.

- **CA-15.1, carga válida:** **Dado** que se seleccionan paciente, tipo y archivo permitido, **cuando** el servicio confirma la carga multipart, **entonces** el estudio devuelto se incorpora al listado con el paciente y la consulta opcional seleccionados.
- **CA-15.2, archivo requerido:** **Dado** que no hay un archivo seleccionado, **cuando** se intenta guardar, **entonces** se informa el archivo requerido y no se envía la carga.
- **CA-15.3, asociación incorrecta:** **Dado** que la consulta indicada no corresponde al paciente o propietario, **cuando** el backend valida la relación, **entonces** rechaza la asociación en lugar de vincular el archivo a un contexto ajeno.

#### US-TB-16. Buscar e identificar estudios por paciente y fecha

**Relación As-Is:** US-13 y US-14. **Respaldo implementado:** `S-ESTUDIOS`; `EstudiosFacade.filteredEstudios; EstudiosComponent.studyTypeLabel`.

- **CA-16.1, filtro de paciente:** **Dado** que se introduce un nombre o DNI en Estudios, **cuando** se recalculan las coincidencias, **entonces** se muestran los estudios cuyo paciente coincide con el término.
- **CA-16.2, filtro combinado:** **Dado** que se introduce además una fecha, **cuando** se filtra el repositorio, **entonces** se muestran los estudios que cumplen tanto el término como la fecha.
- **CA-16.3, identificación y orden:** **Dado** que existen varios estudios coincidentes, **cuando** se presenta el resultado, **entonces** se muestran ordenados por fecha descendente, con tipo y contexto del paciente.

#### US-TB-17. Abrir y explorar un estudio autorizado en la web

**Relación As-Is:** US-15. **Respaldo implementado:** `S-VISOR`; `EstudiosComponent.openViewer; StudyViewerComponent.openInNewTab; onWheel; onPointerMove; resetZoom`.

- **CA-17.1, imagen:** **Dado** que se obtiene la URL vigente de un estudio de imagen autorizado, **cuando** se abre y se utiliza el visor web, **entonces** se muestra la imagen y sus controles permiten ampliarla entre 1 y 3,5 y desplazarla; cerrar restablece los ajustes.
- **CA-17.2, PDF:** **Dado** que el estudio es un PDF, **cuando** se solicita su apertura desde el visor, **entonces** se ofrece abrir el documento en una pestaña del navegador.
- **CA-17.3, restricción:** **Dado** que el estudio no pertenece al propietario autenticado, **cuando** se solicita su URL mediante el backend, **entonces** no se entrega una URL de acceso para ese registro.

#### US-TB-18. Eliminar un estudio desde la consulta

**Relación As-Is:** Complementa EP-03 mediante eliminación existente. **Respaldo implementado:** `S-ESTUDIOS`; `ConsultasComponent.deleteStudy; EstudiosFacade.deleteEstudio; EstudioService.delete`.

- **CA-18.1, eliminación confirmada:** **Dado** que se selecciona un estudio del historial de consulta autorizado, **cuando** el backend confirma su eliminación, **entonces** se retira el estudio del estado local.
- **CA-18.2, archivo almacenado:** **Dado** que el estudio eliminado tiene una clave de almacenamiento, **cuando** se procesa la baja, **entonces** se encola la eliminación del objeto asociado.
- **CA-18.3, fallo del servicio:** **Dado** que no se confirma la baja del estudio, **cuando** la solicitud termina con error, **entonces** no se retira del estado local como si el borrado hubiera sido confirmado.

#### US-TB-19. Consultar las citas de un paciente

**Relación As-Is:** US-16 y consultas de agenda existentes. **Respaldo implementado:** `S-AGENDA`; `AgendaFacade.openCitasModal; citasByPaciente; nextCitaDate; lastCitaDate`.

- **CA-19.1, citas del paciente:** **Dado** que se selecciona un paciente en agenda, **cuando** se consulta su listado de citas, **entonces** se muestran únicamente las citas de ese paciente ordenadas por fecha.
- **CA-19.2, próxima cita:** **Dado** que existe una cita PROGRAMADA futura del paciente, **cuando** se calcula su próxima cita, **entonces** se selecciona la primera de esas citas por fecha ascendente.
- **CA-19.3, última cita realizada:** **Dado** que existen citas REALIZADA del paciente, **cuando** se calcula la última cita, **entonces** se selecciona la de fecha más reciente.

#### US-TB-20. Programar una cita futura

**Relación As-Is:** US-16. **Respaldo implementado:** `S-AGENDA`; `AgendaFacade.scheduleCita; CitaService.create`.

- **CA-20.1, programación válida:** **Dado** que el paciente está seleccionado y la fecha es futura, **cuando** el médico guarda y recibe confirmación del servicio, **entonces** se incorpora la cita con estado PROGRAMADA.
- **CA-20.2, fecha pasada:** **Dado** que la fecha elegida no es posterior al momento actual, **cuando** se intenta guardar desde el formulario web, **entonces** se muestra el error y no se envía la programación.
- **CA-20.3, fallo del servidor:** **Dado** que el backend no confirma el registro, **cuando** termina la solicitud, **entonces** se muestra el error y no se añade una cita ficticia al listado.

#### US-TB-21. Editar la fecha, motivo y notas de una cita

**Relación As-Is:** Complementa US-16. **Respaldo implementado:** `S-AGENDA`; `AgendaFacade.startEditCita; saveEditCita; CitaService.update`.

- **CA-21.1, edición válida:** **Dado** que se abre una cita existente con su versión vigente, **cuando** se confirma la edición y el servicio la acepta, **entonces** se actualiza la misma cita mediante su identificador.
- **CA-21.2, fecha no admitida en la web:** **Dado** que la cita está PROGRAMADA y se propone una fecha pasada, **cuando** se intenta guardar el formulario, **entonces** se rechaza el envío del cambio.
- **CA-21.3, cancelación de edición:** **Dado** que hay una cita abierta para editar, **cuando** se cancela su edición, **entonces** se descartan los campos del formulario sin enviar una actualización.

#### US-TB-22. Eliminar una cita registrada

**Relación As-Is:** Relacionada con US-18; alcance actual de eliminación. **Respaldo implementado:** `S-AGENDA`; `AgendaFacade.deleteCita; CitaService.delete`.

- **CA-22.1, baja confirmada:** **Dado** que se solicita eliminar una cita del propietario autenticado, **cuando** el backend confirma la operación, **entonces** la cita se retira del listado.
- **CA-22.2, consultas vinculadas:** **Dado** que la cita eliminada está vinculada a consultas, **cuando** el backend procesa su eliminación, **entonces** conserva las consultas y elimina su referencia a esa cita.
- **CA-22.3, fallo de eliminación:** **Dado** que la solicitud de baja falla, **cuando** la web recibe el error, **entonces** mantiene la cita en su estado local y comunica que no pudo eliminarse.

#### US-TB-23. Registrar una atención clínica y sus adjuntos

**Relación As-Is:** US-12, US-19 y US-20. **Respaldo implementado:** `S-CONSULTAS`; `ConsultasFacade.saveConsulta; ConsultasApplicationService.saveAttention; uploadFiles; ClinicalWorkflowService.attend`.

- **CA-23.1, atención sin cita previa:** **Dado** que se selecciona un paciente válido sin cita previa, **cuando** se guarda la atención, **entonces** se registra la consulta con sus campos clínicos y se crea una cita REALIZADA vinculada.
- **CA-23.2, cita programada:** **Dado** que se selecciona una cita PROGRAMADA del mismo paciente, **cuando** se guarda la atención, **entonces** se vincula la consulta y esa cita pasa a REALIZADA; una cita de otro paciente no se acepta.
- **CA-23.3, carga parcial de adjuntos:** **Dado** que la atención se guarda y falla parte de los archivos permitidos, **cuando** se solicita reintentar su carga, **entonces** se conserva la consulta guardada y se reintentan los archivos pendientes sin volver a registrar la atención.

#### US-TB-24. Consultar el historial y editar una atención

**Relación As-Is:** US-21 y US-22. **Respaldo implementado:** `S-CONSULTAS`; `ConsultasFacade.openHistory; consultasByPaciente; openConsultaEdit; ConsultaService.update`.

- **CA-24.1, historial:** **Dado** que se abre el historial de un paciente con atenciones, **cuando** se presenta el listado, **entonces** se muestran sus consultas por fecha descendente y sus estudios asociados por consulta.
- **CA-24.2, edición válida:** **Dado** que se abre una atención para editar con versión vigente, **cuando** se guardan sus notas, **entonces** se actualiza la misma consulta, se conserva createdAt y se actualiza updatedAt.
- **CA-24.3, edición concurrente:** **Dado** que la versión enviada ya no coincide con la almacenada, **cuando** se procesa la actualización, **entonces** se rechaza con conflicto sin sobrescribir la versión vigente.

#### US-TB-25. Configurar las preferencias de la interfaz web

**Relación As-Is:** US-23, US-24, US-25 y US-26. **Respaldo implementado:** `S-PREFERENCIAS`; `I18nService.setLanguage; SettingsService.setTheme; setTextSize; setNotifications`.

- **CA-25.1, idioma web:** **Dado** que la interfaz utiliza claves del catálogo de traducción, **cuando** se selecciona español o inglés, **entonces** se actualizan el idioma activo, los textos del catálogo y el atributo lang del documento.
- **CA-25.2, tema y texto:** **Dado** que se elige tema claro u oscuro y texto normal o grande, **cuando** se aplican los ajustes, **entonces** los atributos correspondientes del documento se actualizan y se guardan esas preferencias en el navegador.
- **CA-25.3, notificaciones:** **Dado** que se cambia el interruptor de notificaciones, **cuando** se guarda la elección, **entonces** se conserva el valor booleano local; el ajuste no acredita un canal de envío de avisos clínicos.

#### US-TB-26. Conocer la propuesta y las funcionalidades de MAX

**Relación As-Is:** Landing documentada en 4.3 y 5.2.2. **Respaldo implementado:** `S-LANDING`; `index.html: inicio; nosotros; funcionalidades; mision-vision; valores`.

- **CA-26.1, presentación institucional:** **Dado** que el visitante abre la landing académica, **cuando** consulta Inicio, Nosotros, Misión y visión y Valores, **entonces** encuentra los contenidos publicados del proyecto.
- **CA-26.2, funcionalidades y recorrido:** **Dado** que el visitante consulta Funcionalidades y Cómo funciona, **cuando** revisa sus tarjetas y pasos, **entonces** se presenta la información publicada sobre organización de citas y documentación.
- **CA-26.3, alcance informativo:** **Dado** que la landing describe funciones dirigidas a médicos y pacientes, **cuando** se acredita esta historia, **entonces** se acredita la publicación de ese contenido, sin afirmar que existe un portal de pacientes o una operación clínica adicional.

#### US-TB-27. Navegar por las secciones de la landing

**Relación As-Is:** Navegación implementada de la landing académica. **Respaldo implementado:** `S-LANDING`; `index.html: enlaces del encabezado y pie; identificadores de sección`.

- **CA-27.1, navegación principal:** **Dado** que se utiliza el encabezado de escritorio, **cuando** se activa un enlace de sección, **entonces** su fragmento apunta al identificador correspondiente de la misma página.
- **CA-27.2, navegación del pie:** **Dado** que el visitante llega al pie de página, **cuando** selecciona una sección de su lista de navegación, **entonces** se utiliza el enlace interno a la sección correspondiente.
- **CA-27.3, sección Contacto:** **Dado** que se selecciona el enlace Contacto, **cuando** se alcanza ese bloque, **entonces** se presenta su llamada a comenzar con MAX; no se presupone un formulario de envío inexistente.

#### US-TB-28. Ingresar a la aplicación desde la landing

**Relación As-Is:** Integración existente entre landing académica y frontend. **Respaldo implementado:** `S-LANDING`; `index.html: Ingresar a MAX; Comenzar con MAX; enlaces al frontend`.

- **CA-28.1, acceso desde el encabezado:** **Dado** que el visitante está en la landing académica, **cuando** activa Ingresar a MAX, **entonces** el enlace dirige a https://max-dev-front.pages.dev/auth.
- **CA-28.2, llamada a comenzar:** **Dado** que se consulta una llamada publicada para comenzar a usar MAX, **cuando** se activa su enlace al producto, **entonces** se utiliza el destino de autenticación del frontend.
- **CA-28.3, sesión separada:** **Dado** que se llega al frontend desde la landing, **cuando** el visitante todavía no se ha autenticado, **entonces** el enlace no crea por sí solo una sesión clínica ni confirma una cita.

#### TS-TB-01. Proteger las credenciales y la sesión web

**Relación As-Is:** TS-01 y TS-02. **Respaldo implementado:** `S-SEGURIDAD`; `AuthService; JwtTokenService; SessionCookieService; SecurityConfig.passwordEncoder`.

- **CA-T01.1, contraseñas:** **Dado** que se registra una cuenta o se acepta cambiar su contraseña, **cuando** se persiste la credencial, **entonces** se almacena el hash bcrypt y se usa el codificador para comprobarla.
- **CA-T01.2, sesión web segura:** **Dado** que la autenticación es válida y se utiliza la configuración segura con legacy bearer desactivado, **cuando** se emite la sesión, **entonces** se escribe la cookie HttpOnly y Secure con SameSite=Lax y no se entrega el token en el cuerpo.
- **CA-T01.3, revocación:** **Dado** que se confirma un cierre o cambio de contraseña, **cuando** se invalidan las sesiones correspondientes, **entonces** un token revocado no se acepta como sesión vigente.

#### TS-TB-02. Aplicar protección CSRF y configuración CORS

**Relación As-Is:** Amplía TS-01 con protección implementada. **Respaldo implementado:** `S-SEGURIDAD`; `SecurityConfig.securityFilterChain; csrfRepository; corsConfigurationSource`.

- **CA-T02.1, token CSRF:** **Dado** que el cliente prepara la sesión web, **cuando** consulta el recurso CSRF, **entonces** obtiene el token que el flujo web utiliza para sus solicitudes protegidas.
- **CA-T02.2, escritura sin protección:** **Dado** que una solicitud de escritura requiere protección CSRF, **cuando** se envía sin un token aceptable, **entonces** el filtro de seguridad rechaza esa solicitud.
- **CA-T02.3, orígenes configurados:** **Dado** que el navegador realiza una solicitud entre orígenes, **cuando** se evalúa la política CORS, **entonces** se utilizan los orígenes configurados y la opción de credenciales de la API.

#### TS-TB-03. Limitar intentos de acceso y registro

**Relación As-Is:** Control existente de seguridad de EP-01. **Respaldo implementado:** `S-LIMITADOR`; `AccessLimiter.check; failure; AuthController.login; register`.

- **CA-T03.1, ventana de control:** **Dado** que llega una solicitud de login o registro, **cuando** el controlador consulta el limitador, **entonces** se cuentan los intentos dentro de su ventana configurada.
- **CA-T03.2, límite alcanzado:** **Dado** que la cuenta o IP alcanza su límite aplicable, **cuando** se procesa otro intento dentro de la ventana, **entonces** se responde con HTTP 429.
- **CA-T03.3, credenciales fallidas:** **Dado** que un login es rechazado por credenciales incorrectas, **cuando** el controlador procesa el rechazo, **entonces** se registra el fallo de la cuenta mediante su identificador derivado.

#### TS-TB-04. Aplicar permisos, aislamiento y control de versiones

**Relación As-Is:** TS-01 y repositorios existentes. **Respaldo implementado:** `S-INTEGRIDAD`; `SecurityConfig; AuthenticationSupport; repositorios por propietario; RecordValidation.version`.

- **CA-T04.1, aislamiento:** **Dado** que una sesión solicita registros clínicos, **cuando** se ejecuta su consulta o modificación, **entonces** se resuelven los datos por el propietario autenticado, sin aceptar un identificador ajeno como recurso propio.
- **CA-T04.2, permiso administrativo:** **Dado** que la sesión no tiene rol ADMIN, **cuando** solicita /api/admin/, **entonces** el filtro de seguridad rechaza la operación.
- **CA-T04.3, versión desactualizada:** **Dado** que una actualización no envía la versión vigente, **cuando** el servicio compara las versiones, **entonces** se responde con HTTP 409 sin omitir la comprobación.

#### TS-TB-05. Procesar las operaciones clínicas compuestas con idempotencia

**Relación As-Is:** TS-06 y flujo compuesto existente. **Respaldo implementado:** `S-INTEGRIDAD`; `ClinicalWorkflowService.register; attend; IdempotentOperations.execute`.

- **CA-T05.1, operación válida:** **Dado** que se recibe una clave válida con el alta o atención, **cuando** se ejecuta el flujo compuesto, **entonces** se conserva el recibo del resultado dentro de la transacción.
- **CA-T05.2, repetición equivalente:** **Dado** que se repite la misma clave para el mismo usuario y operación con la misma entrada, **cuando** se procesa la repetición, **entonces** se devuelve el resultado del recibo sin ejecutar otra vez la acción.
- **CA-T05.3, reutilización incompatible:** **Dado** que se reutiliza una clave con datos distintos, **cuando** se compara la huella de entrada, **entonces** se responde con conflicto sin repetir la acción.

#### TS-TB-06. Validar y gestionar los archivos clínicos

**Relación As-Is:** TS-04 y TS-05. **Respaldo implementado:** `S-STORAGE`; `EstudioService.prepareUpload; validateMagic; accessUrl; EstudioStorageLifecycle`.

- **CA-T06.1, validación:** **Dado** que se recibe un archivo clínico, **cuando** se prepara la carga, **entonces** se comprueban tipo permitido, extensión, firma y tamaño no vacío de hasta 20 MiB para JPEG, PNG, WebP o PDF.
- **CA-T06.2, acceso al archivo:** **Dado** que un estudio autorizado tiene una clave de almacenamiento, **cuando** se solicita su acceso, **entonces** se devuelve la URL temporal si el almacenamiento está configurado o un error de servicio no disponible si no lo está.
- **CA-T06.3, limpieza diferida:** **Dado** que se elimina un registro con un archivo almacenado, **cuando** se procesa la cola de limpieza de objetos sin estudio vigente, **entonces** se intenta eliminar el objeto y se conserva una tarea de reintento si el proveedor falla.

#### TS-TB-07. Persistir las preferencias visuales y de notificaciones localmente

**Relación As-Is:** TS-08 con alcance local comprobado. **Respaldo implementado:** `S-PREFERENCIAS`; `SettingsService.persist; loadSettings; apply`.

- **CA-T07.1, persistencia:** **Dado** que el usuario cambia una preferencia admitida, **cuando** se ejecuta su setter, **entonces** se guarda el conjunto de preferencias en la clave local max_settings.
- **CA-T07.2, recuperación:** **Dado** que el navegador contiene preferencias guardadas con valores válidos, **cuando** se construye el servicio, **entonces** se recuperan el tema, tamaño y valor booleano de notificaciones.
- **CA-T07.3, datos no válidos:** **Dado** que el valor almacenado no puede interpretarse o contiene opciones no admitidas, **cuando** se cargan las preferencias, **entonces** se utilizan los valores predeterminados o normalizados correspondientes.

### 8.3.2. To-Be Product Backlog

El Product Backlog consolida las mismas **35 historias** del catálogo anterior, sin incorporar funcionalidades hipotéticas. El orden agrupa primero el acceso y la administración, luego pacientes, estudios, agenda y atenciones, preferencias y landing; finalmente presenta los habilitadores técnicos. Es un orden documental de valor y alcance, no la cronología en que se construyeron las funcionalidades ni una autorización para ignorar sus dependencias.

Los Story Points conservan la escala 1, 2, 3, 5 y 8. En esta edición son **estimaciones documentales retrospectivas de complejidad**, sujetas a revisión por el equipo; no son mediciones del esfuerzo realmente empleado, horas trabajadas ni puntos de desarrollo pendiente. El estado común de los elementos es **implementado en el código revisado**, con el alcance de evidencia señalado en 8.3.1.

| Orden | User Story ID | Título | Descripción | Story Points |
|---|---|---|---|---|
| 1 | US-TB-01 | Iniciar sesión en MAX | Como usuario registrado, deseo iniciar sesión con mi correo y contraseña, para acceder al área correspondiente a mi perfil | 3 |
| 2 | US-TB-02 | Registrar una cuenta médica | Como profesional médico, deseo registrar mi cuenta con mis datos y credenciales, para utilizar MAX | 3 |
| 3 | US-TB-03 | Cerrar sesión de forma segura | Como usuario autenticado, deseo cerrar mi sesión, para finalizar el acceso desde el navegador | 2 |
| 4 | US-TB-04 | Consultar y actualizar el perfil médico | Como médico, deseo consultar y actualizar mis datos de perfil y fotografía, para mantener correcta mi identificación en MAX | 5 |
| 5 | US-TB-05 | Cambiar la contraseña | Como médico, deseo cambiar mi contraseña comprobando la actual, para actualizar mis credenciales de acceso | 3 |
| 6 | US-TB-06 | Consultar el resumen del consultorio | Como médico, deseo consultar el dashboard con pacientes, estudios, atenciones y próximas citas, para revisar la actividad de mi espacio | 3 |
| 7 | US-TB-07 | Consultar perfiles y configurar su límite | Como administrador, deseo consultar los perfiles y configurar el límite de cuentas médicas, para controlar el cupo de MAX | 5 |
| 8 | US-TB-08 | Ingresar al contexto de un perfil médico | Como administrador, deseo ingresar al contexto de un perfil médico registrado, para acceder a su espacio mediante la operación administrativa existente | 5 |
| 9 | US-TB-09 | Eliminar un perfil con confirmación explícita | Como administrador, deseo confirmar la eliminación de un perfil y sus datos asociados, para gestionar una baja con conocimiento de su alcance | 5 |
| 10 | US-TB-10 | Registrar un paciente con historial inicial | Como médico, deseo registrar los datos personales y médicos de un paciente, para crear su expediente con el historial inicial que genera MAX | 5 |
| 11 | US-TB-11 | Consultar y buscar pacientes por nombre o DNI | Como médico, deseo consultar mis pacientes y filtrarlos por nombre o DNI, para localizar su expediente | 3 |
| 12 | US-TB-12 | Consultar el detalle del paciente sin editarlo | Como médico, deseo abrir la información de un paciente en modo de consulta, para revisar su expediente sin modificarlo | 2 |
| 13 | US-TB-13 | Editar la información personal y médica del paciente | Como médico, deseo actualizar los datos personales, antecedentes, alergias, diagnóstico y riesgo del paciente, para mantener su expediente al día | 5 |
| 14 | US-TB-14 | Eliminar un paciente con confirmación | Como médico, deseo confirmar la eliminación de un paciente y conocer que alcanza a sus registros asociados, para evitar una baja involuntaria | 3 |
| 15 | US-TB-15 | Adjuntar un estudio al paciente y a su consulta | Como médico, deseo cargar un estudio indicando paciente y, cuando corresponda, una consulta de ese paciente, para centralizar su documentación clínica | 5 |
| 16 | US-TB-16 | Buscar e identificar estudios por paciente y fecha | Como médico, deseo filtrar los estudios por paciente y fecha e identificar su tipo, para localizar el documento necesario | 3 |
| 17 | US-TB-17 | Abrir y explorar un estudio autorizado en la web | Como médico, deseo abrir un PDF o explorar la imagen de un estudio autorizado, para revisar su contenido desde la web | 5 |
| 18 | US-TB-18 | Eliminar un estudio desde la consulta | Como médico, deseo eliminar un estudio asociado que ya no corresponda, para mantener organizada la documentación de la consulta | 3 |
| 19 | US-TB-19 | Consultar las citas de un paciente | Como médico, deseo consultar las citas y sus estados por paciente, para revisar su agenda registrada | 2 |
| 20 | US-TB-20 | Programar una cita futura | Como médico, deseo registrar una cita futura con paciente, fecha, motivo y notas, para organizar su atención | 3 |
| 21 | US-TB-21 | Editar la fecha, motivo y notas de una cita | Como médico, deseo editar la fecha, motivo y notas de una cita existente, para actualizar la agenda conservando su identidad | 3 |
| 22 | US-TB-22 | Eliminar una cita registrada | Como médico, deseo eliminar una cita de la agenda mediante la acción disponible, para retirar ese registro | 3 |
| 23 | US-TB-23 | Registrar una atención clínica y sus adjuntos | Como médico, deseo registrar una atención con sus notas y archivos, con o sin cita previa, para documentar la atención del paciente | 8 |
| 24 | US-TB-24 | Consultar el historial y editar una atención | Como médico, deseo revisar el historial del paciente y corregir las notas de una atención, para recuperar y actualizar su información clínica | 5 |
| 25 | US-TB-25 | Configurar las preferencias de la interfaz web | Como médico, deseo configurar idioma, tema, tamaño de texto y preferencia de notificaciones, para adaptar el uso de MAX en el navegador | 5 |
| 26 | US-TB-26 | Conocer la propuesta y las funcionalidades de MAX | Como visitante, deseo consultar la presentación, funcionalidades, misión, visión y valores de MAX, para conocer la propuesta del proyecto | 3 |
| 27 | US-TB-27 | Navegar por las secciones de la landing | Como visitante, deseo utilizar la navegación de la landing, para acceder a sus secciones informativas | 2 |
| 28 | US-TB-28 | Ingresar a la aplicación desde la landing | Como visitante, deseo acceder al inicio de sesión desde las llamadas a la acción de la landing, para comenzar a utilizar MAX | 2 |
| 29 | TS-TB-01 | Proteger las credenciales y la sesión web | Como desarrollador, deseo almacenar hashes bcrypt y gestionar sesiones web con JWT y cookies protegidas, para controlar el acceso a MAX | 8 |
| 30 | TS-TB-02 | Aplicar protección CSRF y configuración CORS | Como desarrollador, deseo aplicar la protección CSRF y la política de orígenes configurada, para controlar las solicitudes web a la API | 5 |
| 31 | TS-TB-03 | Limitar intentos de acceso y registro | Como desarrollador, deseo aplicar el limitador de intentos por cuenta e IP, para restringir solicitudes repetidas de autenticación | 3 |
| 32 | TS-TB-04 | Aplicar permisos, aislamiento y control de versiones | Como desarrollador, deseo filtrar por propietario, restringir la administración y comprobar versiones, para proteger los registros de MAX | 5 |
| 33 | TS-TB-05 | Procesar las operaciones clínicas compuestas con idempotencia | Como desarrollador, deseo procesar el alta con historial y la atención mediante una clave idempotente, para controlar la repetición de esas operaciones | 5 |
| 34 | TS-TB-06 | Validar y gestionar los archivos clínicos | Como desarrollador, deseo validar los archivos y gestionar sus URLs de acceso y limpieza, para mantener los adjuntos asociados a los estudios autorizados | 8 |
| 35 | TS-TB-07 | Persistir las preferencias visuales y de notificaciones localmente | Como desarrollador, deseo conservar tema, tamaño de texto y preferencia de notificaciones en el navegador, para recuperarlos al iniciar MAX | 2 |

#### Dependencias para la ejecución

La siguiente matriz resume las dependencias funcionales de las capacidades existentes. Identifica los controles y registros necesarios para utilizarlas o comprobarlas; no presenta su implementación como trabajo todavía pendiente.

| Elemento | Prerrequisitos | Motivo |
|---|---|---|
| US-TB-01 y US-TB-02 | TS-TB-01, TS-TB-02 y TS-TB-03 | Aplicar credenciales, sesión, protección web y limitación de intentos |
| US-TB-03 a US-TB-06 | Sesión válida; TS-TB-01 y TS-TB-04 | Cerrar sesión, gestionar el perfil y consultar el contexto clínico permitido |
| US-TB-07 a US-TB-09 | Rol ADMIN y TS-TB-04; TS-TB-06 para limpieza de archivos | Consultar y administrar perfiles con sus permisos y alcance de baja |
| US-TB-10 | Sesión válida, TS-TB-04 y TS-TB-05 | Crear el paciente y su historial mediante la operación compuesta |
| US-TB-11 a US-TB-14 | Paciente del propietario; TS-TB-04; TS-TB-06 para archivos asociados | Consultar, editar con versión y eliminar solo registros del espacio autorizado |
| US-TB-15 a US-TB-18 | Paciente autorizado, TS-TB-04 y TS-TB-06; consulta compatible cuando se vincula | Relacionar el documento, validar su carga y resolver acceso y limpieza |
| US-TB-19 a US-TB-22 | Paciente autorizado; TS-TB-04 en actualización y resolución del registro | Consultar, programar, editar y eliminar citas existentes |
| US-TB-23 | Paciente autorizado, TS-TB-05 y TS-TB-06; cita compatible si se selecciona | Guardar la atención y completar adjuntos respetando el resultado parcial |
| US-TB-24 | Historial del paciente y TS-TB-04 | Consultar atenciones y comprobar la versión de una edición |
| US-TB-25 | Sesión web válida y TS-TB-07 para las preferencias locales persistidas | Aplicar idioma y preferencias sin presumir sincronización con el backend |
| US-TB-26 a US-TB-28 | Landing académica publicada; frontend disponible para completar el acceso | Consultar información pública, navegar e ingresar a la web |
| TS-TB-01 a TS-TB-03 | Configuración de seguridad de la aplicación | Proteger sesión, solicitudes web y frecuencia de acceso |
| TS-TB-04 y TS-TB-05 | Identidad autenticada; repositorios y transacción del backend | Separar propietarios y controlar versiones y repetición de operaciones compuestas |
| TS-TB-06 | Registros autorizados; almacenamiento configurado para los objetos en nube | Validar archivos, emitir acceso y procesar la limpieza diferida |
| TS-TB-07 | Almacenamiento local del navegador disponible | Persistir tema, tamaño de texto y preferencia de notificaciones |

#### Trazabilidad y estimación consolidada

Las historias describen el producto actual que sirve como referencia para experimentar. Su existencia no acredita que estén listas las variantes B, el tracking o las sesiones con participantes.

| Experimento | Capacidades existentes de referencia | Alcance de la relación |
|---|---|---|
| EXP-01, ERQ-01 y H-01 | US-TB-11, US-TB-12, US-TB-16 y US-TB-17; TS-TB-04 y TS-TB-06 | Búsqueda del paciente y localización y consulta del estudio en web; no demuestra la mejora de la variante B |
| EXP-02, ERQ-02 y H-02 | US-TB-19, US-TB-20 y US-TB-21; TS-TB-04 | Consulta, programación y edición de citas existentes; no acredita bloqueo automático de cruces ni el recorrido guiado propuesto |
| EXP-03, ERQ-03 y H-03 | US-TB-25 y TS-TB-07 como referencia funcional de preferencias web | La configuración web no acredita la intervención ni la evaluación en Android; se mantiene el alcance móvil definido en 8.1 y 8.2 |
| Resto del catálogo | Acceso, administración, pacientes, atenciones, landing y soporte técnico | Cobertura del producto implementado; no se asigna a estas historias una hipótesis experimental nueva |

| Tipo | Cantidad | Story Points de referencia |
|---|---|---|
| Historias funcionales | 28 | 104 |
| Historias técnicas | 7 | 36 |
| Total | 35 | 140 |

Cada historia se contabiliza una sola vez. Las épicas y los controles compartidos no añaden puntos por cada función que utilizan. Estos puntos tampoco cubren reclutamiento, instrumentos de medición ni resultados de los experimentos.

#### Criterios de preparación y terminación

Para comprobar una historia se identifica su versión de respaldo, se utiliza un entorno autorizado con datos sintéticos y se recorren sus criterios positivos y las restricciones descritas. La existencia de código permite documentar una capacidad implementada; una nueva comprobación funcional requiere registrar por separado el entorno, los pasos y el resultado observado.

El catálogo conserva los límites encontrados: la agenda web permite crear, editar y eliminar citas, pero no se acredita aquí un bloqueo automático de solapamientos; eliminar una cita es una baja del registro, no un cambio demostrado a estado CANCELADA. La eliminación de pacientes alcanza sus registros asociados. Las preferencias de tema, texto y notificaciones se guardan localmente; el cambio de idioma web utiliza el catálogo de traducción, y no se afirma sincronización remota de preferencias ni envío de recordatorios clínicos.

La landing dispone de contenido y enlaces al producto. Sus enlaces legales de marcador y el bloque Contacto no se convierten en historias de políticas publicadas, formularios enviados o mensajes entregados. La tarjeta de Configuración con versión y el literal Operativo tampoco se presenta como un diagnóstico en tiempo real.

La preparación y ejecución de EXP-01 a EXP-03 conserva las condiciones de 8.1 y 8.2. Se documentarán las variantes, instrumentos, consentimiento, sesiones y resultados cuando existan. El catálogo y el backlog de funciones implementadas no acreditan esas actividades ni los beneficios planteados en las hipótesis.

Esta tabla es el registro documental del backlog. La publicación del tablero en una herramienta de gestión, su enlace y captura requieren evidencia real; no se incorpora una URL ficticia ni se atribuye a este cambio una publicación que no se ha realizado.

## Conclusiones

A continuación, se presentan las conclusiones y recomendaciones derivadas del trabajo realizado durante el desarrollo de **MAX**. Estas consideran los principales resultados obtenidos durante el **AV1**, que comprendió el desarrollo de los capítulos relacionados con la definición de la startup y solución, el levantamiento y análisis de requerimientos, la especificación de requisitos, el diseño del producto y los avances correspondientes a la implementación de la solución.

El trabajo realizado permitió evolucionar desde la identificación inicial del problema y de los segmentos objetivo hacia la definición de una solución digital compuesta por una Landing Page, una aplicación web, una aplicación móvil, un Backend y una base de datos. Asimismo, permitió establecer una base metodológica y técnica para continuar con las etapas posteriores de validación, DevOps y experimentación del producto.

- El desarrollo del **Startup Profile de MAX** permitió establecer la identidad inicial de la propuesta mediante la definición de su misión, visión, valores y objetivos, orientando el producto hacia la mejora de la interacción entre médicos cirujanos y pacientes.

- La definición del **Solution Profile** permitió delimitar el problema que busca abordar MAX y establecer una propuesta de solución basada en la centralización de citas y documentación relacionada con la atención médica.

- Se definieron claramente los dos segmentos objetivo principales de MAX: **médicos cirujanos y pacientes**. Esta separación permitió analizar necesidades diferentes para cada tipo de usuario y posteriormente diseñar funcionalidades específicas para cada uno.

- La investigación realizada sobre el contexto de la información médica digital permitió sustentar la relevancia de contar con soluciones tecnológicas que faciliten la organización y disponibilidad de información relacionada con la atención de los pacientes.

- La aplicación de **Lean UX** permitió organizar los principales supuestos del producto mediante Problem Statements, Assumptions, Hypothesis Statements y Lean UX Canvas, estableciendo una base para validar posteriormente las decisiones tomadas durante el desarrollo.

- Las hipótesis planteadas permitieron orientar MAX hacia aspectos concretos como la centralización de citas y documentos, recordatorios, acceso a recetas e informes, intercambio de documentación y facilidad de uso de la plataforma.

- El proceso de **Requirements Elicitation & Analysis** permitió obtener información directamente de representantes de los segmentos objetivo mediante entrevistas a pacientes y profesionales médicos.

- Las entrevistas realizadas permitieron identificar situaciones relevantes para el diseño de MAX, como dificultades para recordar citas, información distribuida entre diferentes medios, almacenamiento de recetas y estudios, necesidad de consultar información previa y preocupación por la privacidad y el acceso a la información.

- La etapa de **Needfinding**, mediante User Personas, User Task Matrix, User Journey Mapping, Empathy Mapping y As-Is Scenario Mapping, permitió transformar los resultados obtenidos en las entrevistas en representaciones concretas de las necesidades, tareas y problemas de los usuarios.

- La elaboración del **Ubiquitous Language** permitió establecer un vocabulario común para conceptos relevantes dentro de MAX, facilitando que términos relacionados con pacientes, médicos, citas, consultas, estudios y documentación sean utilizados de manera consistente dentro del proyecto.

- El análisis competitivo permitió evaluar soluciones existentes y comprender qué características podían servir como referencia para MAX, identificando oportunidades para diferenciar el producto mediante una experiencia enfocada específicamente en la interacción entre médicos cirujanos y pacientes.

- La elaboración del **To-Be Scenario Mapping** permitió representar cómo podría mejorar la experiencia de los usuarios mediante MAX, trasladando los problemas identificados durante el escenario actual hacia una experiencia futura soportada por la plataforma.

- La especificación de requerimientos permitió transformar las necesidades identificadas durante la investigación en **Epics, User Stories y Technical Stories**, estableciendo una relación entre las necesidades del usuario y las funcionalidades que posteriormente serían implementadas.

- El **Product Backlog de MAX** permitió organizar y priorizar el desarrollo del producto mediante un total de **35 historias y 107 Story Points**, distribuidos entre funcionalidades relacionadas con identidad y acceso, pacientes, estudios, consultas, agenda clínica y configuración de preferencias.

- La Primera Entrega del Product Backlog permitió concentrar el desarrollo en las funcionalidades fundamentales del producto, incluyendo autenticación y seguridad, gestión integral de pacientes y almacenamiento de estudios médicos adjuntos.

- La Segunda Entrega permitió extender el alcance previsto hacia funcionalidades relacionadas con agenda médica, atención clínica y configuración de preferencias del sistema, proporcionando una ruta progresiva para la evolución del producto.

- La definición de las interfaces y experiencia de usuario permitió establecer una representación visual coherente de MAX para sus diferentes plataformas, considerando las necesidades particulares de los médicos cirujanos y pacientes.

- La implementación de la **Landing Page** permitió disponer de un punto público de presentación de MAX, comunicando su propósito, funcionalidades, valores y propuesta de valor.

- La implementación del **Frontend Web** permitió materializar las principales interfaces destinadas a la gestión de información dentro de MAX, incluyendo autenticación, Dashboard, pacientes y estudios médicos.

- El desarrollo de la **aplicación móvil** permitió avanzar hacia una experiencia adaptada a dispositivos móviles, complementando la solución web y considerando las necesidades de acceso de los usuarios desde este tipo de dispositivos.

- La implementación del **Backend** permitió establecer los servicios necesarios para soportar las funcionalidades de la plataforma y gestionar la comunicación entre las aplicaciones cliente y la información persistida por MAX.

- La utilización de una base de datos **MySQL** permitió establecer la persistencia de información relacionada con usuarios, pacientes, citas, consultas, estudios y configuraciones de la aplicación.

- El despliegue del Backend y la base de datos mediante **Railway**, del Frontend Web mediante **Cloudflare Pages** y de la Landing Page mediante **GitHub Pages** permitió contar con entornos accesibles para comprobar progresivamente la integración y funcionamiento de los componentes desarrollados.

- El uso de **GitHub** como plataforma de gestión del código fuente permitió mantener separados los principales componentes del producto y conservar trazabilidad sobre los cambios realizados durante el desarrollo.

- La organización del trabajo mediante **Sprints, Product Backlog y la matriz Leadership and Collaboration Matrix (LACX)** permitió distribuir responsabilidades entre los integrantes y mantener una estructura de colaboración durante la implementación.

- El Sprint 1 permitió trabajar sobre las **20 User Stories y Technical Stories de la Primera Entrega**, correspondientes a un total de **62 Story Points**, estableciendo una primera base funcional de MAX.

- La documentación de evidencias de desarrollo, ejecución, servicios y deployment permitió mantener trazabilidad entre los requerimientos definidos, el código implementado y el funcionamiento observable de los diferentes componentes de MAX.

- En conjunto, el trabajo realizado hasta el AV1 permitió que MAX avance desde una propuesta inicial hacia una solución con requerimientos definidos, diseño, backlog priorizado y componentes de software implementados, estableciendo una base para continuar posteriormente con las actividades de verificación, validación, DevOps y Experiment-Driven Development.

### Recomendaciones

- Continuar validando las **Hypothesis Statements de Lean UX** mediante experimentos con usuarios reales, evitando considerar una hipótesis como validada únicamente porque una funcionalidad haya sido diseñada o implementada.

- Ampliar progresivamente la cantidad de **médicos cirujanos y pacientes entrevistados**, buscando participantes con diferentes edades, especialidades, niveles de experiencia y frecuencia de uso de servicios médicos para reducir posibles sesgos en los resultados.

- Mantener una trazabilidad clara entre los resultados de las entrevistas, User Personas, Scenario Maps, Epics, User Stories, criterios de aceptación y funcionalidades implementadas.

- Actualizar el **Product Backlog** conforme aparezcan nuevos hallazgos durante las entrevistas, pruebas de usabilidad y futuras actividades de experimentación, evitando mantener historias que hayan perdido relevancia para los usuarios.

- Mantener el **Ubiquitous Language** como un elemento vivo del proyecto y actualizarlo cuando aparezcan nuevos conceptos relevantes durante el desarrollo o la investigación con usuarios.

- Refinar las User Stories antes de cada Sprint, asegurando que sus criterios de aceptación sean suficientemente específicos para permitir comprobar objetivamente cuándo una funcionalidad puede considerarse terminada.

- Incorporar progresivamente criterios de aceptación en formato **Given/When/Then**, facilitando posteriormente la implementación de pruebas BDD y la trazabilidad entre requerimientos y pruebas.

- Realizar pruebas de usabilidad adicionales sobre los flujos principales de MAX, especialmente en autenticación, gestión de pacientes, citas, acceso a documentación y consulta de estudios médicos.

- Mantener consistencia visual y funcional entre la **aplicación web y la aplicación móvil**, utilizando los Style Guidelines definidos durante el diseño del producto como referencia para futuras funcionalidades.

- Priorizar la **seguridad y privacidad de la información** durante todas las futuras iteraciones, debido a la naturaleza de los datos gestionados por MAX.

- Fortalecer los mecanismos de autenticación, autorización y control de acceso, asegurando que cada usuario pueda acceder únicamente a la información y funcionalidades correspondientes a su rol.

- Evitar almacenar credenciales, secretos, tokens o configuraciones sensibles directamente en los repositorios de GitHub, utilizando variables de entorno y mecanismos seguros de configuración para los diferentes entornos.

- Implementar y ampliar las **pruebas unitarias, de integración y de sistema** para los principales flujos de MAX, especialmente aquellos relacionados con autenticación, pacientes, citas, consultas y estudios.

- Incorporar pruebas automatizadas dentro del flujo de integración del proyecto para detectar errores antes de integrar nuevos cambios a las ramas principales.

- Fortalecer el proceso de **Continuous Integration**, incorporando validaciones automáticas de compilación, pruebas y calidad de código para los diferentes componentes del producto.

- Mantener entornos diferenciados de desarrollo, pruebas y producción para reducir el riesgo de que cambios todavía no validados afecten las versiones utilizadas durante las demostraciones o validaciones con usuarios.

- Fortalecer el proceso de **Continuous Deployment** utilizado con Cloudflare Pages, Railway y GitHub Pages, documentando claramente las variables de entorno y configuraciones necesarias para reproducir cada deployment.

- Implementar mecanismos de **Continuous Monitoring** sobre el Backend y los servicios desplegados, considerando métricas como disponibilidad, tiempo de respuesta y errores producidos por la API.

- Definir mecanismos de respaldo y recuperación para la base de datos MySQL, considerando la importancia de mantener disponible la información gestionada por la plataforma.

- Mantener una documentación actualizada de la **RESTful API**, de manera que los responsables del Frontend Web y de la aplicación móvil puedan conocer los endpoints, parámetros, estructuras de solicitud y respuestas disponibles.

- Mantener sincronización frecuente entre los responsables del Frontend, Mobile y Backend para evitar diferencias entre las interfaces desarrolladas y los servicios realmente disponibles en la API.

- Utilizar Pull Requests y revisiones entre integrantes antes de integrar cambios importantes, reduciendo la posibilidad de introducir errores y mejorando el conocimiento compartido del código.

- Mantener commits pequeños y descriptivos siguiendo **Conventional Commits**, así como una estrategia consistente de ramas basada en GitFlow para conservar la trazabilidad del desarrollo.

- Continuar utilizando la matriz **LACX** para distribuir liderazgo y colaboración, pero revisar los responsables en cada Sprint de acuerdo con las funcionalidades que deban desarrollarse.

- Para las siguientes etapas del proyecto, diseñar experimentos que permitan comprobar las hipótesis más importantes de MAX con **médicos cirujanos y pacientes reales**, definiendo previamente qué se desea aprender y qué evidencia permitirá tomar una decisión.

- Establecer para cada experimento una hipótesis falsable, su correspondiente hipótesis nula, métricas, condiciones de control y experimentación y criterios objetivos para decidir si una funcionalidad debe **perseverar, iterar o descartarse**.

- Instrumentar métricas relacionadas con los principales objetivos del producto antes de ejecutar los experimentos, evitando depender exclusivamente de opiniones cualitativas de los participantes.

- Realizar las futuras **To-Be Validation Interviews** utilizando las funcionalidades realmente implementadas para determinar si los cambios propuestos solucionan los problemas identificados durante la etapa inicial de investigación.

- Utilizar los resultados de las futuras validaciones y experimentos para repriorizar el Question Backlog y Product Backlog, de manera que las siguientes decisiones de MAX estén respaldadas por evidencia y no únicamente por supuestos del equipo.

- Mantener sesiones de **shareback** al finalizar los ciclos de experimentación para que todos los integrantes comprendan los resultados obtenidos, las decisiones tomadas y los cambios que deberán incorporarse al producto.

- Continuar evolucionando MAX de manera iterativa, priorizando primero aquellas funcionalidades que demuestren aportar mayor valor a médicos cirujanos y pacientes antes de ampliar el alcance del producto con características adicionales.
  
### Video About-the-Team

---

## Bibliografía

Huapaya-Huertas, O., Palomino-Rojas, J., Calle-Texeira, C., Alvarez-Huiman, G., Montesinos-Segura, R., & Taype-Rondan, A. (2021). Experiencia del Complejo Hospitalario San Pablo (Perú) en la implementación de un sistema de historias clínicas electrónicas. *Anales de la Facultad de Medicina, 82*(4), 349–354.  

https://doi.org/10.15381/anales.v82i4.22211

Rojas-Mezarina, L., Cedamanos-Medina, C. A., & Vargas-Herrera, J. (2015). Registro nacional de historias clínicas electrónicas en Perú. *Revista Peruana de Medicina Experimental y Salud Pública, 32*(2), 395–396.  

https://doi.org/10.17843/rpmesp.2015.322.1639

GitHub. (2026). *GitHub Documentation*.  

https://docs.github.com/

Cloudflare. (2026). *Cloudflare Pages Documentation*.  

https://developers.cloudflare.com/pages/

Railway. (2026). *Railway Documentation*.  

https://docs.railway.com/

MySQL. (2026). *MySQL Documentation*.  

https://dev.mysql.com/doc/

Git. (2026). *Git Documentation*.  

https://git-scm.com/doc


---

## Anexos
### Anexo A. Videos de Exposiciones
*(Incluir de forma progresiva el título e hipervínculo al video de Exposición en Microsoft Stream para cada entrega AV1, TB1, AV2, TB2).*
