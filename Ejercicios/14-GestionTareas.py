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

lista_tareas = []

class Tarea:
    def __init__(self, titulo, descripcion, fecha_creacion, completada, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.completada = completada
        self.prioridad = prioridad


menu_activo = True

while menu_activo:
    try:
        seleccion = int(input("""
=====================================

MENU DE TAREAS

=====================================


        """))

