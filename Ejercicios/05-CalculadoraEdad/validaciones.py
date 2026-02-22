import datetime as dt
fecha_actual = dt.date.today()

def verificar_fecha(fecha):
    if fecha_actual >= fecha:
        return True
    else:
        print("La fecha ingresada es futura a la fecha actual, ingrese una fecha valida")
        return False 

def validar_errores(error):
        mensaje_error = str(error)

        if mensaje_error == "month must be in 1..12":
            print(f"El valor ingresado en mes es incorrecto, el valor debe de ser entre 1 al 12")
        elif mensaje_error == "day is out of range for month":
            print("El dia ingresado no existe dentro del mes, elija un dia valido")
        else:
            print("Ingrese valores numericos")

