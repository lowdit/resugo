# Challenge — CV « Ère IA » (Resugo Evidence)

> Statut : cadrage v0 — 2026-10-19 · incrément `P-resugo-cv-ere-ia-stackr-01` (approuvé) · affine `P-resugo-evidence-stackr-01` (proposé).
> Pilote : candidature Product Manager Stackr — `bertrandkeller.github.io/content/resume/stackr-product-manager/index.md` (draft).

## 1. Problème

Une candidature est la rencontre de deux attentes contradictoires du recruteur :

- **La « pépite »** : une personne originale, transversale, qui comprend des sujets variés.
- **Le concret** : chiffres, roadmap, prévisibilité, indicateurs. C'est l'attente qui l'emporte, parce qu'elle rassure la hiérarchie et permet de décider.

Le profil de Bertrand Keller est transversal. Le risque connu, vécu avec des supérieurs et des recruteurs : **passer pour celui qui fait trop à sa manière**. Un CV chronologique classique ne lève pas ce doute ; un CV « original » le renforce.

Le CV Ère IA doit donc être **original sur la forme et plus rassurant qu'un CV classique sur le fond** : plus clair, plus vérifiable, orienté décision.

## 2. Décisions (2026-10-19)

| Sujet | Décision |
| --- | --- |
| Lecture du poste | Le PM Stackr est un chef de projet produit / PO élargi : il centralise, répartit et contrôle le travail. Capteurs et IoT = métier de l'entreprise, pas compétence exigée du candidat. |
| Message central | Senior, mature, droit au but ; s'inscrit dans le cadre de l'entreprise et le fait avancer. Pas de manifeste, pas de « ma méthode ». |
| Ce qui montre le passage de cap | Les compétences de pilotage produit **à l'heure de la fabrique IA** : gouvernance, qualité produit, sécurité des données, risques, éthique, veille au rythme hebdomadaire des outils. |
| Lettre | Remplacée par une **synthèse qui analyse les besoins IA de l'entreprise** (hypothèses à valider en entretien) et propose un cadre de contribution. |
| Fabrique IA | Fabrique personnelle prouvée par la pratique ; contribution à la Fabrique de l'entreprise **avec** PO, CTO, QA. Jamais « directeur Fabrique ». |
| Lowdit | Nommé. Statut exact : « sites construits, mise en ligne en cours ». Jamais « livré ». |
| Sujets en exploration | Formulés « j'explore / je compare / j'essaie » ; jamais « je maîtrise ». |
| Office / outils internes | **Ne pas en parler.** Le doute se lève par la clarté et le cadre, pas par une justification. |

## 3 bis. Version v1 (2026-10-19, 11 h 30) — CV en deux parties

Arbitrage humain : CV original dans la présentation, en deux parties distinctes ; remplace la structure v0 ci-dessous dans le brouillon.

1. **« 1 · Mon usage de l'IA aujourd'hui »** — schéma `ia-systeme.svg` (boucle cadrer → déléguer → contrôler → décider → capitaliser, harnais qualité / sécurité des données / risques / éthique et compétences / sobriété), puis 6 paragraphes courts.
2. **« 2 · Les expériences qui m'y ont mené »** — frise `parcours-competences.svg` (compétence acquise par période), puis chaque expérience titrée par la compétence acquise ; employeur et intitulé réel en sous-titre.

Choix associés : version une page désactivée (`skipOnePage`) ; anglais et international valorisés (Sopra Steria, Handicap International) ; lettre en prose, sans gras, trois intertitres, accroche qui assume de sortir du ton traditionnel et expose la vision d'une Fabrique IA chez un éditeur SaaS B2B.

Les deux SVG sont dans le bundle de la page (`bertrandkeller.github.io/content/resume/stackr-product-manager/`), avec `<title>`, `<desc>` et un texte alternatif dans le CV.

## 3. Concept v0 (historique) — « Piloter un produit à l'heure de la fabrique IA »

**Principe.** Le CV ne raconte pas une succession de postes : il montre une **carte de compétences en 6 domaines**, chacune adossée à des preuves, puis un parcours court qui explique le chemin jusqu'à ce niveau.

**Ordre de lecture (page 1).**

1. Accroche : senior, cadre, IA intégrée au delivery.
2. **Carte des 6 domaines** (grille de cartes Resugo) — c'est le visuel.
3. **Preuves** (cartes « focus ») : 4 situations vérifiables.
4. Parcours : chaque poste = une brique du chemin, 2–3 lignes, résultats pour la direction.
5. Formation.

**Effet recherché en 30 secondes.** « Il sait piloter un produit de façon classique (roadmap, backlog, KPI), et il a déjà intégré ce que l'IA change : rythme, risques, contrôle. Il cadre plus qu'il n'improvise. »

### Carte des 6 domaines et niveaux

Les niveaux restent dans ce document (relecture, entretien) ; le CV ne les affiche pas, mais n'écrit rien au-delà.

| Domaine | Contenu affiché | Niveau | Preuve |
| --- | --- | --- | --- |
| Produit & roadmap | Vision, priorisation, roadmap, backlog, KPI | prouve | DINUM, Sopra Steria |
| Delivery en fabrique IA | Incréments cadrés, agents de code, revue par une 2e session, validation humaine | pratique | Freelance 2026, Lowdit |
| Qualité produit | Critères d'acceptation, Definition of Done, recette, accessibilité des interfaces | prouve | Sopra Steria, Handicap International, DINUM |
| Sécurité & données | Données client hors outils IA, secrets hors dépôts, règles de confidentialité écrites | pratique | Gouvernance IA écrite (Lowdit) |
| Risques & éthique | Besoin réel d'IA, biais, dépendance fournisseur, maintien des compétences | pratique (cadre) · a-acquerir (à l'échelle d'une équipe) | `GOUVERNANCE-IA.md` |
| Veille & adoption | Revue de veille structurée, essai borné avant adoption, coût par résultat accepté | pratique · exploration (RAG / wiki versionné, subagents, tokens) | Process veille, lowdit-ai-lab |

## 4. Synthèse « besoins IA » (remplace la lettre)

Structure en 6 temps, ton pair professionnel, environ 450 mots :

1. **Ce que je lis** : Stackr cherche un PM qui porte aussi la transformation IA.
2. **Les besoins IA d'un éditeur comme Stackr** (hypothèses explicites) : accélérer le delivery sans dette ; IA dans le produit (aide à la décision → explicabilité) ; données multi-clients (cloisonnement, confidentialité) ; sécurité (fuites, secrets) ; rythme hebdomadaire des outils ; compétences de l'équipe.
3. **Le cadre que je propose** : 90 jours en 3 temps (cartographier, cadrer avec CTO/QA, piloter un flux mesuré).
4. **Ce que j'apporte** : preuves (DINUM, Sopra Steria, pratique IA 2026).
5. **Ce que j'apprendrai chez vous** : une phrase (domaine, outillage SaaS).
6. **Modalités et entretien.**

## 5. Garde-fous

**Interdits** : inventer KPI, clients, dates, titres ; « 5 ans de PM SaaS B2B » ; « j'ai dirigé une Fabrique IA » ; « je maîtrise » sur les sujets en exploration ; « Lowdit livré » ; formule « Madame, Monsieur » ; jargon (« passionné », « visionnaire ») ; information indispensable seulement dans un visuel.

**Faits à vérifier avant envoi**

- [ ] Sopra Steria : « animation d'experts national / international » — formulation exacte.
- [ ] Lowdit : année de départ et artefacts datés, si une durée est affichée (sinon ne pas en mettre).
- [ ] Frago : lien public consultable.
- [ ] Localisation / présence attendue par Stackr.
- [ ] Anglais : niveau à afficher (non sourcé dans les CV existants) ; confirmer « en français et en anglais » pour le réseau Sopra Steria et le travail avec les antennes Handicap International.
- [ ] Contrôle par une seconde session IA : confirmer que la pratique est régulière (le CV et la lettre l'affirment).

## 6. Prompt — IA externe (conseil, session séparée)

```text
Tu es conseiller en recherche d'emploi : original, professionnel, rigoureux.
Ton but : que j'obtienne le poste de Product Manager chez Stackr (SaaS B2B,
~20 ans, 500+ clients, mission incluant la "Fabrique IA"). Il faut impressionner
le recruteur et montrer que mon profil est déjà passé dans l'ère de l'IA.

Lis : resugo/docs/CHALLENGE-CV-EVIDENCE-IA.md (cadrage, faits, interdits)
et bertrandkeller.github.io/content/resume/stackr-product-manager/index.md (brouillon).

La tension : le recruteur veut une "pépite" transversale, mais privilégie le
concret (chiffres, roadmap, indicateurs). Mon risque connu : passer pour
"celui qui fait trop à sa manière". L'originalité qui donne l'image d'un
électron libre est un échec.

Demande :
1. Diagnostic du brouillon en 5 lignes (forces, faiblesses).
2. Deux alternatives de forme réellement différentes (une audacieuse, une sobre),
   avec ce que le recruteur ressent en 30 secondes.
3. La carte des 6 domaines : est-elle lisible, crédible, complète
   (gouvernance, qualité, sécurité des données, risques, éthique, veille) ?
4. La synthèse "besoins IA" : les hypothèses sont-elles pertinentes pour un
   éditeur SaaS B2B ? Laquelle manque ? Laquelle sonne présomptueuse ?
5. Les 3 phrases les plus fortes et les 5 à supprimer ou reformuler.
6. Verdict : brouillon / prêt pour relecture humaine / ne pas envoyer.

Interdit : inventer des faits ; proposer "5 ans PM SaaS", "directeur Fabrique",
"je maîtrise" sur l'exploration. Réponds en français, bullets courts.
Tu n'as aucun droit de réécrire les fichiers.
```

Règle d'usage : appliquer au plus la moitié des suggestions, après arbitrage humain.

## 6 bis. Version v2 (2026-10-19, 11 h 50)

- Page 1 : accroche courte (un paragraphe) + schéma « Comment je pilote un produit avec l'IA » en trois niveaux (ce que je vise, comment je travaille, ce que j'évite / harnais), palette chaude (crème, terracotta) + navy ; deux lignes « pourquoi » et « outils ».
- Saut de page forcé avant la partie 2 (`break-before: page` dans le contenu, sans toucher aux layouts).
- Page 2 : frise réchauffée (2026 en terracotta) + tableau compact « Postes et repères » à la place des fiches d'expérience longues ; section Formation retirée (UTC dans l'accroche).
- Lettre : signature finale retirée, version resserrée, enquête de démarrage (variété technique, métier, pratiques IA existantes).

## 8. Déclinaisons Resugo (à arbitrer)

Quatre présentations envisagées : **CV IA long** (actuel), **CV IA court**, **CV classique long**, **CV classique court**.

Lecture : ce sont **deux angles** (IA / classique) × **deux longueurs** (long / court). Resugo sait déjà produire deux longueurs depuis une même page (feuille complète et feuille « one-page ») ; il ne sait pas produire deux angles.

| Option | Principe | Pour | Contre |
| --- | --- | --- | --- |
| A — contenu seul | Deux pages par candidature (`…-ia`, `…-classique`), chacune avec sa version longue et sa version une page | Rapide, aucun changement de thème | Expériences dupliquées, risque de divergence des faits |
| B — évolution Resugo | Parcours unique en données (`data/` ou fichier partagé) + paramètre `angle: ia \| classique` ; les layouts composent les quatre sorties | Une seule source de faits, réutilisable pour toutes les candidatures | Incrément Resugo à cadrer, layouts à modifier |

Recommandation : A pour Stackr (version classique en complément, utile pour les logiciels de tri), B comme incrément Resugo séparé ensuite.

## 7. Prochaines étapes

1. Relecture humaine du brouillon (preview : `hugo server -D` dans `bertrandkeller.github.io`, page `/resume/stackr-product-manager/`).
2. Contrôle par l'IA externe (prompt §6).
3. Schéma SVG de la carte des 6 domaines (SeeCode) dans `resugo/docs/diagrams/` avec alternative texte — seulement après validation du contenu.
4. Faits §5 vérifiés, puis décision d'envoi (humain, canal https://stackr-group.com/on-recrute/).
