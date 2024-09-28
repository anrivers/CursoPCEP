"""
Ejercicio intermedio:

Dadas las siguientes variables:

x = 10
y = 20
z = 30


Utiliza operadores lógicos y de comparación para determinar si:

x es menor que y y y es menor que z

x es menor que y o y es mayor que z
"""
x = 10
y = 20
z = 30

variable1 = x < y and y < z
print("x es menor que y y y es menor que z:",variable1)

variable2 = x < y or y > z
print("x es menor que y o y es mayor que z:",variable2)