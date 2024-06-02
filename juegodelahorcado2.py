import random

def seleccionar_palabra():
    palabras = ["programacion", "computadora", "teclado", "laptop", "pantalla", "elefante", "gato"]
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = [letra if letra in letras_adivinadas else '_' for letra in palabra]
    return ' '.join(progreso)

def jugar_ahorcado():
    palabra = seleccionar_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6
    adivinada = False

    print("¡Bienvenido al juego del Ahorcado!")
    print(mostrar_progreso(palabra, letras_adivinadas))
    print("\n")

    while not adivinada and intentos_restantes > 0:
        intento = input("Adivina una letra: ").lower()

        if len(intento) != 1:
            print("Por favor, introduce una sola letra.")
        elif intento in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        elif intento not in palabra:
            print("La letra no está en la palabra.")
            intentos_restantes -= 1
            letras_adivinadas.add(intento)
        else:
            print("¡Bien hecho! La letra está en la palabra.")
            letras_adivinadas.add(intento)

        progreso_actual = mostrar_progreso(palabra, letras_adivinadas)
        print(progreso_actual)
        print(f"Te quedan {intentos_restantes} intentos.\n")

        if '_' not in progreso_actual:
            adivinada = True

    if adivinada:
        print("¡Felicidades! Has adivinado la palabra.")
    else:
        print(f"Lo siento, has perdido. La palabra era '{palabra}'.")

if __name__ == "__main__":
    jugar_ahorcado()
            