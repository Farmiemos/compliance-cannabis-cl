# Pack: Ley 21.663 — Ley Marco de Ciberseguridad

> Aplica a quien preste un **servicio esencial** o sea calificado **operador de importancia vital** (OIV). Para el
> ecosistema del cannabis medicinal la pregunta útil no es la OSFL sino **el proveedor del software**: la ley
> incluye como servicio esencial los "servicios digitales y servicios de tecnología de la información gestionados
> por terceros". Citas verificadas contra el XML oficial (versión BCN 2024-04-08) descargado el **2026-11-06**. La
> entrada en vigencia escalonada de sus obligaciones está en sus artículos transitorios, **no** leídos
> `[verificar contra fuente oficial]`.

## Lo que dice la ley (citas textuales)

### 1. A quién se aplica — Art. 4
"La presente ley se aplicará a las instituciones que presten servicios calificados como esenciales [...] y a aquellas
que sean calificadas como operadores de importancia vital". Son servicios esenciales, entre otros, los de
instituciones privadas que realicen "servicios digitales y servicios de tecnología de la información gestionados por
terceros" y la "prestación institucional de salud por entidades tales como hospitales, clínicas, consultorios y
centros médicos, y la producción y/o investigación de productos farmacéuticos". La Agencia "identificará, mediante
resolución exenta [...] las infraestructuras, procesos o funciones específicas que serán calificadas como esenciales".

### 2. Operadores de importancia vital — Arts. 5 y 6
La Agencia califica como OIV a prestadores de servicios esenciales cuyo servicio "dependa de las redes y sistemas
informáticos" y cuya afectación "tenga un impacto significativo" en el orden público o la provisión de servicios
esenciales; "siempre se deberá tener en consideración el tamaño de la institución privada". La nómina se revisa "Al
menos cada tres años" por resolución, con consulta pública.

### 3. Deberes generales — Art. 7
"Las instituciones obligadas por la presente ley deberán aplicar de manera permanente las medidas para prevenir,
reportar y resolver incidentes de ciberseguridad", conforme a los protocolos y estándares de la Agencia, que serán
"diferenciadas según el tipo de organización".

### 4. Reporte de incidentes — Art. 9
Todas las instituciones del Art. 4 reportan al CSIRT Nacional los incidentes "que puedan tener efectos
significativos": alerta temprana "Dentro del plazo máximo de tres horas"; actualización "Dentro del plazo máximo de
setenta y dos horas" (24 horas si es OIV con el servicio afectado); informe final "Dentro del plazo máximo de quince
días corridos".

### 5. Deberes adicionales del OIV — Art. 8
Entre otros: "Implementar un sistema de gestión de seguridad de la información continuo", "Mantener un registro de las
acciones ejecutadas" y "Elaborar e implementar planes de continuidad operacional y ciberseguridad, los cuales deberán
certificarse".

## Decisión que el pack SÍ resuelve: ¿quién está obligado?

| Sujeto | ¿Servicio esencial por el Art. 4? | Resultado |
|---|---|---|
| OSFL que cultiva y entrega a socios | No presta atención institucional de salud ni produce productos farmacéuticos registrados | **No obligada**, salvo calificación expresa de la Agencia |
| Proveedor del software que gestiona datos de terceros (SaaS) | Puede caer en "servicios digitales y servicios de tecnología de la información gestionados por terceros" | **Revisar la resolución de la Agencia** que identifica esos servicios; si lo incluye, aplican los Arts. 7 y 9 |
| Cualquiera de los dos | ¿Figura en la nómina de OIV? | Solo si una resolución lo nombra (Art. 6) |

Mientras la resolución no lo nombre, el proveedor **no está obligado** por esta ley, pero el reporte de brechas de la
Ley 21.719 (control `inc-brechas`) sí aplica. Preparar el procedimiento del Art. 9 cuesta poco y deja listo el plazo
de tres horas si la calificación llega.

## Controles que exige (ver `references/controls.md`)
`ciber-calificacion` (siempre). Si la institución está obligada: `ciber-reporte-csirt`, y si es OIV,
`ciber-sgsi-oiv`. Reutiliza: `inc-brechas`, `sec-monitoring`, `sec-logs`, `sec-backups`.

## Documentos a generar
Ninguno propio: el procedimiento de reporte se agrega como anexo al plan de respuesta a brechas de `ley-21719`
(`21719-plan-respuesta-brechas.md`), con los plazos de tres horas, 72 horas y quince días.
