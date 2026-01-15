"""

Ejercicio 2: Analizador de Texto
Objetivo: Practicar manipulación de Strings y métodos de Listas. Consigna:

Definir una variable con un texto (ej: un párrafo corto).
Contar cuántas veces aparecen letras específicas (ej: 'a', 'e').
Convertir el texto a una lista de palabras.
Invertir el orden de las palabras en la lista y mostrar el resultado.
Indicar si la palabra "Python" está presente en el texto.

"""

mi_texto = input("Ingrese un parrafo: ")
letra_seleccionada = input("Seleccione que letra desea contar: ")
repeticiones_letra = mi_texto.count(letra_seleccionada)
lista_palabras = mi_texto.split()
existe_python = "Python" in lista_palabras

print(f"El caracter {letra_seleccionada} se repite {repeticiones_letra} veces\nLa lista de palabras es: {lista_palabras}\nLa lista invertida es: {lista_palabras[::-1]}\n¿Python aparece en el parrafo?: {existe_python}")