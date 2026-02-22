### EJERCICIOS DE PRÁCTICA - PYTHON PRINCIPIANTE ###

"""
Este archivo contiene una serie de ejercicios que integran todos los temas
que has estudiado en tu curso de Python. Cada ejercicio tiene una descripción
de lo que debes lograr.

INSTRUCCIONES:
- Lee cada ejercicio cuidadosamente
- Escribe tu código debajo de cada descripción
- Puedes ejecutar cada ejercicio por separado comentando los demás
- Intenta resolver los ejercicios sin mirar las soluciones primero
"""

# ============================================================================
# EJERCICIO 1: CALCULADORA DE EDAD
# ============================================================================
"""
OBJETIVO: Crear un programa que calcule la edad de una persona y determine
si es mayor de edad.

REQUISITOS:
- Usar el módulo datetime para obtener el año actual
- Solicitar al usuario su año de nacimiento usando input()
- Calcular la edad restando el año de nacimiento del año actual
- Usar condicionales para determinar si es mayor de edad (18+)
- Imprimir un mensaje personalizado con formato f-string

TEMAS INVOLUCRADOS: Variables, operadores, strings, condicionales, módulos, input
"""

# Tu código aquí:




# ============================================================================
# EJERCICIO 2: GESTOR DE LISTA DE COMPRAS
# ============================================================================
"""
OBJETIVO: Crear un sistema para gestionar una lista de compras con diferentes
operaciones.

REQUISITOS:
- Crear una lista vacía para almacenar productos
- Agregar al menos 5 productos a la lista
- Mostrar la lista completa
- Eliminar un producto específico
- Verificar si un producto existe en la lista
- Ordenar la lista alfabéticamente
- Mostrar cuántos productos hay en total

TEMAS INVOLUCRADOS: Listas, métodos de listas, operadores, condicionales
"""

# Tu código aquí:




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

# Tu código aquí:




# ============================================================================
# EJERCICIO 4: JUEGO DE ADIVINANZA
# ============================================================================
"""
OBJETIVO: Crear un juego donde el usuario debe adivinar un número aleatorio.

REQUISITOS:
- Usar el módulo random para generar un número entre 1 y 50
- Usar un bucle while para permitir múltiples intentos
- Solicitar al usuario que ingrese un número
- Dar pistas si el número es mayor o menor
- Contar cuántos intentos tomó adivinar
- Usar try/except para manejar errores si el usuario ingresa texto en vez de número
- Terminar el juego cuando adivine correctamente

TEMAS INVOLUCRADOS: Módulos (random), bucles, condicionales, excepciones, variables
"""

# Tu código aquí:




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

# Tu código aquí:




# ============================================================================
# EJERCICIO 6: SISTEMA DE BIBLIOTECA
# ============================================================================
"""
OBJETIVO: Crear una clase Libro y gestionar una pequeña biblioteca.

REQUISITOS:
- Crear una clase Libro con propiedades: titulo, autor, año, disponible
- Crear un método para prestar el libro (cambiar disponible a False)
- Crear un método para devolver el libro (cambiar disponible a True)
- Crear un método que muestre la información del libro
- Crear al menos 3 instancias de libros
- Crear una lista con todos los libros
- Usar un bucle para mostrar solo los libros disponibles

TEMAS INVOLUCRADOS: Clases, listas, bucles, condicionales, métodos
"""

# Tu código aquí:




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

# Tu código aquí:




# ============================================================================
# EJERCICIO 8: AGENDA DE CONTACTOS
# ============================================================================
"""
OBJETIVO: Crear una agenda de contactos con un menú interactivo.

REQUISITOS:
- Crear un diccionario vacío para almacenar contactos
- Cada contacto debe tener: nombre, teléfono, email
- Crear un menú con opciones:
  1. Agregar contacto
  2. Buscar contacto por nombre
  3. Eliminar contacto
  4. Mostrar todos los contactos
  5. Salir
- Usar un bucle while para mantener el menú activo
- Usar try/except para manejar errores de entrada
- Validar que no se agreguen contactos duplicados

TEMAS INVOLUCRADOS: Diccionarios, bucles, condicionales, excepciones, input
"""

# Tu código aquí:




# ============================================================================
# EJERCICIO 9: GENERADOR DE CONTRASEÑAS
# ============================================================================
"""
OBJETIVO: Crear una función que genere contraseñas aleatorias seguras.

REQUISITOS:
- Crear una función generar_contraseña(longitud)
- La función debe generar una contraseña con:
  * Letras mayúsculas
  * Letras minúsculas
  * Números
  * Al menos un carácter especial (!@#$%&*)
- Usar el módulo random para seleccionar caracteres aleatorios
- La contraseña debe tener la longitud especificada
- Crear una tupla con 5 contraseñas generadas
- Mostrar todas las contraseñas

TEMAS INVOLUCRADOS: Funciones, módulos (random), strings, tuplas, bucles
"""

# Tu código aquí:




# ============================================================================
# EJERCICIO 10: CALCULADORA DE FECHAS
# ============================================================================
"""
OBJETIVO: Crear un programa que calcule diferencias entre fechas.

REQUISITOS:
- Usar el módulo datetime
- Solicitar al usuario una fecha de nacimiento (día, mes, año)
- Calcular cuántos días ha vivido la persona
- Calcular cuántos días faltan para su próximo cumpleaños
- Determinar qué día de la semana nació
- Mostrar toda la información de forma clara y formateada
- Usar try/except para manejar fechas inválidas

TEMAS INVOLUCRADOS: Módulos (datetime), variables, operadores, excepciones, strings
"""

# Tu código aquí:




# ============================================================================
# EJERCICIO FINAL: SISTEMA DE GESTIÓN DE TAREAS
# ============================================================================
"""
OBJETIVO: Crear un sistema completo de gestión de tareas que integre
TODOS los conceptos aprendidos.

REQUISITOS:
- Crear una clase Tarea con: titulo, descripcion, fecha_creacion, completada, prioridad
- Crear una lista para almacenar todas las tareas
- Implementar funciones para:
  * Agregar nueva tarea
  * Marcar tarea como completada
  * Eliminar tarea
  * Mostrar tareas pendientes
  * Mostrar tareas completadas
  * Filtrar tareas por prioridad (alta, media, baja)
  * Guardar tareas en un archivo de texto (opcional avanzado)
- Crear un menú interactivo con todas las opciones
- Usar excepciones para manejar errores
- Usar el módulo datetime para registrar fechas
- Ordenar tareas por prioridad o fecha

TEMAS INVOLUCRADOS: Clases, listas, diccionarios, funciones, bucles, 
condicionales, excepciones, módulos, strings, operadores
"""

# Tu código aquí:




# ============================================================================
# ¡FELICIDADES!
# ============================================================================
"""
Si completaste todos estos ejercicios, has demostrado dominio de:
✓ Variables y tipos de datos
✓ Operadores (aritméticos, comparativos, lógicos)
✓ Strings y sus métodos
✓ Listas, tuplas, sets y diccionarios
✓ Condicionales (if, elif, else)
✓ Bucles (while, for)
✓ Funciones
✓ Clases y objetos
✓ Excepciones
✓ Módulos (random, math, datetime)

¡Sigue practicando y creando tus propios proyectos!
"""
