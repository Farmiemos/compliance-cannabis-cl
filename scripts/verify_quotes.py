#!/usr/bin/env python3
"""Check that every quoted passage in the packs appears verbatim in an official source.

Sources are the BCN XML files and the SII documents downloaded with the recipes in sources/FUENTES.md
(sources/*.xml, sources/*.txt, sources/.cache/*.xml, sources/.cache/sii/*.txt). They are not redistributed, so
download them first.

A quote is any text of 20+ characters between straight double quotes in a pack.md. "[...]" splits a quote into
parts that must each appear. Quotes that are not legal citations (document names, suggested labels) go in
scripts/quote-allowlist.txt, one per line.

Usage: python -I scripts/verify_quotes.py [packs/<id>/pack.md ...]   (default: every .md under packs/)
Exit code 1 when a quote is not found or a source is missing.
"""
from __future__ import annotations

import html
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE_GLOBS = ["sources/*.xml", "sources/*.txt", "sources/.cache/*.xml", "sources/.cache/sii/*.txt"]
# The BCN XML of the Constitution interleaves margin notes inside sentences and splits words ("fís ica"),
# so a quote that fails the normal match is retried with notes and all whitespace removed.
MARGIN_NOTES = re.compile(
    r"CPR Art\. ?\d+° ?(N° ?\d+°?)?|D\.O\.( ?\d{2}\.\d{2}\.\d{4})?|\d{2}\.\d{2}\.\d{4}"
    r"|LEY N° ?[\d.]+ Art\. ?único N° ?\d+"
)


def norm(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


def load_corpus() -> tuple[str, str, str]:
    chunks = []
    for pattern in SOURCE_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            raw = path.read_bytes().decode("utf-8", errors="replace")
            if path.suffix == ".xml":
                raw = re.sub(r"<[^>]+>", " ", html.unescape(raw))
            chunks.append(raw)
    corpus = norm(" ".join(chunks))
    clean = norm(MARGIN_NOTES.sub(" ", corpus))
    return corpus, clean, re.sub(r"\s", "", clean)


def quotes_in(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)  # blockquote markers
    text = re.sub(r"`[^`\n]*`", "", text)  # code spans never hold legal text
    # Pair every quote first, then filter by length: a short quote must not leave its closing mark to open the next.
    return [norm(q) for q in re.findall(r'"([^"]*)"', norm(text)) if len(q) >= 20]


def main(argv: list[str]) -> int:
    corpus, clean, compact = load_corpus()
    if len(corpus) < 100_000:
        print("Sources missing: download them with the recipes in sources/FUENTES.md.")
        return 1
    allow_file = ROOT / "scripts" / "quote-allowlist.txt"
    allow = {norm(line) for line in allow_file.read_text(encoding="utf-8").splitlines() if line.strip()} if allow_file.exists() else set()
    packs = [pathlib.Path(a).resolve() for a in argv] or sorted(ROOT.glob("packs/**/*.md"))
    missing = 0
    for pack in packs:
        found = 0
        for quote in quotes_in(pack):
            if quote in allow:
                continue
            parts = [p.strip(" ,.;:") for p in quote.split("[...]") if p.strip(" ,.;:")]
            if all(p in corpus or p in clean or re.sub(r"\s", "", p) in compact for p in parts):
                found += 1
            else:
                missing += 1
                print(f"NOT FOUND  {pack.relative_to(ROOT)}: \"{quote[:140]}\"")
        print(f"{pack.relative_to(ROOT)}: {found} quotes verified")
    print("OK" if missing == 0 else f"{missing} quote(s) not found in the official sources")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
