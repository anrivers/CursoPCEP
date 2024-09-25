"""
Ejercicio intermedio:
Escribe un programa con tres variables, x ,  y y z. Luego, calcula e imprime:

a) La suma de x y z, y división con y

b) La división entera de z e y, y luego restadas con x

c) La elevación de y sobre x, y luego el módulo entre z
"""
x = 78
y = 1596.23 
z = 73

primerCalculo = (x + z) / y
print("La suma de x y z, y división con y es:",primerCalculo)

segundoCalculo = (z // y) - x
print("La división entera de z e y, y luego restadas con x es:",segundoCalculo)

tercerCalculo = (y ** x) % z
print("La elevación de y sobre x, y luego el módulo entre z es:",tercerCalculo)