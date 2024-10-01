"""
Ejercicio intermedio:

Crea tres variables con números enteros y calcula lo siguiente:

El producto de los tres números.

La suma del primero y el segundo número, dividida por el tercer número.

El promedio de los tres números.

Muestra los resultados por consola utilizando f-strings.
"""
numero1 = int(input("Ingresa el primer numero:"))
numero2 = int(input("Ingresa el segundo numero:"))
numero3 = int(input("Ingresa el tercero numero:"))

producto = numero1 * numero2 * numero3

ejercicio = (numero1 + numero2) / numero3

promedio = (numero1 + numero2 + numero3) / 3

print(f"El producto de los tres números {numero1}, {numero2}, {numero3} es de: {producto}")
print(f"La suma del primero y el segundo número, dividida por el tercer número: {ejercicio}")
print(f"El promedio de los tres números {numero1}, {numero2}, {numero3} es de: {promedio}")