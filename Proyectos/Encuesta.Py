def realizar_encuesta():
    print("Bienvenido a la encuesta.")
    nombre = input("Por favor, ingresa tu nombre: ")
    print(f"Hola {nombre}, gracias por participar en nuestra encuesta.")

    respuestas = {}
    preguntas = [
        "1. ¿Cuál es tu color favorito?",
        "2. ¿Qué tipo de comida prefieres?",
        "3. ¿Cuál es tu pasatiempo favorito?"
    ]

    for pregunta in preguntas:
        respuesta = input(pregunta + " ")
        respuestas[pregunta] = respuesta

    print("\n¡Gracias por completar la encuesta!")
    print("Aquí están tus respuestas:")
    for pregunta, respuesta in respuestas.items():
        print(pregunta)
        print("Respuesta:", respuesta)
        print("-" * 20)

if __name__ == "__main__":
    realizar_encuesta()
