"""
Ejercicio intermedio:
Solicita al usuario que ingrese una palabra. Utiliza un bucle for para mostrar por consola la palabra invertida.
"""

palabra = input("Ingresa una palabra:")

palabra_invertida = ""
for letra in palabra:
    palabra_invertida = letra + palabra_invertida

# Mostrar la palabra invertida
print(f"La palabra invertida es: {palabra_invertida}")