# Sprint v0.6 — Domain Model Assurance

## Objectif
Introduire les objets métier nécessaires à une intégration réelle avec un SI assureur.

## Nouveaux objets
- Policy
- Coverage
- Insured
- Risk
- ThirdParty
- Damage
- ExpertiseDecision
- SettlementProposal
- RecourseDecision

## Nouveau moteur
CoverageAnalyzer :
- reçoit une police d'assurance ;
- vérifie contrat actif ;
- mappe le type de sinistre vers une garantie ;
- extrait franchise et plafond ;
- explique pourquoi la garantie est mobilisable ou non.

## Endpoint
`POST /api/v1/claims/analyze-v4`

## Valeur
Atlas ne suppose plus seulement que le contrat est actif.
Il est prêt à recevoir des données contrat depuis le SI assureur.