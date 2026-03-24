# Legal Chat AI

Asistente inteligente basado en IA diseñado para brindar orientación legal, en el ámbito presupuestal y de administración pública, facilitando la comprensión de leyes, generación de documentos y análisis de situaciones presupuestales.

---

## Descripción

**Legal Chat AI** es una aplicación que utiliza modelos de lenguaje natural para simular asesoramiento presupuestal.  

Permite a los usuarios:
- Obtener orientación sobre situaciones legales
- Generar textos legales (oficios, justificaciones, etc.)
- Interpretar información jurídica de forma sencilla

---

## Tecnologías

- Python 3.13+
- Cuenta de Google AI Studio con API key de Gemini
- Embeddings
- ChromaDB / Vectorstore


---
## Estructura del proyecto

```
legal-chat/
│── app.py             # chatbot
│── config.py          # variables generales
│── docs_limpieza.py   # Proceso ETL
│── embedding.py       # Funciones para vectorizar y hacer los embeddings
│── main.py            # Inicialización (ejecución de la extracción, de los embeddings y de la colección)
│── retrieval.py       # Retriaval del vectorstore 
│── llm_model.py       # Configuración del modelo de lenguaje
│── requirements.txt   # Dependencias
│── .env               # Variables de entorno 
```

----

## Instalación y uso

1. Clona el repositorio:
```bash
git clone https://github.com/InciDorantes/legal-chat.git
cd legal-chat

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## Configuración

Crea un archivo `.env` en la raíz del proyecto:

```
GEMINI_API_KEY=tu_api_key_aqui
```

Puedes obtener tu API key en [Google AI Studio](https://aistudio.google.com/).

---

## Uso

1. Para configurar las fuentes y tu vectorstore
```bash
python main.py
```
2. Para chatear
 ```bash
python app.py
```  

## Autora

Inci Dorantes Malpica
[LinkedIn](https://www.linkedin.com/in/inci-dorantes-malpica-366b131b9/) 
| [GitHub](https://github.com/InciDorantes)
