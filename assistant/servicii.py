from django.db import transaction

from recipes.models import Ingredient, Recipe, RecipeIngredient

from .calorii import calculeaza_calorii, normalizeaza


@transaction.atomic
def salveaza_reteta_ai(reteta, autor=None):
    """
    Salvează în baza de date o rețetă primită de la genereaza_reteta().
    Rețeta intră cu status PENDING (merge la aprobare la admin).
    Întoarce (obiectul Recipe, lista ingredientelor fără calorii în tabel).
    """
    total_kcal, necunoscute = calculeaza_calorii(reteta["ingrediente"])

    pasi = "\n".join(f"{nr}. {pas}" for nr, pas in enumerate(reteta["pasi"], start=1))
    obiect = Recipe.objects.create(
        titlu=reteta["titlu"],
        pasi_preparare=pasi,
        timp_preparare_min=reteta["timp_minute"],
        calorii_totale=total_kcal,
        sursa="AI",
        status="PENDING",
        autor=autor,
    )

    # Ingredientele existente, căutate după nume fără diacritice
    existente = {normalizeaza(ing.nume): ing for ing in Ingredient.objects.all()}

    for item in reteta["ingrediente"]:
        cheie = normalizeaza(item["nume"])
        ingredient = existente.get(cheie)
        if ingredient is None:
            # Ingredient nou: îl adăugăm cu 0 kcal, adminul îi poate completa caloriile
            ingredient = Ingredient.objects.create(nume=cheie, kcal_per_100g=0)
            existente[cheie] = ingredient

        legatura, creata = RecipeIngredient.objects.get_or_create(
            reteta=obiect, ingredient=ingredient,
            defaults={"cantitate_grame": item["grame"]},
        )
        if not creata:  # același ingredient de două ori în rețetă: adunăm gramele
            legatura.cantitate_grame += item["grame"]
            legatura.save()

    return obiect, necunoscute