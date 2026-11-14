from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Favorite


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('nume', 'kcal_per_100g')
    search_fields = ('nume',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('titlu', 'status', 'sursa', 'timp_preparare_min', 'calorii_totale', 'autor', 'data_crearii')
    list_filter = ('status', 'sursa')
    search_fields = ('titlu', 'descriere')
    inlines = [RecipeIngredientInline]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('utilizator', 'reteta', 'data_adaugarii')