# ============================================================================
# EJERCICIO 9: GENERADOR DE CONTRASEÑAS
# ============================================================================
"""
OBJETIVO: Crear una función que genere contraseñas aleatorias seguras.

REQUISITOS:
- Crear una función generar_contraseña(longitud)
- La función debe generar una contraseña con:
  * Letras mayúsculas
  * Letras minúsculas
  * Números
  * Al menos un carácter especial (!@#$%&*)
- Usar el módulo random para seleccionar caracteres aleatorios
- La contraseña debe tener la longitud especificada
- Crear una tupla con 5 contraseñas generadas
- Mostrar todas las contraseñas

TEMAS INVOLUCRADOS: Funciones, módulos (random), strings, tuplas, bucles
"""

import random
import string

tupla_contraseñas = ()

def generar_contraseña(longitud):
    contraseña = ""
    existe_signo = False

    if longitud < 8:
        print("La contraseña debe tener una longitud minima de 8 caracteres")
    else:
        while len(contraseña) < longitud:
            caracter = random.choice(string.ascii_letters + string.digits + string.punctuation)
            contraseña += caracter
            if caracter in string.punctuation:
                existe_signo = True
            
            if len(contraseña) == longitud - 1:
                if not(existe_signo):
                    caracter = random.choice(string.punctuation)
                    contraseña += caracter
                    return contraseña
    return contraseña


menu_activo = True

while menu_activo:
    try:
        seleccion = int(input("""
=====================================

SELECCIONE UNA OPCION

=====================================

1- Generar una contraseña
2- Ver las contraseñas guardadas
3- Salir 

        """))

        if seleccion == 1:
            try:
                numero = int(input("Ingrese la longitud de caracteres de la contraseña, esta debe ser igual o mayor a 8: "))

                if numero < 8:
                    print("Ingrese un numero igual o mayor a 8")
                else:
                    contraseña = generar_contraseña(numero)
                    tupla_contraseñas += (contraseña,)
                    print(f"Se genero la contraseña: {contraseña}")
            except ValueError:
                print("Ingrese un valor numerico")

        elif seleccion == 2:
            print(f"Cantidad de contraseñas generadas: {len(tupla_contraseñas)}")
            for contraseña in tupla_contraseñas:
                print(contraseña)
        elif seleccion == 3:
            break
        else:
            print("Ingrese un valor entre el 1 y el 3")
    except ValueError:
        print("Ingrese un valor numerico")
    