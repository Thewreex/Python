"""

Ejercicio 4: Gestión de Inventario Simple
Objetivo: Practicar Listas (mutables) y Tuplas (inmutables). Consigna:

Crear una lista de productos disponibles en una tienda.
Crear una tupla con los precios fijos de esos productos (para asegurar que no cambien accidentalmente).
El usuario "compra" un producto: eliminarlo de la lista de productos disponibles.
Mostrar el inventario actualizado y cuántos productos quedan.

"""

productos = ["Expedition 33", "Cyberpunk 2077", "Ea fc 26", "Dragon ball sparking zero", "Elden ring", "Baldurs gate 3", "Metaphor refantazio"]
precios = (30, 45, 60, 50, 40, 60, 40)
producto_comprado = input("Seleccione un producto a comprar: ")
producto_comprado = producto_comprado.capitalize()
productos.remove(producto_comprado)
print(f"El inventario de productos actual es: {productos}")












   
