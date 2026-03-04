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

contacto = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingresa el numero telefonico del contacto: ")
    email = input("Ingrese el email del contacto: ")

    if nombre in contacto:
            print("El contacto ya existe, ingrese uno nuevo")
    else:
        contacto[nombre] = {
            "Nombre": nombre,
            "Telefono": telefono,
            "Email": email
            }
        print("Ingreso realizado correctamente")

def buscar_contacto():
    nombre_seleccionado = input("Ingrese el nombre para consultar: ")

    if nombre_seleccionado in contacto:
        if contacto[nombre_seleccionado]:
            print(f"""
Nombre: {contacto[nombre_seleccionado]["Nombre"]}
Telefono: {contacto[nombre_seleccionado]["Telefono"]}
Email: {contacto[nombre_seleccionado]["Email"]}
            """) 
    else:
        print("El contacto no existe")

def eliminar_contacto():
    nombre_borrar = input("Ingrese el nombre del contacto a borrar: ")

    if nombre_borrar in contacto:
        if contacto[nombre_borrar]:
            del contacto[nombre_borrar]
            print("El contacto fue borrado de forma exitosa")
    else:
        print("El valor ingresado no existe")

def mostrar_contacto():
    for index, cont in contacto.items():
        print(f"Nombre: {cont["Nombre"]} -- Telefono: {cont["Telefono"]} -- Email: {cont["Email"]}")
    


menu_activo = True
while menu_activo:
    try:
        seleccion = int(input(f"""
    ===================================================

    SELECCIONE UNA ACCION A REALIZAR

    ===================================================

    1: Agregar un contacto nuevo
    2: Buscar un contacto por su nombre
    3: Eliminar un contacto
    4: Mostrar todos los contactos
    0: Salir
        """))

        if seleccion == 1:
            agregar_contacto()
        elif seleccion == 2:
            buscar_contacto()
        elif seleccion == 3:
            eliminar_contacto()
        elif seleccion == 4:
            mostrar_contacto()
        elif seleccion == 0:
            menu_activo = False
        else:
            print("Seleccione un numero del 0 al 4")
    
    except ValueError:
        print("El valor ingresado es invalido, ingrese solo numeros")

