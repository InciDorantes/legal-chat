archivos = {
    "LPCGEY": "data/LPCGEY.pdf",
    "CAPY":   "data/CAPY.pdf",
    "RECAPY": "data/RECAPY.pdf",
}

basura_lpcg = ["LEY DEL PRESUPUESTO", "Y CONTABILIDAD", "GUBERNAMENTAL DEL ESTADO DE YUCATÁN ","H. Congreso del Estado de Yucatán","Secretaría General", "del Poder Legislativo","Unidad de Servicios Técnico-Legislativos ","Última Ref. D.O.",'Última Reforma D.O.','Fracción recorrida D.O.','Artículo reformado D.O.','Párrafo reformado D.O']
basura_capy = ["Publicado D.O.","Última reforma D.O."]
basura_recapy =["Publicado D.O.","Última reforma D.O."]

patron_1 = r"(Artículo\s+\d{1,3}([A-Za-z]+)?(\.-)?)"
patron_2= r"(Artículo\s+\d{1,3}( \s[A-Za-z]+)?.)"

names = {
    "LPCG": "Ley del Presupuesto y Contabilidad Gubernamental del Estado de Yucatán",
    "CAPY":   "Código de la Administración Pública de Yucatán",
    "RECAPY": "Reglamento del Código de la Administración Pública de Yucatán",
}
