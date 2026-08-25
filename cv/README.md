# CV source

LaTeX (moderncv, `classic` style), compiled with [tectonic](https://tectonic-typesetting.github.io/).
Replaces the old manually-maintained Word doc.

- `cv.tex` — everything except the publication list: career, funding,
  supervision, talks, teaching, etc. Edit this by hand.
- `generate_pubs.py` — reads `../_bibliography/papers.bib` (the same file the
  website's `/papers/` page uses) and writes `pubs_generated.tex`, grouped by
  year descending, numbered within each year, with Chris's own name bolded.
  **Do not edit `pubs_generated.tex` by hand** — it's overwritten on every
  build. Add papers via `/publish-paper` or by editing `papers.bib` directly.
- `build.sh` — runs the generator, compiles with tectonic, and copies the
  result to `../assets/pdf/ChrisSmithCV.pdf` (what the site's `cv` page
  serves).

## Rebuild

```bash
./build.sh
```

Requires `uv` (for the generator script) and `tectonic` (`brew install tectonic`).

## Known quirks

- The bold-own-name heuristic matches family name "Smith" + given name
  starting with "C" — correct for every current entry, but would falsely
  bold a hypothetical co-author "Smith, Charles" or similar. Check the diff
  after adding a paper by someone else named Smith.
- `papers.bib` has a couple of pre-existing data-quality issues found while
  building this (bad `date` fields, one swapped family/given name) that were
  fixed directly in the bib file rather than worked around here — if the
  generated CV ever looks wrong for one entry, check the bib entry itself
  before suspecting the generator.
