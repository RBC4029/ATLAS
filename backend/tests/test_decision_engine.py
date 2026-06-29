from app.brain.decision_engine import analyze_claim

def test_mrh_dde_irsi_recourse():
    text = "Dégât des eaux au 12 rue Victor Hugo. Fuite du voisin du dessus. Photos et devis 2350 euros."
    result = analyze_claim(text)
    assert result["branch"] == "MRH"
    assert result["claim_type"] == "Dégât des eaux"
    assert result["convention"] == "IRSI"
    assert result["recourse_recommendation"] == "Oui, recours recommandé"

def test_auto_irsa_ida():
    text = "Accident automobile avec tiers identifié. Constat amiable, photos et devis 980 euros."
    result = analyze_claim(text)
    assert result["branch"] == "AUTO"
    assert "IRSA" in result["convention"]