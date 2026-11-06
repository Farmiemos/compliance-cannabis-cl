---
name: compliance-cannabis-cl
description: >-
  Esta skill se usa cuando el usuario pide "armar el compliance", "cumplir la Ley 21.719",
  "preparar la protección de datos", "auditar datos personales", "generar política de privacidad /
  DPA / RAT / EIPD / consentimiento", "cumplir la ley de datos en Chile", "modelo de prevención de
  delitos (Ley 21.595)", o "compliance de cannabis medicinal", "Ley 20.000", "receta de cannabis",
  "trazabilidad de cannabis", "autorización SAG", "DS 404 / Decreto 84". Audita un repo y genera, SIN
  abogado, la documentación de cumplimiento para un SaaS, empresa u organización que trabaja con cannabis
  medicinal en Chile, contrastada contra el texto oficial de la ley. Cubre la Ley 21.719, la 21.595 y el
  pack sanitario-cannabis (Ley 20.000, DS 867, DS 404/405, Decreto 84/2015, Código Sanitario) y los packs
  ley-20584 (ficha clínica), ley-20500 (la OSFL como asociación), tributario, ley-21663 (ciberseguridad) y
  ley-19628 (transitorio). Derivada
  de compliance-cl de Lelemon (MIT).
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# compliance-cl — Motor de cumplimiento (Chile), multi-marco y self-service

Auditar una aplicación contra uno o varios **packs** de ley, **resolver las decisiones** con el criterio
de la ley y **generar toda la documentación rellenada** (sin dejar tarea), dejando un **estado versionado**
en el repo que se re-corre en el tiempo. Objetivo: que un founder cumpla **solo**; el abogado es opcional
(ver `references/cuando-acudir-a-abogado.md`).

> **DISCLAIMER OBLIGATORIO** — No constituye asesoría legal (un software no asume la responsabilidad legal
> del usuario). Genera borradores fundados en la normativa chilena para cumplir sin abogado. Incluir este
> disclaimer al pie de cada documento legal generado.

## Modelo mental
- **Controles** = unidades reutilizables que satisfacen varios marcos a la vez. Catálogo + crosswalk:
  `references/controls.md`.
- **Packs** = una ley cada uno (`packs/<id>/pack.md`): obligaciones, controles que exige y documentos a
  generar. Hoy: `ley-21719`, `ley-21595`, `sanitario-cannabis`, `ley-20584`, `ley-20500`,
  `tributario`, `ley-21663`, `ley-19628`.
- **Estado** = el output vive en `<repo>/.compliance/` versionado por git. Formato: `references/output-model.md`.
- **Fuentes (verdad)** = textos OFICIALES en `sources/` (`FUENTES.md`). Toda afirmación legal cita
  **ley + artículo + archivo**; lo no verificable se marca `[verificar contra fuente oficial]`. NADA
  inventado. Numeración verificada: `references/mapa-articulos-21719.md`.

## Flujo

### Fase 0 — Encuadre (CUESTIONARIO: recoger todo para no dejar `[COMPLETAR]`)
Mostrar el disclaimer. Luego preguntar al usuario (con `AskUserQuestion` cuando aplique) y **registrar las
respuestas para rellenar los documentos**. No dejar placeholders salvo que el dato sea genuinamente
desconocido; en ese caso, proponer un **default sensato** y marcarlo.
Recoger:
1. Repo a auditar y **packs** a activar (default: `ley-21595` + `ley-21719`; agregar `sanitario-cannabis`
   si la organización cultiva, custodia, entrega o registra cannabis, o si el software lo hace por ella;
   agregar `ley-20584` si el software guarda datos de salud: diagnósticos, recetas o atenciones;
   `ley-20500` y `tributario` si es una OSFL; `ley-21663` siempre (el test dice si obliga); `ley-19628`
   mientras la fecha sea anterior al 1-dic-2026).
2. **Empresa:** razón social, RUT, domicilio, correo de contacto, tamaño, representante legal.
3. **Responsable de datos / encargado de prevención** designado (en micro suele ser el dueño).
4. Por flujo de datos: rol **responsable** vs **encargado**.
5. **Plazos de retención** por tipo de dato; si no los sabe, proponer defaults razonables.
6. ¿Tratan **datos sensibles** (salud, etc.)? ¿Usuarios en la **UE** (gatilla GDPR a futuro)?
7. Con `sanitario-cannabis`: forma jurídica; ¿cultiva y con qué apoyo (Art. 8 inc. 2 o autorización del
   SAG)?; ¿entrega a terceros con receta?; ¿maneja productos registrados en el ISP?; ¿tiene superficies
   públicas (sitio, catálogo, redes)?
8. Con `ley-20584`: ¿la organización otorga atenciones de salud (consultas, evaluaciones, indicaciones)?
   ¿Quién escribe los registros de salud y en qué rol?
9. Con `ley-20500`: fines textuales de los estatutos, N° de inscripción, directorio, cómo se fijan los aportes
   (acuerdo de asamblea, cuota igual o monto por cantidad recibida) y por qué el Estado y el sector privado no
   cubren el tratamiento de los socios (eslabón 2 de la cadena del fundamento).
Si ya existe `<repo>/.compliance/state.json`, leerlo: esta corrida es una re-evaluación.

### Fase 1 — Descubrimiento (leer el código, no asumir)
Recorrer el repo con Grep/Glob para levantar evidencia de cada control:
- Datos personales (esquemas/migraciones/modelos/formularios): `email|phone|telefono|rut|address|nombre|name|ip|lat|lng|password`; marcar **datos sensibles** específicos (salud, biométricos, menores).
- Proveedores externos y transferencias internacionales (`.env*`, `package.json`, configs): AWS, Google, Meta, etc.; marcar los que procesan fuera de Chile.
- Medidas técnicas: TLS, cifrado en reposo, hashing de password, MFA, logs/auditoría, segregación por tenant, secretos fuera del código, seudonimización, privacy-by-default.
- Gobernanza (no está en el código): tomarla del cuestionario; marcar `❓` lo no verificable por código.
- Con `sanitario-cannabis`: esquema y validación de la receta (emisor, diagnóstico, tratamiento, duración,
  vía de administración); bloqueo de entregas con receta vencida; límites por persona; libro de movimientos
  de lotes y balance de gramos; catálogo de vías de administración (buscar `fumad|combust|smok`); textos de
  las superficies públicas (precios, promociones, invitaciones al consumo).
- Con `ley-20584`: dónde aparece "ficha clínica" o "historia clínica" (textos visibles, PDFs, nombres de
  campos y rutas); qué guarda ese registro y quién lo escribe; permisos de lectura, log de accesos,
  versionado de cambios, exportación al titular y retención automática.
- Con `ley-20500` y `tributario`: registro de socios con historial, retiro voluntario, actas, cómo se calcula el
  aporte (¿por gramo?) y si la retención o la supresión borran respaldos de pagos antes de seis años.

### Fase 2 — Evaluar controles y RESOLVER decisiones
Para cada control de `references/controls.md`: estado (✅/⚠️/❌/❓) + evidencia + remediación. Un control
se propaga a todos los marcos que lo exigen.
**Resolver las decisiones** (no dejarlas abiertas), citando el artículo:
- **DPO** (Art. 50): obligatorio solo para organismos públicos o datos sensibles a gran escala; si no,
  basta el responsable designado → dar el resultado.
- **EIPD** (Art. 15 ter): aplicar el test de `packs/ley-21719/templates/eipd.md`; si aplica un supuesto, es obligatoria.
- **Base de licitud** por flujo y **mecanismo de transferencia** (cláusulas modelo).
- **Excepción, `sanitario-cannabis`:** las cuatro preguntas de `packs/sanitario-cannabis/pack.md` ("Preguntas
  que el pack NO resuelve") **nunca se resuelven**: se registran como abiertas en
  `san-fundamento-modelo-operativo.md`. Afirmar que un modelo de cultivo o entrega es legal o ilegal está
  fuera del alcance de la skill.
- **¿El registro es una ficha clínica?** (`ley-20584`): **sí se resuelve**, con el test de
  `packs/ley-20584/pack.md` (Ley 20.584 Arts. 3 y 12). Si no lo es, no se le llama así en ningún texto.
- **¿Quién está obligado por la Ley 21.663?** **Sí se resuelve**, con la tabla de `packs/ley-21663/pack.md`.
- **DJ 1945 (`tributario`):** si los ingresos del año superan 4.000 UF, es obligatoria. Informa las cuotas de
  asociados; no las justifica ni las exime. Lo que las sostiene es el DL 824 Art. 17 N° 11 y los hechos que pide el
  SII (Oficio 2419/2013: regla de estatutos, uniforme para todos).
- **Licitud de los fines (`ley-20500`) e IVA del aporte (`tributario`): nunca se resuelven.** El fundamento
  constitucional (Art. 19 N° 1, 9 y 15) se documenta como argumento con evidencia por eslabón, no como regla.

### Fase 3 — Generar TODA la documentación (rellenada)
Por cada pack activo, leer su `pack.md` y generar **todos** sus `templates/`, **rellenados con las
respuestas de Fase 0 y los hallazgos de Fase 1**. Para `ley-21719`: rat, política, consentimiento,
canal-derechos, dpa, anexo-transferencias, plan-respuesta-brechas, registro-vulneraciones, y eipd (si el
test la hace obligatoria). Para `ley-21595`: modelo-prevencion-delitos, código-etica, matriz-riesgos,
acta-encargado-prevencion, reglamento-canal-denuncias. Para `sanitario-cannabis`: fundamento-modelo-operativo,
politica-receta, registro-trazabilidad, y bitacora-sag (solo con cultivo autorizado). Para `ley-20584`:
clasificacion-registro, y politica-ficha-clinica (solo si el registro es ficha clínica). Para `ley-20500`:
gobierno-asociativo. Reemplazar todos los placeholders; usar
`[COMPLETAR: ...]` solo para lo realmente desconocido.

### Fase 4 — Escribir el estado versionado
Escribir en `<repo>/.compliance/` según `references/output-model.md`: `state.json` (controles + score por
marco), `docs/` (todo lo generado), `INSTRUCTIVO.md` (runbooks desde `references/instructivo-situaciones.md`)
y `RESUMEN.md` (postura, brechas priorizadas, **diff vs la corrida anterior**, y qué quedó resuelto solo +
el único insumo externo: supervisión anual del MPD). Sugerir commitear `.compliance/`.

### Fase 5 — Cierre y construcción
Reportar la postura por marco. Para cada hueco con remediación de código, **ofrecer construirlo** (esta
skill corre en Claude Code) siguiendo las **recetas de `references/build/`** (MFA, cifrado en reposo,
audit log + actor/IP, endpoints ARCO, consentimiento, retención): en una rama, con tests y los gates del
repo. Ofrecer también **montar el monitoreo** (`references/build/monitoreo.md`: secret scanning + HIBP +
alertas + watcher); la skill no vigila en vivo, pero deja el monitoreo instalado. Sugerir **agendar
re-corridas periódicas** (`references/revisiones-periodicas.md`) para detectar drift. Cerrar con UN siguiente paso.

## Reglas
- **Fuente de verdad = `sources/`.** Cita ley + artículo + archivo; `[verificar contra fuente oficial]` si
  no se confirma. Nunca basar una afirmación normativa en un blog.
- **Self-service:** rellenar todo desde el cuestionario; resolver las decisiones; no derivar al abogado lo
  que la skill puede entregar. El abogado es opcional (ver `references/cuando-acudir-a-abogado.md`).
- No inventar datos de la empresa ni normativa. `[COMPLETAR]` solo para lo desconocido; `❓` para lo no
  verificable por código.
- Distinguir responsable vs encargado en cada flujo.
- No prometer "cumplimiento garantizado/certificado". Insumos NO self-service: la **supervisión externa
  anual del MPD (21.595)**, la representación si hay fiscalización, y el **monitoreo/detección de
  filtraciones en tiempo real** (es un servicio aparte; la skill prepara el plan de respuesta y puede
  configurar alertas sobre el audit log, pero no hace vigilancia 24/7).

## Recursos
- `references/controls.md` — catálogo de controles + crosswalk.
- `references/output-model.md` — formato del estado `.compliance/`.
- `references/mapa-articulos-21719.md` — artículos verificados contra el texto oficial.
- `references/cuando-acudir-a-abogado.md` — por qué el abogado es opcional.
- `references/instructivo-situaciones.md` — runbooks (ARCO, brecha, fiscalización, calendario).
- `references/build/` — **recetas de construcción** (cómo implementar cada remediación: MFA, cifrado,
  audit log + actor/IP, ARCO, consentimiento, retención, monitoreo) con librerías verificadas. Ver
  `references/build/index.md`.
- `references/revisiones-periodicas.md` — automatizar la re-corrida (`/loop`, cron headless `claude -p`,
  `/schedule`) para detectar drift entre corridas.
- `packs/ley-21719/`, `packs/ley-21595/`, `packs/sanitario-cannabis/`, `packs/ley-20584/`, `packs/ley-20500/`,
  `packs/tributario/`, `packs/ley-21663/`, `packs/ley-19628/` — obligaciones +
  plantillas por marco.
- `sources/` — textos legales oficiales (ley 21.719 PDF/txt, cláusulas modelo, XML) + `FUENTES.md`.
  ⚠️ Para **retener** datos hace falta el **Código Tributario** y el **Código del Trabajo**, que NO se
  versionan acá (repo público, redistribución BCN sin confirmar): `FUENTES.md` trae el `curl` para bajarlos y
  los artículos ya verificados. Sin ellos una retención queda sin fundamento — la 21.719 remite a la
  obligación legal, pero la pone otra ley.
