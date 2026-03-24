from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
print(GEMINI_API_KEY)
GEMINI_API_KEY_CRUDO ='AIzaSyCvAp2puxKoW2k9NuzVxsnMgQumzZmdV7oe'
print(GEMINI_API_KEY_CRUDO)

def get_client(api_key):
    return genai.Client(api_key=api_key)

def generar_respuesta(prompt):
    keys = [GEMINI_API_KEY_CRUDO,GEMINI_API_KEY]

    for key in keys:
        try:
            client = get_client(key)
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite-preview",
                contents=prompt
            )
            return response.text

        except Exception as e:
            print(f"Falló con key {key}...: {e}")

    raise Exception("Todas las API keys fallaron")

# uso
print(generar_respuesta("Hola"))