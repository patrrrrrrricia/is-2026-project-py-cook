from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    #definim cele doua roluri
    ROL_CHOICES=[
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    #campul suplimentar pentru rol
    rol=models.CharField(max_length=10,choices=ROL_CHOICES,default='user')

    def __str__(self):
        return f"{self.username}({self.rol})"