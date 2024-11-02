---
layout: page
title: Radiative kernels
description:
img: assets/img/project_thumbs/kernels.png
importance: 5
category: work
related_publications: false
---

Radiative kernels describe how the top of atmosphere or surface radiation changes for a small change in an atmospheric or surface state. They are commonly used in climate feedback studies, to isolate the contributions to climate feedbacks from individual processes (e.g. temperature, water vapour, surface albedo and clouds).

I have produced radiative kernels from two generations of the UK Met Office's global climate model: HadGEM3-GA7.1 (CMIP6) and HadGEM2-ES (CMIP5). In both cases the base state is a pre-industrial climatology. Kernels are provided for both the 38 or 85 native model levels in HadGEM2 and HadGEM3, and the 17 or 19 standard CMIP5/CMIP6 pressure levels respectively. Changes in top-of-atmosphere (TOA) radiative flux and surface radiative flux are provided for perturbations in atmospheric temperature of 1 K, specific humidity (change in specific humidity that preserves relative humidity for an increase in temperature of 1 K), surface (skin) temperature of 1 K and surface albedo of 1 % (absolute). For the model-level kernels the model pressure level and thickness (in pressure coordinates) of the layer is also provided.

- HadGEM3-GA7.1: [Download here](https://doi.org/10.5281/zenodo.3594672). Please cite [Smith et al. (2020)](https://essd.copernicus.org/articles/12/2157/2020/). For reasons outlined in the paper this kernel is preferable to the HadGEM2 one for use with CMIP6 model output.
- HadGEM2: [Download here](https://doi.org/10.5518/406). Please cite [Smith et al. (2018)](https://gmd.copernicus.org/articles/17/2387/2024/).


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/ta_q_kernel.png" title="HadGEM3 radiative kernels" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Top-of-atmosphere radiative kernels for temperature and specific humidity derived from the HadGEM3-GA7.1 model.
</div>