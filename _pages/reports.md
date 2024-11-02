---
layout: page
permalink: /reports/
title: Reports
description: IPCC and other reports.
nav: false
nav_order:
---

Total {% bibliography_count --file reports %} items.

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography --file reports %}

</div>
