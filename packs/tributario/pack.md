# Pack: Tributario — la OSFL frente al SII (Código Tributario, IVA y Renta)

> Ya vigente. Aplica a la OSFL que recibe aportes de sus socios y al software que registra esos movimientos.
> Citas verificadas contra el XML oficial de Ley Chile (BCN) descargado el **2026-11-06** (`sources/FUENTES.md`,
> sección "Pack tributario"). Lo no verificado lleva `[verificar contra fuente oficial]`; lo que exige
> interpretación lleva `[criterio jurídico]`. El SII interpreta estas normas por circulares y oficios que este
> pack **no** leyó: antes de decidir, buscar el pronunciamiento del SII aplicable `[verificar contra fuente oficial]`.

## Qué normas cubre

| Norma | Qué regula para este pack | Archivo de caché |
|---|---|---|
| **Código Tributario** (DL 830) | Conservación de libros y documentos; plazos de revisión del SII | `codigo-tributario-dl830.xml` |
| **Ley sobre Impuesto a las Ventas y Servicios** (DL 825) | Qué es "venta" y quién es "vendedor" | `dl-825-iva.xml` |
| **Ley sobre Impuesto a la Renta** (DL 824) | Exención de primera categoría para instituciones de beneficencia | `dl-824-renta.xml` |
| Código Civil Arts. 556 y 557-1 | Aportes, prohibición de repartir excedentes, contabilidad | `codigo-civil.xml` (ver `packs/ley-20500/`) |

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
  como venta. Lo que lo distingue es el hecho, no la etiqueta: una cuota social fijada por la asamblea (CC Art. 556),
  igual para todos y no ligada a la cantidad recibida, se parece a un aporte; un monto por gramo entregado se parece a
  un precio.

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

## Preguntas que el pack NO resuelve `[criterio jurídico]`
1. **¿El pago del socio al recibir cannabis está afecto a IVA?** Depende de si es venta (DL 825 Art. 2 N° 1) y de si la
   OSFL es vendedor habitual (N° 3). Se cruza con la pregunta 1 de `sanitario-cannabis`: una "venta" de cannabis es
   además una "transferencia a cualquier título" (Ley 20.000 Art. 4 inc. 2; DS 404 Art. 5).
2. **¿Las rentas de la OSFL pagan impuesto de primera categoría?** Sin decreto del Art. 40 N° 4, la regla general.
3. **¿Qué documento tributario emite la OSFL por cada aporte?** Depende de las dos anteriores.

## Controles que exige (ver `references/controls.md`)
`trib-conservacion`, `trib-aporte-trazable`, `trib-documento`. Reutiliza: `osfl-contabilidad`, `osfl-sin-lucro`,
`data-minimizacion`.

## Documentos a generar
Ninguno propio: las preguntas abiertas se registran en `san-fundamento-modelo-operativo.md` (fila "Contribución
económica") y los plazos de conservación en el RAT de `ley-21719`.
