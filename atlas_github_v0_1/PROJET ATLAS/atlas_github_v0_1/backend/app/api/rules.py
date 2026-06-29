from fastapi import APIRouter
from app.brain.decision_engine import DEFAULT_RULES

router = APIRouter(prefix="/rules", tags=["rules"])

@router.get("")
def list_rules():
    return DEFAULT_RULES