# El usuario ingresa una cadena
cadena = input("Ingresa una cadena de texto: ")
#variable para contar las vocales
contador_vocales = 0
#tupla con las cinco vocales
vocales = ('a', 'e', 'i', 'o', 'u')
# Itera sobre cada carácter en la cadena
for caracter in cadena:
    # Verifica si el carácter actual es una vocal
    if caracter in vocales:
        # Incrementa el contador de vocales
        contador_vocales += 1
#  el resultado
print("La cadena tiene", contador_vocales, "vocales.")
