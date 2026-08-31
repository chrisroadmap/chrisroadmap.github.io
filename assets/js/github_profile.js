// Enhances .repo-list-item[data-github-user] with a live snapshot from the
// public GitHub API (avatar, name, public repo/follower counts). Falls back
// to the static "GitHub profile" link already in the markup if the fetch
// fails or is rate-limited.
(function () {
  const CACHE_TTL_MS = 60 * 60 * 1000;

  function renderProfile(item, data) {
    const avatar = item.querySelector("[data-gh-avatar]");
    const fallbackIcon = item.querySelector("[data-gh-fallback-icon]");
    const meta = item.querySelector("[data-gh-meta]");
    const name = item.querySelector(".repo-name");

    if (avatar && data.avatar_url) {
      avatar.src = data.avatar_url;
      avatar.hidden = false;
      if (fallbackIcon) fallbackIcon.hidden = true;
    }
    if (name && data.name) {
      name.textContent = data.name;
    }
    if (meta) {
      const parts = [];
      if (typeof data.public_repos === "number") parts.push(`${data.public_repos} repos`);
      if (typeof data.followers === "number") parts.push(`${data.followers} followers`);
      if (parts.length) meta.textContent = parts.join(" · ");
    }
  }

  async function loadProfile(item) {
    const username = item.dataset.githubUser;
    if (!username) return;

    const cacheKey = `gh-profile:${username}`;
    try {
      const cached = JSON.parse(sessionStorage.getItem(cacheKey));
      if (cached && Date.now() - cached.fetchedAt < CACHE_TTL_MS) {
        renderProfile(item, cached.data);
        return;
      }
    } catch (e) {
      // ignore malformed cache entries
    }

    try {
      const response = await fetch(`https://api.github.com/users/${username}`);
      if (!response.ok) return;
      const data = await response.json();
      renderProfile(item, data);
      try {
        sessionStorage.setItem(cacheKey, JSON.stringify({ fetchedAt: Date.now(), data }));
      } catch (e) {
        // storage full or unavailable; not critical
      }
    } catch (e) {
      // network error or rate limit; keep the static fallback markup
    }
  }

  document.querySelectorAll(".repo-list-item[data-github-user]").forEach(loadProfile);
})();
