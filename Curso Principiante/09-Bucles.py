### Bucles ###

# While

mi_condicion = 0

while mi_condicion <= 10: # Se le pasa una condicion al bucle, mientras la condicion sea true, seguira ejecuando el codigo
    print(mi_condicion)
    mi_condicion += 1 # Suma 1 en cada iteracion, cuando llegue a 10, se detendra el bucle
else:
    print("Mi condicion es mayor que 10") # Funcion que se ejecuta al terminar el bucle


while mi_condicion <= 20: 
    mi_condicion += 1 
    print(mi_condicion)
    if mi_condicion == 15: # Implementacion de un if dentro para ejecutar una condicion dentro del bucle
        print("El valor de la condicion es igual 15")
        break # Break nos permite detener el bucle
else:
    print("Mi condicion es mayor que 20") 


# For 

# Itera por cada elemento que hay en una lista, sirve para todo tipo de conjunto de datos


# For con lista
mi_lista = [22, 19, 30, 49, 12, 40, 23]

for element in mi_lista:
    print(element)

# For con tupla

mi_tupla = (35, 1.77, "Juan", "Pablo")

for element in mi_tupla:
    print(element)

# For con Set

mi_set = {"Juan", "Pablo", 20}

for element in mi_set:
    print(element)


# For con diccionario (llaves)

mi_diccionario = {
    "Nombre":"Juan Pablo",
    "Apellido":"Diaz",
    "Edad": 20,
    "Lenguajes": {"Python", "C#", "JavaScript"}
    }

for element in mi_diccionario:
    print(element)

# For con diccionario (Valores)

for element in (mi_diccionario.values()):
    print(element)
else:
    print("El bucle for para mi diccionario ha terminado") # Tambien se pueden usar else

for element in mi_diccionario:
    print(element)
    if element == "Edad":
        continue # Continue nos permite seguir con el bucle desde el inicio, ignorando todo lo que viene despues
    else:
        print("Se Ejecuta")
else:
    print("El bucle for para diccionario a finalizado")