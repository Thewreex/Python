"""

Ejercicio 1: La Calculadora de Propinas
Objetivo: Practicar variables, tipos de datos (int/float) y operadores aritméticos. Consigna:

Crear variables para el monto_cuenta y el porcentaje_propina.
Calcular la propina y el total a pagar.
Imprimir un mensaje con formato (f-string o concatenación) que diga: "La propina es X y el total es Y".

"""

monto_cuenta = int(input("Ingrese el total de la cuenta: "))
monto_propina = monto_cuenta * 0.15
total_pago = monto_cuenta + porcentaje_propina
print(f"La propina es de un total de {porcentaje_propina} y el valor total es de {total_pago}")