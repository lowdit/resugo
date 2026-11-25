# Changelog — resugo

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), versions
SemVer. Chaque entrée dit **quoi · où · migrer**. « Non publié » = ce que
reçoivent les sites qui suivent `main`. Politique :
`lowtech-dev-method/docs/TAGS-MODULES-HUGO.md`.

## Non publié

### Cassé

- **Retiré : `content/`** (`_index.md`). Hugo monte le contenu d'un
  thème chez chaque site qui l'importe : ces pages arrivaient chez tous les
  consommateurs.
  Où : un site qui comptait sur l'accueil ou la page d'erreur du module.
  Migrer : écrire `content/_index.md` dans le site ; la page introuvable vient
  désormais du kit (`404.html`).
- **Retiré : `layouts/interview-prep/single.html`**, gabarit du blog personnel
  (qui garde le sien) ; il appelait `utils/nav-depth`, absent de resugo.
- **Plus de copies de la marque dans resugo** (jetons, base, composants, vues,
  partials de coque) : elles sont servies par `lowdit-kit`.
  Où : un site qui charge resugo **sans** `lowdit-kit` ni minigo.
  Migrer : ajouter le kit en dernier dans la liste des thèmes,
  `theme = ["github.com/lowdit/resugo", "github.com/lowdit/lowdit-kit"]`
  (ou garder minigo, qui l'apporte).
- **Classes `minigo-*` renommées `lowdit-*`** dans les gabarits (7 classes,
  correspondance 1:1).
  Où : CSS ou JS d'un site qui cible `.minigo-*`. Pas d'erreur au build : le
  style ne s'applique plus.
  Migrer : remplacer `minigo-` par `lowdit-` dans les sélecteurs du site.
- **Retiré** : `layouts/_default/baseof.html`, gabarit Overgo déjà masqué partout
  (minigo ou higo passent devant). La coque vient du gabarit de base de `lowdit-kit`.

### Ajouté

- Modèle `cv` déclaré (`[params.lowdit.models.cv]`).
- Feuille du modèle `assets/css/views/cv-vitrine.css`, venue de `lowdit-kit` (même
  chemin : transparent).
- `exampleSite` fonctionne sans minigo : `theme = ["github.com/lowdit/resugo", "github.com/lowdit/lowdit-kit"]`.

### Corrigé

- `cv-vitrine.css` lit les rôles du kit (`--lowdit-color-*`) au lieu de la palette
  Lowdit : une marque déclinée s'y applique. Même rendu pour Lowdit.

## v0.3.3

Dernière version distribuée avec des copies de la marque Brand. Historique antérieur : `git log`.
