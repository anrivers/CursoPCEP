"""
Solicita al usuario que ingrese una cadena de texto. Utiliza un condicional para determinar si la cadena tiene una longitud mayor a 10 caracteres. Si es mayor a 10 caracteres, muestra por consola la cadena en mayúsculas. Si no, muestra la cadena en minúsculas.
"""
cadena = input("Ingresa una cadena de texto: ")

if len(cadena) > 10:
    print(cadena.upper())
else:
    print(cadena.lower())
