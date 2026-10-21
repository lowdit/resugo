---
title: Vitrine composants
date: 2026-10-21
description: CV fictif complet — diagrammes, why, positions, focus, skill-grid et lettre de motivation.
resume:
  name: Noémie Fabre
  job: Cheffe de produit · démo Resugo
  accent: "#2b4c7e"
  skipOnePage: false
  social:
    phone: "06 00 00 00 00"
    linkedin: "https://www.linkedin.com/noemiF"
    blog: "https://example.org"
  traits:
    - label: Pilotage
      detail: roadmap · KPI
    - label: Qualité
      detail: recette · a11y
    - label: Fabrique IA
      detail: cadrage · contrôle
  summary: |-
    Profil **fictif** pour l'exampleSite Resugo : ce CV montre les blocs YAML les plus utiles (diagrammes générés, why, positions, cartes focus, grilles de compétences).
    Les expériences et chiffres sont inventés ; le but est de documenter la mise en page web, PDF et impression.
  section:
    - name: 1 · Usage de l'IA (diagramme + why)
      element:
        - diagram:
            type: ia
            titre: "Comment je cadre un produit avec l'IA"
            vise:
              - "Des livrables utiles"
              - "Une équipe sereine"
              - "Des décisions tracées"
            etapes:
              - titre: "1 · Cadrer"
                lignes: ["objectif", "hors-scope", "critère de fin"]
              - titre: "2 · Déléguer"
                lignes: ["specs courtes", "un fil à la fois"]
              - titre: "3 · Contrôler"
                lignes: ["relecture pair", "tests"]
              - titre: "4 · Décider"
                lignes: ["arbitrage humain", "avec l'équipe"]
            eviter: ["données sensibles dans les outils", "livraison sans recette", "dépendance aveugle"]
            legende: "Données fictives — le diagramme est du HTML/CSS, pas une image."
        - why:
            heading: "Pourquoi ce cadre :"
            quote: "Les modèles changent vite ; les règles de décision doivent tenir dans le temps."
            principles:
              - title: "Incréments courts"
                text: "Livrer, mesurer, ajuster — pas de grand saut non testé."
              - title: "Double regard"
                text: "Ce que produit l'IA est relu avant mise en production."
              - title: "Compétence conservée"
                text: "L'équipe garde la main sur le produit et les arbitrages."
            tools:
              label: "Outils (exemple)"
              items: ["Git", "Tests auto", "Revues", "Docs versionnées"]
            exploring:
              label: "En exploration"
              items: ["evals", "RAG interne", "agents spécialisés"]

    - name: 2 · Parcours (frise + positions)
      element:
        - title: Frise des compétences
          date: "2018 → 2026"
          diagram:
            type: parcours
            titre: "Compétences acquises au fil des postes"
            description: "Frise textuelle générée — accessible et imprimable."
            items:
              - periode: "2018–2020"
                titre: "Livrer en équipe agile"
                lieux: "Startup fictive · backlog, sprints, recette"
              - periode: "2020–2023"
                titre: "Piloter un portefeuille"
                lieux: "Collectivité fictive · multi-prestataires, KPI"
              - periode: "2024–2026"
                titre: "Intégrer l'IA au delivery"
                lieux: "Éditeur SaaS fictif · gouvernance, qualité"
        - title: Postes synthétiques
          positions:
            - period: "2024 — aujourd'hui"
              organisation: "Éditeur SaaS Horizon (fictif)"
              role: "cheffe de produit"
              markers: "Roadmap trimestrielle, coordination design / dev / support"
            - period: "2020 — 2024"
              organisation: "Métropole du delta (fictif)"
              role: "product owner"
              markers: "Portefeuille de huit services numériques citoyens"
            - period: "2018 — 2020"
              organisation: "Startup Nova (fictif)"
              role: "product manager junior"
              markers: "Discovery, métriques d'activation, releases bi-mensuelles"

    - name: Preuves (cartes focus)
      element:
        - focus:
            - name: "Portail citoyen v2"
              date: "2025"
              description: |
                Refonte du parcours **demande en ligne** : -40 % d'abandon sur le tunnel principal (donnée fictive).
              skills: Discovery · UX · KPI
            - name: "Charte fabrique IA"
              date: "2026"
              description: |
                Document de gouvernance partagé avec CTO et QA : périmètres, contrôles, secrets hors dépôts.
              skills: Gouvernance · Qualité · Sécurité

    - name: Compétences (skill-grid)
      element:
        - skills:
            - name: Produit
              element:
                - Roadmap
                - Priorisation
                - OKR
                - Discovery
            - name: Delivery
              element:
                - Backlog
                - Recette
                - Definition of Done
                - Métriques
            - name: Transverse
              element:
                - Accessibilité
                - Documentation
                - Animation d'ateliers

    - name: Formation
      element:
        - title: Master Management de projets
          company: École de management (fictif)
          date: "2018"
          text: Spécialisation produits numériques et services publics.
address: false
motivation: |

  ### Ce que je lis dans votre offre

  Vous cherchez une cheffe de produit capable de **tenir la roadmap** tout en faisant monter l'équipe sur des pratiques IA **cadrées**. Les postes qui mélangent produit et transformation demandent souvent des preuves concrètes : indicateurs, rituels, gouvernance — pas seulement une accroche « passionné·e par l'IA ».

  ### Ce que je propose (hypothèses fictives)

  Pour un éditeur SaaS B2B, je commencerais par **cartographier** les flux où l'IA intervient déjà (support, spec, code, contenu), puis par ** trois règles partagées** avec la QA : ce qu'on ne met jamais dans un outil externe, comment on relit, comment on mesure un incrément pilote.

  ### Modalités

  Disponible pour un entretien sous quinze jours. Ce texte illustre le rendu **lettre de motivation** (web, export PDF, mode impression « lettre seule »). Toutes les entités citées sont inventées pour la démo Resugo.
---
