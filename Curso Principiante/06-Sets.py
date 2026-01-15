# Sets

my_set = set()
mi_otro_set = {}

print(type(mi_otro_set)) # al definirlo con corchetes vacios, inicia como diccionario

mi_otro_set = {"Juan", "Pablo", 20}

print(type(mi_otro_set)) # al definirlo con datos, se define como set

print(len(mi_otro_set)) # Imprime la cantidad de elementos del set

# print (mi_otro_set[0]) no se pueden acceder a los elementos como en las listas

mi_otro_set.add("JP") # Con el comando add se pueden agregar elementos
print(mi_otro_set) # Los sets no son estructuras ordenadas, por lo cual no se puede acceder a elementos especificos

mi_otro_set.add(20)
print(mi_otro_set) # El set no admite repetidos

print("Juan" in mi_otro_set)
print("PaBlo" in mi_otro_set ) # Indica si el valor existe en el set

mi_otro_set.remove("Pablo") # Borra un dato especifico del set
print(mi_otro_set)

mi_otro_set.clear() # Limpia el set
print(mi_otro_set)

mi_otro_set = {"Juan", "Pablo", 20}


mi_otro_set = list(mi_otro_set)
print(type(mi_otro_set)) # Cambia el set a lista
mi_otro_set = set(mi_otro_set)

mi_set_lenguajes = {"Python", "Javascript", "CSharp"}
mi_nuevo_set = mi_otro_set.union(mi_set_lenguajes)
print(mi_nuevo_set) # Unifica 2 sets

print(mi_nuevo_set.difference(mi_otro_set)) # Indica los elementos que posee un set y que el otro no