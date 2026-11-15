from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, login_page_view

urlpatterns = [
    # Ruta pentru API-ul de înregistrare (JSON)
    path('register/api/', RegisterView.as_view(), name='api_register'),

    # Ruta pentru API-ul de Token JWT (dacă îl folosiți pentru teste cu Postman/frontend separat)
    path('api/token/', TokenObtainPairView.as_view(), name='login_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]