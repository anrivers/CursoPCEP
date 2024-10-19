"""
Pide al usuario que ingrese un número entero. Utiliza un condicional para determinar si el número es par o impar y muestra el resultado por consola. Si el número es impar, también muestra su cuadrado.
"""
numero = int(input("Ingresa un número entero:"))

if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")
    
    