"""

Ejercicio 3: Organizador de Invitados
Objetivo: Practicar el uso de Sets para manejo de colecciones únicas y operaciones de conjuntos. Consigna:

Crear dos sets: invitados_confirmados y invitados_vip.
Encontrar quiénes están en ambas listas (intersección).
Encontrar quiénes están confirmados pero NO son VIP (diferencia).
Agregar un nuevo invitado a la lista de confirmados.

"""

nuevo_invitado = input("Ingrese un invitado confirmado: ")
invitados_confirmados = {"Juan", "Diego", "Perez", "Pablo", "Jaime", "Gonzalo"}
invitados_confirmados.add(nuevo_invitado)
invitados_vip = {"Perez", "Gustavo", "Joaquin", "Gonzalo"}
coincidencias = invitados_confirmados.intersection(invitados_vip)
diferencia = invitados_confirmados.difference(invitados_vip)
print(f"Los invitados confirmados son: {invitados_confirmados}\nLos invitados VIP son: {invitados_vip}\nLos invitados VIP confirmados son: {coincidencias}\nLos invitados confirmados que no son VIP: {diferencia}")