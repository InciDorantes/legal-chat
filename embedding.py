from sentence_transformers import SentenceTransformer
import chromadb

import re
import numpy as np

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
cliente = chromadb.PersistentClient(path="./vectorstore")
coleccion = cliente.get_or_create_collection(
    name     = "leyes_yucatan",
    metadata = {"hnsw:space": "cosine"}
)

patron = r"Artículo\s*(.*?)\."

def vectorizar (data):
    vectore_store = []
    for l in data:
        vector = model.encode(l['texto'])  
        match = re.search(patron, l['articulo'], re.DOTALL)
        id = f"{l['ley_corto']}-{match.group(1)}"
        document = f"{l['articulo']}- {l['texto']}"

        emb = {
            "id":id,
            "document":document,
            "metadata": l,
            "embedding":vector
        }
        vectore_store.append(emb)

    return vectore_store

def vector_db (vector_store):
    ids = []
    documents = []
    metadatas = []
    embeddings = []
    for v in vector_store:
        ids.append(v['id'])
        documents.append(v['document'])
        metadatas.append(v['metadata'])
        emebding = (v['embedding']).tolist()
        embeddings.append(emebding)

    coleccion.upsert(
        ids        = ids,
        documents  = documents,
        metadatas  = metadatas,
        embeddings = embeddings
    )

    return coleccion