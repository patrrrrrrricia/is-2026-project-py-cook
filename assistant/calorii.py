import json
import unicodedata
from pathlib import Path

FISIER_CALORII = Path(__file__).resolve().parent / "calorii.json"


def normalizeaza(nume):
    """'Brânză Telemea ' -> 'branza telemea' (fără diacritice, litere mici)."""
    fara_diacritice = unicodedata.normalize("NFKD", nume).encode("ascii", "ignore").decode()
    return " ".join(fara_diacritice.lower().split())


def incarca_calorii():
    """Întoarce dicționarul {ingredient: kcal la 100 g} din tabelul Ingredient."""
    from recipes.models import Ingredient

    return {
        normalizeaza(nume): kcal
        for nume, kcal in Ingredient.objects.values_list("nume", "kcal_per_100g")
    }

def calculeaza_calorii(ingrediente):
    """
    Primește lista de ingrediente a unei rețete, de ex.
    [{"nume": "ou", "grame": 120}, {"nume": "roșie", "grame": 100}]
    și întoarce (total_kcal, ingrediente_necunoscute).
    """
    tabel = incarca_calorii()
    total = 0
    necunoscute = []
    for ing in ingrediente:
        nume = normalizeaza(ing["nume"])
        if nume in tabel:
            total += tabel[nume] * ing["grame"] / 100
        else:
            necunoscute.append(ing["nume"])
    return round(total), necunoscute


# Test: python assistant/calorii.py
if __name__ == "__main__":
    reteta = [
        {"nume": "ou", "grame": 120},
        {"nume": "brânză telemea", "grame": 50},
        {"nume": "roșie", "grame": 100},
        {"nume": "ulei", "grame": 10},
        {"nume": "sare", "grame": 2},
        {"nume": "piper", "grame": 1},
    ]
    total, necunoscute = calculeaza_calorii(reteta)
    print(f"Total: {total} kcal")
    if necunoscute:
        print("Ingrediente fără calorii în tabel:", necunoscute)