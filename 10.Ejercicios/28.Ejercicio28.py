"""
Crea una función llamada es_primo que reciba un número entero como parámetro y retorne True si el número es primo, de lo contrario, retorne False. Pide al usuario que ingrese un número entero y utiliza la función es_primo para determinar si es primo o no. Muestra el resultado por consola.
"""
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero_usuario = int(input("Ingresa un número entero: "))

if es_primo(numero_usuario):
    print(f"El número {numero_usuario} es primo.")
else:
    print(f"El número {numero_usuario} no es primo.")