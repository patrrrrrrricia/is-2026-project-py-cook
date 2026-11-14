import json
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Încarcă cheia din fișierul .env de lângă manage.py
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

# Modelele încercate pe rând: dacă primul e ocupat, trece la următorul
MODELE = ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-3.7-flash"]

# Cât așteptăm răspunsul unui model, în milisecunde (60 de secunde)
TIMP_MAXIM_MS = 60000

PROMPT = """Ești un bucătar. Inventează o rețetă folosind în principal aceste ingrediente: {ingrediente}.
Poți presupune că utilizatorul are sare, piper, ulei și apă.
Scrie totul în limba română.
Răspunde DOAR cu JSON, exact în acest format:
{{
  "titlu": "numele rețetei",
  "ingrediente": [{{"nume": "ou", "grame": 120}}],
  "pasi": ["primul pas", "al doilea pas"],
  "timp_minute": 20
}}"""


class EroareAI(Exception):
    """Orice problemă cu AI-ul: lipsește cheia, nu răspunde sau răspunde greșit."""


def genereaza_reteta(ingrediente):
    """Primește o listă de ingrediente și întoarce o rețetă (dicționar) inventată de AI."""
    cheie = os.getenv("GEMINI_API_KEY")
    if not cheie:
        raise EroareAI("Lipsește GEMINI_API_KEY din fișierul .env")

    client = genai.Client(
        api_key=cheie,
        http_options=types.HttpOptions(timeout=TIMP_MAXIM_MS),
    )

    ultima_eroare = None
    for model in MODELE:
        try:
            raspuns = client.models.generate_content(
                model=model,
                contents=PROMPT.format(ingrediente=", ".join(ingrediente)),
                config=types.GenerateContentConfig(response_mime_type="application/json"),
            )
            reteta = json.loads(raspuns.text)
            break  # a mers, ieșim din buclă
        except json.JSONDecodeError:
            raise EroareAI("AI-ul nu a răspuns cu JSON valid")
        except Exception as e:
            ultima_eroare = e  # model ocupat sau indisponibil: încercăm următorul
    else:
        raise EroareAI(f"Niciun model AI nu a răspuns: {ultima_eroare}")

    for camp in ("titlu", "ingrediente", "pasi", "timp_minute"):
        if camp not in reteta:
            raise EroareAI(f"Lipsește câmpul '{camp}' din răspunsul AI-ului")

    reteta["sursa"] = "AI"
    return reteta


# Test: rulează fișierul direct cu  python assistant/ai.py
if __name__ == "__main__":
    from pprint import pprint
    pprint(genereaza_reteta(["ou", "brânză telemea", "roșie"]))