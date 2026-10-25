# Resugo — idées d’évolution

> **Statut :** bac à idées (2026-10-25). Aucun incrément `approuvé` — ne pas implémenter sans NEXT dédié.  
> **Lié :** [`CHALLENGE-CV-EVIDENCE-IA.md`](./CHALLENGE-CV-EVIDENCE-IA.md) (Evidence / niveaux) · [`CHALLENGE-EXPORT-ATS.md`](./CHALLENGE-EXPORT-ATS.md).

---

## Idée — composant `posture` (candidature consciente)

### Problème

Les CV Resugo sont de plus en plus **co-produits avec l’IA**. Le risque : surface lisse, peu de **prise de position** sur le **fit réel** au poste. L’offre demande souvent seniorité et Fabrique IA ; le candidat a des **lacunes honnêtes** (domaine, outillage, échelle) déjà modélisées en `prouve` | `pratique` | `transferable` | `a-acquerir` dans Evidence.

**Posture** = bloc structuré qui répond : *comment je m’inscris sur **ce** poste*, avec remise en cause réaliste et **plan d’action si j’obtiens le poste** (régime de croisière, pas promesse marketing).

### Intention — arbitrage 2026-10-25

**Par défaut (palier actuel) :** `posture` = **annexe personnelle**, **page supplémentaire à l’impression** (PDF multi-pages Resugo), **non incluse dans l’envoi candidature** sauf choix explicite.

| Mode | Usage |
| --- | --- |
| **`annexe_perso`** *(défaut)* | Documenter le profil **face à l’offre** : fit, lacunes, plan si poste — prep entretien, archivage, relecture ; **optionnel** à remettre en entretien |
| **`envoi`** *(opt-in)* | Même contenu joint volontairement au dossier — cas par cas |
| **`recruteur`** *(futur)* | Intégré au flux principal du CV — **hors scope** tant que non arbitré |

Message type (interne) : *« Oui, j’ai des lacunes sur X ; voici comment je les comble en 30 / 90 jours si j’obtiens le poste, et ce que j’apporte dès J1. »* — **hypothèse de travail**, pas promesse au recruteur tant que `annexe_perso`.

### Complément aux niveaux de maîtrise

Déjà esquissé dans Evidence : **6 domaines × niveau** (ou échelle 1–5 par métier/compétence). Le composant `posture` **ne remplace pas** la carte de compétences ; il **relie** l’offre (`job_ref`) aux niveaux et au plan.

```yaml
# Esquisse — non implémentée
posture:
  job_ref: "stackr-product-manager"   # slug offre / index.md
  audience: annexe_perso              # défaut · envoi = opt-in explicite
  print: true                         # page additionnelle à l'impression (PDF)
  include_in_application: false       # true seulement si envoi volontaire
  fit:
    headline: "PM senior + cadrage IA ; montée domaine capteurs/FM chez vous"
    forces:                          # 3 max, faits vérifiables
      - "Pilotage roadmap / parties prenantes (DINUM, Sopra)"
      - "Boucle IA cadrer → contrôler → décider (documentée)"
    ecarts:                          # lacunes assumées
      - id: domaine-iot-fm
        niveau_actuel: 2             # 1–5 ou prouve|pratique|a-acquerir
        niveau_cible_croisiere: 4
        delai: "90 j"
      - id: fabrique-equipe
        niveau_actuel: pratique
        niveau_cible_croisiere: pratique
        delai: "90 j avec PO/CTO/QA"
  plan_si_poste:                     # régime de croisière
    j30:
      - "Immersion parcours client + métriques produit existantes"
      - "Cartographier un flux Fabrique IA avec l'équipe (sans imposer ma méthode perso)"
    j60:
      - "Un incrément livré avec critères de fin et eval mesurée"
    j90:
      - "Rituels Fabrique partagés ; revue des écarts domaine"
  garde_fous:
    - "Aucun fait inventé par l'IA — niveaux validés humain"
    - "Pas de 'je maîtrise' sur a-acquerir"
    - "Plan = hypothèse à valider en entretien, pas contrat"
```

### Types de blocs Resugo (évolution)

Aujourd’hui (exampleSite / Stackr) : `diagram`, `why`, `focus`, expériences, etc.

| Type | Rôle |
| --- | --- |
| **`posture`** | Fit poste, écarts, plan si embauche |
| *(futur)* **`mastery-map`** | Grille compétences × niveaux 1–5 (lecture entretien) |
| *(existant Evidence)* | Carte 6 domaines + niveaux en doc, pas forcément à l’écran |

Partial Hugo cible (futur) : `layouts/_partials/resume/posture.html` — rendu sobre (listes, pas de score gamifié).

### Génération IA — règles

1. **Entrées obligatoires :** texte offre (ou résumé), `resume:` existant, tableau niveaux Evidence / CHALLENGE §3.  
2. **Sortie :** brouillon YAML `posture` — l’humain **arbitre** chaque `ecart` et chaque ligne de `plan_si_poste`.  
3. **Interdit :** inventer années d’XP, clients, outils entreprise ; transformer `a-acquerir` en `prouve`.  
4. **Prompt type :** même esprit que CHALLENGE §6 (contrôle adverse), rôle « recruteur sceptique » + « plan coach réaliste ».

Lien méthode Lowdit (concept R&D) : **dispersion / bouclage** — le plan si poste peut citer *une* boucle à fermer en 90 j (ex. montée compétence domaine + éprouver avec un client pilote), sans jargon interne Lowdit sur CV client.

### Déclinaisons (avec §8 CHALLENGE)

| Variante | Contenu |
| --- | --- |
| PDF **candidature** (envoi) | Feuille(s) principale(s) seulement — **sans** annexe posture par défaut |
| PDF **complet** (perso / print) | CV + **page annexe `posture`** (`break-before: page` ou layout dédié) |
| **ATS** | Exclure `posture` du linearize — cf. CHALLENGE-EXPORT-ATS |

### Prochain arbitrage humain

1. ~~Envoi par défaut ?~~ **Tranché :** annexe perso, envoi **opt-in**.  
2. Échelle **1–5** vs **prouve / pratique / transferable / a-acquerir** — une seule échelle canon.  
3. Incrément Resugo : `P-resugo-posture-component-01` (proposé) — partial annexe print + 1 exemple Stackr `annexe_perso`.

**Essai pilote :**  
`bertrandkeller.github.io/content/resume/stackr-product-manager/posture.yaml` (bundle page) · partial `resugo/layouts/_partials/resume/posture.html` · panneau **Imprimer → Reporting posture (annexe)**. Le dossier « tout en un PDF » **exclut** l’annexe (`include_in_application: false`).

---

## Autres idées (file)

| Idée | Statut |
| --- | --- |
| Option B Evidence — `data/` unique + `angle: ia \| classique` | Voir CHALLENGE §8 |
| Export ATS linearize | CHALLENGE-EXPORT-ATS |
| Carte 6 domaines SVG SeeCode | CHALLENGE §7 — après validation contenu |
