---
layout: page
permalink: /github/
title: github
description: A short summary of my GitHub activity.
nav: true
nav_order: 5
---

{% if site.data.repositories.github_users %}

## GitHub users

<ul class="repo-list list-unstyled">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.liquid username=user %}
  {% endfor %}
</ul>

---

{% endif %}

{% if site.data.repositories.github_repos %}

## GitHub Repositories

<ul class="repo-list list-unstyled">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.liquid repository=repo %}
  {% endfor %}
</ul>
{% endif %}

<script src="{{ '/assets/js/github_profile.js' | relative_url | bust_file_cache }}" defer></script>
