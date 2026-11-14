from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from recipes.models import Ingredient, Recipe, RecipeIngredient


class Command(BaseCommand):
    help = "Populează baza de date cu ingrediente și 12 rețete de test în limba română"

    def handle(self, *args, **options):
        User = get_user_model()
        autor_default = User.objects.first()

        ingrediente_data = {
            "Piept de pui": 165.0,
            "Ouă": 155.0,
            "Orez basmati": 130.0,
            "Paste integrale": 124.0,
            "Roșii": 18.0,
            "Castraveți": 15.0,
            "Brânză feta": 264.0,
            "Telemea de vacă": 270.0,
            "Ulei de măsline": 884.0,
            "Unt": 717.0,
            "Usturoi": 149.0,
            "Ceapă galbenă": 40.0,
            "Ardei gras": 26.0,
            "Ciuperci champignon": 22.0,
            "Spanac proaspăt": 23.0,
            "Smântână de gătit": 200.0,
            "Cartofi": 77.0,
            "Morcovi": 41.0,
            "File de somon": 208.0,
            "Lămâie": 29.0,
            "Avocado": 160.0,
            "Pâine integrală": 247.0,
            "Fulgi de ovăz": 389.0,
            "Lapte 1.5%": 46.0,
            "Banană": 89.0,
            "Miere": 304.0,
            "Iaurt grecesc 2%": 73.0,
            "Ton în suc propriu": 116.0,
            "Porumb dulce": 86.0,
            "Măsline negre": 115.0,
        }

        ingrediente_obj = {}
        for nume, kcal in ingrediente_data.items():
            obj, _ = Ingredient.objects.get_or_create(
                nume=nume,
                defaults={"kcal_per_100g": kcal},
            )
            ingrediente_obj[nume] = obj

        retete_data = [
            {
                "titlu": "Piept de pui la tigaie cu orez basmati și legume",
                "descriere": "O masă echilibrată, bogată în proteine, gata în 25 de minute.",
                "pasi_preparare": "1. Fierbe orezul basmati 12 minute.\n2. Taie pieptul de pui cubulețe și rumenește-l în ulei de măsline cu usturoi.\n3. Adaugă ardeiul gras și morcovul tăiate fâșii și mai gătește 5 minute.\n4. Servește alături de orezul cald.",
                "timp_preparare_min": 25,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("Piept de pui", 200),
                    ("Orez basmati", 150),
                    ("Ardei gras", 80),
                    ("Morcovi", 60),
                    ("Ulei de măsline", 10),
                    ("Usturoi", 5),
                ],
            },
            {
                "titlu": "Omletă țărănească cu telemea, roșii și spanac",
                "descriere": "Mic dejun sățios și rapid cu legume proaspete.",
                "pasi_preparare": "1. Bate ouăle cu un praf de sare și piper.\n2. Călește ușor spanacul și roșiile tăiate cuburi într-o tigaie cu puțin unt.\n3. Toarnă ouăle bătute și presară telemeaua sfărâmată deasupra.\n4. Gătește 4-5 minute la foc mic.",
                "timp_preparare_min": 12,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("Ouă", 180),
                    ("Telemea de vacă", 50),
                    ("Roșii", 80),
                    ("Spanac proaspăt", 40),
                    ("Unt", 10),
                ],
            },
            {
                "titlu": "Paste integrale cu piept de pui, ciuperci și sos cremos",
                "descriere": "Paste aromate cu ciuperci trase la tigaie și sos fin de smântână.",
                "pasi_preparare": "1. Fierbe pastele integrale conform instrucțiunilor.\n2. Rumenește pieptul de pui și ciupercile feliate în ulei de măsline.\n3. Adaugă usturoiul zdrobit și smântâna de gătit, lăsând să scadă 3 minute.\n4. Amestecă pastele cu sosul obținut.",
                "timp_preparare_min": 30,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("Paste integrale", 180),
                    ("Piept de pui", 150),
                    ("Ciuperci champignon", 120),
                    ("Smântână de gătit", 80),
                    ("Ulei de măsline", 10),
                    ("Usturoi", 5),
                ],
            },
            {
                "titlu": "Salată grecească autentică cu feta și măsline",
                "descriere": "Salată proaspătă de vară, fără gătire, plină de vitamine.",
                "pasi_preparare": "1. Taie roșiile, castraveții, ardeiul gras și ceapa în bucăți potrivite.\n2. Adaugă măslinele negre și cuburile de brânză feta.\n3. Stropește totul cu ulei de măsline extravirgin și oregano.",
                "timp_preparare_min": 10,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("Roșii", 200),
                    ("Castraveți", 150),
                    ("Brânză feta", 80),
                    ("Măsline negre", 40),
                    ("Ardei gras", 60),
                    ("Ceapă galbenă", 30),
                    ("Ulei de măsline", 15),
                ],
            },
            {
                "titlu": "Somon la cuptor cu cartofi natur și lămâie",
                "descriere": "File fraged de somon aromatizat cu lămâie și usturoi.",
                "pasi_preparare": "1. Fierbe cartofii tăiați cuburi în apă cu sare timp de 15 minute.\n2. Așază fileul de somon pe hârtie de copt, unge-l cu ulei de măsline, usturoi și suc de lămâie.\n3. Coace somonul 15 minute la 190°C și servește-l cu cartofii calzi.",
                "timp_preparare_min": 30,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("File de somon", 200),
                    ("Cartofi", 220),
                    ("Lămâie", 30),
                    ("Ulei de măsline", 10),
                    ("Usturoi", 5),
                ],
            },
            {
                "titlu": "Toast cu avocado, ou poșat și roșii cherry",
                "descriere": "Brunch sănătos și cremos, bogat în grăsimi bune.",
                "pasi_preparare": "1. Prăjește feliile de pâine integrală.\n2. Pasează avocado cu un strop de lămâie și sare, apoi întinde-l pe pâine.\n3. Pune deasupra oul gătit și roșiile tăiate jumătăți.",
                "timp_preparare_min": 15,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("Pâine integrală", 90),
                    ("Avocado", 100),
                    ("Ouă", 120),
                    ("Roșii", 60),
                    ("Lămâie", 10),
                ],
            },
            {
                "titlu": "Terci de ovăz cu banană, lapte și miere",
                "descriere": "Mic dejun dulce și energizant, gata în mai puțin de 10 minute.",
                "pasi_preparare": "1. Fierbe fulgii de ovăz în lapte la foc mic timp de 5-6 minute, amestecând continuu.\n2. Pune terciul într-un bol, adaugă banana feliată și stropește cu miere.",
                "timp_preparare_min": 8,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("Fulgi de ovăz", 70),
                    ("Lapte 1.5%", 200),
                    ("Banană", 100),
                    ("Miere", 15),
                ],
            },
            {
                "titlu": "Salată rapidă cu ton, porumb și iaurt grecesc",
                "descriere": "O cină ușoară și proteică fără maioneză.",
                "pasi_preparare": "1. Scurge tonul și porumbul dulce.\n2. Amestecă-le într-un bol cu castraveți cubulețe, ceapă tocată fin și iaurt grecesc.\n3. Potrivește de sare, piper și suc de lămâie.",
                "timp_preparare_min": 10,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("Ton în suc propriu", 140),
                    ("Porumb dulce", 80),
                    ("Iaurt grecesc 2%", 70),
                    ("Castraveți", 80),
                    ("Ceapă galbenă", 25),
                    ("Lămâie", 10),
                ],
            },
            {
                "titlu": "Ciuperci sotate cu usturoi, spanac și telemea",
                "descriere": "Garnitură sau fel principal vegetarian plin de savoare.",
                "pasi_preparare": "1. Taie ciupercile felii și sotează-le în unt 7-8 minute.\n2. Adaugă usturoiul tocat și frunzele de spanac până se înmoaie.\n3. Presară telemea rasă deasupra înainte de servire.",
                "timp_preparare_min": 15,
                "status": "APPROVED",
                "sursa": "AI",
                "ingrediente": [
                    ("Ciuperci champignon", 250),
                    ("Spanac proaspăt", 100),
                    ("Telemea de vacă", 60),
                    ("Unt", 15),
                    ("Usturoi", 8),
                ],
            },
            {
                "titlu": "Supă cremă de morcovi și cartofi cu crutoane",
                "descriere": "Supă catifelată, reconfortantă și ușor de digerat.",
                "pasi_preparare": "1. Fierbe morcovii, cartofii și ceapa tăiate bucăți timp de 20 de minute.\n2. Pasează legumele cu blenderul vertical adăugând puțin unt.\n3. Servește cu cubulețe de pâine integrală rumenită.",
                "timp_preparare_min": 30,
                "status": "APPROVED",
                "sursa": "USER",
                "ingrediente": [
                    ("Morcovi", 250),
                    ("Cartofi", 200),
                    ("Ceapă galbenă", 60),
                    ("Unt", 15),
                    ("Pâine integrală", 50),
                ],
            },
            {
                "titlu": "Bowl proteic cu orez, somon, avocado și castraveți",
                "descriere": "Inspirat din poke bowl, proaspăt și sățios.",
                "pasi_preparare": "1. Pune orezul basmati fiert la baza unui bol.\n2. Așază deasupra bucățile de somon gătit, feliile de avocado și castraveții.\n3. Stropește cu suc de lămâie.",
                "timp_preparare_min": 20,
                "status": "PENDING",
                "sursa": "AI",
                "ingrediente": [
                    ("Orez basmati", 150),
                    ("File de somon", 140),
                    ("Avocado", 70),
                    ("Castraveți", 80),
                    ("Lămâie", 15),
                ],
            },
            {
                "titlu": "Clătite proteice din ovăz și banană",
                "descriere": "Desert sănătos fără zahăr rafinat, gata în 15 minute.",
                "pasi_preparare": "1. Pasează banana și amestec-o cu ouăle, fulgii de ovăz măcinați și laptele.\n2. Coace clătite mici într-o tigaie antiaderentă câte 2 minute pe fiecare parte.\n3. Servește cu iaurt grecesc și miere.",
                "timp_preparare_min": 15,
                "status": "PENDING",
                "sursa": "USER",
                "ingrediente": [
                    ("Banană", 120),
                    ("Ouă", 120),
                    ("Fulgi de ovăz", 60),
                    ("Lapte 1.5%", 60),
                    ("Iaurt grecesc 2%", 50),
                    ("Miere", 10),
                ],
            },
        ]

        create_count = 0
        for item in retete_data:
            reteta, created = Recipe.objects.get_or_create(
                titlu=item["titlu"],
                defaults={
                    "descriere": item["descriere"],
                    "pasi_preparare": item["pasi_preparare"],
                    "timp_preparare_min": item["timp_preparare_min"],
                    "status": item["status"],
                    "sursa": item["sursa"],
                    "autor": autor_default,
                },
            )

            calorii_totale = 0.0
            for nume_ing, grame in item["ingrediente"]:
                ing_obj = ingrediente_obj[nume_ing]
                RecipeIngredient.objects.get_or_create(
                    reteta=reteta,
                    ingredient=ing_obj,
                    defaults={"cantitate_grame": grame},
                )
                calorii_totale += (ing_obj.kcal_per_100g * grame) / 100.0

            reteta.calorii_totale = round(calorii_totale, 1)
            reteta.save(update_fields=["calorii_totale"])
            if created:
                create_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Gata! Au fost adăugate {create_count} rețete noi și {len(ingrediente_obj)} ingrediente în baza de date."
            )
        )