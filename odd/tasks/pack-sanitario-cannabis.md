# Cannabis compliance for Chile: packs on top of compliance-cl

Objective: a repo derived from Lelemon-studio/compliance-cl (MIT) that covers every legal framework needed to operate with medical cannabis in Chile, starting with the sanitary pack, verified against official BCN texts.
Branch: `feat/pack-sanitario-cannabis` (from upstream `4972a82`). Delivery: one commit per pack, no push (publishing is the owner's decision). Checks: structural readback; every legal claim cites norm + article + source file, verified against the downloaded BCN text.

## Specs
- S1 Repository. The user asked (verbatim): "quiero generar un repo como https://github.com/Lelemon-studio/compliance-cl/ pero que incluya todo el compliance para trabajar con cannabis en chile." Local clone of the upstream skill, upstream kept as remote `upstream`, MIT attribution preserved. Assumption: path `Desktop/web/compliance-cannabis-cl`, name to be confirmed by the owner.
- S2 Sanitary pack. The user asked (verbatim): "empieza armar el pack". Pack `sanitario-cannabis`: obligations, controls and templates for Ley 20.000, its regulation, Código Sanitario, DS 404/405 as amended by Decreto 84/2015, and electronic prescription, each article quoted from the official text. Unverifiable items are marked `[verificar contra fuente oficial]`.
- S3 Sources policy (inherited from upstream `4972a82`): BCN texts are not redistributed; `sources/FUENTES.md` keeps idNorma, SHA-256 prefix and the download recipe; the local cache lives in the git-ignored `sources/.cache/`.
- S4 Roadmap packs (not in this delivery): `ley-20584`, `ley-20500`, `ley-21663`, `tributario`, `ley-19628` (transitional).

## Tasks
- T1 (S1, S3) clone + gitignore + feature doc — inline — done
- T2 (S2) identify and download the official sanitary texts, record idNorma and SHA-256 — inline — done (13 norms identified by title, type, number and date of the XML itself)
- T3 (S2) `packs/sanitario-cannabis/pack.md` + 10 `san-*` controls in `references/controls.md` + 4 templates — inline — done (28 legal quotes found verbatim in the official XML; 9 non-legal false positives)
- T4 (S2) SKILL.md (renamed `compliance-cannabis-cl`), README, NOTICE and FUENTES.md — inline — done

## Log
- L1 2026-11-06 user request (verbatim): "empieza armar el pack, quiero generar un repo como https://github.com/Lelemon-studio/compliance-cl/ pero que incluya todo el compliance para trabajar con cannabis en chile."
- L2 2026-11-06 BCN rate-limits `obtxml` ("Service limit has been reached"); fetches are retried with 20 s spacing.
- L3 2026-11-06 findings: (a) Decreto 41/2012 MINSAL is the "Reglamento sobre Fichas Clínicas", not an electronic-prescription rule (FARMIEMOS `matriz-normativa.md:33` says otherwise); (b) Ley 20.000 Art. 8 inc. 2 (added by Ley 21.575, 2023) fixes the five prescription requirements, including "no podrá ser mediante combustión"; (c) DS 404 Art. 5 (version 2020-11-19) prohibits "transferencia a cualquier título, expendio, posesión y tenencia" of cannabis outside ISP authorizations, and Ley 20.000 Art. 4 inc. 2 punishes transferring "a cualquier título" for another's use: the pack records the OSFL delivery model as an open legal question and never resolves it; (d) no dedicated electronic-prescription law exists; a MINSAL regulation was in public consultation and Boletín 17355-11 was in first stage (April 2025).
- L4 2026-11-06 next: pack `ley-20584` (resolves the "ficha clínica" naming question raised in FARMIEMOS), then `ley-20500`, `tributario`, `ley-21663`, `ley-19628`. Repo name and GitHub publication are the owner's decision.
