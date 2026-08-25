# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Generate cv/pubs_generated.tex from ../_bibliography/papers.bib.

Single source of truth: the website's papers.bib. Groups entries by year
(descending), numbers within each year (restarting at 1), formats author
lists as "Lastname Initials" with Chris's own name bolded, and escapes
LaTeX special characters. Run this, then `tectonic cv.tex`, whenever
papers.bib changes.

This intentionally does NOT use biblatex: the bold-own-name / hyphenated-
initials / per-year-restart formatting this CV uses is easier to get right
and keep readable in a small Python script than in a biblatex .bbx driver.
"""
import re
import sys
from pathlib import Path

BIB_PATH = Path(__file__).parent.parent / "_bibliography" / "papers.bib"
OUT_PATH = Path(__file__).parent / "pubs_generated.tex"
COUNT_PATH = Path(__file__).parent / "pub_count.tex"


def find_entries(text):
    entries = []
    for m in re.finditer(r"@article\{([^,]+),", text):
        key = m.group(1).strip()
        start = m.end()
        depth = 1
        i = start
        while depth > 0 and i < len(text):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        entries.append((key, text[start : i - 1]))
    return entries


def parse_fields(body):
    fields = {}
    i = 0
    n = len(body)
    while i < n:
        m = re.match(r"\s*,?\s*([A-Za-z][A-Za-z0-9_]*)\s*=\s*", body[i:])
        if not m:
            i += 1
            continue
        name = m.group(1).lower()
        i += m.end()
        if i < n and body[i] == "{":
            depth = 1
            j = i + 1
            while depth > 0 and j < n:
                if body[j] == "{":
                    depth += 1
                elif body[j] == "}":
                    depth -= 1
                j += 1
            fields[name] = body[i + 1 : j - 1]
            i = j
        else:
            m2 = re.match(r"[^,]*", body[i:])
            fields[name] = m2.group(0).strip()
            i += m2.end()
    return fields


def strip_braces(s):
    return s.replace("{", "").replace("}", "")


def latex_escape(s):
    s = strip_braces(s)
    # papers.bib is pre-escaped for jekyll-scholar's own `latex` filter in a
    # couple of entries (e.g. "Communications Earth \& Environment") --
    # normalise back to plain characters before re-escaping, or these come
    # out double-escaped ("\\&").
    for esc, plain in {r"\&": "&", r"\%": "%", r"\_": "_", r"\#": "#"}.items():
        s = s.replace(esc, plain)
    # normalise unusual space characters (thin/narrow/non-breaking space) that
    # the default Latin Modern Sans font can't glyph-render
    for space_char in (" ", " ", " ", " ", " "):
        s = s.replace(space_char, " ")
    repl = {
        "&": r"\&",
        "%": r"\%",
        "_": r"\_",
        "#": r"\#",
        "–": "--",
        "—": "---",
        "‘": "'",
        "’": "'",
        "“": "``",
        "”": "''",
    }
    for a, b in repl.items():
        s = s.replace(a, b)
    return s


def format_initials(given):
    given = strip_braces(given).strip()
    parts = re.split(r"\s+", given)
    out = []
    for p in parts:
        p = p.replace(".", "")
        if "-" in p:
            out.append("-".join(seg[0].upper() for seg in p.split("-") if seg))
        elif p:
            out.append(p[0].upper())
    return "".join(out)


def is_chris(family, given):
    return family.strip().lower() == "smith" and format_initials(given).startswith("C")


def format_authors(author_field):
    names = [a.strip() for a in strip_braces(author_field).split(" and ")]
    out = []
    for name in names:
        if "," in name:
            family, given = name.split(",", 1)
        else:
            bits = name.rsplit(" ", 1)
            given, family = (bits[0], bits[1]) if len(bits) == 2 else ("", name)
        family = family.strip()
        initials = format_initials(given)
        rendered = f"{latex_escape(family)} {initials}".strip()
        if is_chris(family, given):
            rendered = r"\textbf{" + rendered + "}"
        out.append(rendered)
    return ", ".join(out)


def format_entry(f):
    authors = format_authors(f.get("author", ""))
    year = strip_braces(f.get("year", ""))
    title = latex_escape(f.get("title", ""))
    journal = latex_escape(f.get("journal", ""))
    volume = strip_braces(f.get("volume", ""))
    number = strip_braces(f.get("number", ""))
    pages = latex_escape(f.get("pages", ""))
    doi = strip_braces(f.get("doi", ""))

    vol_issue = volume
    if number:
        vol_issue += f"({number})"

    bits = [f"{authors}, {year}.", f"{title}."]
    journal_bit = journal
    if vol_issue:
        journal_bit += f", {vol_issue}"
    if pages:
        journal_bit += f", {pages}"
    bits.append(journal_bit + ".")
    if doi:
        bits.append(r"\doilink{" + doi + "}")
    return " ".join(bits)


def main():
    text = BIB_PATH.read_text(encoding="utf-8")
    entries = find_entries(text)
    by_year = {}
    for key, body in entries:
        f = parse_fields(body)
        year = strip_braces(f.get("year", "0000"))
        date = strip_braces(f.get("date", "")) or f"{year}-01-01"
        by_year.setdefault(year, []).append((date, f))

    out = []
    for year in sorted(by_year, reverse=True):
        items = sorted(by_year[year], key=lambda t: t[0], reverse=True)
        out.append(f"\\cvsubsection{{{year}}}")
        out.append("\\begin{enumerate}")
        for _, f in items:
            out.append(f"\\item {format_entry(f)}")
        out.append("\\end{enumerate}")
        out.append("")

    OUT_PATH.write_text("\n".join(out), encoding="utf-8")
    total = sum(len(v) for v in by_year.values())
    COUNT_PATH.write_text(f"\\newcommand{{\\pubcount}}{{{total}}}\n", encoding="utf-8")
    print(f"Wrote {total} entries across {len(by_year)} years to {OUT_PATH}")


if __name__ == "__main__":
    sys.exit(main())
