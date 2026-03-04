# ============================================================================
# EJERCICIO 6: SISTEMA DE BIBLIOTECA
# ============================================================================
"""
OBJETIVO: Crear una clase Libro y gestionar una pequeña biblioteca.

REQUISITOS:
- Crear una clase Libro con propiedades: titulo, autor, año, disponible
- Crear un método para prestar el libro (cambiar disponible a False)
- Crear un método para devolver el libro (cambiar disponible a True)
- Crear un método que muestre la información del libro
- Crear al menos 3 instancias de libros
- Crear una lista con todos los libros
- Usar un bucle para mostrar solo los libros disponibles

TEMAS INVOLUCRADOS: Clases, listas, bucles, condicionales, métodos

"""

lista_libro = []


class Libro:
    def __init__(self, titulo, autor, año, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible
        lista_libro.append( {
            "Nombre": self.titulo,
            "Autor": self.autor,
            "Año": self.año,
            "Disponible": self.disponible
        })
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("El libro ha sido prestado")
        else:
            print("El libro no se puede prestar porque no esta disponible")
    def devolver(self):
        if not(self.disponible):
            self.disponible = True
            print("El libro ha sido devuelto")
        else:
            print("El libro no se puede devolver, porque ya esta disponible")
    def información(self):
        print(f"""
INFORMACION DEL LIBRO:

Titulo: {self.titulo}
Autor: {self.autor}
Año: {self.año}
Disponibilidad: {"Disponible" if self.disponible else "No disponible"}
        """)

la_odisea = Libro("La Odisea", "Diego Agrimbau", 2014)
cien_anios_de_soledad = Libro("Cien años de soledad", "Gabriel Garcia Marquez", 1967)
el_nombre_del_viento = Libro("El nombre del viento", "Patrick Rothfuss", 2007, False)

libros_disponibles = []

for libros in lista_libro:
    if libros["Disponible"]:
        libros_disponibles.append(libros)

print(libros_disponibles)
