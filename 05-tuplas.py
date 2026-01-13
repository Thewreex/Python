# Tuplas

mi_tupla = tuple() # Inicializar tuplas
mi_otra_tupla = ("JP", 9)

mi_tupla = (35, 1.77, "Juan", "Pablo") # Ingresar datos
print(mi_tupla)

print(mi_tupla[0]) # Imprimir un valor especifico

print(mi_tupla.index("Pablo")) # Indica el valor del indice de un dato especifico

# mi_tupla[1] = 1.80  Da error, puesto que las tuplas son inmutables
# print(mi_tupla)

mi_tupla_sumada = mi_tupla + mi_otra_tupla

print(mi_tupla_sumada) # Sumar tuplas si es posible, puesto que se crea una nueva tupla, no modifica

mi_tupla_lista = list(mi_tupla) # Cambia una tupla a una lista, para que ahora pueda ser mutable

print(type(mi_tupla_lista))

mi_tupla_lista[0] = "21"

print(mi_tupla_lista)

print(type(tuple(mi_tupla_lista)))