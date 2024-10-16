"""
Pide al usuario que ingrese tres números enteros separados por comas. Crea un diccionario con dos claves: "suma" y "producto", donde "suma" almacene la suma de los números ingresados y "producto" almacene el producto de los números ingresados. Muestra por consola la suma y el producto utilizando f-strings.
"""
numeros = input("Ingresa tres números enteros separados por comas: ")

numeros_lista = list(map(int, numeros.split(',')))

suma = sum(numeros_lista)
producto = 1
for numero in numeros_lista:
    producto *= numero

resultado = {
    "suma": suma,
    "producto": producto
}

print(f"El diccionario es: {resultado}")
print(f"La suma de los números es: {resultado['suma']}")
print(f"El producto de los números es: {resultado['producto']}")