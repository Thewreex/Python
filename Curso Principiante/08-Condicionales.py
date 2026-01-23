### Condicionales ###

# Si se cumple una condicion, se ejecuta una accion, si no, se puede ejecutar otra

mi_condicion = True

if mi_condicion:
    print("Se ejecuta la condicion del if") # Como la condicion es true, se ejecuta el codigo


mi_condicion = 5 * 4

if mi_condicion == 11: # Comprueba si el valor de mi condicion cumple con la igualdad
    print("Se esta ejecutando condicion del segundo if")

if mi_condicion >= 10: 
    print("Se esta ejecutando condicion del tercer if")


if mi_condicion > 10:  # Con el else, puedes ejecutar codigo si no se cumple la condicion
    print("El valor es mayor que 10")
else:
    print("Es menor o igual que 10")



if mi_condicion > 10 and mi_condicion < 20: # Uso de operadores logicos para las condicionales
    print("El valor es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


if mi_condicion > 10 and mi_condicion < 20: # Usar mas de una condicion, va por jerarquia, si el primer if no cumple, pasa al siguente elif.
    print("El valor es mayor que 10 y menor que 20")
elif mi_condicion == 1:
    print("El valor es 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


mi_cadena = "Cadena" 

if mi_cadena:
    print("Mi cadena de texto no es vacia") # Las cadenas de texto vacias son tomadas como false


if mi_cadena == "Cadena": # Verifica si 2 cadenas son iguales
    print("Las cadenas de texto coinciden")

if not mi_cadena == "Casdena": # Verifica si 2 cadenas son iguales
    print("Las cadenas de texto coinciden")

