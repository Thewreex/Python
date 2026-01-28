### Modulos ###

# Con los modulos podemos importartar ficheros tantos externos, como internos y usarlos en nuestro fichero

from modulo import sumar # con esto, podemos importar la funcion sumar del fichero modulo

sumar(2,3,4)

# import modulo tambien podemos importar un modulo completo
# modulo.printValue("a", "b", "c") al importar un modulo completo, para llamar a una funcion se escribe el nombre del modulo.lafuncion

import math # tambien podemos importar modulos externos que vienen en python para usarlos, como math

print(math.pi) # nos permite acceder a pi
print(math.pow(2, 8)) # nos permite hacer potencias

from datetime import datetime as tiempo # con el as, podemos cambiar el como nos tenemos que referenciar a un modulo o funcion especifica

print(tiempo.now())