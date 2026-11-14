from recipes.models import Ingredient
from recipes.service import salveaza_reteta  # funcția Colegei 2 (schimbă calea dacă e în alt fișier)

from .calorii import normalizeaza


def salveaza_reteta_ai(reteta, autor=None):
    """
    Pregătește o rețetă primită de la genereaza_reteta() și o salvează
    cu funcția generală salveaza_reteta() a Colegei 2.
    Rețeta intră cu status PENDING (merge la aprobare la admin).
    Întoarce (obiectul Recipe, lista ingredientelor care nu erau în tabel).
    """
    # Numele ingredientelor din baza de date, căutate fără diacritice:
    # "roșie" de la AI -> "rosie" din tabel
    nume_din_tabel = {
        normalizeaza(nume): nume
        for nume in Ingredient.objects.values_list("nume", flat=True)
    }

    # Potrivim numele și adunăm gramele dacă AI-ul pune același ingredient de două ori
    cantitati = {}
    for item in reteta["ingrediente"]:
        cheie = normalizeaza(item["nume"])
        nume = nume_din_tabel.get(cheie, cheie)
        cantitati[nume] = cantitati.get(nume, 0) + item["grame"]

    necunoscute = [nume for nume in cantitati if normalizeaza(nume) not in nume_din_tabel]

    pasi = "\n".join(f"{nr}. {pas}" for nr, pas in enumerate(reteta["pasi"], start=1))

    obiect = salveaza_reteta(
        titlu=reteta["titlu"],
        descriere="",
        pasi_preparare=pasi,
        timp_preparare_min=reteta["timp_minute"],
        ingrediente=[{"nume": n, "cantitate_grame": g} for n, g in cantitati.items()],
        autor=autor,
        status="PENDING",
        sursa="AI",
    )
    return obiect, necunoscute