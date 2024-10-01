"""
Ejercicio avanzado:
Solicita al usuario que ingrese el radio de un círculo. 
Calcula el área y el perímetro del círculo utilizando la constante pi. Muestra los resultados por consola utilizando f-strings.
"""
radioCirculo = float(input("Ingresa el radio del circulo:"))
pi = 3.14159

area = pi * (radioCirculo ** 2)
perimetro = (2 * pi) * radioCirculo

print(f"El área del círculo con radio {radioCirculo} es: {area:.2f}")
print(f"El perímetro del círculo con radio {radioCirculo} es: {perimetro:.2f}")
