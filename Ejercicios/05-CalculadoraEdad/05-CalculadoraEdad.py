# ============================================================================
# EJERCICIO 1: CALCULADORA DE EDAD
# ============================================================================
"""
OBJETIVO: Crear un programa que calcule la edad de una persona y determine
si es mayor de edad.

REQUISITOS BÁSICOS:
- Usar el módulo datetime para obtener el año actual
- Solicitar al usuario su año de nacimiento usando input()
- Calcular la edad restando el año de nacimiento del año actual
- Usar condicionales para determinar si es mayor de edad (18+)
- Imprimir un mensaje personalizado con formato f-string

TEMAS INVOLUCRADOS: Variables, operadores, strings, condicionales, módulos, input

# ============================================================================
# 🚀 RETOS PARA MEJORAR EL EJERCICIO
# ============================================================================

NIVEL 1: VALIDACIONES BÁSICAS 🟢
--------------------------------
1. Validar que el año ingresado no sea mayor al año actual
2. Validar que el año sea razonable (entre 1900 y año actual)
3. Manejar errores cuando el usuario no ingrese un número (try-except)
   

NIVEL 2: CÁLCULO MÁS PRECISO 🟡
-------------------------------
4. Pedir también el mes y día de nacimiento para calcular la edad exacta
5. Mostrar si la persona ya cumplió años este año o aún no
6. Usar datetime.date() para crear fechas completas
   
   Conceptos nuevos: datetime.date(), comparación de fechas, métodos de fecha

NIVEL 3: FUNCIONALIDADES EXTRA 🟠
---------------------------------
7. Calcular cuántos días faltan para su próximo cumpleaños
8. Mostrar cuántos días, meses y años tiene de vida (timedelta)
9. Determinar si nació en año bisiesto
10. Calcular en qué día de la semana nació (lunes, martes, etc.)
    
    Conceptos nuevos: timedelta, calendar module, strftime(), operador %

NIVEL 4: CATEGORÍAS Y MENÚ 🔴
-----------------------------
11. Clasificar por categorías de edad:
    - Niño (0-12)
    - Adolescente (13-17)
    - Adulto joven (18-35)
    - Adulto (36-59)
    - Adulto mayor (60+)
12. Crear un menú interactivo con opciones:
    - Calcular edad
    - Ver estadísticas detalladas
    - Calcular múltiples personas
    - Salir del programa
13. Usar funciones para organizar el código
14. Guardar resultados en una lista o diccionario
    
"""

import datetime as dt
import locale
import calendar
from usuarios import datos_usuario, lista_usuarios, listar_usuarios
from calculos import calcular_edad, print_edad, estadisticas_detalladas, crear_lista_edades
from validaciones import verificar_fecha

locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

fecha_actual = dt.date.today()


menu_activo = True

while menu_activo:

    seleccion = int(input(f"""
Seleccione una accion a realizar:

1 - Ingresar la fecha de nacimiento de un usuario
2 - Calcular la edad de un usuario ingresado 
3 - Ver estadisticas detalladas
0 - Salir del programa

"""))

    if seleccion == 1:
        datos_usuario()
        menu_activo = True  


    elif seleccion == 2:
        listar_usuarios()
        menu_activo = True


    elif seleccion == 3:
        crear_lista_edades(lista_usuarios)
        estadisticas_detalladas(lista_usuarios)

    elif seleccion == 0:
        print("Cerrando Programa")
        menu_activo = False
    else:
        print("Seleccione una opcion correcta")



