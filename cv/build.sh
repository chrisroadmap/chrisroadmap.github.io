#!/usr/bin/env bash
# Regenerate the publication list from ../_bibliography/papers.bib, compile
# cv.tex with tectonic, and drop the result where the website's cv.md
# permalink expects it.
set -euo pipefail
cd "$(dirname "$0")"

uv run generate_pubs.py
tectonic cv.tex
cp cv.pdf ../assets/pdf/ChrisSmithCV.pdf

echo "Built cv/cv.pdf and copied to assets/pdf/ChrisSmithCV.pdf"
