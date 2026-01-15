# Tipos de variables

mi_variable_cadena = "Mi primera variable"
print(mi_variable_cadena)

mi_variable_int = 12
print(mi_variable_int)

mi_variable_booleana = True
print(mi_variable_booleana)

print(mi_variable_cadena, mi_variable_int, mi_variable_booleana)

# Las comas generan un espacio
print("Hola","-","Mundo")

# Pasar de entero a cadena
mi_variable_de_entero_a_cadena = str(mi_variable_int)
print(type(mi_variable_de_entero_a_cadena)) 

# Funcion que devuelve la cantidad de caracteres de una variable

print(len("Variable string de 32 caracteres")) 

# Combinacion entre cadenas y variables
print("Este es el valor de mi string:", mi_variable_cadena)
print("Este es el valor de mi entero:", mi_variable_int)
print("Este es el valor de mi booleano:", mi_variable_booleana)

# Funcion input

nombre = input("Cual es tu nombre: ")
edad = input("Cual es tu edad: ")

print("Bienvenido,", nombre, "De edad: ", edad)
