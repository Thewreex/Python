# Strings

mi_string = "Mi string"
mi_otro_string = "Mi otro string"

print(len(mi_string))
print(len(mi_otro_string))

print(mi_string + " " + mi_otro_string) # Concatenara con espacio

mi_string_con_salto_de_linea = "Este es mi string\ncon salto de linea"
print(mi_string_con_salto_de_linea)

string_tabulado = "\tEste es un string con tabulacion"
print(string_tabulado)

string_con_scape = "\\tEste es un string \n escapado"
print(string_con_scape)

# Formateo

name, surname, age = "Juan", "Pablo", 20

print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Funcion para formatear los datos
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Funcion para insertar los datos
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Funcion para formatear los datos mas resumida

# Desempaquetado de caracteres


lenguaje = "Python"

# Da error, al no haber suficientes variables
# a, b = lenguaje

# print(a)
# print(b)

# Version correcta

a, b, c, d, e, f = lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division

lenguaje_slice = lenguaje[1:3] # No cuenta el segundo numero
print(lenguaje_slice)

lenguaje_slice = lenguaje[1:] # Empezar desde el primero
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2] # segundo valor desde el final
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:6:3] # El tercer numero refleja hasta donde debe saltar, en este caso, solo tomara los numeros 0, 3, 6, 9 . . . 3n
print(lenguaje_slice)


# Reverse

lenguaje_reverse = lenguaje[::-1] # Da vuelta a la cadena
print(lenguaje_reverse)

# Funciones

print(lenguaje.capitalize()) # Deja la primera letra en mayuscula
print(lenguaje.upper()) # Deja todo en mayuscula
print(lenguaje.count("t")) # Cuenta cuantas veces se repite un caracter en la cadena
print(lenguaje.isnumeric()) # Verifica si es numero entero
print(lenguaje.lower()) # Pone toda la cadena en minuscula
print(lenguaje.isupper()) # Verifica si esta en mayuscula
print(lenguaje.startswith("py")) # Verifica si una cadena empieza con cierta cadena