# Inventaire — vague 3 composition CSS (Resugo)

> **Date :** 2026-11-13 · Réf. [`MIGRATION-UNIVERS-CSS.md`](../../lowdit-brand/docs/MIGRATION-UNIVERS-CSS.md).

## Layouts écran

| Fichier | Compositions | Métier |
| --- | --- | --- |
| `index.html` | délègue `home/cv.html` | — |
| `_partials/home/cv.html` | `.wrapper[data-width=wide]` | `resume-gallery-grid`, cards CV |
| `interview-prep/single.html` | `.wrapper[data-width=reading]`, `.doc-body` | `interview-prep-*` |
| `resume/*` | print / galerie | `resume-*` (CV métier, styles inline legacy à traiter vague 4) |

## Hors scope vague 3

- `_partials/resume/sheet.html` (print HTML autonome)
- Styles inline restants dans diagrammes / tableaux (vague 4 contenus)

## Vérifications

```bash
hs test resugo
```
