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

**Estado:** esta sección especifica el trabajo por realizar. Las variantes, la instrumentación y las sesiones con participantes todavía no están implementadas ni ejecutadas para estos experimentos. Las historias y el backlog no constituyen evidencia de beneficios obtenidos, despliegues, reclutamiento o mediciones. Tampoco se sustituyen por las pruebas de disponibilidad del capítulo VII.

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

Las historias To-Be expresan el incremento necesario para las tres intervenciones y su medición. Los identificadores `US-TB`, `TS-TB` y `SP-TB` distinguen historias funcionales, técnicas y spikes de las historias del capítulo III. Las épicas EP-03, EP-04 y EP-05 conservan sus nombres y alcance de referencia; no se renumeran las épicas ni se reemplazan las historias As-Is.

El cuadro central identifica las épicas y las historias. La prioridad numérica coincide con el orden por valor del backlog de 8.3.2; los criterios completos se desarrollan en el texto enlazado, en presente y con estructura Dado–Cuando–Entonces. Las épicas agrupan historias y no reciben puntos adicionales que dupliquen la estimación de sus componentes.

| Story ID | User | Priority | Epic | Title | Description | Acceptance Criteria |
|---|---|---|---|---|---|---|
| EP-03 | Médico | — | EP-03 | Gestión de Placas y Estudios | Agrupa la localización y consulta contextual de estudios de EXP-01 | Historias US-TB-01 y US-TB-02 |
| US-TB-01 | Médico | 1 | EP-03 | Localizar estudios por paciente | Como médico, deseo localizar los estudios del paciente consultado conservando su contexto, para reducir la carga de búsqueda | [CA-01.1 a CA-01.3](#us-tb-01-localizar-estudios-por-paciente) |
| US-TB-02 | Médico | 2 | EP-03 | Consultar el estudio correcto | Como médico, deseo comprobar la correspondencia de un estudio y consultar su archivo, para utilizar la documentación del paciente adecuado | [CA-02.1 a CA-02.3](#us-tb-02-consultar-el-estudio-correcto) |
| EP-04 | Médico | — | EP-04 | Gestión de Consultas y Agenda Clínica | Agrupa las mejoras de programación y reprogramación de EXP-02 | Historias US-TB-03 y US-TB-04 |
| US-TB-03 | Médico | 3 | EP-04 | Programar una cita con un recorrido guiado | Como médico, deseo programar una cita con disponibilidad y datos revisados antes de confirmarla, para completar correctamente la gestión de agenda | [CA-03.1 a CA-03.3](#us-tb-03-programar-una-cita-con-un-recorrido-guiado) |
| US-TB-04 | Médico | 4 | EP-04 | Reprogramar una cita conservando su integridad | Como médico, deseo cambiar el horario de una cita conservando su identidad y sus restricciones, para reorganizar la agenda sin duplicaciones ni cambios incorrectos | [CA-04.1 a CA-04.3](#us-tb-04-reprogramar-una-cita-conservando-su-integridad) |
| EP-05 | Médico | — | EP-05 | Configuración y Preferencias del Sistema | Agrupa la legibilidad de EXP-03 y el apoyo a la valoración de experiencia | Historias US-TB-05 y US-TB-06 |
| US-TB-05 | Médico | 5 | EP-05 | Configurar la legibilidad en Android | Como médico, deseo configurar y previsualizar los ajustes permitidos de legibilidad, para realizar las tareas móviles con una configuración adecuada | [CA-05.1 a CA-05.3](#us-tb-05-configurar-la-legibilidad-en-android) |
| US-TB-06 | Médico participante | 6 | EP-05 | Valorar la facilidad del recorrido | Como médico participante, deseo valorar opcionalmente la facilidad de cada recorrido, para aportar información sobre mi experiencia con la variante evaluada | [CA-06.1 a CA-06.3](#us-tb-06-valorar-la-facilidad-del-recorrido) |
| TS-TB-01 | Developer | 7 | Transversal: EP-03, EP-04 y EP-05 | Preparar condiciones y casos aislados | Como desarrollador, deseo preparar asignaciones y casos sintéticos versionados y aislados, para comparar A y B bajo condiciones equivalentes | [CA-T01.1 a CA-T01.3](#ts-tb-01-preparar-condiciones-y-casos-aislados) |
| TS-TB-02 | Developer | 8 | Transversal: EP-03, EP-04 y EP-05 | Registrar eventos experimentales | Como desarrollador, deseo registrar los eventos mínimos del protocolo con validación y deduplicación, para obtener mediciones trazables sin información clínica real | [CA-T02.1 a CA-T02.3](#ts-tb-02-registrar-eventos-experimentales) |
| TS-TB-03 | Developer | 9 | Transversal: EP-03, EP-04 y EP-05 | Generar registros e indicadores reproducibles | Como desarrollador, deseo transformar los registros válidos en pares e indicadores del catálogo, para preparar un análisis reproducible con pérdidas explícitas | [CA-T03.1 a CA-T03.3](#ts-tb-03-generar-registros-e-indicadores-reproducibles) |
| SP-TB-01 | Developer | 10 | Transversal: EP-03, EP-04 y EP-05 | Verificar contratos y viabilidad de las variantes | Como desarrollador, deseo investigar los contratos y capacidades existentes de los tres recorridos, para identificar restricciones y preparar las variantes sin cambios de arquitectura no evaluados | [CA-S01.1 a CA-S01.3](#sp-tb-01-verificar-contratos-y-viabilidad-de-las-variantes) |
| SP-TB-02 | Developer | 11 | Transversal: EP-03, EP-04 y EP-05 | Calibrar instrumentos de captura y tiempo | Como desarrollador, deseo investigar la medición de duración y captura mínima en web y Android, para elegir instrumentos adecuados antes de integrar el tracking | [CA-S02.1 a CA-S02.3](#sp-tb-02-calibrar-instrumentos-de-captura-y-tiempo) |

#### US-TB-01. Localizar estudios por paciente

**Relación As-Is:** US-08, US-09 y US-13. **Trazabilidad:** ERQ-01 → EXP-01 → H-01; M-01, M-02 y M-05. Su valor consiste en mantener el contexto de búsqueda; no se presenta la búsqueda básica existente como una funcionalidad nueva.

- **CA-01.1, caso favorable:** **Dado** que el médico tiene una sesión autorizada y un caso sintético asignado, **cuando** localiza los estudios del paciente de ese caso, **entonces** el resultado corresponde a ese paciente e incluye la información de contexto prevista en la rúbrica para identificar el estudio solicitado.
- **CA-01.2, restricción:** **Dado** que un documento no está dentro del ámbito autorizado del médico, **cuando** se solicita su localización, **entonces** el sistema conserva la restricción de acceso y no entrega ese documento ni sus metadatos protegidos.
- **CA-01.3, ausencia de coincidencias:** **Dado** que el conjunto asignado no contiene un estudio coincidente, **cuando** se realiza la búsqueda, **entonces** se comunica la ausencia de resultado y no se selecciona ni se asocia automáticamente un estudio de otro paciente.

#### US-TB-02. Consultar el estudio correcto

**Relación As-Is:** US-14 y US-15. **Trazabilidad:** ERQ-01 → EXP-01 → H-01; M-01, M-02 y M-05. La historia completa el recorrido focalizado con una correspondencia verificable entre paciente, estudio y archivo.

- **CA-02.1, caso favorable:** **Dado** que existe un estudio autorizado en el contexto del paciente consultado, **cuando** el médico solicita su consulta, **entonces** se recupera el archivo asociado a ese estudio y se conserva la información necesaria para verificar su correspondencia con el caso.
- **CA-02.2, archivo no disponible:** **Dado** que el archivo no está disponible o su recuperación falla, **cuando** se solicita consultarlo, **entonces** se informa el fallo y no se sustituye el contenido por otro archivo ni se declara completada la consulta.
- **CA-02.3, cambio de contexto:** **Dado** que una solicitud sigue pendiente y el contexto autorizado cambia, **cuando** llega su respuesta, **entonces** un archivo ajeno al contexto vigente no se presenta como el estudio solicitado actualmente.

#### US-TB-03. Programar una cita con un recorrido guiado

**Relación As-Is:** US-16 y US-17. **Trazabilidad:** ERQ-02 → EXP-02 → H-02; M-03, M-04 y M-05. El tratamiento modifica el recorrido, conservando las restricciones de agenda de la condición de referencia.

- **CA-03.1, caso favorable:** **Dado** que el médico está autorizado, el paciente sintético corresponde al caso y el horario está disponible, **cuando** se revisan los datos y se confirma la programación, **entonces** queda una única cita con el paciente, fecha y horario solicitados y con confirmación del servicio correspondiente.
- **CA-03.2, horario ocupado:** **Dado** que el horario solicitado está ocupado, **cuando** se intenta confirmar la cita, **entonces** se rechaza esa programación sin modificar la cita existente ni aceptar un cruce de horario.
- **CA-03.3, corrección previa:** **Dado** que los datos todavía no se han confirmado, **cuando** el médico los corrige o cancela la operación, **entonces** la validación se realiza sobre los datos definitivos y no se crea una cita por una operación cancelada.

#### US-TB-04. Reprogramar una cita conservando su integridad

**Relación As-Is:** complementa US-16 y US-17; conserva la separación con la cancelación de US-18. **Trazabilidad:** ERQ-02 → EXP-02 → H-02; M-03, M-04 y M-05. La viabilidad del contrato actual se resuelve en SP-TB-01 antes de implementar esta historia.

- **CA-04.1, caso favorable:** **Dado** que existe una cita sintética autorizada y un nuevo horario permitido, **cuando** el médico confirma su reprogramación, **entonces** la misma cita queda asociada al horario solicitado sin generar una segunda cita activa para representar el cambio.
- **CA-04.2, cambio inválido:** **Dado** que la nueva fecha u hora no cumple las restricciones, **cuando** se solicita reprogramar, **entonces** se rechaza el cambio y se conserva el estado válido anterior de la cita.
- **CA-04.3, respuesta no confirmada:** **Dado** que se interrumpe la respuesta de una reprogramación, **cuando** el resultado aún no está confirmado, **entonces** el sistema no afirma éxito ni repite automáticamente una operación que pueda duplicar el cambio; primero verifica el estado de la cita mediante las capacidades disponibles del servicio.

#### US-TB-05. Configurar la legibilidad en Android

**Relación As-Is:** US-24 y US-25. **Trazabilidad:** ERQ-03 → EXP-03 → H-03; M-06, M-07 y M-05. La historia facilita configurar y comprobar ajustes existentes; no atribuye un beneficio de salud visual a la variante.

- **CA-05.1, caso favorable:** **Dado** que el médico parte de una configuración segura y tiene disponibles los ajustes permitidos, **cuando** configura y previsualiza su elección, **entonces** los ajustes se reflejan coherentemente en el contenido de prueba y las funciones requeridas por las tareas permanecen disponibles.
- **CA-05.2, ajuste no permitido:** **Dado** que se recibe un valor fuera de las opciones admitidas para el caso, **cuando** se intenta aplicarlo, **entonces** se rechaza el valor y se conserva una configuración válida.
- **CA-05.3, restauración y accesibilidad:** **Dado** que se necesita iniciar otra condición del estudio, **cuando** se restablece la configuración de referencia acordada, **entonces** permanecen disponibles las ayudas habituales del participante y no se mantienen ajustes experimentales de la condición anterior que alteren la comparación.

#### US-TB-06. Valorar la facilidad del recorrido

**Relación As-Is:** apoyo a la evaluación de experiencia asociada con las preferencias de EP-05; no sustituye historias clínicas. **Trazabilidad:** EXP-01, EXP-02 y EXP-03; M-09. La valoración es opcional y separada de la ejecución cronometrada.

- **CA-06.1, respuesta válida:** **Dado** que finaliza una condición y el participante acepta responder, **cuando** comunica una puntuación entera de 1 a 7, **entonces** se registra la respuesta con su código seudónimo, experimento y variante, sin datos clínicos.
- **CA-06.2, respuesta inválida:** **Dado** que una respuesta no pertenece a la escala admitida, **cuando** se valida, **entonces** no se acepta como puntuación válida ni se transforma silenciosamente en otro valor.
- **CA-06.3, respuesta omitida o retiro:** **Dado** que el participante decide no valorar o retirar su participación, **cuando** comunica esa decisión, **entonces** no se le exige una puntuación ni se registra cero como si fuera una respuesta; los datos se tratan según el consentimiento aplicable.

#### TS-TB-01. Preparar condiciones y casos aislados

**Trazabilidad:** los tres experimentos; esquema de asignación y M-10. Habilita las comparaciones sin introducir un rol de paciente ni alterar datos de producción.

- **CA-T01.1, asignación válida:** **Dado** que existe un protocolo y un caso versionados, **cuando** se prepara una asignación para el participante seudónimo, **entonces** el registro identifica experimento, plataforma, secuencia AB/BA, variantes y conjuntos de casos reproducibles conforme al balance previsto.
- **CA-T01.2, entorno no autorizado:** **Dado** que un destino no corresponde al entorno experimental autorizado, **cuando** se solicita preparar sus casos, **entonces** se rechaza la operación y no se escriben datos en ese destino.
- **CA-T01.3, aislamiento entre condiciones:** **Dado** que una condición modifica un caso de agenda o ajustes de prueba, **cuando** se prepara la siguiente condición, **entonces** esta parte de su estado aislado equivalente y no de las modificaciones dejadas por otro bloque o participante.

#### TS-TB-02. Registrar eventos experimentales

**Trazabilidad:** catálogo de eventos de 8.2.8, M-01 a M-10 y los tres experimentos. Integra la captura con los recorridos una vez disponibles; no presupone un endpoint de analítica ya publicado. El contrato de `ease_answered` puede verificarse con registros sintéticos en esta historia; la interacción para obtener una respuesta del médico se incorpora después mediante US-TB-06.

- **CA-T02.1, registro válido:** **Dado** que existe consentimiento aplicable y se emite un evento permitido de un caso sintético, **cuando** se valida y acepta, **entonces** queda un registro con los campos requeridos, su identificador, variante y versión, y se confirma su aceptación sin incorporar información clínica real.
- **CA-T02.2, registro inválido:** **Dado** que el evento carece de campos obligatorios, tiene una duración incoherente o incluye información prohibida por 8.2.8, **cuando** se procesa, **entonces** se rechaza como registro válido y se conserva una causa de validación sin almacenar el contenido sensible rechazado.
- **CA-T02.3, duplicación o ausencia de final:** **Dado** que un identificador se recibe de nuevo o falta el cierre de un bloque, **cuando** se valida el conjunto, **entonces** el duplicado no incrementa los conteos y el bloque incompleto no se declara exitoso por ausencia de un resultado contrario.

#### TS-TB-03. Generar registros e indicadores reproducibles

**Trazabilidad:** M-01 a M-10 y preparación de la evaluación de 8.2.7. No realiza anticipadamente el análisis de resultados reales ni añade métricas no definidas.

- **CA-T03.1, transformación reproducible:** **Dado** un conjunto sintético versionado con pares completos, fallos de tarea y respuestas opcionales, **cuando** se aplica la transformación documentada, **entonces** se obtienen los indicadores del catálogo con sus unidades, numeradores y denominadores, y el mismo conjunto produce el mismo resultado.
- **CA-T03.2, pérdidas y tiempos penalizados:** **Dado** que hay una tarea fallida medible y otro bloque con captura incompleta, **cuando** se preparan los datos, **entonces** el primero conserva el tiempo penalizado de su tarjeta y el segundo se informa como pérdida, sin convertir ninguno en tiempo cero o éxito.
- **CA-T03.3, exportación y protección:** **Dado** que se solicita un conjunto para análisis, **cuando** se genera la salida estructurada, **entonces** se conserva la trazabilidad necesaria del estudio y la salida agregada no publica identidades, contenido clínico ni registros excluidos contra el consentimiento.

#### SP-TB-01. Verificar contratos y viabilidad de las variantes

**Objetivo de investigación:** determinar cómo reutilizar las funciones actuales de búsqueda, consulta, agenda y preferencias para preparar A y B. El spike no genera por sí solo una funcionalidad terminada.

- **CA-S01.1, revisión documentada:** **Dado** que se dispone de las fuentes y contratos existentes, **cuando** se revisa la viabilidad de cada recorrido, **entonces** se documentan capacidades, restricciones de autorización y alternativas compatibles con el alcance de los tres experimentos.
- **CA-S01.2, incertidumbre de reprogramación:** **Dado** que no se ha acreditado el contrato necesario para conservar una cita al cambiarla, **cuando** se estudian sus solicitudes, respuestas y fallos, **entonces** se registra una conclusión respaldada por un ejemplo controlado o un bloqueo explícito; no se inventa una operación existente ni se ejecuta un cambio clínico real.
- **CA-S01.3, cambio fuera de alcance:** **Dado** que la solución requiere un endpoint, esquema o cambio de arquitectura adicional, **cuando** se identifica esa necesidad, **entonces** se presenta su justificación, impacto y propuesta para revisión antes de implementar; no se declara resuelta mediante una modificación no evaluada.

#### SP-TB-02. Calibrar instrumentos de captura y tiempo

**Objetivo de investigación:** comprobar un mecanismo viable para medir duración y capturar los campos mínimos en web y Android antes de implementar TS-TB-02. Es una comprobación técnica; no sustituye al piloto con médicos.

- **CA-S02.1, prueba mínima:** **Dado** un escenario técnico sintético en cada plataforma, **cuando** se registra una secuencia de inicio y final, **entonces** se documenta una duración obtenida con reloj monotónico y su correspondencia con el esquema previsto.
- **CA-S02.2, interrupciones:** **Dado** que se provoca una pausa, reinicio o pérdida de un evento dentro del escenario técnico, **cuando** se examina la captura, **entonces** se identifica la limitación y el tratamiento del dato faltante sin fabricar una duración.
- **CA-S02.3, conclusión del spike:** **Dado** que finaliza la comprobación acotada, **cuando** se revisan sus resultados, **entonces** quedan documentados el mecanismo recomendado, la evidencia de la prueba, las limitaciones y los ajustes necesarios para TS-TB-02; su conclusión no se presenta como confirmación de las hipótesis de usuario.

### 8.3.2. To-Be Product Backlog

El backlog ordena el trabajo To-Be según el valor que aporta a las preguntas priorizadas: primero la consulta de estudios, luego la gestión de citas y la legibilidad, y después el apoyo a su medición. El orden expresa prioridad de valor, no una secuencia que permita ignorar dependencias. Un elemento bloqueado no se inicia por aparecer antes en la tabla.

Las estimaciones usan Story Points de la escala 1, 2, 3, 5 y 8. Son estimaciones iniciales relativas a alcance, incertidumbre y complejidad; deben revisarse después de los spikes. No equivalen a horas, días, número de participantes ni resultados de experimentos. Todos los elementos tienen estado **propuesto, pendiente de implementación o investigación**, según su tipo.

| Orden | User Story ID | Título | Descripción | Story Points |
|---|---|---|---|---|
| 1 | US-TB-01 | Localizar estudios por paciente | Como médico, deseo localizar los estudios del paciente consultado conservando su contexto, para reducir la carga de búsqueda | 5 |
| 2 | US-TB-02 | Consultar el estudio correcto | Como médico, deseo comprobar la correspondencia de un estudio y consultar su archivo, para utilizar la documentación del paciente adecuado | 3 |
| 3 | US-TB-03 | Programar una cita con un recorrido guiado | Como médico, deseo programar una cita con disponibilidad y datos revisados antes de confirmarla, para completar correctamente la gestión de agenda | 5 |
| 4 | US-TB-04 | Reprogramar una cita conservando su integridad | Como médico, deseo cambiar el horario de una cita conservando su identidad y sus restricciones, para reorganizar la agenda sin duplicaciones ni cambios incorrectos | 5 |
| 5 | US-TB-05 | Configurar la legibilidad en Android | Como médico, deseo configurar y previsualizar los ajustes permitidos de legibilidad, para realizar las tareas móviles con una configuración adecuada | 5 |
| 6 | US-TB-06 | Valorar la facilidad del recorrido | Como médico participante, deseo valorar opcionalmente la facilidad de cada recorrido, para aportar información sobre mi experiencia con la variante evaluada | 2 |
| 7 | TS-TB-01 | Preparar condiciones y casos aislados | Como desarrollador, deseo preparar asignaciones y casos sintéticos versionados y aislados, para comparar A y B bajo condiciones equivalentes | 5 |
| 8 | TS-TB-02 | Registrar eventos experimentales | Como desarrollador, deseo registrar los eventos mínimos del protocolo con validación y deduplicación, para obtener mediciones trazables sin información clínica real | 8 |
| 9 | TS-TB-03 | Generar registros e indicadores reproducibles | Como desarrollador, deseo transformar los registros válidos en pares e indicadores del catálogo, para preparar un análisis reproducible con pérdidas explícitas | 3 |
| 10 | SP-TB-01 | Verificar contratos y viabilidad de las variantes | Como desarrollador, deseo investigar los contratos y capacidades existentes de los tres recorridos, para identificar restricciones y preparar las variantes sin cambios de arquitectura no evaluados | 2 |
| 11 | SP-TB-02 | Calibrar instrumentos de captura y tiempo | Como desarrollador, deseo investigar la medición de duración y captura mínima en web y Android, para elegir instrumentos adecuados antes de integrar el tracking | 2 |

#### Dependencias para la ejecución

| Elemento | Prerrequisitos | Motivo |
|---|---|---|
| SP-TB-01 | Ninguno dentro de este backlog | Resolver viabilidad antes de comprometer la implementación |
| SP-TB-02 | SP-TB-01 | Calibrar instrumentos en el contexto técnico identificado |
| TS-TB-01 | SP-TB-01 | Preparar casos y condiciones compatibles con los contratos revisados |
| US-TB-01 | TS-TB-01 | Disponer de casos y condiciones aisladas para la búsqueda |
| US-TB-02 | US-TB-01 | Completar el recorrido focalizado de consulta |
| US-TB-03 | TS-TB-01 | Programar contra casos de agenda controlados |
| US-TB-04 | US-TB-03 | Completar la batería de agenda con reprogramación verificable |
| US-TB-05 | TS-TB-01 | Mantener casos y configuración de referencia entre condiciones |
| TS-TB-02 | SP-TB-02, TS-TB-01, US-TB-02, US-TB-04 y US-TB-05 | Integrar y verificar la captura en los tres recorridos completos |
| US-TB-06 | TS-TB-02 | Asociar la respuesta opcional con la condición correcta |
| TS-TB-03 | TS-TB-02 | Transformar datos de captura validados y representar respuestas opcionales, incluidas ausencias |

La secuencia técnica empieza por los spikes y la preparación, aunque el backlog muestre primero el valor funcional. Es posible preparar una historia con casos controlados sin declarar que todo el experimento está listo; la preparación del piloto exige además instrumentación, calidad de datos y protocolo aprobado.

#### Trazabilidad y estimación consolidada

| Experimento | Historias funcionales | Habilitadores compartidos | Métricas de referencia |
|---|---|---|---|
| EXP-01, ERQ-01 y H-01 | US-TB-01, US-TB-02; US-TB-06 para valoración | TS-TB-01 a TS-TB-03; SP-TB-01 y SP-TB-02 | M-01, M-02, M-05, M-08, M-09 y M-10 |
| EXP-02, ERQ-02 y H-02 | US-TB-03, US-TB-04; US-TB-06 para valoración | TS-TB-01 a TS-TB-03; SP-TB-01 y SP-TB-02 | M-03, M-04, M-05, M-08, M-09 y M-10 |
| EXP-03, ERQ-03 y H-03 | US-TB-05; US-TB-06 para valoración | TS-TB-01 a TS-TB-03; SP-TB-01 y SP-TB-02 | M-06, M-07, M-05, M-08, M-09 y M-10 |

| Tipo | Cantidad | Story Points propuestos |
|---|---|---|
| Historias funcionales | 6 | 25 |
| Historias técnicas | 3 | 16 |
| Spikes | 2 | 4 |
| Total | 11 | 45 |

Los habilitadores se contabilizan una sola vez, aunque apoyen a los tres experimentos. No se suman nuevamente por experimento ni por épica. El reclutamiento, la disponibilidad de médicos, las sesiones y el calendario de confirmación de 8.2.5 son recursos y actividades del estudio; no se consideran cubiertos por estos 45 Story Points de trabajo sobre producto e instrumentos.

#### Criterios de preparación y terminación

Una historia queda lista para iniciar cuando su alcance y criterios son entendidos, sus dependencias están resueltas, existe un caso sintético verificable y se ha identificado el entorno autorizado. Los spikes se acotan a producir evidencia y una conclusión; no se cierran únicamente por haber dedicado tiempo a investigar.

Una historia funcional o técnica se acepta cuando cumple sus criterios, conserva las reglas existentes, dispone de comprobaciones positivas y negativas, identifica la versión evaluada y deja evidencia reproducible con datos sintéticos. La cobertura de captura se valida al integrar TS-TB-02. Aceptar una historia no demuestra que se haya alcanzado el ahorro de tiempo, la tasa de acierto o una hipótesis del experimento.

Antes del piloto deben estar disponibles las variantes requeridas, los casos equivalentes, la rúbrica, la asignación y los instrumentos. Las pruebas técnicas y los datos controlados permiten comprobar preparación; los resultados con médicos se registran solo después de ejecutar las sesiones bajo las condiciones de 8.2. Para declarar éxito experimental se aplicarán sus reglas de calidad, escala y análisis.

Esta tabla es el registro documental del backlog To-Be. La publicación en la herramienta de gestión indicada por el curso, su enlace público y la captura correspondiente quedan pendientes de su registro real; no se incorpora una URL o captura ficticia como evidencia de gestión. Tampoco se incluyen aquí implementaciones o evidencias de 8.3.3, que quedan fuera del alcance de esta sección.
