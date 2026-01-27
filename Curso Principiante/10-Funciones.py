### Funciones ###

def mi_funcion():
    print("Esto es una funcion") #Crea una funcion con la palabra reservada def

mi_funcion() # Con esto se llama a la funcion, para ejecutar su codigo

def sumar_dos_numeros(num1, num2): # Se le pueden asignar variables a la funcion
    my_sum = num1 + num2
    return my_sum

print(sumar_dos_numeros(3, 12)) # Se puede llamar a la variable ingresandole datos, para que ejecute la funcion segun estos datos

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Pablo", name =  "Juan")

def print_name(name, surname, alias  = "Sin alias"): # Se le pueden agregar valores por defecto que se usaaran en caso de que no se le pase el valor a la funcion
    print(f"{name} {surname} {alias}")

print_name("Juan", "Pablo", "JP")

def print_textos(*text): # El asterisco permite ingresar infinitos elementos a la funcion como lista
    print(text)

print_textos("Hola", "Python", "JP")