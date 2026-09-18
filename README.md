
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
#### 5.1.3. Source Code Style Guide & Conventions
#### 5.1.4. Software Deployment Configuration
### 5.2. Product implementation & deployment
#### 5.2.1. Sprint 1
##### 5.2.1.1. Sprint Planning 1
##### 5.2.1.2. Aspect Leaders and Collaborators
##### 5.2.1.3. Sprint Backlog 1
##### 5.2.1.4. Development Evidence for Sprint Review
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
