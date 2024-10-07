"""
Ejercicio avanzado:
Pide al usuario que ingrese una cadena con palabras separadas por espacios. 
Crea una lista con las palabras ingresadas y luego crea una nueva lista con las palabras ordenadas alfabéticamente. Muestra ambas listas por consola.
"""
cadena = input("Por favor, ingresa una cadena separadas por espacios:")

lista_palabras = cadena.split()

lista_ordenada = sorted(lista_palabras)

print("Lista original de palabras:", lista_palabras)
print("Lista de palabras ordenadas alfabéticamente:", lista_ordenada)