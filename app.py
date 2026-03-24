from retrieval import retrival_question


while True:
    q = input("\nHaz una pregunta o escribe salir: ")
    if q.lower() == "salir":
        break
    
    print("\nRespuesta:\n")
    respuesta = retrival_question(q)
    print(respuesta,"\n")