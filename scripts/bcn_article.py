"""Print the text of articles from a Ley Chile (BCN) XML, to verify citations against the official text.

Usage: python scripts/bcn_article.py <file.xml> <article> [<article> ...]
       python scripts/bcn_article.py <file.xml> --grep <regex>

<article> matches the start of the article text ("8", "4", "40 bis"). The XML is the one downloaded by the
recipe in sources/FUENTES.md; nothing here is redistributed.
"""
import html
import re
import sys
import xml.etree.ElementTree as ET


def strip_ns(tag: str) -> str:
    return tag.split("}", 1)[-1]


def articles(path: str):
    root = ET.parse(path).getroot()
    for el in root.iter():
        if strip_ns(el.tag) != "EstructuraFuncional":
            continue
        if not el.get("tipoParte", "").startswith("Art"):
            continue
        texto = next((c for c in el if strip_ns(c.tag) == "Texto"), None)
        if texto is None or not (texto.text or "").strip():
            continue
        text = html.unescape(texto.text).replace("\r", "")
        yield el.get("fechaVersion", ""), text.strip()


def main() -> None:
    path, args = sys.argv[1], sys.argv[2:]
    items = list(articles(path))
    if args[:1] == ["--grep"]:
        rx = re.compile(args[1], re.I)
        for version, text in items:
            if rx.search(text):
                print(f"--- (version {version})\n{text[:1200]}\n")
        return
    for wanted in args:
        rx = re.compile(rf"^\s*(Art[íi]culo|ART[ÍI]CULO|Art\.)\s*{re.escape(wanted)}(?![0-9])(?!\s*bis)(?!\s*ter)", re.I)
        if " " in wanted:  # "40 bis" must match itself, not be excluded by the lookaheads above
            rx = re.compile(rf"^\s*(Art[íi]culo|ART[ÍI]CULO|Art\.)\s*{re.escape(wanted)}", re.I)
        hits = [(v, t) for v, t in items if rx.search(t)]
        if not hits:
            print(f"=== Article {wanted}: NOT FOUND in {path}\n")
        for version, text in hits:
            print(f"=== Article {wanted} (version {version})\n{text}\n")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
