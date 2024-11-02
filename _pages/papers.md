---
layout: page
permalink: /papers/
title: Papers
description: Peer-reviewed, published journal articles.
nav: false
nav_order:
---

Total {% bibliography_count --file papers %} items.

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

<div class="publications">

{% bibliography --file papers %}

</div>
