from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Funcția care preia datele din formularul HTML de înregistrare
def register_page_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            User.objects.create_user(username=username, password=password)
            return redirect('login')

    return render(request, 'register.html')
from django.contrib.auth import authenticate, login as auth_login

# Funcția care preia datele din formularul HTML de login
def login_page_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autentificăm utilizatorul folosind modelul CustomUser
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Te duce pe pagina principală după login reușit
        else:
            # Poți afișa o eroare dacă datele sunt greșite
            pass

    return render(request, 'login.html')