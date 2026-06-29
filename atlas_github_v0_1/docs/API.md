# API Atlas

## POST /api/v1/claims/analyze

Request:
```json
{
  "claim_id": "D-1001",
  "text": "Dégât des eaux...",
  "contract_active": true
}
```

Response:
```json
{
  "claim_id": "D-1001",
  "branch": "MRH",
  "claim_type": "Dégât des eaux",
  "convention": "IRSI",
  "amount": 2350,
  "confidence": 92,
  "missing_documents": [],
  "expertise_recommendation": "Téléexpertise",
  "settlement_recommendation": "À étudier",
  "recourse_recommendation": "Oui, recours recommandé",
  "decision_path": "Téléexpertise possible"
}
```