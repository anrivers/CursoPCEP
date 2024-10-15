"""
Crea un diccionario con tres pares clave-valor que representen el nombre, apellido y edad de una persona.
Además, añade una clave "amigos" con una lista de nombres de tres amigos.
Muestra por consola el valor de la clave "nombre" y el nombre del segundo amigo de la lista.
"""

persona = {'Nombre':'Andres', 
           'Edad': 23, 
           'Apellido':'Rivera',
           "Amigos": [
               "Denis",
               "Zezar", 
               "Ever"]}

nombre = persona['Nombre']
SegundoAmigo = persona['Amigos'][1]

print(persona)
print("Nombre:", nombre)
print("El segundo amigo es:", SegundoAmigo)
