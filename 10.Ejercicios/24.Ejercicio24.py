"""
Ejercicio intermedio:
Pide al usuario que ingrese una cadena de texto. Utiliza un bucle while para contar e imprimir la cantidad de vocales que hay en la cadena.
"""
cadena = input("Ingresa una cadena de texto:")
vocales = "aeiouAEIOU"

contador = 0
i = 0

while i < len(cadena):
    if cadena[i] in vocales:
        contador += 1
    i += 1
    
print(f"La cantidad de vocales en la cadena es: {contador}")