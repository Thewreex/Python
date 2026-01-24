# Diccionario

mi_diccionario = dict()
mi_otro_diccionario = {} # Inicializar Un Diccionario

print(type(mi_diccionario))
print(type(mi_otro_diccionario))

# Ingresar datos en un diccionario

mi_otro_diccionario = {
    "Nombre":"Juan Pablo",
    "Apellido":"Diaz",
    "Edad": 20,
    1: "Python"
}

mi_diccionario = {
    "Nombre":"Juan Pablo",
    "Apellido":"Diaz",
    "Edad": 20,
    "Lenguajes": {"Python", "C#", "JavaScript"}
    }

print(mi_diccionario)
print(mi_otro_diccionario)

print(len(mi_diccionario)) # Cuenta por vada claves tiene el diccionario

print(mi_diccionario["Nombre"]) # Imprime el valor del elemento del diccionario

mi_diccionario["Nombre"] = "Pedro" # Actualiza el valor de la clave especificada del diccionario
print(mi_diccionario["Nombre"])

mi_diccionario["Estatura"] = 1.82
print(mi_diccionario) # Agrega una nueva clave al diccionario

del mi_diccionario["Estatura"] # Elimina una clave del diccionario
print(mi_diccionario)

print("Diaz" in mi_diccionario)
print("Diez" in mi_diccionario)
print("Diaz" in mi_diccionario["Apellido"]) # Consultar si existen claves o valores en el diccionario

print(mi_diccionario.items()) # Imprime una lista con todos los items del diccionario
print(mi_diccionario.keys()) # Imprime todas las llaves del diccionario
print(mi_diccionario.values()) # Imprime todos los valores del diccionario

mi_lista = ["Nombre", "Empresa"]
mi_nuevo_diccionario = dict.fromkeys((mi_lista)) 
print(mi_nuevo_diccionario) # Crea un diccionario con los datos de una lista
mi_nuevo_diccionario = dict.fromkeys(mi_lista, 1)
print(mi_nuevo_diccionario) # Crea el nuevo diccionario con un valor especifico