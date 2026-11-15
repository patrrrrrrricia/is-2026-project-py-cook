from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.salveaza_reteta, name='recipe_add'),
    path('search/', views.search_ingredients_view, name='recipe_search_db'),
]