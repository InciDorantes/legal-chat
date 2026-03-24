import fitz
import re
from config import names
delete_words = ["CAPÍTULO","TÍTULO","LIBRO","SECCIÓN"]

def extract_text(pdf):
    doc_text = ""
    try:
        doc = fitz.open(pdf)
        for page in doc:
            doc_text +=page.get_text()
        return doc_text
    except:
        return " "

def limpiar_texto(texto, lista_negra):
    lista_negra_limpia = [" ".join(p.split()).lower() for p in lista_negra]
    texto_limpio = []
    for linea in texto.splitlines():
        linea_normalizada = " ".join(linea.split()).lower()
        if linea_normalizada and not any(prohibido in linea_normalizada for prohibido in lista_negra_limpia) and not linea_normalizada.isdigit():
           texto_limpio.append(linea)
    texto_final = "\n".join(texto_limpio).strip()
    return texto_final

def split_chunks(texto, patron):
    pre_chunks = []
    for l in re.split(patron, texto):
        if l:
            pre_chunks.append(l)
    
    art = 0
    chunks =[]
    pre = []
    for i in pre_chunks:
        if "Artículo" in i and art == 0:
            pre.append(i)
            art = 1
        elif "Artículo" not in i and art ==1:
            pre.append(i)
        elif "Artículo" in i and art ==1:

            texto_com = "\n".join(pre).strip()
            chunks.append(texto_com)
            pre = []
            pre.append(i)
            art = 1
    texto_com = "\n".join(pre).strip()       
    chunks.append(texto_com)

    resultado = []

    for item in chunks:
        item_stripped = item.strip()
        
        if item_stripped.startswith("Artículo"):
            resultado.append(item)
        else:
            if resultado:
                resultado[-1] = resultado[-1] + " " + item
            else:
                resultado.append(item)
    
    chunks_limpio_final= []
    for i, l in enumerate(resultado):
        if i == 0:
            chunks_limpio_final.append(l)
        elif any(prohibido in l for prohibido in delete_words):
            resultado = re.split(r"CAPÍTULO|TÍTULO|SECCIÓN|LIBRO", l)
            chunks_limpio_final.append(resultado[0])
        else:
            chunks_limpio_final.append(l)
    
    return chunks_limpio_final

def ETL (pdf, lista_negra, patron):
    etapa_uno = extract_text(pdf)
    etapa_dos = limpiar_texto(etapa_uno, lista_negra)
    etapa_tres = split_chunks(etapa_dos, patron)

    return etapa_tres

def chunks (ley,data):
    chunks = []
    patron = r"(Artículo\s+\d{1,3}(?:\s+[A-Za-z]+)?\.)\s*(.*)"
    for i, l in enumerate(data):
        if i != 0:
            match = re.search(patron, l, re.DOTALL)
            if match:
                articulo = match.group(1)
                articulo_limpio= " ".join(articulo.split())
                txt = match.group(2) if match.group(2) else "NA"
                txt_limpio = txt.lstrip(" \n\r\t.-")
                chunk = {
                  "ley_corto":ley,
                  "ley_largo":names[ley],
                  "articulo":articulo_limpio,
                  "texto": txt_limpio
                }
                chunks.append(chunk)
    return chunks