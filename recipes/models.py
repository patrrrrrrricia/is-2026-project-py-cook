from django.conf import settings
from django.db import models


class Ingredient(models.Model):
    nume = models.CharField(max_length=100, unique=True, verbose_name="Nume ingredient")
    kcal_per_100g = models.FloatField(default=0.0, verbose_name="Calorii per 100g")

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingrediente"

    def __str__(self):
        return f"{self.nume} ({self.kcal_per_100g} kcal/100g)"


class Recipe(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'În așteptare'),
        ('APPROVED', 'Aprobată'),
        ('REJECTED', 'Respinsă'),
    ]

    SURSA_CHOICES = [
        ('USER', 'Utilizator'),
        ('AI', 'Asistent AI'),
    ]

    titlu = models.CharField(max_length=200, verbose_name="Titlu rețetă")
    descriere = models.TextField(blank=True, verbose_name="Descriere")
    pasi_preparare = models.TextField(verbose_name="Pași de preparare")
    timp_preparare_min = models.PositiveIntegerField(default=30, verbose_name="Timp preparare (minute)")
    calorii_totale = models.FloatField(default=0.0, verbose_name="Calorii totale")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING', verbose_name="Status")
    sursa = models.CharField(max_length=10, choices=SURSA_CHOICES, default='USER', verbose_name="Sursă")
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='retete_create',
        verbose_name="Autor",
    )
    data_crearii = models.DateTimeField(auto_now_add=True, verbose_name="Data creării")

    class Meta:
        verbose_name = "Rețetă"
        verbose_name_plural = "Rețete"

    def __str__(self):
        return f"{self.titlu} [{self.get_status_display()}]"


class RecipeIngredient(models.Model):
    reteta = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingrediente_reteta', verbose_name="Rețetă")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='in_retete', verbose_name="Ingredient")
    cantitate_grame = models.FloatField(default=100.0, verbose_name="Cantitate (grame)")

    class Meta:
        unique_together = ('reteta', 'ingredient')
        verbose_name = "Ingredient din rețetă"
        verbose_name_plural = "Ingrediente din rețetă"

    def __str__(self):
        return f"{self.reteta.titlu} - {self.ingredient.nume} ({self.cantitate_grame}g)"

class Favorite(models.Model):
    utilizator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='retete_favorite',
        verbose_name="Utilizator",
    )
    reteta = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='aprecieri', verbose_name="Rețetă")
    data_adaugarii = models.DateTimeField(auto_now_add=True, verbose_name="Data adăugării")

    class Meta:
        unique_together = ('utilizator', 'reteta')
        verbose_name = "Rețetă favorită"
        verbose_name_plural = "Rețete favorite"

    def __str__(self):
        return f"{self.utilizator} -> {self.reteta.titlu}"