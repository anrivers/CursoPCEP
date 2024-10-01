"""
Ejercicio básico:
Crea una variable que represente tu altura en metros y otra que represente tu peso en kilogramos.
Calcula tu índice de masa corporal (IMC) utilizando la fórmula:

IMC = peso / (altura^2).

Muestra el resultado por consola utilizando f-strings.
"""
altura = float(input("Ingresa tu altura:"))
peso = float(input("Ingresa tu peso:"))

IMC = peso / (altura**2)

print(f"Mi alura es de {altura} metros. Mi peso es de {peso} kilogramos. El indice de masa corporal (IMC) es de: {IMC:.2f}")