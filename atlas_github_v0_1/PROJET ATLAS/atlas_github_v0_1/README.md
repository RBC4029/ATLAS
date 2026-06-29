# Atlas

Atlas est un copilote de pré-instruction des sinistres.

Objectif :
- analyser une déclaration ;
- qualifier le sinistre ;
- appliquer les règles métier ;
- recommander un parcours ;
- laisser la validation finale au gestionnaire.

## Modules
- `backend/` : API FastAPI
- `frontend/` : interface React simple
- `knowledge-base/` : règles métier IRSI / IRSA-IDA
- `docs/` : documentation d'intégration

## Lancer le backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API :
- `GET /health`
- `POST /api/v1/claims/analyze`

## Lancer le frontend
Pour la v0.1, ouvrir :
`frontend/index.html`