import datetime as dt
import calendar
from collections import Counter
import datetime as dt

fecha_actual = dt.datetime.today()

lista_edades = []
lista_menores = []
lista_mayores = []
cumpleaños_por_mes = {
    "Enero": 0,
    "Febrero": 0,
    "Marzo": 0,
    "Abril": 0,
    "Mayo": 0,
    "Junio": 0,
    "Julio": 0,
    "Agosto": 0,
    "Septiembre": 0,
    "Octubre": 0,
    "Noviembre": 0,
    "Diciembre": 0
}

cumpleaños_por_dia = {
    "Lunes": 0,
    "Martes": 0,
    "Miércoles": 0,
    "Jueves": 0,
    "Viernes": 0,
    "Sábado": 0,
    "Domingo": 0
}

numero_bisiestos = 0

usuario_mas_viejo = ["", 0]
usuario_mas_joven = ["", 1000]

def crear_lista_edades(lista):
    global usuario_mas_joven
    global usuario_mas_viejo
    global numero_bisiestos 

    lista_edades.clear()
    lista_menores.clear()
    lista_mayores.clear()
    usuario_mas_joven = ["", 1000]
    usuario_mas_viejo = ["", 0]
  
    for clave in cumpleaños_por_dia:
        cumpleaños_por_dia[clave] = 0  
    for clave in cumpleaños_por_mes:
        cumpleaños_por_mes[clave] = 0
    numero_bisiestos = 0

    for usuario in lista:
        edad = calcular_edad(usuario["Nombre"], dt.date.today(), usuario["Fecha"])["Edad"]
        lista_edades.append(edad)

        if edad > usuario_mas_viejo[1]:
            usuario_mas_viejo[0] = usuario["Nombre"]
            usuario_mas_viejo[1] = edad
        if edad < usuario_mas_joven[1]:
            usuario_mas_joven[0] = usuario["Nombre"]
            usuario_mas_joven[1] = edad

        if edad >= 18:
            lista_mayores.append(edad)
        else:
            lista_menores.append(edad)
        

        cumpleaños_por_mes[usuario["Fecha"].strftime("%B").capitalize()] += 1
        nombre_dia = usuario["Fecha"].strftime("%A").capitalize()
        cumpleaños_por_dia[nombre_dia] += 1

        if calendar.isleap(usuario["Fecha"].year):
            numero_bisiestos += 1


def barra_progreso(valor, total, longitud=30):
    if total == 0:
        return "[Sin datos]"

    porcentaje = valor / total
    bloques = int(porcentaje * longitud)
    barra = "█" * bloques + "-" * (longitud - bloques)

    return f"[{barra}] {porcentaje:.1%}"



def calcular_edad(nombre, actual, usuario, mostrar = False):    
    if actual.month > usuario.month:
        edad_usuario = actual.year - usuario.year
        cumple_este_año = "Si"
    elif actual.month < usuario.month:
        edad_usuario = (actual.year - usuario.year) - 1
        cumple_este_año = "No"
    else:
        if usuario.day <= actual.day:
            edad_usuario = actual.year - usuario.year
            cumple_este_año = "Si"
        else:
            edad_usuario = (actual.year - usuario.year) - 1
            cumple_este_año = "No"
    
    dias_cumpleaños = dt.date(actual.year, usuario.month, usuario.day) - actual  
    
    if mostrar:
        print_edad(nombre, edad_usuario, cumple_este_año, dias_cumpleaños.days, actual, usuario)
    else:
        return {
            "Nombre": nombre,
            "Edad": edad_usuario,
            "Cumple este año": cumple_este_año,
            "Dias cumpleaños": dias_cumpleaños,
            "Fecha actual": actual,
            "Fecha de nacimiento": usuario
        }


def print_edad(nombre, edad, cumple_este_año, dias_cumpleaños, actual, usuario):
    if edad >= 18:
        esMayor = "Mayor"
    else:
        esMayor = "Menor"

    if dias_cumpleaños > 0:
        mensaje_cumpleaños = f"El usuario celebrara su cumpleaños en {dias_cumpleaños} dias"
    elif dias_cumpleaños < 0:
        mensaje_cumpleaños = f"El usuario celebro su cumpleaños hace {dias_cumpleaños * -1} dias"
    else:
        mensaje_cumpleaños = f"El usuario celebra hoy su cumpleaños"
    
    if calendar.isleap(usuario.year):
        mensaje_bisiesto = "El usuario nacio en año bisiesto"
    else:
        mensaje_bisiesto = "El usuario no nacio en un año bisiesto"
    
    meses_de_vida = (edad * 12 + (actual.month - usuario.month))
    dias_de_vida = (actual - usuario).days
    dia_de_nacimiento = calendar.weekday(usuario.year, usuario.month, usuario.day)
    print(f"""
    El nombre del usuario es: {nombre}
    Su fecha de nacimiento es: {usuario.strftime("%d/%m/%Y")}
    La Fecha actual es {actual.strftime("%d/%m/%Y")}
    El usuario tiene {edad} años, por lo tanto es {esMayor} de edad y {cumple_este_año} ha celebrado su cumpleaños este {actual.year}
    {mensaje_cumpleaños}
    El usuario tiene: {edad} años de vida, {meses_de_vida} meses de vida y {dias_de_vida} dias de vida
    El usuario nacio un {calendar.day_name[dia_de_nacimiento]}
    {mensaje_bisiesto}
    """)




def estadisticas_detalladas(lista):
    total = len(lista_edades)
    ninos = len([n for n in lista_edades if 0 <= n <= 12])
    adolescentes = len([n for n in lista_edades if 13 <= n <= 17])
    adulto_joven = len([n for n in lista_edades if 18 <= n <= 35])
    adulto = len([n for n in lista_edades if 36 <= n <= 59])
    adulto_mayor = len([n for n in lista_edades if n >= 60])

    print(f"""

===============================

    ESTADISTICAS GENERALES

===============================



Numero de usuarios registrados: {len(lista)}
Edad Promedio: {sum(lista_edades) / len(lista_edades)}
Edad con mas apariciones: {Counter(lista_edades).most_common(1)[0][0]}
Usuario con mayor edad: {usuario_mas_viejo[0]} - {usuario_mas_viejo[1]} Años
Usuario con menor edad: {usuario_mas_joven[0]} - {usuario_mas_joven[1]} Años
Cantidad de mayores de edad: {len(lista_mayores)}
Cantidad de menores de edad: {len(lista_menores)}
Cuantos cumplen años este mes: {cumpleaños_por_mes[fecha_actual.strftime('%B').capitalize()]}
Mes con mas cumpleaños: {max(cumpleaños_por_mes, key=cumpleaños_por_mes.get)}
Dia de la semana mas comun: {max(cumpleaños_por_dia, key=cumpleaños_por_dia.get)}
Nacimientos en año bisiesto: {numero_bisiestos}


===============================

      CATEGORIAS DE EDAD

===============================


Niño ( 0 - 12 Años ): {ninos}

{barra_progreso(ninos, total)}

Adolecente ( 13 - 17 Años ): {adolescentes}

{barra_progreso(adolescentes, total)}

Adulto Joven ( 18 - 35 Años ): {adulto_joven}

{barra_progreso(adulto_joven, total)}

Adulto ( 36 - 59 Años ): {adulto}

{barra_progreso(adulto, total)}

Adulto Mayor ( 60+ Años ): {adulto_mayor}

{barra_progreso(adulto_mayor, total)}


""")