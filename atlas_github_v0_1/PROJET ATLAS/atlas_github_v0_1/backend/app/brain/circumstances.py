from app.brain.extractors import contains

def analyze_circumstances(text: str) -> dict:
    t = text.lower()

    result = {
        "branch": "UNKNOWN",
        "claim_type": "Non identifié",
        "cause": "Inconnue",
        "origin": "Inconnue",
        "third_party": "Inconnu",
        "probable_responsible": "Inconnu",
    }

    if contains(t, ["fuite", "dégât des eaux", "degat des eaux", "eau", "plafond", "parquet", "canalisation", "évier", "evier", "toiture"]):
        result.update({
            "branch": "MRH",
            "claim_type": "Dégât des eaux",
            "cause": "Fuite / infiltration"
        })
        if contains(t, ["voisin", "tiers", "dessus"]):
            result.update({
                "origin": "Voisin / tiers",
                "third_party": "Oui",
                "probable_responsible": "Voisin"
            })
        elif contains(t, ["toiture"]):
            result.update({"origin": "Toiture"})
        elif contains(t, ["canalisation", "évier", "evier"]):
            result.update({"origin": "Canalisation privative"})

    if contains(t, ["incendie", "fumée", "fumee", "feu", "court-circuit"]):
        result.update({"branch": "MRH", "claim_type": "Incendie", "cause": "Incendie / fumée"})

    if contains(t, ["vol", "effraction", "cambriolage"]):
        result.update({"branch": "MRH", "claim_type": "Vol", "cause": "Effraction"})

    if contains(t, ["accident", "collision", "véhicule", "vehicule", "auto", "pare-chocs", "voiture"]):
        result.update({"branch": "AUTO", "claim_type": "Collision", "cause": "Choc automobile"})
        if contains(t, ["tiers", "constat", "percuté", "percute"]):
            result.update({"third_party": "Oui", "probable_responsible": "Conducteur tiers"})

    if contains(t, ["pare-brise", "bris de glace", "vitrage"]):
        result.update({"branch": "AUTO", "claim_type": "Bris de glace", "cause": "Bris de vitrage"})

    return result