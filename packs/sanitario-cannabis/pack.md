# Pack: Sanitario cannabis — Ley 20.000, su reglamento, Código Sanitario y DS 404/405

> Ya vigente. Aplica a quien cultive, custodie, transfiera o registre cannabis con fines medicinales en
> Chile, y al software que lleve ese registro. Todas las citas están verificadas contra el XML oficial de
> Ley Chile (BCN) descargado el **2026-11-06** con la receta de `sources/FUENTES.md` (sección
> "Pack sanitario-cannabis"). Lo que no se pudo verificar lleva `[verificar contra fuente oficial]`; lo
> que exige interpretación lleva `[criterio jurídico]`.

## Qué normas cubre

| Norma | Qué regula para este pack | Archivo de caché |
|---|---|---|
| **Ley 20.000** (texto vigente, versión 2026-05-23) | Delitos de tráfico, cultivo, porte; justificación por tratamiento médico | `ley-20000.xml` |
| **Ley 21.575** (2023) | Agregó a la Ley 20.000 el Art. 8 inc. 2 (receta para el cultivo medicinal) | `ley-21575.xml` |
| **DS 867/2007 Interior**, reglamento de la Ley 20.000 | Clasificación de sustancias; autorización del SAG para cultivar | `ds-867-reglamento-ley-20000.xml` |
| **DS 404/1983 Salud**, Reglamento de Estupefacientes | Prohibición general del cannabis; excepciones del ISP; venta en farmacia | `ds-404-estupefacientes.xml` |
| **DS 405/1983 Salud**, Reglamento de Psicotrópicos | THC: excepción del ISP para productos farmacéuticos | `ds-405-psicotropicos.xml` |
| **Decreto 84/2015 Salud** | Modificó los DS 404 y 405 para permitir productos farmacéuticos con cannabis | `decreto-84-2015.xml` |
| **Código Sanitario** (DFL 725) | Receta (Art. 101), publicidad de productos farmacéuticos (Art. 100) | `codigo-sanitario-dfl-725.xml` |
| Ley 20.724, Ley 21.267, Res. Ex. 1143/2023, Decreto 11/2025 | Receta electrónica y validación de recetas gráficas (contexto) | ver `FUENTES.md` |

**Corrección de un error común:** el **Decreto 41 de 2012 del MINSAL es el "Reglamento sobre Fichas
Clínicas"** (idNorma 1046753), no un reglamento de receta electrónica. No hay en Chile una ley propia de
receta electrónica: la materia está repartida en el Código Sanitario Art. 101 y las normas de la tabla.

## Lo que dicen las normas (citas textuales)

### 1. La receta que justifica el cultivo — Ley 20.000 Art. 8 inc. 2 (agregado por Ley 21.575)
> "Se entenderá justificado el cultivo de especies vegetales del género cannabis para la atención de un
> tratamiento médico, con la presentación de la receta extendida para ese efecto por un médico cirujano
> tratante, la que deberá indicar el diagnóstico de la enfermedad, su tratamiento y duración, además de la
> forma de administración del cannabis, la que no podrá ser mediante combustión."

Mismo inciso: quien "falsifique o maliciosamente haga uso de recetas falsas para justificar el cultivo"
recibe presidio mayor en su grado mínimo, y la pena sube un grado si el objeto es "la comercialización de
la droga o su facilitación a un tercero".

**Cinco requisitos verificables por código:** (a) emisor médico cirujano tratante, (b) diagnóstico, (c)
tratamiento, (d) duración, (e) forma de administración distinta de combustión.

### 2. Tratamiento médico y uso personal — Ley 20.000 Arts. 4 y 50
- Art. 4 inc. 1: la posesión de pequeñas cantidades se castiga "a menos que justifique que están
  destinadas a la atención de un tratamiento médico o a su uso o consumo personal exclusivo y próximo en el
  tiempo".
- Art. 4 inc. 2: "En igual pena incurrirá el que adquiera, transfiera, suministre o facilite a cualquier
  título pequeñas cantidades de estas sustancias, drogas o materias primas, con el objetivo de que sean
  consumidas o usadas por otro."
- Art. 50 inc. final: "Se entenderá justificado el uso, consumo, porte o tenencia de alguna de dichas
  sustancias para la atención de un tratamiento médico."

### 3. Cultivo autorizado por el SAG — Ley 20.000 Arts. 8, 9 y 10; DS 867 Arts. 6-14
- Ley 20.000 Art. 9: "La autorización a que se refiere el artículo anterior será otorgada por el Servicio
  Agrícola y Ganadero." No se otorga a quien tenga condena o suspensión condicional por esta ley, ni a la
  persona jurídica cuyos representantes, administradores o socios (sociedades no anónimas) estén en esa
  situación; se suspende al formalizarse una investigación y se cancela con condena ejecutoriada.
- Ley 20.000 Art. 10: el autorizado que "desvíe o destine al tráfico ilícito" las especies o sus partes
  activas recibe presidio mayor; abandonar plantas o rastrojos o no cumplir "las obligaciones establecidas
  en el reglamento sobre cierro y destrucción" también se sanciona.
- DS 867: solicitud en la Dirección Regional del SAG (Art. 6) con al menos **cuatro meses** de antelación
  (Art. 7); aviso de la fecha exacta de siembra con **30 días** de anticipación (Art. 11); **guía de libre
  tránsito** del SAG para transportar la cosecha (Art. 12); predio "del todo cerrado" (Art. 13);
  destrucción de plantas y rastrojos en presencia de funcionarios (Art. 14).
- DS 867 Art. 5 califica a "Cannabis Sativa L" como especie vegetal productora a que se refiere el Art. 8.

### 4. El cannabis fuera de la farmacia — DS 404 Art. 5 (texto vigente, versión 2020-11-19)
> "La importación, exportación, tránsito, extracción, producción, fabricación, fraccionamiento,
> preparación, distribución, transporte, transferencia a cualquier título, expendio, posesión y tenencia
> de acetorfina, cannabis, resina de cannabis, extractos y tinturas de cannabis, [...] estarán prohibidas en
> el territorio nacional."

Excepciones del mismo artículo: investigación científica autorizada por el ISP, y "el Instituto de Salud
Pública podrá autorizar y controlar el uso de cannabis, resina de cannabis, extractos y tinturas de
cannabis para la elaboración de productos farmacéuticos de uso humano". El Decreto 84/2015 agregó al
Art. 23: esas especialidades "podrán expenderse al público en farmacias o laboratorios mediante receta
médica retenida con control de existencia". El DS 405 Art. 6 y Art. 23 hacen lo mismo para los
tetrahidrocanabinoles.

### 5. La receta en el Código Sanitario — Art. 101
- "La prescripción indicará asimismo el período de tiempo determinado para el tratamiento total, o a
  repetir periódicamente".
- La receta se extiende "en documento gráfico o electrónico"; el reglamento fija elementos "que impidan o
  dificulten la falsificación o la sustitución de la receta".
- "La receta y su contenido [...] serán reservados y considerados datos sensibles sujetándose a lo
  establecido en la ley N° 19.628."

### 6. Publicidad — Código Sanitario Art. 100 inc. 2 y Ley 20.000 Art. 3
- CS Art. 100 inc. 2: la publicidad de un producto farmacéutico al consumidor "sólo estarán permitidas
  respecto de medicamentos de venta directa".
- Ley 20.000 Art. 3: las penas del Art. 1 se aplican también a quienes "por cualquier medio, induzcan,
  promuevan o faciliten el uso o consumo de tales sustancias".

## Preguntas que el pack NO resuelve `[criterio jurídico]`
Se registran en `fundamento-modelo-operativo.md`; nunca se dan por resueltas en un documento generado.
1. **Cultivo colectivo y entrega a socios.** El Art. 8 inc. 2 justifica el cultivo "para la atención de un
   tratamiento médico" con receta, pero el texto no dice si una persona jurídica puede cultivar para el
   tratamiento de varias personas. El Art. 4 inc. 2 sanciona transferir o facilitar "a cualquier título" con
   el objetivo de que lo use otro, y el DS 404 Art. 5 prohíbe la "transferencia a cualquier título" fuera
   de las excepciones del ISP. Llamar "aporte" a la contribución no cambia el texto "a cualquier título".
2. **Si el cultivo de la organización necesita autorización del SAG** (Ley 20.000 Art. 9; DS 867 Art. 6)
   o si se sostiene solo en la justificación del Art. 8 inc. 2.
3. **Si un producto de cannabis entregado por la organización es "producto farmacéutico"** para el
   Código Sanitario, lo que activaría los Arts. 100 y 101 completos y el control del ISP.
4. **Si un catálogo público de variedades o productos** es publicidad (CS Art. 100) o promoción del uso
   (Ley 20.000 Art. 3).

## Controles que exige (ver `references/controls.md`)
`san-receta-requisitos`, `san-receta-vigencia`, `san-receta-autenticidad`, `san-receta-reserva`,
`san-destino-personal`, `san-trazabilidad`, `san-no-combustion`, `san-publicidad`, `san-sag` (si hay
cultivo autorizado), `san-farmaceutico` (si se manejan productos registrados en el ISP). Reutiliza de
otros packs: `sec-logs`, `sec-rest`, `data-privacy-by-design`, `gov-registro`.

## Sanciones relevantes (Ley 20.000, verificadas)
- Cultivo sin autorización (Art. 8 inc. 1): presidio menor en su grado máximo a presidio mayor en su grado
  mínimo y multa de 40 a 400 UTM, salvo justificación de uso personal.
- Receta falsa para justificar el cultivo (Art. 8 inc. 2): presidio mayor en su grado mínimo; un grado más
  si busca comercializar o facilitar a un tercero.
- Desvío por un autorizado (Art. 10): presidio mayor en sus grados mínimo a medio y multa de 40 a 400 UTM.
- Facilitar un inmueble o mueble a sabiendas (Art. 11): la misma pena del delito respectivo.

## Documentos a generar (templates/ → `<repo>/.compliance/docs/` con prefijo `san-`)
`fundamento-modelo-operativo.md` (siempre), `politica-receta.md` (siempre),
`registro-trazabilidad.md` (siempre), `bitacora-sag.md` (solo si hay cultivo autorizado por el SAG).
