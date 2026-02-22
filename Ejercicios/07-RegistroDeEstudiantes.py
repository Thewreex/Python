# ============================================================================
# EJERCICIO 3: REGISTRO DE ESTUDIANTES
# ============================================================================
"""
OBJETIVO: Crear un diccionario que almacene información de estudiantes y
permita realizar consultas.

REQUISITOS:
- Crear un diccionario con al menos 3 estudiantes
- Cada estudiante debe tener: nombre, edad, calificaciones (como lista)
- Calcular el promedio de calificaciones de cada estudiante
- Determinar qué estudiante tiene el promedio más alto
- Agregar un nuevo estudiante al diccionario
- Imprimir toda la información de forma organizada

TEMAS INVOLUCRADOS: Diccionarios, listas, bucles, operadores, funciones
"""

estudiantes = {
    "Estudiante 1": {
        "nombre": "Juan Perez",
        "edad": 23,
        "calificaciones": [7.0, 5.4, 3.9, 6.5, 5.5]
    },
    "Estudiante 2": {
        "nombre": "Pedro Dominguez",
        "edad": 19,
        "calificaciones": [5.0, 3.9, 4.1, 6.0, 2.0]
    },
    "Estudiantes 3": {
        "nombre": "Pablo Domingo",
        "edad": 20,
        "calificaciones": [5.9, 4.2, 6.9, 3.2, 6.6]
    }
}


estudiantes["Estudiante 4"] = {
    "nombre": "Pablo Buendia",
    "edad": 24,
    "calificaciones": [3.2, 2.9, 7.0, 7.0, 5.2]
}

mayor_promedio = ["", 0]

print("""
==================================

 PROMEDIO DE NOTAS DE LOS ALUMNOS

==================================
""")
for estudiante in estudiantes:
    promedio = round(sum(estudiantes[estudiante]["calificaciones"]) / len(estudiantes[estudiante]["calificaciones"]), 2)
    print(f"{estudiantes[estudiante]['nombre']} = {promedio}") 
    if promedio > mayor_promedio[1]:
        mayor_promedio = [estudiantes[estudiante]["nombre"], promedio]

print(f"""
El estudiante con mayor promedio es: {mayor_promedio[0]} con un promedio {mayor_promedio[1]}""")