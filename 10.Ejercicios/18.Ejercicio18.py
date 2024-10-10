"""
Solicita al usuario que ingrese su nombre y edad. 
Crea una tupla con esos datos y muestra por consola el mensaje "Hola, [nombre]. Tienes [edad] años." utilizando f-strings.
"""
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

datos = (nombre, edad)

print(f"Hola, {datos[0]}. Tienes {datos[1]} años.")