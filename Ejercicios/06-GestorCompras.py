# ============================================================================
# EJERCICIO 2: GESTOR DE LISTA DE COMPRAS
# ============================================================================
"""
OBJETIVO: Crear un sistema para gestionar una lista de compras con diferentes
operaciones.

REQUISITOS:
- Crear una lista vacía para almacenar productos
- Agregar al menos 5 productos a la lista
- Mostrar la lista completa
- Eliminar un producto específico
- Verificar si un producto existe en la lista
- Ordenar la lista alfabéticamente
- Mostrar cuántos productos hay en total

TEMAS INVOLUCRADOS: Listas, métodos de listas, operadores, condicionales
"""

productos = []

productos.append("1L de leche")
productos.append("1KG de pan")
productos.append("Galletas de agua")
productos.append("Manjar")
productos.append("Queso")
productos.append("Enjuague Bucal")
productos.append("Lavaloza")


print(f"Lista de productos: {productos}")

if "1KG de pan" in productos:
    productos.remove("1KG de pan")


print("Platano" in productos)
print("Manjar" in productos)

productos_ordenados = sorted(productos)

print(f"Lista ordenada alfabeticamente de menor a mayor: {productos_ordenados}")

print(f"La cantidad de productos es: {len(productos)}")
