# ============================================================================
# EJERCICIO 7: PROCESADOR DE NÚMEROS
# ============================================================================
"""
OBJETIVO: Crear un programa que procese una lista de números y genere
estadísticas.

REQUISITOS:
- Crear una lista con al menos 10 números (pueden ser aleatorios)
- Usar el módulo math para calcular:
  * La raíz cuadrada del número más grande
  * El número más pequeño elevado al cuadrado
- Separar los números en dos listas: pares e impares
- Calcular el promedio de cada lista
- Usar sets para eliminar duplicados si los hay
- Mostrar todos los resultados de forma organizada

TEMAS INVOLUCRADOS: Listas, sets, módulos (math, random), bucles, operadores
"""

import math

lista_numeros = [10, 25, 32, 11, 45, 32, 90, 85 , 6 , 14, 25, 25, 11, 6]

numero_mayor = max(lista_numeros)
numero_menor = min(lista_numeros)


raiz_mayor = math.sqrt(numero_mayor)


cuadrado_menor = math.pow(numero_menor, 2)

lista_pares = [n for n in lista_numeros if n % 2 == 0]
lista_impares = [n for n in lista_numeros if n % 2 != 0]

 
promedio_lista = sum(lista_numeros) / len(lista_numeros) if lista_numeros else 0
promedio_pares = sum(lista_pares) / len(lista_pares) if lista_pares else 0
promedio_impares = sum(lista_impares) / len(lista_impares) if lista_impares else 0


sin_duplicados = set(lista_numeros)


print(f"""

DATOS DE LA LISTA DE NUMEROS: 

La raiz cuadrada del numero mayor de la lista: {raiz_mayor:.2f@}
El cuadrado del numero menor de la lista: {cuadrado_menor}
Los numeros pares de la lista son: {lista_pares}
Los numeros impares de la lista son: {lista_impares}
El promedio de los numeros de la lista es: {promedio_lista}
El promedio de los numeros pares de la lista es: {promedio_pares}
El promedio de los numeros impares de la lista es: {promedio_impares}
La lista sin duplicados es: {list(sin_duplicados)}

""")
