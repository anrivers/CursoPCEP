"""
Pide al usuario que ingrese un número entero. Utiliza condicionales para determinar si el número es negativo, cero o positivo. Además, indica si es par o impar. Si el número es positivo y par, muestra la suma de los dos primeros números de la lista [2, 4, 6, 8, 10].
"""
numero = int(input("Por favor, ingrese un número entero: "))
numeros_lista = [2, 4, 6, 8, 10]

if numero < 0:
    print(f"El número {numero} es negativo.")
elif numero == 0:
    print(f"El número {numero} es cero.")
else:
    print(f"El número {numero} es positivo.")

if numero % 2 == 0:
    print(f"El número {numero} es par.")
    if numero > 0:
        suma = numeros_lista[0] + numeros_lista[1]
        print(f"La suma de los dos primeros números de la lista es {suma}.")
else:
    print(f"El número {numero} es impar.")