# Intégration assureur

Atlas ne remplace pas le SI sinistre.

## Modes d'intégration

1. Copilot Web  
Le gestionnaire ouvre Atlas à côté de son logiciel actuel.

2. API  
Le SI sinistre envoie le dossier à Atlas via `POST /api/v1/claims/analyze`.

3. Widget  
Atlas est intégré dans un panneau latéral du SI existant.

4. Connecteur GED  
Atlas lit les documents entrants et prépare une fiche de pré-instruction.

## Réponse API attendue
Atlas renvoie :
- branche ;
- type de sinistre ;
- convention ;
- pièces manquantes ;
- expertise ;
- indemnisation directe ;
- recours ;
- niveau de confiance ;
- explication.