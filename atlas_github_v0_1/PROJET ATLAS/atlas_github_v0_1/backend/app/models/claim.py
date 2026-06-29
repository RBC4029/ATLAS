from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class ClaimAnalyzeRequest(BaseModel):
    claim_id: str = "DEMO"
    text: str
    contract_active: bool = True

class ClaimAnalyzeResponse(BaseModel):
    claim_id: str
    branch: str
    claim_type: str
    convention: Optional[str]
    amount: Optional[int]
    confidence: int
    missing_documents: List[str]
    expertise_recommendation: str
    settlement_recommendation: str
    recourse_recommendation: str
    decision_path: str
    explanation: List[str]
    raw: Dict[str, Any]