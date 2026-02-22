import datetime as dt
from validaciones import validar_errores, verificar_fecha
from calculos import calcular_edad

fecha_actual = dt.date.today()

lista_usuarios = [
    {"Nombre": "Carlos Mendoza",     "Fecha": dt.date(1990,  3, 15)},
    {"Nombre": "María González",     "Fecha": dt.date(1985,  7, 22)},
    {"Nombre": "Juan Pérez",         "Fecha": dt.date(2000,  1,  8)},
    {"Nombre": "Ana López",          "Fecha": dt.date(1978, 11, 30)},
    {"Nombre": "Lucía Fernández",    "Fecha": dt.date(1995,  5, 12)},
    {"Nombre": "Diego Ramírez",      "Fecha": dt.date(1983,  9,  4)},
    {"Nombre": "Valentina Torres",   "Fecha": dt.date(2003,  2, 18)},
    {"Nombre": "Martín Sánchez",     "Fecha": dt.date(1970,  6, 27)},
    {"Nombre": "Camila Herrera",     "Fecha": dt.date(1998, 12,  1)},
    {"Nombre": "Sebastián Díaz",     "Fecha": dt.date(1992,  4, 10)},
    {"Nombre": "Florencia Castro",   "Fecha": dt.date(1987,  8, 23)},
    {"Nombre": "Nicolás Vega",       "Fecha": dt.date(2001, 10,  5)},
    {"Nombre": "Sofía Morales",      "Fecha": dt.date(1975,  1, 14)},
    {"Nombre": "Agustín Romero",     "Fecha": dt.date(1994,  3, 29)},
    {"Nombre": "Paula Jiménez",      "Fecha": dt.date(1989,  7,  7)},
    {"Nombre": "Federico Álvarez",   "Fecha": dt.date(1968,  5, 19)},
    {"Nombre": "Natalia Ruiz",       "Fecha": dt.date(2004, 11, 11)},
    {"Nombre": "Rodrigo Navarro",    "Fecha": dt.date(1982,  2,  3)},
    {"Nombre": "Gabriela Molina",    "Fecha": dt.date(1997,  9, 16)},
    {"Nombre": "Ignacio Ortega",     "Fecha": dt.date(1973, 12, 25)},
    {"Nombre": "Daniela Suárez",     "Fecha": dt.date(1991,  6,  8)},
    {"Nombre": "Tomás Vargas",       "Fecha": dt.date(2002,  4, 20)},
    {"Nombre": "Renata Medina",      "Fecha": dt.date(1986, 10, 13)},
    {"Nombre": "Benjamín Rojas",     "Fecha": dt.date(1979,  1, 31)},
    {"Nombre": "Isabella Gil",       "Fecha": dt.date(1996,  8,  2)},
    {"Nombre": "Valeria Ramos",      "Fecha": dt.date(1988, 11, 17)},
    {"Nombre": "Emilio Reyes",       "Fecha": dt.date(1965,  7,  9)},
    {"Nombre": "Jimena Flores",      "Fecha": dt.date(1993,  5, 24)},
    {"Nombre": "Santiago Espinosa",  "Fecha": dt.date(1980,  2, 14)},
    {"Nombre": "Antonella Cruz",     "Fecha": dt.date(1999, 12, 28)},
    {"Nombre": "Leandro Ríos",       "Fecha": dt.date(1984,  9,  3)},
    {"Nombre": "Patricio Soto",      "Fecha": dt.date(1972,  4,  1)},
    {"Nombre": "Micaela Aguilar",    "Fecha": dt.date(1990, 10, 22)},
    {"Nombre": "Lisandro Cabrera",   "Fecha": dt.date(2000,  7, 30)},
    {"Nombre": "Celeste Campos",     "Fecha": dt.date(1983,  1, 11)},
    {"Nombre": "Esteban Acosta",     "Fecha": dt.date(1977,  8, 19)},
    {"Nombre": "Milagros Ponce",     "Fecha": dt.date(1995, 11,  6)},
    {"Nombre": "Hernán Delgado",     "Fecha": dt.date(1969,  3, 23)},
    {"Nombre": "Ezequiel Luna",      "Fecha": dt.date(1993,  8, 27)},
    {"Nombre": "Facundo Montoya",    "Fecha": dt.date(1997,  7, 18)},
    # Menores de edad
    {"Nombre": "Sofía Guerrero",     "Fecha": dt.date(2009,  5, 14)},
    {"Nombre": "Mateo Blanco",       "Fecha": dt.date(2010,  8, 22)},
    {"Nombre": "Valentina Ríos",     "Fecha": dt.date(2011,  1,  3)},
    {"Nombre": "Lucas Ibáñez",       "Fecha": dt.date(2012,  9, 17)},
    {"Nombre": "Emma Serrano",       "Fecha": dt.date(2013,  4, 30)},
    {"Nombre": "Santiago Vera",      "Fecha": dt.date(2014,  7, 11)},
    {"Nombre": "Isabella Ramos",     "Fecha": dt.date(2015,  2, 25)},
    {"Nombre": "Nicolás Cruz",       "Fecha": dt.date(2013, 11,  8)},
    {"Nombre": "Camila Pereira",     "Fecha": dt.date(2010,  6, 19)},
    {"Nombre": "Benjamín Contreras", "Fecha": dt.date(2011, 12,  5)},
]


def ingresar_usuario(nombre, fecha):

    fecha_valida = verificar_fecha(fecha)

    if (fecha_valida):
        nuevo_usuario = {
            "Nombre": nombre,
            "Fecha": fecha
        }
        lista_usuarios.append(nuevo_usuario)
        print("""


==============================

Ingreso realizado correctamente

==============================
""")

def datos_usuario():
    try:
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        fecha_usuario = dt.date(
            int(input("Ingrese su año de nacimiento: ")),
            int(input("Ingrese su mes de nacimiento: ")),
            int(input("Ingrese su dia de nacimiento: "))
        )
    except ValueError as error:
        validar_errores(error)
    else:
        if (fecha_usuario.year < 1900):
            print(f"El año seleccionado es invalido, seleccione un año en un rango de 1900 - {fecha_actual.year}")
        else:
            ingresar_usuario(nombre_usuario, fecha_usuario)

def listar_usuarios():
    pagina = 0

    while True:
        inicio = pagina * 10
        fin = inicio + 10

        print("\nUsuarios:")
        for i in range(inicio, min(fin, len(lista_usuarios))):
            print(f"{i + 1} - {lista_usuarios[i]['Nombre']}")

        opcion = input("\nEscribe 'd' para derecha, 'a' para izquierda, 'q' para salir: ")

def listar_usuarios():
    pagina = 0

    while True:
        inicio = pagina * 10
        fin = inicio + 10

        print("\nUsuarios:")
        for i in range(inicio, min(fin, len(lista_usuarios))):
            print(f"{i + 1} - {lista_usuarios[i]['Nombre']}")

        opcion = input("\nd = derecha | a = izquierda | q = salir: ")

        if opcion == "d":
            if fin < len(lista_usuarios):
                pagina += 1
        elif opcion == "a":
            if pagina > 0:
                pagina -= 1
        elif opcion == "q":
            break
        elif opcion.isdigit():
            calcular_edad(lista_usuarios[int(opcion) - 1]["Nombre"], fecha_actual, lista_usuarios[int(opcion) - 1]["Fecha"], mostrar=True)
        else:
            print("Ingrese un valor valido")
