from django.shortcuts import render, redirect
from .models import Recipe


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
    recipes = []

    if query:
        recipes = Recipe.objects.filter(titlu__icontains=query, status='APPROVED')

    return render(request, 'search_ingredients.html', {'recipes': recipes, 'query': query})


def home_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})