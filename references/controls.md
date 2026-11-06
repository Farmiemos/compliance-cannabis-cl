# Catálogo de controles + crosswalk

Cada **control** es una unidad reutilizable de cumplimiento. Un mismo control satisface
requisitos de **varios marcos a la vez** → se evalúa una vez y se propaga. Esta es la pieza
que hace genérico al motor: para agregar un marco nuevo, se le suman columnas a esta tabla
(o el pack referencia los `id` de control que exige).

> Estado por control: ✅ cumple · ⚠️ parcial · ❌ falta · ❓ no verificable por código.
> `evidencia`: `archivo:línea` o "declarado por el usuario". Anota remediación si no es ✅.

## Crosswalk (control → marcos)

| id | Control | 21.719 (Datos) | 21.595 (MPD) | Futuro (ISO 27001 / SOC 2 / GDPR) | Fuente de evidencia |
|----|---------|----------------|--------------|-----------------------------------|---------------------|
| `gov-responsable` | Responsable/oficial designado | DPO si aplica | Oficial de cumplimiento | ISO A.5.3 / SOC2 CC1 | usuario |
| `gov-registro` | Registro/inventario formal | RAT | Matriz de riesgos de delitos | ISO A.5.9 | usuario + código |
| `gov-politicas` | Políticas documentadas | Política de privacidad | Código de ética | ISO A.5.1 | docs generados |
| `gov-capacitacion` | Capacitación al personal | buena práctica | Capacitación (obligatoria) | ISO A.6.3 | usuario |
| `gov-auditoria` | Auditoría/revisión periódica | parte del MPI | Auditoría del modelo | ISO 9.2 / SOC2 CC4 | usuario |
| `gov-disciplinario` | Régimen disciplinario interno | parte del MPI | Sí (sanciones internas) | ISO A.6.4 | usuario |
| `gov-denuncias` | Canal de reporte/denuncias | canal de contacto/derechos | Canal anónimo de denuncias | ISO A.5.x / GDPR Art.38 | código + usuario |
| `data-licitud` | Base de licitud / consentimiento opt-in | Sí | — | GDPR Art.6 | código (formularios) |
| `data-derechos` | Derechos del titular (ARCO+portabilidad+bloqueo) | Sí (30 días) | — | GDPR Art.15-22 | código (endpoints) |
| `data-info` | Deber de información / aviso de privacidad | Sí | — | GDPR Art.13 | código + docs |
| `data-minimizacion` | Minimización y retención | Sí | — | GDPR Art.5 | código |
| `data-dpa` | Contratos con encargados (DPA) | Sí | control de terceros | GDPR Art.28 | docs + usuario |
| `data-transfer` | Transferencias internacionales con mecanismo | Sí | — | GDPR Cap.V | código (.env/proveedores) |
| `data-consent-text` | Texto de consentimiento opt-in + revocación | Sí (Art. 12/16) | — | GDPR Art.7 | docs + código |
| `data-rights-channel` | Canal/formulario para ejercer derechos | Sí (Art. 14 ter) | — | GDPR Art.12 | docs + código |
| `data-eipd` | Evaluación de Impacto (alto riesgo) | Sí (Art. 15 ter) | — | GDPR Art.35 | docs + usuario |
| `data-privacy-by-design` | Privacidad desde el diseño y por defecto | Sí (Art. 14 quáter) | — | ISO A.8.x / GDPR Art.25 | código |
| `data-pseudonym` | Seudonimización de datos | Sí (Art. 14 quinquies) | — | GDPR Art.32 | código |
| `sec-tls` | Cifrado en tránsito (TLS/HTTPS) | Sí | control interno TI | ISO A.8.24 / SOC2 CC6 | código/infra |
| `sec-rest` | Cifrado en reposo (datos sensibles/credenciales) | Sí | — | ISO A.8.24 / SOC2 CC6 | código/infra |
| `sec-passwords` | Hashing fuerte de contraseñas (bcrypt/argon2) | Sí | — | ISO A.8.5 | código |
| `sec-mfa` | MFA en accesos administrativos | Sí | control de acceso | ISO A.8.5 / SOC2 CC6.1 | código/infra/usuario |
| `sec-logs` | Logs de acceso y auditoría | Sí | control interno | ISO A.8.15 / SOC2 CC7 | código |
| `sec-tenant` | Segregación por tenant/cliente | Sí | — | SOC2 CC6 | código (`organizationId`) |
| `sec-secrets` | Secretos fuera del código | Sí | control interno | ISO A.8.24 | código (.env/secret mgr) |
| `sec-backups` | Backups y borrado/retención | Sí | — | ISO A.8.13 | infra/usuario |
| `inc-brechas` | Gestión de incidentes + notificación de brechas | Sí (sin dilaciones indebidas, Art. 14 sexies) | — | GDPR Art.33 / SOC2 CC7 | docs + usuario |
| `ctrl-interno` | Control interno: segregación de funciones / autorizaciones | — | Sí | ISO A.5.x / SOC2 CC | usuario + código |
| `sec-monitoring` | Monitoreo y alertas (audit log, secretos, errores) | detección de brechas | detección delitos informáticos | SOC2 CC7 | infra + usuario |

## Controles del pack `sanitario-cannabis`

Citas textuales y archivo de caché en `packs/sanitario-cannabis/pack.md`. La columna "21.719" indica cuando el
mismo control también cuenta para datos personales (se evalúa una vez).

| id | Control | Norma sanitaria | 21.719 | Cómo se verifica en el código |
|----|---------|-----------------|--------|-------------------------------|
| `san-receta-requisitos` | La receta registrada exige emisor médico cirujano, diagnóstico, tratamiento, duración y forma de administración | Ley 20.000 Art. 8 inc. 2 | — | campos obligatorios en el esquema y en la validación; rechazo si falta alguno |
| `san-receta-vigencia` | No se entrega fuera del período del tratamiento | Ley 20.000 Art. 8 inc. 2 ("duración"); CS Art. 101 ("período de tiempo determinado") | — | la entrega consulta la fecha de término y bloquea; prueba con receta vencida |
| `san-receta-autenticidad` | La receta se verifica contra su emisor o sistema y se detecta la falsificación | Ley 20.000 Art. 8 inc. 2 (receta falsa); CS Art. 101 (elementos contra la falsificación) | — | integración con el sistema de validación, huella del documento, revisión humana registrada |
| `san-receta-reserva` | La receta y su contenido se tratan como dato sensible reservado | CS Art. 101 | `sec-rest`, `data-privacy-by-design` | cifrado en reposo, acceso por permiso, registro de lecturas |
| `san-destino-personal` | Cada entrega va al titular de la receta, dentro de su cantidad, sin traspaso a terceros | Ley 20.000 Arts. 4 y 50 | — | límites por persona y período; entrega solo al titular verificado; sin entrega a no socios |
| `san-trazabilidad` | Cadena cultivo → lote → entrega con balance de masa y destrucción registrada | Ley 20.000 Art. 10 (desvío); DS 867 Art. 14 (destrucción) | `sec-logs` | libro de movimientos inmutable; balance de gramos; registro de mermas y destrucción |
| `san-no-combustion` | El software no ofrece ni registra la combustión como forma de administración | Ley 20.000 Art. 8 inc. 2 | — | catálogo de vías de administración sin "fumada"; validación del campo |
| `san-publicidad` | Las superficies públicas no promueven el uso ni publicitan productos | CS Art. 100 inc. 2; Ley 20.000 Art. 3 | — | revisión de textos públicos, catálogos y sitios por organización `[criterio jurídico]` |
| `san-sag` | Autorización del SAG, avisos, guía de libre tránsito, cierre y destrucción (si aplica) | Ley 20.000 Art. 9; DS 867 Arts. 6-14 | — | registro de la resolución, fechas de aviso y guías; usuario |
| `san-farmaceutico` | Productos registrados en el ISP solo con receta retenida y control de existencia (si aplica) | DS 404 Art. 23; DS 405 Art. 23 (Decreto 84/2015) | — | tipo de receta y control de existencias por producto |

## Controles del pack `ley-20584`

Citas textuales en `packs/ley-20584/pack.md`. `pac-ficha-clasificacion` aplica siempre; el resto, solo si el
test del pack da Resultado A (el registro es una ficha clínica).

| id | Control | Norma | Reutiliza | Cómo se verifica en el código |
|----|---------|-------|-----------|-------------------------------|
| `pac-ficha-clasificacion` | El registro está clasificado (ficha clínica o no) y su nombre visible coincide con esa clasificación | Ley 20.584 Arts. 3 y 12; DS 41 Arts. 2 y 4 | — | buscar `ficha clínica\|historia clínica\|clinical.record` en textos visibles, PDFs y campos; contrastar con el resultado del test |
| `pac-ficha-contenido` | La ficha tiene el contenido mínimo y cada registro identifica y firma al profesional | DS 41 Arts. 6 y 7 | — | campos (a)-(d) en el esquema; autor y firma por entrada |
| `pac-ficha-integridad` | Los cambios no borran la versión anterior; respaldo y restauración probados | Ley 20.584 Art. 12 inc. 2; DS 41 Art. 8 | `sec-backups`, `sec-logs` | historial de versiones o registro inmutable; doble copia; prueba de restore |
| `pac-ficha-acceso` | Solo accede quien participa en la atención; cada acceso queda registrado | Ley 20.584 Art. 13 inc. 4; DS 41 Art. 9 | `sec-logs`, `sec-rest` | permiso por vínculo de atención, no solo por rol; log de lecturas con fecha y persona |
| `pac-ficha-entrega` | El titular obtiene copia íntegra, gratuita, en formato estructurado y portable | Ley 20.584 Art. 13 inc. final | `data-derechos` | exportación estructurada (JSON/FHIR o similar) disponible al titular |
| `pac-ficha-conservacion` | Conservación de al menos 15 años desde el último ingreso | Ley 20.584 Art. 13 inc. 1; DS 41 Art. 11 | `data-minimizacion` | la retención automática no borra fichas antes del plazo |
| `pac-ficha-eliminacion` | Eliminación con destrucción efectiva y acta protocolizada (privados) | DS 41 Art. 12 | — | procedimiento y registro del acta; usuario |
| `pac-consentimiento` | Consentimiento informado escrito en la ficha cuando el riesgo lo exige; en salud digital, con firma conforme a la Ley 19.799 | Ley 20.584 Art. 14 | — | registro de aceptación o rechazo con fecha, contenido informado y firma |
| `pac-reclamos` | Sistema de registro y respuesta escrita de reclamos (prestador institucional) | Ley 20.584 Art. 37 | `gov-denuncias` | canal, registro y respuesta; usuario |

## Controles del pack `ley-20500`

Citas textuales en `packs/ley-20500/pack.md`.

| id | Control | Norma | Reutiliza | Cómo se verifica en el código |
|----|---------|-------|-----------|-------------------------------|
| `osfl-estatutos` | Estatutos inscritos con fines, derechos y deberes de socios, incorporación y exclusión | CC Arts. 548 y 548-2; Ley 20.500 Arts. 5 y 8 | — | inscripción en el Registro Nacional; usuario |
| `osfl-registro-socios` | Registro de socios, directores y autoridades permanentemente actualizado | CC Art. 557-3 | `gov-registro` | altas, bajas y cambios de estado con fecha y autor; historial que no se borra |
| `osfl-afiliacion-libre` | El socio se retira cuando quiere, sin trabas | Ley 20.500 Art. 3 | `data-derechos` | acción de retiro disponible al socio; sin bloqueo por deuda ni plazo de permanencia |
| `osfl-cuentas-socios` | Todo socio accede al estado de cuentas, actividades y programas | Ley 20.500 Art. 4; CC Art. 551 | — | vista o informe de cuentas para socios |
| `osfl-actas` | Actas de directorio y asamblea en un registro que asegura su fidelidad | CC Art. 557-3 | `sec-logs` | actas versionadas o selladas (hash), sin edición posterior silenciosa |
| `osfl-sin-lucro` | Aportes fijados por la asamblea; excedentes solo a los fines, nunca repartidos | CC Arts. 556 y 557-2 | `ctrl-interno` | aportes ligados a un acuerdo de asamblea; sin pagos a socios fuera de gastos o remuneraciones informadas |
| `osfl-contabilidad` | Contabilidad, memoria y balance anual aprobados por la asamblea | CC Art. 557-1 | — | exportación contable; usuario |
| `osfl-directorio` | Directorio de al menos tres, sin condenados a pena aflictiva; remuneraciones informadas a la asamblea | CC Arts. 551 y 551-1 | `gov-responsable` | registro del directorio y de sus remuneraciones; usuario |

## Controles del pack `tributario`

Citas textuales en `packs/tributario/pack.md`.

| id | Control | Norma | Reutiliza | Cómo se verifica en el código |
|----|---------|-------|-----------|-------------------------------|
| `trib-conservacion` | Registros de aportes, compras y gastos conservados al menos seis años, aunque el titular pida suprimirlos | Código Tributario Arts. 17 y 200 | `data-minimizacion` | la retención y la supresión no borran respaldos tributarios antes del plazo |
| `trib-aporte-trazable` | Cada aporte queda ligado a su acuerdo de asamblea y separado de la entrega de cannabis | DL 825 Art. 2 N° 1; CC Art. 556 | `osfl-sin-lucro` | el monto no se calcula por gramo entregado `[criterio jurídico]` |
| `trib-documento` | Cada ingreso tiene el documento tributario que corresponda | DL 825 Art. 2; DL 824 Art. 40 N° 4 | — | registro del documento emitido por ingreso; usuario `[criterio jurídico]` |

## Controles del pack `ley-21663`

Citas textuales en `packs/ley-21663/pack.md`.

| id | Control | Norma | Reutiliza | Cómo se verifica en el código |
|----|---------|-------|-----------|-------------------------------|
| `ciber-calificacion` | Está determinado si la organización o el proveedor es servicio esencial u OIV, con la resolución que lo dice | Ley 21.663 Arts. 4-6 | — | usuario: resolución de la Agencia revisada y fecha |
| `ciber-reporte-csirt` | Procedimiento de reporte al CSIRT Nacional: 3 horas, 72 horas y 15 días (si está obligado) | Ley 21.663 Art. 9 | `inc-brechas`, `sec-monitoring` | plan de respuesta con los tres plazos y responsables |
| `ciber-sgsi-oiv` | Sistema de gestión de seguridad de la información y planes certificados (solo OIV) | Ley 21.663 Art. 8 | `gov-auditoria` | usuario |

## Controles del pack `ley-19628` (transitorio, hasta el 1-dic-2026)

Citas textuales en `packs/ley-19628/pack.md`.

| id | Control | Norma | Reutiliza | Cómo se verifica en el código |
|----|---------|-------|-----------|-------------------------------|
| `t19628-base-sensible` | Los datos de salud se tratan solo con consentimiento escrito e informado o autorización legal | Ley 19.628 Arts. 4 y 10 | `data-licitud`, `data-consent-text` | consentimiento registrado antes de guardar diagnóstico o receta |
| `t19628-plazo-derechos` | Las solicitudes del titular se responden dentro de dos días hábiles | Ley 19.628 Art. 16 | `data-rights-channel` | plazo de respuesta configurado y alertado |

## Cómo usarlo
1. En Fase 1, junta evidencia para cada `id` que tengan los packs activos.
2. En Fase 2, asigna estado + evidencia + remediación por control.
3. El score de cada marco = % de sus controles requeridos en ✅ (⚠️ cuenta como medio).
4. Guarda el resultado por control en `state.json` (ver `output-model.md`).
