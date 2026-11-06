# Pack: Tributario — la OSFL frente al SII (Código Tributario, IVA y Renta)

> Ya vigente. Aplica a la OSFL que recibe aportes de sus socios y al software que registra esos movimientos.
> Citas verificadas contra el XML oficial de Ley Chile (BCN) y contra los documentos del SII en sii.cl, descargados el
> **2026-11-06** (`sources/FUENTES.md`, secciones "Pack tributario" y "Documentos del SII"). Lo no verificado lleva
> `[verificar contra fuente oficial]`; lo que exige interpretación lleva `[criterio jurídico]`. Los oficios del SII
> responden consultas concretas: orientan, pero no obligan al fiscalizador frente a hechos distintos.

## Qué normas cubre

| Norma | Qué regula para este pack | Archivo de caché |
|---|---|---|
| **Código Tributario** (DL 830) | Conservación de libros y documentos; plazos de revisión del SII | `codigo-tributario-dl830.xml` |
| **Ley sobre Impuesto a las Ventas y Servicios** (DL 825) | Qué es "venta" y quién es "vendedor" | `dl-825-iva.xml` |
| **Ley sobre Impuesto a la Renta** (DL 824) | Exención de primera categoría para instituciones de beneficencia | `dl-824-renta.xml` |
| Código Civil Arts. 556 y 557-1 | Aportes, prohibición de repartir excedentes, contabilidad | `codigo-civil.xml` (ver `packs/ley-20500/`) |
| **Res. Ex. SII 103/2017** (mod. Res. 94/2023) y su Anexo 2 | Declaración Jurada 1945 de las OSFL | `sii/reso94-2023.txt`, `sii/dj1945-instrucciones-2023.txt` |
| **Oficios SII 2419/2013 y 3616/2002; Ord. 678/2009** | Cuotas de asociados: renta, IVA y documento | `sii/oficio-2419-2013.txt`, `sii/oficio-3616-2002.txt`, `sii/ordinario-678-2009.txt` |

## Lo que dicen las normas (citas textuales)

### 1. Conservar libros y respaldos — Código Tributario Arts. 17 y 200
- Art. 17 inc. 2: los libros de contabilidad deben ser "conservados por los contribuyentes, junto con la
  documentación correspondiente, mientras esté pendiente el plazo que tiene el Servicio para la revisión de las
  declaraciones".
- Art. 200: el SII puede revisar y girar "dentro del término de tres años contado desde la expiración del plazo
  legal en que debió efectuarse el pago"; "será de seis años para la revisión de impuestos sujetos a declaración,
  cuando ésta no se hubiere presentado o la presentada fuere maliciosamente falsa".
- **Consecuencia para el software:** los registros de aportes, compras y gastos se conservan **al menos seis años**
  desde el pago que respaldan, aunque el socio pida suprimir sus datos: es la obligación legal que permite negar la
  supresión (Ley 21.719 Art. 7, ver `references/mapa-articulos-21719.md`).

### 2. "Aporte" o "venta": el nombre no decide — DL 825 Art. 2
- N° 1: es "venta" "toda convención independiente de la designación que le den las partes, que sirva para transferir
  a título oneroso el dominio de bienes corporales muebles".
- N° 3: es "vendedor" quien "se dedique en forma habitual a la venta de bienes corporales muebles [...] sean ellos de
  su propia producción o adquiridos de terceros. Corresponderá al Servicio de Impuestos Internos calificar la
  habitualidad."
- **Consecuencia:** llamar "aporte" al pago que el socio hace cuando recibe cannabis no impide que el SII lo califique
  como venta: decide el hecho, no la etiqueta. Qué hechos sostienen una cuota de asociado está en la sección 5.

### 3. Exención de Renta — DL 824 Art. 40 N° 4
"Estarán exentas del impuesto de la presente categoría" las rentas de "Las instituciones de beneficencia que
determine el Presidente de la República", solo si "no persigan fines de lucro y que tengan por objeto principal y
efectivo proporcionar ayuda, aun cuando no se otorgue de manera totalmente gratuita, de modo directo a personas de
escasos recursos económicos". **No es automática**: requiere el decreto, y el objeto de una OSFL de cannabis
medicinal (tratar a sus socios) no coincide por sí solo con ayudar a "personas de escasos recursos".

### 4. Destino de los excedentes — Código Civil Arts. 556 y 557-2
Los excedentes "no podrán distribuirse entre los asociados", y las rentas de actividades económicas "sólo deberán
destinarse a los fines de la asociación". Ser sin fines de lucro **no** significa estar exento de impuestos: la
exención la da una norma tributaria, no la forma jurídica.

### 5. Cuotas de asociados según el SII
- **No son renta** — DL 824 Art. 17 N° 11: "No constituye renta: [...] Las cuotas que eroguen los asociados".
- **Pueden ser variables** — Oficio 2419/2013 (cuotas de asociados de una corporación de alimentos donados): no
  constituyen renta "conforme a lo previsto en el N° 11, del artículo 17 de la LIR", y "tampoco se divisa
  inconveniente en que el monto de las cuotas señaladas sea variable, dependiendo del volumen de ayuda que recibe cada
  asociado, dado que lo que nuestro ordenamiento jurídico prohíbe a este tipo de entidades es el lucro de sus
  asociados". La corporación puede "imponer cuotas ordinarias como extraordinarias, fijas o variables a sus socios".
- **No llevan IVA** — el mismo oficio: "no se verifica" un hecho gravado; Oficio 3616/2002: las cuotas sociales "no
  remuneran la prestación de un servicio en los términos del artículo 2°, N° 2, del D.L. N° 825", por lo que "no
  procede la emisión de facturas por servicios no gravados o exentos de IVA, pudiendo emitirse un comprobante de
  ingreso que acredite dichos pagos".
- **Requisitos que fija el SII** (Oficio 2419, para que el asociado las deduzca como gasto): cuotas establecidas en
  los estatutos "con carácter de uniformidad y generalidad para todos los asociados", y destinadas "al cumplimiento de
  los fines propios de la asociación".
- **Límite:** el SII advierte que "corresponde a la instancia de fiscalización respectiva verificar los antecedentes de
  hecho que concurran en cada operación". En el Oficio 2419 los asociados eran instituciones que redistribuían
  alimentos donados; un socio que recibe cannabis para su propio tratamiento es un hecho distinto, y ese oficio no lo
  resuelve `[criterio jurídico]`. El Ord. 678/2009 confirma que el SII mira los estatutos y los hechos de cada caso.

### 6. Declaración Jurada 1945 — informar, no justificar
- La Res. Ex. SII 103/2017 la establece: "DECLARACIÓN JURADA ANUAL SOBRE INGRESOS, DESEMBOLSOS Y OTROS ANTECEDENTES DE
  LAS ORGANIZACIONES SIN FINES DE LUCRO". La Res. 94/2023 bajó el umbral: reemplazó "12.000 UF" por "4.000 UF".
- Obliga a la OSFL que reciba ingresos "por montos superiores a 4.000 UF vigente al 31 de diciembre de cada año, por
  cualquier título o concepto, tales como donaciones, diezmos, ofrendas, asignaciones, aporte de fundadores, cuota de
  asociados" (instrucciones, Anexo 2).
- Identifica por RUT a quienes aportaron los montos más altos hasta cubrir "el 80% del total de ingresos en dinero".
- La sección C informa exenciones con el documento "mediante la cual se le otorgó dicha exención".
- **Lo que la DJ 1945 no hace:** no califica el ingreso ni lo exime. Sus propias instrucciones lo dicen: "Las OSFL y
  entidades religiosas, en la medida que puedan ser afectadas con impuestos, están sujetas al mismo tratamiento
  tributario que el resto de los contribuyentes, especialmente en relación al Impuesto a la Renta e Impuesto al Valor
  Agregado." Declarar las cuotas en la DJ 1945 deja constancia ante el SII; lo que las sostiene como cuotas es el Art.
  17 N° 11 y los hechos de la sección 5.
- Con ingresos de 4.000 UF o menos la OSFL no la presenta, pero debe poder probar igual cada cuota (Arts. 17 y 200 del
  Código Tributario).

## Preguntas que el pack NO resuelve `[criterio jurídico]`
1. **¿El pago del socio al recibir cannabis es cuota de asociado o venta?** El SII aceptó cuotas variables según lo
   que recibe cada asociado (sección 5), pero en un caso distinto. Si el fiscalizador ve venta, aplican el DL 825 Art.
   2 N° 1 y N° 3. Se cruza con la pregunta 1 de `sanitario-cannabis`: una "venta" de cannabis es además una
   "transferencia a cualquier título" (Ley 20.000 Art. 4 inc. 2; DS 404 Art. 5).
2. **¿Las rentas de la OSFL pagan impuesto de primera categoría?** Sin decreto del Art. 40 N° 4, la regla general.
3. **¿Qué documento emite la OSFL por cada cuota?** Si es cuota de asociado, un comprobante de ingreso (Oficio 3616);
   si el SII la califica como venta, el documento tributario de la venta.

## Controles que exige (ver `references/controls.md`)
`trib-conservacion`, `trib-aporte-trazable`, `trib-documento`, `trib-dj1945`. Reutiliza: `osfl-contabilidad`, `osfl-sin-lucro`,
`data-minimizacion`.

## Documentos a generar
Ninguno propio: las preguntas abiertas se registran en `san-fundamento-modelo-operativo.md` (fila "Contribución
económica") y los plazos de conservación en el RAT de `ley-21719`.
