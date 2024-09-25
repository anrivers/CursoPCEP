"""
Ejercicio 3
Dadas las siguientes variables:

a = 3.5
b = 7.2
c = 1.8


Utiliza operadores aritméticos para calcular y mostrar:

a) El promedio de los tres números

b) El mayor de los tres números

c) El menor de los tres números 

d) La suma de los cuadrados de a, b y c
"""
a = 3.5
b = 7.2
c = 1.8

promedio = (a + b + c) / 3
print("El promedio de los números es:",promedio)

mayor = (max(a, b, c))
print("El mayor de los números es:",mayor)

menor = (min(a, b, c))
print("El menor de los números es:",menor)

sumaCuadrados = (a ** 2) + (b ** 2) + (c ** 2)
print("La suma de los cuadrados es:", sumaCuadrados)
