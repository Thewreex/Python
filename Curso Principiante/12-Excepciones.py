### Excepciones ###

# las excepciones sirven para evitar que el programa se deje de ejecutar al enfrentarse a un error

try:
    print(hola) # Cpn try podemos definir el codigo que puede tener errores
except:
    print("Se genero un error") # el except es un codigo que se ejecutara si el codigo de try da error


try:
    print("hola")
except:
    print("Se genero un error")
else:
    print("La ejecuccion continua correctamente") # el else es un codigo que se ejecutara si el codigo del try se ejecuta correctamente

try:
    print(hola)
except:
    print("Se genero un error")
else:
    print("La ejecuccion continua correctamente")
finally:
    print("La ejecuccion continua") # el finally es un codigo que se ejecutara en cualquier circuntancia

# print(hola) este codigo es de tipo NameError

try:
    print(hola)
except TypeError: # tambien podemos definir excepciones segun tipo de error, en este caso se tiene una excepcion typeerror
    print("Se geenero un error TypeError")
except NameError as error: # con as error, se puede crear una variable que almacena la informacion del error
    print("Se genero un error NameError") 
    print(error) # Como el codigo del try da NameError, entonces sera ejecutada esta excepcion, haciendo print a la variable que almacena informacion del error
except Exception as error:
    print(error)