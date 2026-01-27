### Clases ###

class PersonaVacia: # inicia una clase vacia
    pass # pass nos sirve para ejecutar funciones vacias

class Persona: # con las clases podemos definir propiedades que debe cumplir y funciones que se pueden ejecutar
    def __init__(self, nombre, apellido, alias = "Sin Alias"): # para definir la propiedades, se usa el init y el self obligatoriamente
        self.nombre = nombre # Para iniciar una propiedad en una clase, se usa el self
        self.apellido = apellido
        self.alias = alias
        self.nombre_completo = f"{nombre} {apellido} {alias}"
    def caminar(self): # se pueden crear funciones dentro de la clase, tambien se usa self
        print(f"{self.nombre_completo} Esta caminando")

mi_persona = Persona("Juan", "Pablo") # pasar valores a la clase y se los asigna a la variable de mi persona
print(f"{mi_persona.nombre} {mi_persona.apellido}") # Imprime los valores de Persona
mi_persona.caminar() # Ejecuta la funcion de la clase

mi_otra_persona = Persona("Juan", "Pablo", "JP") # Al igual que en las funciones, se pueden poner valores por defecto
mi_otra_persona.caminar()