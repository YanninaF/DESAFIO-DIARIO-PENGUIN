    # Defini una función para imprimir la tabla de multiplicar
def imprimir_tabla_de_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# el  usuario debe ingresar un número
numero = int(input("Ingresa un número: "))

# Llama a la función para imprimir la tabla de multiplicar
imprimir_tabla_de_multiplicar(numero)

