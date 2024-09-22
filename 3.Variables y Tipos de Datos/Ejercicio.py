"""
Ejercicio 3
Ejercicio avanzado: Conversión de tipos de datos
Enunciado: Asigne valores a tres variables (una cadena, un entero y un flotante). Convierta el entero a flotante y el flotante a entero. 
Imprima las variables y sus tipos de datos.
"""

cadena = 'Mi nombre es Andrés Rivera'
entero = 8
flotante = 8.5

print("Numero entero:",entero)
entero = float(entero)
print("Numero entero a flotante",entero)

print("Numero flotante:",flotante)
flotante = int(flotante)
print("Numero flotante a entero:",flotante)

print("Cadena:",cadena,", Tipo de dato:",type(cadena))
print(entero,", Tipo de dato:",type(entero))
print(flotante,", Tipo de dato:",type(flotante))