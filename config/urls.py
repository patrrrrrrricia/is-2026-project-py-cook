from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Paginile site-ului
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('search/', TemplateView.as_view(template_name='search_ingredients.html'), name='search_ingredients'),
    path('add-recipe/', TemplateView.as_view(template_name='add_recipe.html'), name='add_recipe'),
    path('recipe/<int:pk>/', TemplateView.as_view(template_name='recipe_detail.html'), name='recipe_detail'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),

    # Admin și API
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/recipes/', include('recipes.urls')),
    path('api/assistant/', include('assistant.urls')),
]