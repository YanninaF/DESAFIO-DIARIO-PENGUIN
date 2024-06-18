# Creamos una lista con los nombres de los alumnos
alumna = ["Lucia", "Gustavo", "Elias", "Sol"]
# Creamos una lista con las notas correspondientes a cada alumno
nota = [5, 4, 5, 2]
# Inicializamos un diccionario vacío para almacenar los nombres y notas
diccionario = {}
# Recorremos las listas de alumnos y notas utilizando un bucle for
for i in range(4):
# Agregamos una entrada al diccionario con el nombre del alumno como clave
# y su nota correspondiente como valor    
    diccionario[alumna[i]] = nota[i]
    
# Imprimimos el diccionario resultante
print(diccionario)