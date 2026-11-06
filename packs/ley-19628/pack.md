# Pack: Ley 19.628 — protección de la vida privada (transitorio, hasta el 1-dic-2026)

> **Rige hoy** y deja de regir en su texto actual cuando entra en vigencia la Ley 21.719 (1 de diciembre de
> 2026, ver `packs/ley-21719/pack.md`). Úsalo para lo que pase **antes** de esa fecha: el pack `ley-21719`
> prepara el cumplimiento futuro, este dice qué se exige ahora. Citas verificadas contra
> `sources/ley-19628-consolidada.xml` (versión BCN 2022-11-10). Lo no verificado lleva
> `[verificar contra fuente oficial]`.

## Lo que dice la ley (citas textuales)

### 1. La salud es dato sensible — Art. 2 letra g)
"Datos sensibles, aquellos datos personales que se refieren a las características físicas o morales de las
personas o a hechos o circunstancias de su vida privada o intimidad, tales como [...] los estados de salud
físicos o psíquicos". Diagnóstico, receta, tratamiento y dosis de cannabis medicinal son datos sensibles.

### 2. Base para tratar datos sensibles — Art. 10
"No pueden ser objeto de tratamiento los datos sensibles, salvo cuando la ley lo autorice, exista
consentimiento del titular o sean datos necesarios para la determinación u otorgamiento de beneficios de salud
que correspondan a sus titulares."

### 3. Consentimiento escrito e informado — Art. 4
- "El tratamiento de los datos personales sólo puede efectuarse cuando esta ley u otras disposiciones legales lo
  autoricen o el titular consienta expresamente en ello."
- "La persona que autoriza debe ser debidamente informada respecto del propósito del almacenamiento de sus datos
  personales y su posible comunicación al público. La autorización debe constar por escrito."
- La autorización "puede ser revocada, aunque sin efecto retroactivo".
- Inciso final: no requiere autorización el tratamiento que "realicen personas jurídicas privadas para el uso
  exclusivo suyo, de sus asociados y de las entidades a que están afiliadas, con fines estadísticos, de
  tarificación u otros de beneficio general de aquéllos". **No sirve para datos de salud:** el Art. 10 es la
  regla especial de los datos sensibles y no contiene esa excepción `[criterio jurídico]`.

### 4. Secreto y diligencia — Arts. 7 y 11
- Art. 7: quienes trabajan en el tratamiento "están obligadas a guardar secreto sobre los mismos [...] obligación
  que no cesa por haber terminado sus actividades en ese campo".
- Art. 11: el responsable "deberá cuidar de ellos con la debida diligencia, haciéndose responsable de los daños".

### 5. Derechos del titular y plazo — Arts. 12 y 16
- Art. 12: información sobre sus datos, "su procedencia y destinatario, el propósito del almacenamiento"; y
  modificación, eliminación o bloqueo en los casos que indica.
- Art. 16: si el responsable "no se pronunciare sobre la solicitud del requirente dentro de dos días hábiles", el
  titular puede recurrir al juez de letras en lo civil. **Hoy el plazo es de dos días hábiles**, no los 30 días
  de la Ley 21.719.

## Controles que exige (ver `references/controls.md`)
`t19628-base-sensible`, `t19628-plazo-derechos`. Reutiliza: `data-licitud`, `data-consent-text`,
`data-derechos`, `data-rights-channel`, `sec-rest`, `sec-logs`, `gov-politicas`.

## Documentos a generar
Ninguno propio: los documentos de `ley-21719` (política, consentimiento, canal de derechos) cubren esta ley si
dicen el plazo vigente de dos días hábiles hasta el 1-dic-2026.
