import random

# Lista de caracteres
character_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '"', '#', '$', '%', '&', '/', '.', ',', '@'
]

# Longitud de la contraseña
longitud_contraseña = random.randint(8, 16)

# Listas separadas para garantizar al menos un carácter de cada tipo
letras_mayusculas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
letras_minusculas = list('abcdefghijklmnopqrstuvwxyz')
numeros = list('0123456789')
simbolos = list('!"#$%&/,.@')

# Generar la contraseña
contraseña = [
    random.choice(letras_mayusculas),
    random.choice(letras_minusculas),
    random.choice(numeros),
    random.choice(simbolos)
]

# Llenar el resto de la contraseña con caracteres aleatorios
while len(contraseña) < longitud_contraseña:
    contraseña.append(random.choice(character_list))

# Desordenar la contraseña
random.shuffle(contraseña)

# Convertir la lista de caracteres en una cadena
contraseña_final = ''.join(contraseña)

# Imprimir la contraseña generada
print(f'{contraseña_final} \n¡es tu contraseña segura!')
