# Fuentes oficiales (corpus primario)

Objetivo: que la auditoría sea **reproducible y contrastada contra la ley vigente, nada inventado**.
Toda afirmación legal de la skill debe poder rastrearse a uno de estos archivos + el artículo.
Si algo no se puede verificar contra estos textos, se marca `[verificar contra fuente oficial]`.

> Descargado: **2026-06-20**. Re-descargable con los comandos de abajo (User-Agent de navegador).

| Archivo | Norma | idNorma | Tipo | SHA-256 (trunc.) | Fuente oficial |
|---|---|---|---|---|---|
| `ley-21719-diariooficial.pdf` | Ley 21.719 Datos Personales | 1209272 | **PDF texto COMPLETO** | `a760962c…` | Diario Oficial 13-12-2024 |
| `ley-21719-datos.xml` | Ley 21.719 (estructura) | 1209272 | XML abreviado | `4b60e4c8…` | Ley Chile (BCN) |
| `ley-21595-delitos-economicos.xml` | Ley 21.595 Delitos Económicos | 1195119 | XML | `17cac690…` | Ley Chile (BCN) |
| `ley-20393-resp-penal-pj.xml` | Ley 20.393 Resp. Penal PJ | 1008668 | XML | `35d67a14…` | Ley Chile (BCN) |
| `ley-19628-consolidada.xml` | Ley 19.628 (texto base que la 21.719 modifica) | 141599 | XML | `4b4a6d85…` | Ley Chile (BCN) |
| `clausulas-modelo-transferencia-economia.pdf/.txt` | Cláusulas Contractuales Modelo (transferencia internacional) | RAEX202503748 | **PDF + texto** | `55f78aef…` | Diario Oficial 19-12-2025 |

## Códigos que NO se versionan acá (se descargan, no se redistribuyen)

Este repo es **público**, y la licencia de redistribución del texto de Ley Chile **no está confirmada con la
BCN**. Los textos de la 21.719/21.595/20.393/19.628 vienen de arriba por decisión previa; para los códigos
—que son mucho más extensos— se optó por **no publicarlos y dejar la receta de descarga**, que es
reproducible y no redistribuye nada. Bajarlos es una línea y quedan igual de citables.

| Norma | idNorma | SHA-256 esperado (trunc.) | Sostiene |
|---|---|---|---|
| Código Tributario (DL 830) | **6374** | `5951bfb4…` | art. 17 inc. 2° + art. 200 — conservación de libros y el plazo de revisión del SII |
| Código del Trabajo (DFL 1) | **207436** | `b66efa69…` | art. 62 — libro auxiliar de remuneraciones (desde 5 trabajadores) |

```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36"
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=6374"   -o codigo-tributario-dl830.xml
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=207436" -o codigo-del-trabajo.xml
sha256sum codigo-*.xml   # deben partir con los prefijos de la tabla
```

## Notas de validez (IMPORTANTE)
- **La 21.719 MODIFICA la Ley 19.628**: el articulado sustantivo de datos (consentimiento,
  encargado, transferencias, Agencia, sanciones) entra en vigor **1-dic-2026** y se lee del **PDF del
  Diario Oficial** (`ley-21719-diariooficial.pdf`), que es el texto completo. El `ley-19628-consolidada.xml`
  aún NO integra esas modificaciones (vigencia futura) → no usarlo como operativo de la parte nueva.
- Los **XML de Ley Chile (opt=7) son ABREVIADOS** (encabezados/estructura). Para texto íntegro usar el
  PDF del Diario Oficial o el visor de BCN.
  **Excepción comprobada (14-ago-2026):** los de los dos códigos que se agregaron ahora **sí traen el texto
  íntegro** de cada artículo, verificado buscando los incisos citados abajo. Si a futuro un XML no trae el
  texto, no asumas que ninguno lo trae: revisa el archivo.
- La **21.595 ya está vigente** (modifica la 20.393; rige desde 1-sep-2024).

### Por qué están el Código Tributario y el del Trabajo (14-ago-2026)

Una **retención** de datos personales no se sostiene sola: el art. 7 romanito ii) de la 21.719 dice que no
procede la supresión cuando el tratamiento es necesario para cumplir una **obligación legal**, pero la
obligación la pone *otra* ley. Sin estos dos textos, toda negativa a suprimir datos contables o de
remuneraciones quedaba citada de memoria — y el art. 11 exige que la negativa sea **fundada**.

Los tres artículos que sostienen los plazos, **verificados palabra por palabra contra el XML de la BCN**
(descargado con la receta de abajo; el texto no se versiona en este repo público):

- **Código Tributario art. 17 inc. 2°** — *"Los libros de contabilidad deberán ser llevados en lengua
  castellana […] debiendo ser conservados por los contribuyentes, junto con la documentación
  correspondiente, mientras esté pendiente el plazo que tiene el Servicio para la revisión de las
  declaraciones."* El plazo no está acá: está en el art. 200.
- **Código Tributario art. 200** — tres años desde que expiró el plazo legal de pago; **seis** para
  impuestos sujetos a declaración *"cuando ésta no se hubiere presentado o la presentada fuere
  maliciosamente falsa"*.
- **Código del Trabajo art. 62** — *"Todo empleador con cinco o más trabajadores deberá llevar un libro
  auxiliar de remuneraciones, el que deberá ser timbrado por el Servicio de Impuestos Internos"*, y las
  remuneraciones que figuren ahí son las únicas imputables como gasto en la contabilidad.

⚠️ **Dos límites que hay que respetar al citarlos:**
1. El art. 62 aplica **desde 5 trabajadores**. Bajo ese umbral no hay obligación de llevar el libro y la
   retención se sostiene solo en el art. 17 del Tributario — que sí aplica siempre, porque el gasto por
   remuneraciones es parte de la contabilidad. Al fundar una negativa, **citar ambos**.
2. **Ninguno de los dos fija un plazo laboral de conservación en años.** El plazo que se le informa al
   titular es siempre el tributario del art. 200. No inventar uno laboral.

## Pendientes de incorporar (con URL, aún no descargados)
- **DS 662/2025** (reglamento del Modelo de Prevención de Infracciones, Min. Hacienda/Economía):
  estaba en toma de razón en Contraloría — verificar publicación en Diario Oficial.
- **Guía oficial de implementación**: https://wikiguias.digital.gob.cl/es/datos-personales/guia-datos-personales

> Cláusulas modelo de transferencia: ✅ ya descargadas
> (`clausulas-modelo-transferencia-economia.pdf`, Diario Oficial 19-12-2025).

## Cómo re-descargar (reproducibilidad)
```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36"
# Texto completo Ley 21.719 (PDF Diario Oficial)
curl -L -A "$UA" "https://www.diariooficial.interior.gob.cl/publicaciones/2024/12/13/44023/01/2583630.pdf" -o ley-21719-diariooficial.pdf
# XML estructurado (cambiar idNorma): 21719=1209272, 21595=1195119, 20393=1008668, 19628=141599
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=1209272" -o ley-21719-datos.xml
# Códigos que sostienen los plazos de conservación (traen texto íntegro)
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=6374"   -o codigo-tributario-dl830.xml
curl -L -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=207436" -o codigo-del-trabajo.xml
# Cláusulas contractuales modelo (transferencia internacional, Min. Economía)
curl -L -A "$UA" "https://www.diariooficial.interior.gob.cl/publicaciones/2025/12/19/44328/01/2742586.pdf" -o clausulas-modelo-transferencia-economia.pdf
# Verificar integridad
sha256sum *.pdf *.xml
```

## Pack sanitario-cannabis (descargado 2026-11-06, no se versiona)

Misma política que los códigos: el texto de la BCN **no se redistribuye**. Se baja a `sources/.cache/`
(ignorado por git) y se lee con `python scripts/bcn_article.py <archivo> <artículo>` o `--grep <regex>`.
Estos XML **sí traen el texto íntegro** de cada artículo (comprobado con los incisos citados en el pack).
Cada `idNorma` se verificó por el título, tipo, número y fecha del propio XML.

| Archivo en caché | Norma | idNorma | Versión del texto | SHA-256 (trunc.) |
|---|---|---|---|---|
| `ley-20000.xml` | Ley 20.000, tráfico ilícito de estupefacientes | 235507 | 2026-05-23 | `e8a44296…` |
| `ley-21575.xml` | Ley 21.575 (agrega el Art. 8 inc. 2 a la Ley 20.000) | 1192530 | 2023-05-23 | `c46cbd74…` |
| `ds-867-reglamento-ley-20000.xml` | DS 867/2007 Interior, reglamento de la Ley 20.000 | 269323 | 2023-09-16 | `530d8a96…` |
| `ds-404-estupefacientes.xml` | DS 404/1983 Salud, Reglamento de Estupefacientes | 13057 | 2020-11-19 (Art. 5) | `fc31df54…` |
| `ds-405-psicotropicos.xml` | DS 405/1983 Salud, Reglamento de Psicotrópicos | 13066 | — | `fe711b19…` |
| `decreto-84-2015.xml` | Decreto 84/2015 Salud (modifica DS 404 y 405: cannabis) | 1085003 | 2015-12-07 | `e904dafd…` |
| `decreto-8-2017.xml` | Decreto 8/2017 Salud (modifica DS 404 y 405) | 1103188 | 2017 | `846d9e47…` |
| `codigo-sanitario-dfl-725.xml` | Código Sanitario (DFL 725) | 5595 | 2025-09-29 | `08e91e88…` |
| `ley-20724.xml` | Ley 20.724 (farmacias y medicamentos; habilitó la receta electrónica) | 1058373 | — | `dcebcba1…` |
| `ley-21267.xml` | Ley 21.267 (adquisición de remedios en pandemia; Art. 101 CS) | 1149723 | — | `b5366591…` |
| `res-1143-2023.xml` | Res. Ex. 1143/2023 Salud, Sistema de Validación de Recetas Gráficas | 1195587 | 2023-09-02 | `a7c743a4…` |
| `decreto-11-2025.xml` | Decreto 11/2025 Salud (modifica el reglamento de farmacias, DS 466/1984) | 1213527 | — | `13b8d098…` |
| `ds-41-2012-fichas-clinicas.xml` | DS 41/2012 Salud, **Reglamento sobre Fichas Clínicas** | 1046753 | 2012-12-15 | `947082e9…` |

Leídos artículo por artículo para el pack: Ley 20.000 Arts. 1, 3, 4, 8, 9, 10, 11, 50; Ley 21.575 Art. 1
N° 4; DS 867 Arts. 5-14; DS 404 Arts. 5 y 23; Decreto 84/2015 Arts. 1 y 2; Código Sanitario Arts. 100 y 101.
Las otras normas de la tabla están identificadas pero **no** leídas artículo por artículo
`[verificar contra fuente oficial]` antes de citarlas.

**Pendiente:** el reglamento de receta electrónica estaba en consulta pública del MINSAL (2025) y el
proyecto de ley Boletín 17355-11 en primer trámite (abril 2025). Revisar si se publicaron.

```bash
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36"
mkdir -p sources/.cache && cd sources/.cache
# La BCN limita las consultas ("Service limit has been reached"): una cada ~20 s.
for pair in 235507:ley-20000 1192530:ley-21575 269323:ds-867-reglamento-ley-20000 13057:ds-404-estupefacientes \
            13066:ds-405-psicotropicos 1085003:decreto-84-2015 1103188:decreto-8-2017 5595:codigo-sanitario-dfl-725 \
            1058373:ley-20724 1149723:ley-21267 1195587:res-1143-2023 1213527:decreto-11-2025 \
            1046753:ds-41-2012-fichas-clinicas; do
  curl -sL -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=${pair%%:*}" -o "${pair#*:}.xml"; sleep 20
done
sha256sum *.xml   # la BCN publica versiones nuevas: un hash distinto significa que la norma cambió, releer
```

## Pack ley-20584 (descargado 2026-11-06, no se versiona)

Misma política y misma receta que el pack anterior. El DS 41/2012 ya está en la tabla de arriba.

| Archivo en caché | Norma | idNorma | Versión del texto | SHA-256 (trunc.) |
|---|---|---|---|---|
| `ley-20584.xml` | Ley 20.584, derechos y deberes de las personas en su atención de salud | 1039348 | 2026-02-16 | `4a673a22…` |

Leídos artículo por artículo para el pack: Ley 20.584 Arts. 1-6, 10, 12, 13, 14, 37 y 38; DS 41/2012
Arts. 1-12. Los montos de sanción del DFL 1/2006 Salud (al que remite el Art. 38) **no** se leyeron.

```bash
curl -sL -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=1039348" -o sources/.cache/ley-20584.xml
```

## Packs ley-20500, tributario, ley-21663 y ley-19628 (descargados 2026-11-06, no se versionan)

Misma política y receta. La Ley 19.628 ya está versionada arriba (`ley-19628-consolidada.xml`).

| Archivo en caché | Norma | idNorma | Versión del texto | SHA-256 (trunc.) |
|---|---|---|---|---|
| `constitucion.xml` | Constitución Política (texto refundido) | 242302 | 2026-04-16 | `f49fa004…` |
| `ley-20500.xml` | Ley 20.500, asociaciones y participación ciudadana | 1023143 | 2011-02-16 | `3e4c4cf2…` |
| `codigo-civil.xml` | Código Civil (Título XXXIII del Libro I) | 172986 | marca BCN `2222-02-02` (versión diferida; artículos leídos en versión 2011-02-16) | `979bb1e1…` |
| `codigo-tributario-dl830.xml` | Código Tributario (DL 830) | 6374 | 2026-10-17 | `65690ff2…` |
| `dl-825-iva.xml` | DL 825, Impuesto a las Ventas y Servicios | 6369 | 2026-02-05 | `18b43c10…` |
| `dl-824-renta.xml` | DL 824, Impuesto a la Renta | 6368 | 2026-10-17 | `c0fd6276…` |
| `ley-21663.xml` | Ley 21.663, Ley Marco de Ciberseguridad | 1202434 | 2024-04-08 | `2302f990…` |

Leídos artículo por artículo: Constitución Art. 19 N° 1, 9, 15 y 21; Ley 20.500 Arts. 1-11, 15 y 16; Código Civil
Arts. 545, 548 a 548-4, 549, 550, 551 a 551-2, 556, 557 a 557-3, 558 y 559; Código Tributario Arts. 17 y 200; DL 825
Art. 2; DL 824 Art. 40; Ley 21.663 Arts. 1, 4-9; Ley 19.628 Arts. 2, 4, 7, 10, 11, 12 y 16. **No leídos:** artículos
transitorios de la Ley 21.663 (vigencia escalonada). Los documentos del SII están en la sección siguiente.

**Ojo con `constitucion.xml`:** el texto viene intercalado con anotaciones de margen ("CPR Art. 19° N° 9",
"D.O. 24.10.1980") en medio de las frases. Para verificar una cita, quitar esas anotaciones antes de comparar.

```bash
for pair in 242302:constitucion 1023143:ley-20500 172986:codigo-civil 6374:codigo-tributario-dl830             6369:dl-825-iva 6368:dl-824-renta 1202434:ley-21663; do
  curl -sL -A "$UA" "https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=${pair%%:*}" -o "sources/.cache/${pair#*:}.xml"; sleep 20
done
```

## Documentos del SII (descargados 2026-11-06, no se versionan)

Fuente: sii.cl. Se guardan en `sources/.cache/sii/`, con el texto extraído en un `.txt` del mismo nombre (el que lee
`scripts/verify_quotes.py`).

| Archivo en caché | Documento | URL | SHA-256 (trunc.) |
|---|---|---|---|
| `reso94-2023.pdf` | Res. Ex. SII 94/2023, modifica la Res. 103/2017 (DJ 1945; umbral 4.000 UF) | https://www.sii.cl/normativa_legislacion/resoluciones/2023/reso94.pdf | `d855f56a…` |
| `dj1945-instrucciones-2023.pdf` | Anexo 2 de la Res. 94/2023: formulario e instrucciones de la DJ 1945 | https://www.sii.cl/normativa_legislacion/resoluciones/2023/reso94_anexo2.pdf | `76e7c457…` |
| `oficio-2419-2013.htm` | Oficio 2419/2013: cuotas de asociados fijas o variables; Renta e IVA | https://www.sii.cl/pagina/jurisprudencia/adminis/2013/renta/ja2419.htm | `1dfe7603…` |
| `oficio-3616-2002.htm` | Oficio 3616/2002: cuotas sociales sin IVA; comprobante de ingreso | https://www.sii.cl/pagina/jurisprudencia/adminis/2002/ventas/ja372.htm | `d1241ed4…` |
| `ordinario-678-2009.pdf` | Ord. 678/2009 (DR Santiago Oriente): aportes de socios e IVA | https://www.sii.cl/documentos/normativa_ddrr/2009/oriente/ordinario678.pdf | `0d1f6016…` |

Los oficios responden consultas concretas y no obligan frente a hechos distintos. No leído: el DS 110/1979 (reglamento
de personas jurídicas) que cita el Oficio 2419 `[verificar vigencia]`.

```bash
mkdir -p sources/.cache/sii && cd sources/.cache/sii
curl -sL -A "$UA" -o reso94-2023.pdf https://www.sii.cl/normativa_legislacion/resoluciones/2023/reso94.pdf
curl -sL -A "$UA" -o dj1945-instrucciones-2023.pdf https://www.sii.cl/normativa_legislacion/resoluciones/2023/reso94_anexo2.pdf
curl -sL -A "$UA" -o oficio-2419-2013.htm https://www.sii.cl/pagina/jurisprudencia/adminis/2013/renta/ja2419.htm
curl -sL -A "$UA" -o oficio-3616-2002.htm https://www.sii.cl/pagina/jurisprudencia/adminis/2002/ventas/ja372.htm
curl -sL -A "$UA" -o ordinario-678-2009.pdf https://www.sii.cl/documentos/normativa_ddrr/2009/oriente/ordinario678.pdf
# texto: PDF con pypdf; HTML del SII viene en cp1252
python -I -c "import pathlib,re,html,pypdf
for f in pathlib.Path('.').iterdir():
    if f.suffix=='.pdf': t='
'.join(p.extract_text() for p in pypdf.PdfReader(f).pages)
    elif f.suffix=='.htm': t=html.unescape(re.sub(r'<[^>]+>',' ',f.read_bytes().decode('cp1252')))
    else: continue
    f.with_suffix('.txt').write_text(t,encoding='utf-8')"
```

## Verificar todas las citas

`python -I scripts/verify_quotes.py` busca cada cita de 20 o más caracteres de `packs/**/*.md` en los textos de
`sources/` y `sources/.cache/` (BCN y SII) y termina con código 1 si alguna no aparece. Los textos entre comillas que
no son citas legales (nombres de sección, etiquetas sugeridas) van en `scripts/quote-allowlist.txt`. Correrlo después
de editar un pack y cada vez que se re-descarguen las fuentes.

## Regla de uso para la skill
1. Antes de afirmar algo legal, búscalo en estos archivos (PDF completo > XML).
2. Cita siempre **ley + artículo + archivo fuente**.
3. Si no está en el corpus o no es verificable, dilo: `[verificar contra fuente oficial / abogado]`.
4. Nunca uses un blog/fuente secundaria como base de una afirmación normativa en el output final.
