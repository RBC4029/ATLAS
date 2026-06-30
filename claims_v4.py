from app.analyzers.decision_engine_v4 import DecisionEngineV4

def test_mrh_policy_coverage_dde():
    engine = DecisionEngineV4()
    result = engine.analyze(
        "Dégât des eaux le 12/06/2026 au 12 rue Victor Hugo. Fuite du voisin du dessus. Photos et devis 2350 euros.",
        "D-DOM-1",
        "MRH"
    )
    assert result["contract_active"] is True
    assert result["guarantee_probable"] is True
    assert result["convention"] == "IRSI"

def test_auto_policy_coverage_collision():
    engine = DecisionEngineV4()
    result = engine.analyze(
        "Accident automobile avec tiers identifié. Constat amiable, photos et devis 980 euros.",
        "A-DOM-1",
        "AUTO"
    )
    assert result["contract_active"] is True
    assert result["guarantee_probable"] is True
    assert result["convention"] == "IRSA / IDA"