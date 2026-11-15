from django.shortcuts import render, redirect
from .models import Recipe
from assistant.calorii import normalizeaza

def salveaza_reteta(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        calories = request.POST.get('calories')
        ingredients_text = request.POST.get('ingredients')

        if recipe_name and calories:
            Recipe.objects.create(
                titlu=recipe_name,
                calorii_totale=float(calories),
                status='PENDING',
                sursa='USER',
                pasi_preparare="Adăugat rapid din formularul web."
            )
            return redirect('home')

    return render(request, 'add_recipe.html')


def search_ingredients_view(request):
    query = request.GET.get('ingredients', '')
    ce_am = [normalizeaza(x) for x in query.split(',') if x.strip()]
    recipes = []

    if ce_am:
        toate = Recipe.objects.filter(status='APPROVED').prefetch_related('ingrediente_reteta__ingredient')
        for recipe in toate:
            recipe.potrivite, recipe.lipsa = [], []
            for ri in recipe.ingrediente_reteta.all():
                nume = normalizeaza(ri.ingredient.nume)
                # "oua" se potrivește cu "ou", "branza" cu "branza telemea"
                if any(x in nume or nume in x for x in ce_am):
                    recipe.potrivite.append(ri.ingredient.nume)
                else:
                    recipe.lipsa.append(ri.ingredient.nume)
            if recipe.potrivite:
                recipes.append(recipe)
        # Întâi rețetele la care ai cele mai multe ingrediente
        recipes.sort(key=lambda r: (-len(r.potrivite), len(r.lipsa)))

    return render(request, 'search_ingredients.html', {'recipes': recipes, 'query': query})


def home_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})