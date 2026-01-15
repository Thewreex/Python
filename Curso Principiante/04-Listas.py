# Listas

mi_lista = list() # Crear listas
mi_otra_lista = [] # Otra forma para crear listas

print(len(mi_lista)) # Imprime la cantidad de datos en la lista

mi_lista = [35, 24, 62, 52, 30, 30, 17]

print(mi_lista) 
print(len(mi_lista)) 

mi_otra_lista = [20, 1.82, "Juan", "Pablo"] # Se pueden agregar variedad de datos
 
print(type(mi_otra_lista)) # Imprime valor de tipo list

print(mi_otra_lista[0]) # Elige un valor de la lista segun su posicion, empezando desde el 0
print(mi_otra_lista[1]) # Elige el segundo valor
print(mi_otra_lista[-1]) # Elige el primer valor empezando del final
print(mi_otra_lista[-4]) # Elige el cuarto valor empezando del final
# print(mi_otra_lista[-5])  al escribir un valor que supera la longitud del array, da error
print(mi_lista.count(30)) # la funcion count retorna el numero de apariciones de un valor en la lista

edad, altura, name, apellido = mi_otra_lista # Separar los valores de un array en variables
print(name)

print(mi_lista + mi_otra_lista) # Concatenacion de listas

mi_otra_lista.append("UNAB") # añade un nuevo elemento al final del array
print(mi_otra_lista)

mi_otra_lista.insert(1, "Azul") # Añade un nuevo elemento en una posicion especifica
print(mi_otra_lista)

mi_otra_lista[1] = "Rojo"
print(mi_otra_lista)

mi_otra_lista.remove("Rojo") # Elimina un elemento indicado
print(mi_otra_lista)

mi_lista.pop() # Quita el ultimo elemento
print(mi_lista)

mi_lista.pop(2) # Quita un elemento especifico por su indice
print(mi_lista)

mi_nueva_lista = mi_lista.copy() # Asigna el valor a la variable del estado actual de la variable a copiar


mi_lista.clear() # Elimina todos los elementos
print(mi_lista) 
print(mi_nueva_lista)

mi_nueva_lista.reverse() # Da vuelta la lista
print(mi_nueva_lista)

mi_nueva_lista.sort() # Ordena de menor a mayor 
print(mi_nueva_lista)

print(mi_nueva_lista[1:4]) # Crea sublistas