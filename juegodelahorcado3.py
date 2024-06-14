import random

def seleccionar_palabra(dificultad):
    palabras_faciles = ["perro", "gato", "flor", "mesa", "casa"]
    palabras_medianas = ["elefante", "jirafa", "pantalla", "computadora"]
    palabras_dificiles = ["programacion", "bicicleta", "automovil", "aeropuerto"]

    if dificultad == "facil":
        return random.choice(palabras_faciles)
    elif dificultad == "medio":
        return random.choice(palabras_medianas)
    elif dificultad == "dificil":
        return random.choice(palabras_dificiles)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = [letra if letra in letras_adivinadas else '_' for letra in palabra]
    return ' '.join(progreso)

def mostrar_ahorcado(fallos):
    estados = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]
    print(estados[fallos])


def jugar_ahorcado():
    print("¡Bienvenido al juego del Ahorcado!")
    modo_juego = input("Elige el modo de juego (1: Un jugador, 2: Dos jugadores): ")

    if modo_juego == "1":
        dificultad = input("Elige la dificultad (facil, medio, dificil): ")
        palabra = seleccionar_palabra(dificultad)
    elif modo_juego == "2":
        palabra = input("Jugador 1, introduce una palabra para que adivine el Jugador 2: ").lower()
        print("\n" * 50)  

    palabra = palabra.lower()
    letras_adivinadas = set()
    intentos_restantes = 6
    fallos = 0
    adivinada = False

    print(mostrar_progreso(palabra, letras_adivinadas))
    print("\n")

    while not adivinada and fallos < intentos_restantes:
        intento = input("Adivina una letra: ").lower()

        if len(intento) != 1:
            print("Por favor, introduce una sola letra.")
        elif intento in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif intento not in palabra:
            print("La letra no está en la palabra.")
            fallos += 1
            letras_adivinadas.add(intento)
        else:
            print("¡Bien hecho! La letra está en la palabra.")
            letras_adivinadas.add(intento)

        progreso_actual = mostrar_progreso(palabra, letras_adivinadas)
        print(progreso_actual)
        mostrar_ahorcado(fallos)
        print(f"Te quedan {intentos_restantes - fallos} intentos.\n")

        if '_' not in progreso_actual:
            adivinada = True

    if adivinada:
        print("¡Felicidades! Has adivinado la palabra.")
    else:
        print(f"Lo siento, has perdido. La palabra era '{palabra}'.")

if __name__ == "__main__":
    jugar_ahorcado()