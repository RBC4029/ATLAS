import re

def contains(text: str, words: list[str]) -> bool:
    return any(word in text for word in words)

def extract_amount(text: str):
    match = re.search(r"(\\d+)\\s*(€|eur|euros)", text.lower())
    return int(match.group(1)) if match else None

def detect_documents(text: str) -> dict:
    t = text.lower()
    return {
        "photos": "photo" in t,
        "devis": ("devis" in t) or (extract_amount(t) is not None),
        "constat": "constat" in t,
        "plainte": "plainte" in t,
        "factures": "facture" in t,
        "date": ("/202" in t) or ("date" in t) or ("survenu" in t),
        "adresse": any(w in t for w in ["rue", "avenue", "boulevard", "adresse"]),
    }