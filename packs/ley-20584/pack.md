# Pack: Ley 20.584 — derechos del paciente y ficha clínica (con su reglamento, DS 41/2012)

> Ya vigente. Aplica a todo **prestador de salud** y al software que lleve sus fichas clínicas. Para una
> organización que trabaja con cannabis medicinal, la primera pregunta es si **es** prestador: de eso
> depende si su registro es una "ficha clínica" con todas sus obligaciones. Citas verificadas contra el XML
> oficial de Ley Chile (BCN) descargado el **2026-11-06** con la receta de `sources/FUENTES.md` (sección
> "Pack ley-20584"). Lo no verificado lleva `[verificar contra fuente oficial]`; lo que exige interpretación
> lleva `[criterio jurídico]`.

## Qué normas cubre

| Norma | Qué regula para este pack | Archivo de caché |
|---|---|---|
| **Ley 20.584** (texto vigente, versión 2026-02-16) | Derechos y deberes del paciente; prestador; ficha clínica; consentimiento informado; reclamos | `ley-20584.xml` |
| **DS 41/2012 Salud**, Reglamento sobre Fichas Clínicas | Contenido mínimo, almacenamiento, acceso, conservación y eliminación de la ficha | `ds-41-2012-fichas-clinicas.xml` |

## Lo que dicen las normas (citas textuales)

### 1. Quién es prestador — Ley 20.584 Arts. 1 y 3
- Art. 1 inc. 2: "Sus disposiciones se aplicarán a cualquier tipo de prestador de acciones de salud, sea
  público o privado."
- Art. 3 inc. 1: "Se entiende por prestador de salud, en adelante el prestador, toda persona, natural o
  jurídica, pública o privada, cuya actividad sea el otorgamiento de atenciones de salud. Los prestadores son
  de dos categorías: institucionales e individuales."
- Art. 3 inc. 2: prestadores institucionales son los que "organizan en establecimientos asistenciales medios
  personales, materiales e inmateriales destinados al otorgamiento de prestaciones de salud".
- Art. 3 inc. 3: prestadores individuales son "las personas naturales que [...] otorgan directamente
  prestaciones de salud a las personas o colaboran directa o indirectamente en la ejecución de éstas".
- Art. 3 (salud digital): "se entenderá que el prestador es el responsable de llevar los registros o bases
  de datos de los pacientes [...] y los proveedores tendrán las responsabilidades propias de un mandatario,
  en los términos previstos en la ley N° 19.628". Esto fija el rol del **software**: encargado, no
  responsable, de la ficha que lleva por cuenta del prestador.

### 2. Qué es la ficha clínica — Ley 20.584 Art. 12; DS 41 Arts. 2 y 4
- Art. 12 inc. 1: "La ficha clínica es el instrumento obligatorio en el que se registra el conjunto de
  antecedentes relativos a las diferentes áreas relacionadas con la salud de las personas, custodiada por uno
  o más prestadores de salud, en la medida que realizaron las atenciones registradas".
- Art. 12 inc. 2: puede ser electrónica "siempre que los registros sean completos y se asegure el oportuno
  acceso, conservación y confidencialidad de los datos, así como la autenticidad de su contenido y de los
  cambios efectuados en ella".
- Art. 12 inc. 3: toda la información de la ficha "será considerada como dato sensible".
- DS 41 Art. 2: su contenido "se registrará por el profesional que efectúa la prestación de salud, en el acto
  de otorgarla o inmediatamente después de ello".
- DS 41 Art. 4: "Deberá existir una ficha clínica de cada paciente que atiende el prestador respectivo."

**Consecuencia para el nombre.** La ley define la ficha clínica por **quién la custodia** (un prestador) y
**qué registra** (las atenciones de salud que ese prestador realizó). Un registro que lleva una organización
que no otorga atenciones de salud no es una ficha clínica en el sentido del Art. 12, aunque contenga datos
de salud. Llamarlo "ficha clínica" anuncia obligaciones (conservación de 15 años, contenido del DS 41,
fiscalización de la Superintendencia de Salud) que la organización no asumió, y confunde al titular sobre
quién responde. El control `pac-ficha-clasificacion` aplica el test; ver "Decisión que el pack SÍ resuelve".

### 3. Contenido mínimo — DS 41 Arts. 6 y 7
Art. 6: toda ficha contiene "a lo menos": (a) identificación actualizada del paciente; (b) "Número
identificador de la ficha, fecha de su creación, nombre o denominación completa del prestador"; (c)
"Registro cronológico y fechado de todas la atenciones de salud recibidas"; (d) "Decisiones adoptadas por el
paciente o respecto de su atención, tales como consentimientos informados, rechazos de tratamientos".
Art. 7: cada nuevo registro va "con la identificación del profesional que la otorga y su firma".

### 4. Almacenamiento, integridad y respaldo — DS 41 Art. 8
Repositorio que "garantice que los registros son completos y asegure el acceso oportuno, la conservación y
confidencialidad de los datos, así como la autenticidad de su contenido y de los cambios efectuados en ella".
En soporte electrónico: respaldo en cada incorporación; "una copia de seguridad en el lugar de operación [...]
y otra en un centro de almacenamiento de datos electrónicos que tenga un estricto control de acceso"; barreras
contra accesos no autorizados; restauración "en el menor tiempo posible".

### 5. Acceso restringido y registrado — Ley 20.584 Art. 13 inc. 4; DS 41 Art. 9
- Art. 13 inc. 4: "Los terceros que no estén directamente relacionados con la atención de salud de la persona
  no tendrán acceso a la información contenida en la respectiva ficha clínica. Ello incluye al personal de
  salud y administrativo del mismo prestador, no vinculado a la atención de la persona".
- DS 41 Art. 9: "Este sistema debe llevar registro de las fechas y personas que han accedido a las fichas."

### 6. Entrega al titular y portabilidad — Ley 20.584 Art. 13 inc. 5 y final
La ficha se entrega a solicitud expresa a las personas de las letras a) a h) (titular, tercero con poder,
tribunales, fiscales con autorización judicial, ISP y MINSAL, Superintendencia de Salud, profesionales que
atienden al paciente, y los organismos de licencias médicas). El titular y su apoderado pueden pedir "la
entrega gratuita y sin dilaciones indebidas de una copia íntegra de la información contenida en la ficha
clínica, en un formato estructurado, de uso común y lectura legible, que sea susceptible de ser portado a otro
sistema de ficha clínica".

### 7. Conservación y eliminación — Ley 20.584 Art. 13 inc. 1; DS 41 Arts. 11 y 12
- Art. 13: "Los prestadores deberán conservar la ficha clínica por un período de al menos quince años."
- DS 41 Art. 11: el plazo se cuenta "desde el último ingreso de información que experimenten".
- DS 41 Art. 12: vencido el plazo, el prestador puede eliminarlas por medios "que aseguren la
  confidencialidad de la información y efectiva destrucción"; levanta un acta con "el nombre del paciente y el
  número identificatorio de las fichas"; los prestadores privados deben "protocolizar dicha acta ante notario".

### 8. Consentimiento informado — Ley 20.584 Art. 14
- El derecho se ejerce "en forma libre, voluntaria, expresa e informada".
- Por regla general es verbal, pero "deberá constar por escrito" en procedimientos "que conlleven un riesgo
  relevante y conocido para la salud", y en esos casos la información, su entrega y la aceptación o el rechazo
  "deberán constar por escrito en la ficha clínica del paciente".
- En salud digital, el consentimiento verbal se registra "mediante una declaración escrita en formato papel
  o firmado a través de un sistema electrónico que garantice su autenticidad de conformidad con lo dispuesto
  en la ley N° 19.799".

### 9. Reclamos y fiscalización — Ley 20.584 Arts. 37 y 38
- Art. 37: el prestador institucional "deberá contar con personal especialmente habilitado para este efecto y
  con un sistema de registro y respuesta escrita de los reclamos planteados".
- Art. 38: la Superintendencia de Salud, por su Intendencia de Prestadores, controla el cumplimiento; si las
  irregularidades no se corrigen en el plazo fijado (no más de dos meses), el prestador "será sancionado de
  acuerdo con las normas establecidas en los Títulos IV y V del Capítulo VII, del Libro I del decreto con
  fuerza de ley Nº1, de 2006, del Ministerio de Salud" `[verificar contra fuente oficial]` (montos no leídos).

## Decisión que el pack SÍ resuelve: ¿el registro es una ficha clínica?
Se resuelve con hechos, como el DPO en `ley-21719`. Aplicar el test y dejar el resultado en
`pac-clasificacion-registro.md`:

| Pregunta | Si la respuesta es SÍ | Si es NO |
|---|---|---|
| 1. ¿La organización (o el cliente del software) otorga atenciones de salud: consultas, evaluaciones, indicaciones, procedimientos? (Ley 20.584 Art. 3) | Es prestador. Seguir a la 2. | No es prestador: su registro **no es ficha clínica**. Ir a "Resultado B". |
| 2. ¿El registro guarda las atenciones que ese prestador realizó, escritas por el profesional que las otorgó? (Art. 12; DS 41 Art. 2) | **Resultado A**: es ficha clínica. Aplican todos los controles `pac-*`. | **Resultado B**. |

- **Resultado A — ficha clínica.** Nombrarla así. Aplican `pac-ficha-contenido`, `pac-ficha-integridad`,
  `pac-ficha-acceso`, `pac-ficha-entrega`, `pac-ficha-conservacion`, `pac-ficha-eliminacion`,
  `pac-consentimiento` y, si es institucional, `pac-reclamos`. El software actúa como mandatario (Art. 3).
- **Resultado B — no es ficha clínica.** No usar "ficha clínica" (ni "historia clínica") en textos visibles,
  documentos ni nombres de campos. Usar un nombre que diga qué es: "ficha de ingreso", "registro del socio",
  "antecedentes de la receta". Los datos de salud que contenga (diagnóstico, receta) siguen siendo datos
  sensibles: los protegen la Ley 19.628 / 21.719 y el Código Sanitario Art. 101, y su plazo de conservación
  sale de esas normas o de la finalidad, **no** de los 15 años del Art. 13. Si un médico tratante atiende a
  los socios, la ficha clínica es **de ese médico** (prestador individual), no de la organización.
- **Caso dudoso** `[criterio jurídico]`: la organización tiene un profesional de salud que no prescribe pero
  orienta sobre dosis o vía de administración. Puede encajar en quienes "colaboran directa o indirectamente"
  en la ejecución de prestaciones (Art. 3 inc. 3), aunque ese inciso habla de personas naturales. Registrar la pregunta como abierta; mientras tanto, no llamar ficha clínica
  al registro y no guardar en él atenciones de ese profesional.

## Controles que exige (ver `references/controls.md`)
Siempre: `pac-ficha-clasificacion`. Solo con Resultado A: `pac-ficha-contenido`, `pac-ficha-integridad`,
`pac-ficha-acceso`, `pac-ficha-entrega`, `pac-ficha-conservacion`, `pac-ficha-eliminacion`,
`pac-consentimiento`, `pac-reclamos` (institucional). Reutiliza: `sec-logs`, `sec-backups`, `sec-rest`,
`data-derechos`, `data-minimizacion`.

## Documentos a generar (templates/ → `<repo>/.compliance/docs/` con prefijo `pac-`)
`clasificacion-registro.md` (siempre); `politica-ficha-clinica.md` (solo con Resultado A).
