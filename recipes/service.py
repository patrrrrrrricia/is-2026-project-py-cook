from django.db import transaction
from recipes.models import Ingredient, Recipe, RecipeIngredient


@transaction.atomic
def salveaza_reteta(
    titlu,
    descriere,
    pasi_preparare,
    timp_preparare_min,
    ingrediente,
    autor=None,
    status="PENDING",
    sursa="USER",
):
    """
    Creează o rețetă nouă împreună cu ingredientele ei și calculează caloriile totale.

    Parametrul `ingrediente` este o listă de dicționare:
    [
        {"nume": "Piept de pui", "cantitate_grame": 200, "kcal_per_100g": 165.0},
        {"nume": "Orez basmati", "cantitate_grame": 150},
    ]
    """
    reteta = Recipe.objects.create(
        titlu=titlu.strip(),
        descriere=descriere.strip(),
        pasi_preparare=pasi_preparare.strip(),
        timp_preparare_min=int(timp_preparare_min),
        autor=autor,
        status=status,
        sursa=sursa,
    )

    calorii_totale = 0.0

    for item in ingrediente:
        nume_curat = item["nume"].strip()
        cantitate = float(item["cantitate_grame"])
        kcal_optional = item.get("kcal_per_100g")

        # Căutăm ingredientul fără să conteze literele mari/mici
        ingredient_obj = Ingredient.objects.filter(nume__iexact=nume_curat).first()

        if ingredient_obj is None:
            ingredient_obj = Ingredient.objects.create(
                nume=nume_curat.capitalize(),
                kcal_per_100g=float(kcal_optional) if kcal_optional is not None else 0.0,
            )
        elif ingredient_obj.kcal_per_100g == 0 and kcal_optional is not None:
            ingredient_obj.kcal_per_100g = float(kcal_optional)
            ingredient_obj.save(update_fields=["kcal_per_100g"])

        RecipeIngredient.objects.create(
            reteta=reteta,
            ingredient=ingredient_obj,
            cantitate_grame=cantitate,
        )

        calorii_totale += (ingredient_obj.kcal_per_100g * cantitate) / 100.0

    reteta.calorii_totale = round(calorii_totale, 1)
    reteta.save(update_fields=["calorii_totale"])

    return reteta