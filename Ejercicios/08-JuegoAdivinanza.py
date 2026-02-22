# ============================================================================
# EJERCICIO 4: JUEGO DE ADIVINANZA
# ============================================================================
"""
OBJETIVO: Crear un juego donde el usuario debe adivinar un número aleatorio.

REQUISITOS:
- Usar el módulo random para generar un número entre 1 y 50
- Usar un bucle while para permitir múltiples intentos
- Solicitar al usuario que ingrese un número
- Dar pistas si el número es mayor o menor
- Contar cuántos intentos tomó adivinar
- Usar try/except para manejar errores si el usuario ingresa texto en vez de número
- Terminar el juego cuando adivine correctamente

TEMAS INVOLUCRADOS: Módulos (random), bucles, condicionales, excepciones, variables
"""

import random

numero_random = random.randint(1, 50)


seleccion = None
intentos = 0

while True:
    try:
        if numero_random == seleccion:
            print(f"Has acertado el numero en un total de {intentos} intentos, felicidades!!")
            break
        else:
            if intentos == 0:
               seleccion = int(input("Seleccione un numero: "))
            else:
                 seleccion = int(input(f"El numero seleccionado es incorrecto, intente nuevamente\n(Pista: El numero es {'mayor' if numero_random > seleccion else 'menor'} al numero que ingresaste): "))
        intentos += 1
    except ValueError:
        print("El valor ingresado es invalido, ingrese solo numeros")

