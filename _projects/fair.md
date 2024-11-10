---
layout: page
title: fair model
description: The Finite Amplitude Impulse Response reduced-complexity climate model
img: assets/img/project_thumbs/fair.jpg
importance: 3
category: work
related_publications: false
---

[![image](https://github.com/OMS-NetZero/FAIR/actions/workflows/checks.yml/badge.svg)](https://github.com/OMS-NetZero/FAIR/actions)
[![image](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/OMS-NetZero/FAIR/master?filepath=examples/basic_run_example.ipynb)
[![Documentation Status](https://readthedocs.org/projects/fair/badge/?version=latest)](http://fair.readthedocs.io/en/latest/?badge=latest)
[![image](https://zenodo.org/badge/DOI/10.5281/zenodo.1340643.svg)](https://doi.org/10.5281/zenodo.1340643)
[![image](https://codecov.io/gh/OMS-NetZero/FAIR/branch/master/graph/badge.svg)](https://codecov.io/gh/OMS-NetZero/FAIR)
[![image](https://img.shields.io/pypi/v/fair)](https://pypi.org/project/fair/) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/fair/badges/version.svg)](https://anaconda.org/conda-forge/fair)

The **fair** model is a reduced-complexity climate model designed to produce probabilistic projections of global mean
surface temperature (and other variables) given input emissions, greenhouse gas concentrations or radiative forcing, in
a fraction of a second.

**fair** includes simplified representations of the uptake of emitted CO<sub>2</sub>, methane atmospheric chemistry,
aerosols, ozone and land use change based on simplified relationships calibrated on Earth System Models.

 **fair** is written in python and can be obtained through `conda-forge`, `pip`, or installed [from source](). See the
[installation](https://docs.fairmodel.net/en/stable/install.html) notes in the 
[documentation](https://docs.fairmodel.net).

You can also run a
[very simple example](https://mybinder.org/v2/gh/OMS-NetZero/FAIR/master?filepath=examples/basic_run_example.ipynb) interactively using Binder.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/ssp_inverse.png" title="Projections of future global mean surface temperature using fair" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Projections of future global mean surface temperature from the CMIP6 SSP-RCP scenarios using fair.
</div>

## What's in a name?

The model I call <b>fair</b> is variously spelt FAIR and FaIR. The full name of the model is the Finite Amplitude 
Impulse Response (model). The first iteration was all-caps FAIR. We were made aware of a name clash with 
<a href="https://link.springer.com/article/10.1007/s10666-005-4647-z">another model called FAIR</a> in an overlapping
scientific field. Therefore we changed the official acronym to FaIR and modified the full name (now "Finite-amplitude"...).

However. It can't only be me that thinks the small "a" looks fugly, and there's no good reason why "amplitude" is any
less important than any other word. Therefore, I now prefer to call the model all-lowercase <b>fair</b>.
Distinction from the other FAIR is maintained, and the lowercase form is how it is known within the python ecosystem.
Practically, all three variants are in use and acceptable, and I've even seen it spelt Fair.

<!-- see {% cite leach_fair_2021 smith_fair_2018 %} -->
