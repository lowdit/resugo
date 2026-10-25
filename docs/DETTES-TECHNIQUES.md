# Dettes techniques — Resugo

État constaté le 2026-10-21, complété le 2026-10-23. Ces points sont des
**suspects à corriger**, pas des fonctionnalités validées.

## Corrigés dans cet incrément

- [x] `theme.toml` déclarait `name = "repogo"` et une description d'export PDF
  (copier-coller depuis Repogo). Corrigé en `Resugo`, description CV/curricula.
- [x] La galerie CV dépendait de `catalog/visual-art.html`,
  `catalog/card-visual.html` et `catalog/styles.html`, livrés uniquement par
  Minigo. Elle est désormais autonome : `resume/gallery-art.html`,
  `resume/gallery-card.html`, `resume/gallery-list.html` et
  `assets/css/components/resume-gallery.css` (inliné par
  `resume/gallery-styles.html`).
- [x] Clé i18n `resume-gallery-heading` absente : ajoutée en FR et EN.
- [x] Les shortcodes `diagramme-ia` et `frise-competences` vivaient dans le site
  `bertrandkeller.github.io` alors qu'ils ne font qu'appeler les partials
  Resugo. Déplacés dans `layouts/_shortcodes/`.
- [x] Contrastes de la galerie : `.resume-gallery-card__sub` était à `opacity:
  0.65` (échec Lighthouse AA). Passé à `0.8`.
- [x] Contrastes des diagrammes IA : `#b4552d` sur crème (4,2:1), `#f0a882` sur
  bleu (4,36:1) et `#7a6a5c` sur crème (4,44:1) échouaient AA. Remplacés par
  `#a34722`, `#f7c3a6` et `#746454`.
- [x] Cibles tactiles du panneau d'impression : les radios faisaient moins de
  24 × 24 px. `inline-size`/`block-size: 1.5rem` et libellé à `min-height: 1.5rem`.
- [x] **CV étroit (320/390 px).** `main.html` passe la feuille en flux vertical,
  réduit le bandeau et empile `.focus`, `.skill-grid` et les principes `why`.
  Le diagramme IA passe en étapes verticales et ne déborde plus (flex `0 0 auto`
  en colonne). Le sélecteur mobile cible bien `.section .focus` pour battre la
  règle imbriquée desktop.
- [x] **Aperçu A4 Repogo/Paged.js.** Le document ne déborde plus : le défilement
  horizontal est confiné à `.pagedjs_pages`, la page reste à 210 mm et les liens
  du sommaire gardent une cible de 24 px à l'écran. Impression A4 inchangée.
- [x] **`lowdit/social-meta.html` dépendait de Minigo.** Le blog (Higo) échouait
  au rendu des CV avec `partial "lowdit/social-meta.html" not found`. Resugo
  fournit désormais sa copie autonome dans
  `layouts/_partials/lowdit/social-meta.html`.
- [x] **Contrôle responsive reproductible.** `bin/serve-hugo test responsive`
  démarre un serveur par cible et vérifie à 320/390 px : débordement du document,
  cadres CV et pages Paged.js. Cibles dans `bin/serve-hugo.responsive`, captures
  dans `.cache/responsive/`.
- [x] **Higo 0.9.1.** Le blog passe de `v0.8.6` à `v0.9.1` : `render-image.html`
  ne casse plus sur un SVG (`.Height`). `go.mod` et `_vendor/` alignés ; penser à
  `hugo mod vendor` après chaque modification de thème local.

## Dettes restantes à arbitrer

- [ ] **Coque Minigo encore implicite.** `layouts/_default/baseof.html` appelle
  `lowdit/design-system.html`, `lowdit/favicon.html`, `lowdit/diagrams.html` et
  `lowdit/logo.html`, fournis par Minigo. Le blog n'est pas concerné (il utilise
  le `baseof` de Higo), mais Resugo seul ne peut pas rendre une page de thème.
  `social-meta` a été rapatrié ; décider pour le reste : documenter Minigo comme
  coque officielle, soit rapatrier ces partials.
- [ ] **Decks Sligo sur écran étroit.** Le canvas Reveal 16:9 n'est pas reflowé :
  le document ne déborde pas, mais du contenu peut être coupé en bas de slide.
  Arbitrage à rendre : canvas 16:9 avec zoom/scroll, ou reflow mobile avec
  défilement vertical interne. Ne pas ajouter de test de découpe avant cet
  arbitrage.
- [ ] **Doublon `assets/` / `static/assets/`.** La même CSS existe dans les deux
  arbres (dont `resume-gallery.css`). Vérifier si le doublon `static/` est encore
  nécessaire ou s'il est un vestige de `sync-brand.sh`.
- [ ] **`layouts/_partials/resume/diagram-parcours.html`** : la version du site
  `bertrandkeller.github.io` (avant suppression) différait de celle de Resugo
  (marqueur du dernier point). La version Resugo fait foi ; vérifier le rendu des
  CV concernés.
- [ ] **`layouts/resume/list.html`** contient de la logique de présentation
  (titres « Resumes » / « Letters » codés en dur). À passer en i18n et à couvrir
  par l'exampleSite.
- [ ] **`_vendor/` fige les thèmes.** Le site `bertrandkeller.github.io` possède
  un `_vendor/` ignoré par Git qui masque le `replace ../resugo`. Une modification
  de Resugo n'est visible qu'après `hugo mod vendor`. Décider : supprimer le
  vendoring en développement ou l'automatiser dans le build.
- [ ] **`theme.toml` annonce une licence MIT** mais aucun fichier `LICENSE` n'est
  présent à la racine. Ajouter le texte ou retirer `license`/`licenselink`.
- [ ] **`layouts/gallery/` est vide** : vestige à supprimer ou à documenter.
- [ ] **`/favicon.ico` renvoie 404** sur les deux sites (le navigateur le demande
  même quand des `<link rel=icon>` existent). Ajouter un `favicon.ico` racine.
## Tests du 2026-10-23

- `bin/serve-hugo test dev resugo repogo sligo` : 3/3 OK.
- `bin/serve-hugo test build bertrandkeller` : OK (1 avertissement existant
  `.Site.Data` déprécié).
- `bin/serve-hugo test responsive resugo repogo bertrandkeller` : 320 et 390 px,
  **0 débordement de document**. Captures dans
  `.cache/responsive/{resugo,repogo,bertrandkeller}_*`.
- Sligo : mesure manuelle à 320/390 px, 0 débordement de document mais des
  slides restent découpées en bas. Cible volontairement absente de
  `bin/serve-hugo.responsive` jusqu'à l'arbitrage canvas/reflow.
- Lighthouse accessibilité : CV Resugo **100**, CV blog **100**, aperçu Repogo
  **100** après cible de 24 px sur le sommaire.
- `hugo mod vendor` du blog rafraîchi avec Higo `v0.9.1` et Resugo local ; le
  `_vendor` doit être régénéré après chaque modification de thème.

## Tests du 2026-10-21

- `hugo` complet blog (FR 1910 / EN 41 pages) : OK.
- `hugo -e production` blog : OK.
- `hugo` exampleSite Resugo : OK.
- Crawl HTTP : jusqu'à 306 pages blog + 9 pages exampleSite, **0 lien interne en
  erreur** sur l'état stabilisé.
- Pendant les tests, une réorganisation de `content/resources/accessibility/`
  (renommages `auditeur` → `auditer`, `papers` → `recherches/papers`, etc.) a
  provoqué des 500 transitoires et laissé 2 liens relatifs cassés :
  `veille/contenus/ca11y-contenus-personnalises.md` et
  `auditer/metier/tests-at-2030.md` pointent encore vers les anciens chemins.
  À corriger avec la réorganisation, hors périmètre Resugo.
- Lighthouse (accessibilité) : galerie blog 100, CV blog 100, galerie Resugo 100,
  CV Resugo 100.

## Règle de séparation

- `bertrandkeller.github.io` **consomme** les thèmes (`higo`, `repogo`, `resugo`,
  `sligo`, `fromago`) via `go.mod` ; il ne doit pas redéfinir leurs partials ni
  leurs layouts.
- Toute correction de rendu CV se fait dans Resugo, puis se propage au site.
- Les surcharges locales ne sont acceptables que pour du contenu ou du paramétrage
  propre au site, et doivent être documentées ici.
