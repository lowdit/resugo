# Challenge — export candidature compatible ATS (Resugo)

> **Statut :** arbitrage **clôturé** (2026-11-02) — objectif = **canal candidature (texte linéaire)**, pas produit ATS ni garantie plateforme. Incrément **`P-resugo-ats-export-01` archivé** sans implémentation (reprise = nouvelle décision + retour en `plans/ready/`).  
> **Plan archivé :** [`lowtech-dev-method/plans/archived/P-resugo-ats-export-01.md`](../../lowtech-dev-method/plans/archived/P-resugo-ats-export-01.md) · **Clôture arbitrage :** [`lowtech-dev-method/plans/done/P-resugo-ats-export-arbitrage-2026-11-02.md`](../../lowtech-dev-method/plans/done/P-resugo-ats-export-arbitrage-2026-11-02.md)

**Recadrage (2026-11-02)** : le libellé « ATS » décrit le *contexte d’usage* (upload sur plateformes recrutement), pas le périmètre produit. UI et doc produit privilégient **« export / version texte candidature »**.

## Contexte

**Resugo** sert des CV **en ligne** (vue Minigo `cv-vitrine`), une **galerie de profils** et des **exports print** HTML/PDF éditoriaux. La charte premium dit explicitement que la vitrine **ne simule pas un ATS** ([`lowdit-brand/brand/VUES-PREMIUM.md`](../../lowdit-brand/brand/VUES-PREMIUM.md) — vue `cv-vitrine`).

Les candidats uploadent souvent un **fichier** dans un ATS (Workday, Taleo, Lever, etc.). Ces outils extraient du **texte linéaire** ; les PDF « design » (colonnes, grilles, pills) sont mal ou partiellement lus.

**Question du challenge :** faut-il une **deuxième sortie** Resugo, dédiée à la candidature fichier, **sans** dégrader la vitrine ?

## Définition pragmatique « compatible ATS »

On ne promet pas la compatibilité avec **tous** les ATS du marché. On vise :

| Critère | Attendu |
| --- | --- |
| Texte | Extractible de haut en bas, sans « trous » entre colonnes |
| Structure | Sections nommées de façon standard (Expérience, Formation, Compétences…) |
| Mise en page | Une colonne, pas de tableaux de mise en page, pas d’infographie obligatoire |
| Fichier | **TXT** ou **DOCX** de préférence ; PDF **sobre** en option secondaire |
| Source | Un seul YAML `resume:` (déjà le contrat Resugo) |

**Hors promesse :** score de matching, mots-clés « optimisés », simulation visuelle d’un ATS, validation automatique plateforme par plateforme.

## État actuel (constats repo)

- Données structurées : front matter `resume:` (sections, expériences, skills, social).
- Sortie print : `outputFormats.resume` → HTML riche (`layouts/_partials/resume/sheet.html`, grilles, pills).
- Pas de sortie `text/plain`, docx, ni doc produit « export candidature ».

## Architecture cible (recommandation)

**Une source, deux canaux :**

```text
content/resume/*.md  (resume: YAML)
        │
        ├── Canal vitrine (inchangé) — cv-vitrine, galerie, print éditorial
        │
        └── Canal candidature (nouveau) — linearize → .txt (+ lien docx optionnel)
```

Le canal candidature **ne remplace pas** le print vitrine ; il **coexiste** (bouton ou lien « Version candidature (texte) » sur la page CV).

## Phases de dev proposées

| Phase | Livrable | Effort indicatif |
| --- | --- | --- |
| **1 — Socle** | `outputFormat` `ats` (`text/plain` ou HTML minimal sans CSS) + layout dédié | 1 PR |
| **2 — Linearize** | Partial unique `resume/linearize.html` (ou `.txt`) parcourant `resume.section` en ordre, `plainify` | même PR ou suite |
| **3 — Produit** | Lien i18n sur `resume/main.html`, paragraphe `exampleSite/content/product/`, protocole test manuel | 1 PR doc/UI |
| **4 — DOCX (option)** | Script pandoc en CI ou doc « coller le TXT dans Word » | après arbitrage |

Règles contenu pour l’export ATS (documentées, pas forcément validées en schema) :

- Titres de section stables : privilégier `Expérience`, `Formation`, `Compétences` (aligné avec le tri déjà présent dans `sheet.html`).
- Coordonnées en tête (email, téléphone, LinkedIn en URL pleine).
- Puces `-` pour les descriptions ; dates sur la même ligne que intitulé + employeur.

## Questions de challenge (arbitrage humain)

Répondre **oui / non / plus tard** avant `statut: approuvé` sur le NEXT.

| # | Question | Options | Recommandation |
| --- | --- | --- | --- |
| C1 | Resugo doit-il **annoncer** un « export candidature » ? | Oui canal dédié · Non rester vitrine only | **Oui**, sans revendiquer « 100 % ATS » |
| C2 | Format **prioritaire** ? | TXT · DOCX · PDF simple | **TXT** d’abord (zéro dépendance) |
| C3 | Où vit le layout ATS ? | Thème `resugo` only · Partagé Minigo | **`resugo` only** (métier CV) |
| C4 | Activation par CV ? | Global · `resume.atsExport: false` opt-out | **Opt-out** si besoin (CV portfolio pur) |
| C5 | DOCX automatisé (pandoc) ? | Phase 4 · Jamais | **Plus tard**, si usage réel |
| C6 | Impact charte `cv-vitrine` ? | Aucun · Assouplir ratio portrait | **Aucun** — canal séparé |
| C7 | Tests automatisés ? | Golden file TXT · Manuel seulement | **Golden file** sur 1 CV démo (alex-martin) |

## Promesse marketing acceptable

**OK :**

- « Export **texte candidature** dérivé du même contenu que votre CV en ligne. »
- « Mise en page **simplifiée** pour l’upload sur la plupart des plateformes — **sans garantie** par outil. »

**À éviter :**

- « CV compatible ATS garanti »
- « Optimisé pour le parsing algorithmique / keywords ATS »
- Confondre vitrine web et fichier plateforme

## Protocole de vérification (manuel)

1. Générer l’export ATS d’un CV démo (`exampleSite`).
2. Ouvrir le `.txt` : lecture continue nom → contact → sections → fin.
3. Copier-coller dans un éditeur riche : pas de balises HTML résiduelles.
4. (Option) Importer le TXT dans Word, enregistrer DOCX, uploader sur un ATS de test — noter le résultat dans la fiche de clôture, **sans** généraliser.

## Risques et limites

- **PDF print vitrine** reste mauvais candidat ATS — ne pas le vendre comme tel.
- **Lettre de motivation** : traiter en incrément séparé si linearize LM requis.
- **i18n** : libellés de section en FR ; EN = même structure, titres à harmoniser si site bilingue.

## Décisions validées (à compléter)

| ID | Décision | Date | Par |
| --- | --- | --- | --- |
| C1 | **Oui** — canal « export candidature » dédié, sans revendiquer « 100 % ATS » | 2026-11-02 | arbitrage humain |
| C2 | **TXT** en priorité | 2026-11-02 | défauts challenge acceptés |
| C3 | Layout **`resugo` only** | 2026-11-02 | défauts challenge acceptés |
| C4 | Global avec **opt-out** `resume.atsExport: false` | 2026-11-02 | défauts challenge acceptés |
| C5 | **DOCX pandoc** — plus tard (phase 4) | 2026-11-02 | défauts challenge acceptés |
| C6 | **Aucun** impact charte `cv-vitrine` | 2026-11-02 | défauts challenge acceptés |
| C7 | **Golden file** TXT sur alex-martin (exampleSite) | 2026-11-02 | défauts challenge acceptés |

## Liens

- Incrément : `lowtech-dev-method/prompts/NEXT.md` — `P-resugo-ats-export-01` (**archivé** 2026-11-02).
- Écosystème CV : [`lowdit-brand/docs/UNIVERS-COMPOSITION-SITES.md`](../../lowdit-brand/docs/UNIVERS-COMPOSITION-SITES.md).
