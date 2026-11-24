# Dettes techniques — Resugo

État constaté le 2026-10-21, complété le 2026-10-26. Ces points sont des
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
- [x] **Accueil Resugo sans styles de galerie.** `home/cv.html` vivait dans
  Minigo et rendait les cartes `resume-gallery-card` dans un `catalog-grid` avec
  la CSS `catalog`. Le partial est déplacé dans
  `resugo/layouts/_partials/home/cv.html` ; Minigo ne garde que
  `home/catalog-grid.html`, générique, avec un paramètre `gridClass`. Le profil
  CV passe `resume-gallery-grid` et inline `resume/gallery-styles.html`. Vérifié
  en build `-e development` : 6 cartes, grille 4 colonnes desktop, 1 colonne à
  320 px, bordures et visuels présents.
- [x] **Sligo — lecteur mobile.** Sous 900 px, `sligo.js` n'initialise plus la
  scène Reveal : les slides passent dans le flux (`body.sligo-reader`), une par
  section, en hauteur naturelle. Le défilement vertical est natif, les fragments
  restent lisibles sans clic, les fonds `data-background-color` sont réappliqués
  et le radial devient une pile. Desktop Reveal est inchangé. Cible ajoutée à
  `bin/serve-hugo.responsive`.
- [x] **`hs group` confondait un ancien serveur avec le site attendu.** Le groupe
  ne testait que l'écoute du port. Après renumérotation, un ancien Sligo restait
  sur le port de Repogo et `modules` ouvrait deux Sligo. `group_process_source`
  compare désormais le `-s` du processus Hugo au dossier cible ; en cas de
  conflit, le site est lancé sur le prochain port libre avec un avertissement.

## Dettes restantes à arbitrer

- [ ] **Coque Minigo encore implicite.** `layouts/_default/baseof.html` appelle
  `lowdit/design-system.html`, `lowdit/favicon.html`, `lowdit/diagrams.html` et
  `lowdit/logo.html`, fournis par Minigo. Le blog n'est pas concerné (il utilise
  le `baseof` de Higo), mais Resugo seul ne peut pas rendre une page de thème.
  `social-meta` a été rapatrié ; décider pour le reste : documenter Minigo comme
  coque officielle, soit rapatrier ces partials.
- [ ] **Sligo desktop — une slide déborde de 17 px.** À 1280 px, la slide
  « Le bloc image » a un `scrollHeight` de 817 px pour 800 px visibles, avec
  `overflow: hidden`. Le lecteur mobile n'est pas concerné. À corriger dans la
  composition image ou à couvrir par un contrôle de découpe dédié.
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

## Layouts locaux du blog (bertrandkeller.github.io)

Le 2026-11-24, `_default/single`, `_default/list`, `_default/terms`, `posts/list`
et `links/links-resources` ont été remontés dans Higo (options de site
`higo_single_header_class`, `higo_source_link`, `higo_list_compact`,
`higo_list_by_year`). Restent dans le blog, au même chemin qu'un thème :

- [ ] `layouts/posts/single.html` (Higo) : carte auteur avec avatar personnel
  codé en dur, libellés de série en anglais, `media_url` en `errorf`, pas
  d'image mise en avant. À remonter quand Higo aura une carte auteur paramétrable
  (`author.avatar`) et des libellés i18n compatibles.
- [ ] `layouts/_partials/posts/post-entry.html` (Higo) : liens `RelPermalink`
  et date sans `mt-0`. À supprimer quand Higo passera aux liens relatifs.
- [ ] `layouts/_partials/print/links.html` et `layouts/_partials/utils/nav-depth.html`
  (Higo) : seule différence `RelPermalink` au lieu de `Permalink`. Même condition.
- [ ] `layouts/index.html` (Higo, Resugo, Sligo) : accueil propre au site (textes
  commerciaux, `data/commercial`). Contenu du site, à garder.
- [ ] `layouts/_partials/print/courrier.html` (Repogo) : identique à Repogo à un
  commentaire près. Supprimable après vérification du rendu courrier.
- [ ] `layouts/interview-prep/single.html` (Resugo) : classes `markdown` au lieu
  de `wrapper`/`doc-body`. À trancher dans Resugo, puis supprimer.

Les autres layouts locaux (hubs Lowtus et parutions, `jobs/`, `lowdit/page-date`,
`lowtus/*`, `_markup/render-passthrough`, shortcodes, `expertises`, `competition`, etc.)
n'ont pas d'équivalent dans un thème : contenu ou paramétrage propre au site.

## Tests du 2026-10-26

- `bin/serve-hugo test dev resugo repogo sligo` : 3/3 OK.
- `bin/serve-hugo test build bertrandkeller` : OK (1 avertissement existant
  `.Site.Data` déprécié).
- `bin/serve-hugo test responsive` : 5 URLs sur 4 sites (accueil et CV Resugo,
  aperçu Repogo, CV blog, deck Sligo), 320 et 390 px, **0 débordement de
  document**.
- Sligo lecteur : 23 sections visibles à 320/390 px, `scrollHeight` par section
  inférieur ou égal à la hauteur rendue (0 découpe interne), défilement
  documentaire effectif ; desktop 1280 px conserve Reveal.
- Accueil Resugo dev : 6 cartes, `resume-gallery-grid`, aucun `catalog-grid`.
- `hs group modules --no-open` : 4 sites, Repogo sur `:1328`, un seul Sligo.
  Le garde-fou a aussi été vérifié avec un ancien Sligo sur `:1328` : Repogo
  bascule sur `:1331` avec un message explicite.

## Tests du 2026-10-23

> État historique : le comportement Sligo décrit ci-dessous est remplacé par le
> lecteur mobile du 2026-10-26.

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
