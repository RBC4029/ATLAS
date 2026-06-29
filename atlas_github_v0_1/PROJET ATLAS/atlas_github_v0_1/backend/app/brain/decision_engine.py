from app.brain.circumstances import analyze_circumstances
from app.brain.extractors import detect_documents, extract_amount

DEFAULT_RULES = {
    "recourse_threshold_mrh_dde": 1600,
    "direct_settlement_threshold": 1200,
    "field_expertise_threshold": 3500,
}

def analyze_claim(text: str, claim_id: str = "DEMO", contract_active: bool = True, rules: dict | None = None) -> dict:
    rules = {**DEFAULT_RULES, **(rules or {})}
    circumstances = analyze_circumstances(text)
    documents = detect_documents(text)
    amount = extract_amount(text)

    branch = circumstances["branch"]
    claim_type = circumstances["claim_type"]
    third_party = circumstances["third_party"]

    explanation = []
    guarantee_probable = claim_type != "Non identifié"
    convention = None

    explanation.append(f"Atlas a identifié la branche {branch} et le type {claim_type}.")

    if contract_active:
        explanation.append("Contrat simulé actif dans cette version.")
    else:
        explanation.append("Contrat non actif : validation gestionnaire obligatoire.")

    if guarantee_probable:
        explanation.append("La garantie semble probablement mobilisable selon les circonstances déclarées.")
    else:
        explanation.append("Les circonstances ne permettent pas encore d’identifier une garantie probable.")

    if branch == "MRH" and claim_type == "Dégât des eaux" and third_party == "Oui":
        convention = "IRSI"
        explanation.append("DDE MRH avec tiers identifié : convention IRSI potentiellement applicable.")

    if branch == "AUTO":
        convention = "IRSA / IDA" if third_party == "Oui" else "IRSA / IDA à vérifier"
        explanation.append("Sinistre automobile : convention IRSA / IDA à analyser selon responsabilité et circonstances.")

    missing = []
    if not documents["date"]:
        missing.append("Date du sinistre")
    if branch == "MRH" and not documents["adresse"]:
        missing.append("Adresse du risque")
    if not documents["photos"]:
        missing.append("Photos")
    if not documents["devis"]:
        missing.append("Devis / montant")
    if branch == "AUTO" and third_party == "Oui" and not documents["constat"]:
        missing.append("Constat amiable")
    if claim_type == "Vol" and not documents["plainte"]:
        missing.append("Dépôt de plainte")
    if claim_type == "Vol" and not documents["factures"]:
        missing.append("Factures justificatives")

    complete = len(missing) == 0

    if not contract_active:
        decision_path = "Blocage contrat"
        expertise = "Analyse gestionnaire"
        settlement = "Non"
    elif not guarantee_probable:
        decision_path = "Intervention humaine nécessaire"
        expertise = "Oui"
        settlement = "Non"
    elif not complete:
        decision_path = "Dossier incomplet"
        expertise = "À reporter"
        settlement = "Non"
        explanation.append("Le dossier n'est pas complet : pièces complémentaires nécessaires.")
    elif amount is not None and amount <= rules["direct_settlement_threshold"]:
        decision_path = "Indemnisation directe envisageable"
        expertise = "Non recommandée"
        settlement = "Oui, sous validation gestionnaire"
    elif amount is not None and amount < rules["field_expertise_threshold"]:
        decision_path = "Téléexpertise possible"
        expertise = "Téléexpertise"
        settlement = "À étudier"
    else:
        decision_path = "Expertise terrain recommandée"
        expertise = "Terrain"
        settlement = "Non à ce stade"

    recourse = "Non"
    if branch == "MRH" and claim_type == "Dégât des eaux" and third_party == "Oui" and amount is not None and amount > rules["recourse_threshold_mrh_dde"]:
        recourse = "Oui, recours recommandé"
        explanation.append("Responsable identifié et montant supérieur au seuil paramétré : recours recommandé.")
    elif branch == "AUTO" and third_party == "Oui":
        recourse = "Selon responsabilité et convention IRSA / IDA"

    confidence = 92
    if not complete:
        confidence -= 18
    if amount is None:
        confidence -= 8
    if branch == "UNKNOWN":
        confidence = 45
    if not contract_active:
        confidence = min(confidence, 55)

    return {
        "claim_id": claim_id,
        "branch": branch,
        "claim_type": claim_type,
        "convention": convention,
        "amount": amount,
        "confidence": confidence,
        "missing_documents": missing,
        "expertise_recommendation": expertise,
        "settlement_recommendation": settlement,
        "recourse_recommendation": recourse,
        "decision_path": decision_path,
        "explanation": explanation,
        "raw": {
            "circumstances": circumstances,
            "documents": documents,
            "rules": rules,
            "complete": complete,
            "contract_active": contract_active,
            "guarantee_probable": guarantee_probable,
        }
    }