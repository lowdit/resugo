# Diagrammes — convention et légende

Source des visuels « Resugo Evidence » (carte de continuité). Convention :

```
source/  — spec JSON + générateur Python (stdlib, sans dépendance)
export/  — SVG produit (rejouable : python3 source/generer-carte.py)
```

- **La spec JSON est la source du contenu** (blocs, niveaux, lignes) ; le SVG d'export est un produit, pas un original.
- La page CV (`bertrandkeller.github.io/content/resume/stackr-product-manager/`) embarque une **copie de déploiement** de l'SVG dans son bundle — c'est la seule copie servie ; la source canon reste ici.
- **Alternative textuelle** : `<title>` + `<desc>` complets dans l'SVG, et tout le contenu repris en texte dans le CV (aucune information indispensable uniquement graphique).
- **Impression** : pas de couleur de fond indispensable au sens (les niveaux sont répétés en texte dans le CV) ; contrastes vérifiés — blanc sur `#2b4c7e` ≈ 9,9:1, blanc sur `#b45a3c` ≈ 5,6:1 (texte 12 px bold).

## Légende de la carte de continuité

Chaîne du travail produit : **Produit → Design → Technique → Delivery → Qualité / conformité → IA**, avec le rôle de trait d'union (vision ↔ exécution) en tête. Chaque bloc porte son niveau :

| Niveau | Sens |
| --- | --- |
| **prouvé** | Réalisé et vérifiable par un artefact daté (dépôt, document, build consigné) |
| **pratique** | Mis en œuvre régulièrement, à l'échelle personnelle |
| **transférable** | Acquis dans un contexte proche, à réadapter à l'organisation |
| **à acquérir** | Hypothèse de travail assumée, pas une maîtrise revendiquée |

Référent : [`CHALLENGE-CV-EVIDENCE-IA.md`](../CHALLENGE-CV-EVIDENCE-IA.md) (matrice de preuves § matrice).
