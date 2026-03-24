from sentence_transformers import SentenceTransformer
from llm_model import generar_respuesta
import chromadb
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def retrival (question, coleccion, n_resultados = 6 ):
    emb_q = model.encode(question)
    results = coleccion.query(
        query_embeddings = [emb_q.tolist()],
        n_results = n_resultados
    )
    return results

def obtener_coleccion (path_a_vectorstore):
    cliente = chromadb.PersistentClient(path=path_a_vectorstore)
    coleccion = cliente.get_collection(name="leyes_yucatan")

    return coleccion

path = "./vectorstore"
coleccion = obtener_coleccion(path)

def retrival_question(pregunta):
    resultados = retrival(
        pregunta,
        coleccion
    )

    a = []
    for r in resultados ['metadatas'][0]:
        b = f"{r['ley_largo']}, {r['articulo']}- {r['texto']}"
        a.append(b)

    contexto = "\n ---\n".join(a)


    respuesta_modelo = generar_respuesta(pregunta, contexto)

    return respuesta_modelo
