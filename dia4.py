
# usuario ingresa la lista de números
numeros = input("Ingresa una lista de números separados por espacios: ")

# se convierte la cadena de entrada en una lista de enteros
lista_numeros = list(map(int, numeros.split()))

# se ordena la lista en orden ascendente
lista_ordenada = sorted(lista_numeros)

# y muestra la lista ordenada
print("Lista ordenada en orden ascendente:", lista_ordenada)


