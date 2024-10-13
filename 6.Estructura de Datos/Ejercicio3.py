"""
Pide al usuario que ingrese una serie de números enteros separados por comas. 
Crea una tupla con los números ingresados, luego calcula y muestra por consola la suma y el producto de los números en la tupla.
"""
numeros = (input("Ingresa una serie de numeros enteros separados por comas:"))

tuplas = tuple(map(int, numeros.split(',')))
print(tuplas)

suma = sum(tuplas)

producto = 1
for numero in tuplas:
    producto *= numero


print(f"La suma total de los numeros es: {suma}")
print(f"El producto total de los numeros es: {producto}")
