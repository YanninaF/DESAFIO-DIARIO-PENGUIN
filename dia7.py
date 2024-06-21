import random

# las 3 opciones disponible
opciones = ["piedra", "papel", "tijeras"]

# el usuario selecciona la opcion que quiera
opcion_usuario = input("Ingrese su opción (piedra, papel o tijeras): ").lower()

# Selección aleatoria de la computadora
opcion_computadora = random.choice(opciones)

# Muestra la opción de la computadora
print(f"La computadora eligió: {opcion_computadora}")

# Determinar el resultado del juego
if opcion_usuario == opcion_computadora:
    print("Empate")
elif (opcion_usuario == "piedra" and opcion_computadora == "tijeras") or \
    (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
    (opcion_usuario == "tijeras" and opcion_computadora == "papel"):
    print("¡Ganaste!:)  ")
else:
    print("Has perdido :(  ")


