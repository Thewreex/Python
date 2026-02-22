# ============================================================================
# EJERCICIO 5: ANALIZADOR DE TEXTO
# ============================================================================
"""
OBJETIVO: Crear una función que analice un texto y devuelva estadísticas.

REQUISITOS:
- Crear una función llamada analizar_texto() que reciba un string
- La función debe retornar un diccionario con:
  * Número total de caracteres
  * Número de palabras
  * Número de vocales
  * Texto en mayúsculas
  * Texto en minúsculas
  * Texto invertido
- Probar la función con diferentes textos

TEMAS INVOLUCRADOS: Funciones, strings, diccionarios, bucles, operadores
"""

def analizar_texto(texto):
    vocales = "aeiou"
    texto_lower = texto.lower()
    return  {
        "Caracteres": len(texto),
        "Palabras": len(texto.split()),
        "Numero de vocales": sum(1 for char in texto_lower if char in vocales),
        "Mayuscula": texto.upper(),
        "Minuscula": texto_lower,
        "Invertido": texto[::-1]
    }


seleccion = input("Ingrese un texto: ")
resultado = analizar_texto(seleccion)


print(f"""

===============================

    INFORMACION DEL TEXTO

===============================

Numero de caracteres: {resultado["Caracteres"]}
Numero de Palabras: {resultado["Palabras"]}
Numero de vocales: {resultado["Numero de vocales"]}
Texto en mayusculas: {resultado["Mayuscula"]}
Texto en minusculas: {resultado["Minuscula"]}
Texto invertido: {resultado["Invertido"]}

    """)