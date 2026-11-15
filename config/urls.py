from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from recipes.views import salveaza_reteta, search_ingredients_view, home_view
from accounts.views import register_page_view

urlpatterns = [
    # Paginile site-ului legate dinamic
    path('', home_view, name='home'),
    path('search/', search_ingredients_view, name='search_ingredients'),
    path('add-recipe/', salveaza_reteta, name='add_recipe'),
    path('recipe/<int:pk>/', TemplateView.as_view(template_name='recipe_detail.html'), name='recipe_detail'),
    path('register/', register_page_view, name='register'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),

    # Admin și API
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/recipes/', include('recipes.urls')),
    path('api/assistant/', include('assistant.urls')),
]