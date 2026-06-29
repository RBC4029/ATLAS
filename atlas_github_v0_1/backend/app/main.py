from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.claims import router as claims_router
from app.api.rules import router as rules_router

app = FastAPI(
    title="Atlas API",
    version="0.1.0",
    description="Copilote de pré-instruction des sinistres"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(claims_router, prefix="/api/v1")
app.include_router(rules_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok", "product": "Atlas", "version": "0.1.0"}