from config import archivos, basura_lpcg, basura_capy, basura_recapy, patron_1, patron_2
from docs_limpieza import ETL, chunks
from embedding import vectorizar, vector_db

#1. Extracción y limpieza
etl_lpcg  = ETL(archivos['LPCGEY'],basura_lpcg, patron_1)
etl_capy = ETL(archivos['CAPY'],basura_capy,patron_1 )
etl_recapy = ETL(archivos['RECAPY'],basura_recapy,patron_2 )

#2. Generación de Chunks
chunks_lpcg  = chunks ('LPCG',etl_lpcg)
chunks_capy = chunks ('CAPY',etl_capy)
chunks_recapy = chunks ('RECAPY',etl_recapy)

#3.Vectorizar y preparar metadata
vs_lpcg   = vectorizar(chunks_lpcg)
vs_capy   = vectorizar(chunks_capy)
vs_recapy = vectorizar(chunks_recapy)

#4. Guardar en el vector_db
coleccion = vector_db(vs_lpcg + vs_capy + vs_recapy)

'''
Esta exportación sirve para verificar los chunks

with open("output/lpcg.txt", "w", encoding="utf-8") as f:
    for item in chunks_lpcg:
        f.write(f"{item}\n")

with open("output/capy.txt", "w", encoding="utf-8") as f:
    for item in chunks_capy:
        f.write(f"{item}\n")

with open("output/recapy.txt", "w", encoding="utf-8") as f:
    for item in chunks_recapy:
        f.write(f"{item}\n")

'''

