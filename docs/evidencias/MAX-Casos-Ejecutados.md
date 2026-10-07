# Casos originales ejecutados: MAX

Fecha: 07/10/2026, America/Lima. Los IDs UT/IT/BDD son identificadores de evidencia local; las historias US/TS provienen del informe cuando se indican. No son métricas de cobertura.

## IAM / Android

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-IAM-Android-01 | iam_test.dart | IAM rechaza correo inválido y exige correo al registrarse | IAM rechaza correo inválido y exige correo al registrarse | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Android-02 | iam_test.dart | IAM credenciales inválidas no crean identidad autenticada | IAM credenciales inválidas no crean identidad autenticada | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Android-03 | iam_test.dart | IAM login y logout limpian datos e identidad | IAM login y logout limpian datos e identidad | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Android-04 | iam_test.dart | IAM contraseña actual incorrecta conserva la sesión | IAM contraseña actual incorrecta conserva la sesión | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Android-05 | validators_test.dart | seguridad de contraseña exige longitud, mayúscula, número y signo | seguridad de contraseña exige longitud, mayúscula, número y signo | Aserciones verificadas en el reporte original | Aprobada |

## IAM / Backend

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-IAM-Backend-01 | AuthServiceUnitTest | duplicateRegistrationDoesNotHashOrSave | Correo duplicado: conflicto; no calcular hash ni guardar. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-02 | AuthServiceUnitTest | wrongCurrentPasswordDoesNotRevokeSessions | Contraseña actual incorrecta: rechazo sin revocar sesiones. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-03 | AuthServiceUnitTest | rejectsUnknownAccountWithoutIssuingSession | Cuenta desconocida: 401 y ninguna sesión nueva. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-04 | AuthServiceUnitTest | loginNormalizesEmailAndPreservesIdentityAndCreatedAt | Correo normalizado; conservar ID y createdAt al acceder. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-05 | AuthServiceUnitTest | rejectsWrongPasswordWithoutChangingUserOrSession | Contraseña incorrecta: 401 sin modificar usuario ni sesión. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-06 | AvatarValidatorUnitTest | rejectsInvalidBase64UnsupportedTypeAndOversize | Rechazar avatar inválido, tipo no permitido y exceso de 5 MiB. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-07 | AvatarValidatorUnitTest | acceptsPngSignatureAndRejectsMimeMismatch | Aceptar PNG válido y rechazar MIME incompatible con contenido. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-08 | AvatarValidatorUnitTest | historicalUnchangedValueIsPreserved | Conservar la referencia histórica de avatar sin alteración. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-09 | AvatarValidatorUnitTest | emptyValueRemovesAvatar | Valor vacío elimina la referencia del avatar. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-10 | PasswordPolicyTest | acceptsTheCompletePolicy | Aceptar más de ocho caracteres, mayúscula, número y signo. | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Backend-11 | PasswordPolicyTest | rejectsEveryMissingRequirement | Rechazar cada requisito faltante de contraseña. | Aserciones verificadas en el reporte original | Aprobada |

## IAM / Web

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-IAM-Web-01 | app/core/validation/password.validation.spec.ts | accepts a password with more than eight characters, uppercase, number and sign | accepts a password with more than eight characters, uppercase, number and sign | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Web-02 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: clave#123 | rejects a password that does not satisfy the full policy: clave#123 | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Web-03 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: Clave#abc | rejects a password that does not satisfy the full policy: Clave#abc | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Web-04 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: Clave1234 | rejects a password that does not satisfy the full policy: Clave1234 | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Web-05 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: Cla#1234 | rejects a password that does not satisfy the full policy: Cla#1234 | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Web-06 | app/core/validation/password.validation.spec.ts | rejects a password that does not satisfy the full policy: Clave #123 | rejects a password that does not satisfy the full policy: Clave #123 | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Web-07 | app/core/validation/password.validation.spec.ts | detects different confirmation values | detects different confirmation values | Aserciones verificadas en el reporte original | Aprobada |
| UT-IAM-Web-08 | app/contexts/usuarios/application/auth-store.spec.ts | elimina credenciales antiguas sin borrar preferencias ajenas a la sesión | elimina credenciales antiguas sin borrar preferencias ajenas a la sesión | Aserciones verificadas en el reporte original | Aprobada |

## Patients / Android

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Patients-Android-01 | models_test.dart | paciente conserva contrato JSON del backend | paciente conserva contrato JSON del backend | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Android-02 | patients_test.dart | Patients nombres y DNI se normalizan sin cambiar identidad o versión | Patients nombres y DNI se normalizan sin cambiar identidad o versión | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Android-03 | patients_test.dart | Patients registro inexistente y listado vacío mantienen estado vacío | Patients registro inexistente y listado vacío mantienen estado vacío | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Android-04 | patients_test.dart | Patients un fallo de persistencia no agrega pacientes ficticios | Patients un fallo de persistencia no agrega pacientes ficticios | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Android-05 | patients_test.dart | Patients bloquea doble envío mientras la operación está pendiente | Patients bloquea doble envío mientras la operación está pendiente | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Android-06 | patients_test.dart | Patients descarta pacientes recibidos después del logout | Patients descarta pacientes recibidos después del logout | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Android-07 | validators_test.dart | validaciones de paciente DNI acepta exactamente ocho dígitos | validaciones de paciente DNI acepta exactamente ocho dígitos | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Android-08 | validators_test.dart | validaciones de paciente nombres no aceptan números ni signos arbitrarios | validaciones de paciente nombres no aceptan números ni signos arbitrarios | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Android-09 | validators_test.dart | validaciones de paciente teléfono acepta entre siete y quince dígitos | validaciones de paciente teléfono acepta entre siete y quince dígitos | Aserciones verificadas en el reporte original | Aprobada |

## Patients / Backend

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Patients-Backend-01 | PacienteServiceUnitTest | missingRecordCannotBeUpdated | ID inexistente: rechazar actualización sin guardar. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Backend-02 | PacienteServiceUnitTest | validatesRequiredNamesDniEmailAndPhone | Validar nombres obligatorios y formatos DNI, correo y teléfono. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Backend-03 | PacienteServiceUnitTest | invalidBirthDateIsRejectedBeforeSave | Rechazar fecha inválida/futura antes de guardar. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Backend-04 | PacienteServiceUnitTest | emptyCollectionIsAnEmptyResult | Listado vacío devuelve una colección vacía. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Backend-05 | PacienteServiceUnitTest | staleVersionCannotOverwrite | Versión antigua: conflicto; no sobrescribir datos. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Backend-06 | PacienteServiceUnitTest | updateKeepsPathIdentityAndAuthenticatedOwner | Conservar ID de la ruta y propietario autenticado. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Backend-07 | PacienteServiceUnitTest | creationUsesAuthenticatedOwnerAndNormalizesOptionalFields | Asignar propietario autenticado y normalizar campos opcionales. | Aserciones verificadas en el reporte original | Aprobada |

## Patients / Web

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Patients-Web-01 | app/core/state/clinical-data.service.spec.ts | reutiliza la carga pendiente y evita llamadas duplicadas | reutiliza la carga pendiente y evita llamadas duplicadas | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-02 | app/core/state/clinical-data.service.spec.ts | descarta la respuesta de la sesión anterior después de reset | descarta la respuesta de la sesión anterior después de reset | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-03 | app/core/state/clinical-data.service.spec.ts | expone fallo de pacientes y permite que otros módulos terminen | expone fallo de pacientes y permite que otros módulos terminen | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-04 | app/core/validation/search-input.validation.spec.ts | allows only letters and spaces in name searches | allows only letters and spaces in name searches | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-05 | app/core/validation/search-input.validation.spec.ts | allows at most eight digits in DNI searches | allows at most eight digits in DNI searches | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-06 | app/core/validation/search-input.validation.spec.ts | allows letters, digits and spaces in combined searches | allows letters, digits and spaces in combined searches | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-07 | app/contexts/pacientes/application/pacientes.store.spec.ts | expone estados explícitos y elimina los datos al cambiar de sesión | expone estados explícitos y elimina los datos al cambiar de sesión | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-08 | app/contexts/pacientes/application/patient-input.validation.spec.ts | keeps only letters and spaces in names | keeps only letters and spaces in names | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-09 | app/contexts/pacientes/application/patient-input.validation.spec.ts | keeps only the allowed amount of digits | keeps only the allowed amount of digits | Aserciones verificadas en el reporte original | Aprobada |
| UT-Patients-Web-10 | app/contexts/pacientes/application/patient-input.validation.spec.ts | accepts only real, non-future birth dates within 120 years | accepts only real, non-future birth dates within 120 years | Aserciones verificadas en el reporte original | Aprobada |

## Studies / Android

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Studies-Android-01 | studies_test.dart | Studies conserva relaciones y metadatos del contrato JSON | Studies conserva relaciones y metadatos del contrato JSON | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Android-02 | studies_test.dart | Studies identifica imágenes y PDF histórico por extensión | Studies identifica imágenes y PDF histórico por extensión | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Android-03 | studies_test.dart | Studies informa archivos fallidos y reintenta sin duplicar atención | Studies informa archivos fallidos y reintenta sin duplicar atención | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Android-04 | study_transport_test.dart | multipart conserva el día y el contrato de fecha/hora: 2026-10-07 | multipart conserva el día y el contrato de fecha/hora: 2026-10-07 | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Android-05 | study_transport_test.dart | multipart conserva el día y el contrato de fecha/hora: 2026-10-07T16:45:00 | multipart conserva el día y el contrato de fecha/hora: 2026-10-07T16:45:00 | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Android-06 | study_viewer_test.dart | la imagen histórica embebida usa bytes y conserva el visor | la imagen histórica embebida usa bytes y conserva el visor | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Android-07 | study_viewer_test.dart | referencia embebida no imagen muestra un error accionable | referencia embebida no imagen muestra un error accionable | Aserciones verificadas en el reporte original | Aprobada |

## Studies / Backend

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Studies-Backend-01 | EstudioServiceUnitTest | rejectsOversizeBeforeReadingContent | Rechazar más de 20 MiB antes de leer el contenido. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Backend-02 | EstudioServiceUnitTest | nonexistentOrForeignPatientNeverUploads | Paciente ajeno/inexistente: no ejecutar carga del objeto. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Backend-03 | EstudioServiceUnitTest | acceptsExactly20MiBAndGeneratesServerOwnedKey | Aceptar exactamente 20 MiB; generar clave desde servidor. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Backend-04 | EstudioServiceUnitTest | createCannotAdoptAnArbitraryObjectKey | Rechazar claves arbitrarias al crear un estudio. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Backend-05 | EstudioServiceUnitTest | rejectsUnsupportedExtensionAndForgedContent | Rechazar extensión no admitida y firma de contenido inválida. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Backend-06 | EstudioServiceUnitTest | storageFailureDoesNotSaveStudyMetadata | Fallo de almacenamiento: no guardar metadatos ficticios. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Backend-07 | EstudioServiceUnitTest | localStoragePreservesBytesAndMetadata | Conservar bytes, paciente y metadatos en modo embebido. | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Backend-08 | EstudioServiceUnitTest | unauthorizedAccessNeverSignsOrDeletesAnObject | Acceso ajeno: no firmar ni eliminar objetos. | Aserciones verificadas en el reporte original | Aprobada |

## Studies / Web

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Studies-Web-01 | app/contexts/estudios/application/estudios.store.spec.ts | conserva el error y los datos sin simular un guardado | conserva el error y los datos sin simular un guardado | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Web-02 | app/contexts/estudios/application/estudios.store.spec.ts | revoca URLs temporales y vacía datos al cerrar sesión | revoca URLs temporales y vacía datos al cerrar sesión | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Web-03 | app/contexts/estudios/application/estudios.store.spec.ts | elimina únicamente los estudios del paciente seleccionado | elimina únicamente los estudios del paciente seleccionado | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Web-04 | app/contexts/estudios/infrastructure/estudios.api-client.spec.ts | envía un multipart asociado al paciente sin inventar consulta | envía un multipart asociado al paciente sin inventar consulta | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Web-05 | app/contexts/estudios/infrastructure/estudios.api-client.spec.ts | propaga un fallo HTTP sin devolver un estudio ficticio | propaga un fallo HTTP sin devolver un estudio ficticio | Aserciones verificadas en el reporte original | Aprobada |
| UT-Studies-Web-06 | app/contexts/estudios/infrastructure/estudios.api-client.spec.ts | solicita una URL vigente al abrir un estudio | solicita una URL vigente al abrir un estudio | Aserciones verificadas en el reporte original | Aprobada |

## Integración JUnit: API y BD

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| IT-IAM-01 | AuthIntegrationTest | changingPasswordRejectsAWeakNewPasswordAndKeepsTheSessionOpen | Nueva contraseña débil: 400; sesión actual sigue válida. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Studies-01 | AuthIntegrationTest | dataAndFileAccessAreIsolatedPerProfile | A no puede listar, editar, firmar ni borrar datos/archivos de B. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-01 | AuthIntegrationTest | stalePatientVersionReturnsConflictWithoutOverwritingData | Versión desactualizada: 409; conservar actualización previa. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-02 | AuthIntegrationTest | deletingAppointmentKeepsConsultationAndClearsItsLink | Eliminar cita conserva consulta y desvincula citaId. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-02 | AuthIntegrationTest | registerUsesProtectedCookieAndAccessesAuthenticatedEndpoint | Registro 201, cookie HttpOnly, JSON sin JWT; /me 200. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-03 | AuthIntegrationTest | logoutRevokesServerSession | Logout 204; identidad posterior 401. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-04 | AuthIntegrationTest | registrationRejectsPasswordWithoutEveryRequiredElement | Registro con contraseña débil devuelve 400. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-03 | AuthIntegrationTest | patientInitialHistoryIsAtomicAndIdempotent | Un paciente, una cita y una consulta; repetir clave no duplica. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-04 | AuthIntegrationTest | deletingPacienteCascadesToClinicalData | Eliminar paciente elimina sus registros clínicos asociados. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-05 | AuthIntegrationTest | patientRegistrationRejectsInvalidFieldFormats | Campos inválidos devuelven 400. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-05 | AuthIntegrationTest | loginRateLimitAppliesPerAccountWithoutPermanentLock | Cinco fallos por cuenta producen limitación temporal, sin bloqueo permanente. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-06 | AuthIntegrationTest | rejectsAvatarWhenDeclaredMimeDoesNotMatchItsContent | MIME de avatar falseado devuelve error de validación. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-07 | AuthIntegrationTest | wrongCurrentPasswordKeepsTheSessionOpen | Contraseña actual incorrecta: 422; identidad sigue accesible. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-08 | AuthIntegrationTest | csrfIsRequiredForEveryMutation | Registro sin cabecera CSRF devuelve 403. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-06 | AuthIntegrationTest | attentionCreatesLinkedAppointmentAndUpdatesLastConsultation | Guardar atención crea cita realizada y actualiza ultimaConsulta. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-09 | AuthIntegrationTest | changingPasswordRevokesOlderSessionsAndKeepsCurrentOneOpen | Cambiar contraseña invalida sesiones anteriores y conserva la actual. | Aserciones verificadas en el reporte original | Aprobada |
| IT-X-17 | MaxBackendApplicationTests | contextLoads | Contexto Spring inicia con configuración de pruebas. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-10 | MySqlWorkflowIntegrationTest | changingPasswordRejectsAWeakNewPasswordAndKeepsTheSessionOpen | Nueva contraseña débil: 400; sesión actual sigue válida. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Studies-02 | MySqlWorkflowIntegrationTest | dataAndFileAccessAreIsolatedPerProfile | A no puede listar, editar, firmar ni borrar datos/archivos de B. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-07 | MySqlWorkflowIntegrationTest | stalePatientVersionReturnsConflictWithoutOverwritingData | Versión desactualizada: 409; conservar actualización previa. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-08 | MySqlWorkflowIntegrationTest | deletingAppointmentKeepsConsultationAndClearsItsLink | Eliminar cita conserva consulta y desvincula citaId. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-11 | MySqlWorkflowIntegrationTest | registerUsesProtectedCookieAndAccessesAuthenticatedEndpoint | Registro 201, cookie HttpOnly, JSON sin JWT; /me 200. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-12 | MySqlWorkflowIntegrationTest | logoutRevokesServerSession | Logout 204; identidad posterior 401. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-13 | MySqlWorkflowIntegrationTest | registrationRejectsPasswordWithoutEveryRequiredElement | Registro con contraseña débil devuelve 400. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-09 | MySqlWorkflowIntegrationTest | patientInitialHistoryIsAtomicAndIdempotent | Un paciente, una cita y una consulta; repetir clave no duplica. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-10 | MySqlWorkflowIntegrationTest | deletingPacienteCascadesToClinicalData | Eliminar paciente elimina sus registros clínicos asociados. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-11 | MySqlWorkflowIntegrationTest | patientRegistrationRejectsInvalidFieldFormats | Campos inválidos devuelven 400. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-14 | MySqlWorkflowIntegrationTest | loginRateLimitAppliesPerAccountWithoutPermanentLock | Cinco fallos por cuenta producen limitación temporal, sin bloqueo permanente. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-15 | MySqlWorkflowIntegrationTest | rejectsAvatarWhenDeclaredMimeDoesNotMatchItsContent | MIME de avatar falseado devuelve error de validación. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-16 | MySqlWorkflowIntegrationTest | wrongCurrentPasswordKeepsTheSessionOpen | Contraseña actual incorrecta: 422; identidad sigue accesible. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-17 | MySqlWorkflowIntegrationTest | csrfIsRequiredForEveryMutation | Registro sin cabecera CSRF devuelve 403. | Aserciones verificadas en el reporte original | Aprobada |
| IT-Patients-12 | MySqlWorkflowIntegrationTest | attentionCreatesLinkedAppointmentAndUpdatesLastConsultation | Guardar atención crea cita realizada y actualiza ultimaConsulta. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-18 | MySqlWorkflowIntegrationTest | changingPasswordRevokesOlderSessionsAndKeepsCurrentOneOpen | Cambiar contraseña invalida sesiones anteriores y conserva la actual. | Aserciones verificadas en el reporte original | Aprobada |
| IT-IAM-19 | MySqlWorkflowIntegrationTest | registeredPasswordIsPersistedAsBcryptInsteadOfPlaintext | MySQL guarda bcrypt; coincide con clave válida y rechaza clave incorrecta. | Aserciones verificadas en el reporte original | Aprobada |
| IT-X-35 | MySqlMigrationIntegrationTest | newInstallationRunsElevenMigrationsAndAddsConstraints | Instalar V1–V11, restricciones e índices; segunda migración no altera versión. | Aserciones verificadas en el reporte original | Aprobada |
| IT-X-36 | MySqlMigrationIntegrationTest | approvedLegacyAdoptionPreservesSyntheticRecordsAndWidensTinytext | Adopción explícita conserva filas sintéticas y amplía archivo_url a LONGTEXT. | Aserciones verificadas en el reporte original | Aprobada |
| IT-X-37 | MySqlMigrationIntegrationTest | inconsistentLegacyOwnerStopsBeforeBaseline | Propietario histórico nulo bloquea adopción antes del baseline. | Aserciones verificadas en el reporte original | Aprobada |

## BDD HTTP real

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| BDD-IAM-01 | Cucumber | Credenciales válidas permiten consultar la identidad | Credenciales válidas permiten consultar la identidad | Aserciones verificadas en el reporte original | Aprobada |
| BDD-IAM-02 | Cucumber | Credenciales incorrectas son rechazadas | Credenciales incorrectas son rechazadas | Aserciones verificadas en el reporte original | Aprobada |
| BDD-IAM-03 | Cucumber | Login sin CSRF es rechazado | Login sin CSRF es rechazado | Aserciones verificadas en el reporte original | Aprobada |
| BDD-Patients-01 | Cucumber | Registrar y consultar un paciente | Registrar y consultar un paciente | Aserciones verificadas en el reporte original | Aprobada |
| BDD-Patients-02 | Cucumber | Editar mantiene identidad y datos actualizados | Editar mantiene identidad y datos actualizados | Aserciones verificadas en el reporte original | Aprobada |
| BDD-Patients-03 | Cucumber | Otra cuenta no puede modificar mi paciente | Otra cuenta no puede modificar mi paciente | Aserciones verificadas en el reporte original | Aprobada |
| BDD-Studies-01 | Cucumber | Adjuntar y recuperar un PDF permitido | Adjuntar y recuperar un PDF permitido | Aserciones verificadas en el reporte original | Aprobada |
| BDD-Studies-02 | Cucumber | Rechazar extensión no admitida | Rechazar extensión no admitida | Aserciones verificadas en el reporte original | Aprobada |
| BDD-Studies-03 | Cucumber | Rechazar paciente inexistente | Rechazar paciente inexistente | Aserciones verificadas en el reporte original | Aprobada |

## Unidad Android administrativa adicional

| ID | Unidad | Caso | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| UT-Admin-01 | models_test.dart | perfil administrativo usa id como userId compatible | perfil administrativo usa id como userId compatible | Aserciones verificadas en el reporte original | Aprobada |
