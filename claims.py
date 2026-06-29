from fastapi import APIRouter
from app.models.claim import ClaimAnalyzeRequest, ClaimAnalyzeResponse
from app.brain.decision_engine import analyze_claim

router = APIRouter(prefix="/claims", tags=["claims"])

@router.post("/analyze", response_model=ClaimAnalyzeResponse)
def analyze(req: ClaimAnalyzeRequest):
    return analyze_claim(
        text=req.text,
        claim_id=req.claim_id,
        contract_active=req.contract_active
    )