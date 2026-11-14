import json

from django.core.management.base import BaseCommand

from assistant.calorii import FISIER_CALORII
from recipes.models import Ingredient


class Command(BaseCommand):
    help = "Încarcă caloriile din assistant/calorii.json în tabelul Ingredient"

    def handle(self, *args, **options):
        with open(FISIER_CALORII, encoding="utf-8") as f:
            date = json.load(f)

        noi = 0
        for nume, kcal in date.items():
            _, creat = Ingredient.objects.update_or_create(
                nume=nume, defaults={"kcal_per_100g": kcal}
            )
            noi += creat

        self.stdout.write(self.style.SUCCESS(
            f"Gata: {len(date)} ingrediente ({noi} noi, {len(date) - noi} actualizate)"
        ))