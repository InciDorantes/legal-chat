from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY)

def generar_respuesta(pregunta, contexto):
    prompt = f"""
        Eres un consultor de Leyes Presupuestales y de administración pública del Estado de Yucatán.
        Con base al Contexto proporcionado responde la Pregunta. 
        Cuando respondas y cites, menciona en que artículo de que ley se menciona.

        Contexto:
        {contexto}

        Pregunta:
        {pregunta}
        """
    response = None
    try:
        response = client.models.generate_content(
                model='gemini-3.1-flash-lite-preview',
                contents=types.Part.from_text(text=prompt),
                config=types.GenerateContentConfig(
                    temperature=0,
                    top_p=0.95,
                    top_k=20,
                ),
            )
    except Exception as e:
        print(f"Hubo un error {e}")
        
    return response.text if response else "Error al generar el resumen"

