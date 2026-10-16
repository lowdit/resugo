---
title: Resugo
description: CV en ligne, galerie de profils et exports PDF.
layout: product
weight: 1
---

**Resugo** met en scène des curricula avec la coque Minigo et la vue **cv-vitrine**.

## Directement depuis GitHub (fork)

1. **Forker** [`lowdit/resugo`](https://github.com/lowdit/resugo).
2. **Settings → Pages → Source : GitHub Actions**.
3. Le workflow construit `exampleSite/` et publie la démo. Ajoutez vos profils dans `exampleSite/content/resume/`.

## En local (dépôt cloné)

```bash
git clone https://github.com/lowdit/resugo
cd resugo/exampleSite
hugo server
```

## Dans votre propre site (module Hugo)

```toml
theme = ["minigo", "resugo"]

[params.lowdit]
  siteProfile = "cv"
  view = "cv-vitrine"
```

Puis `hugo server` : vos profils se construisent depuis `content/resume/`.

## GitHub Pages (votre site)

Le workflow construit `exampleSite/` par défaut ; passez à `.` dans `.github/hugo-site-dir` si votre `content/` est à la racine.
