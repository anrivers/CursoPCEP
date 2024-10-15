"""
Solicita al usuario que ingrese su nombre, apellido y edad.
Crea un diccionario con esos datos y muestra por consola el mensaje "Hola, [nombre] [apellido]. Tienes [edad] años." utilizando f-strings.
"""
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")

persona = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad
}

print(persona)
print(f"Hola, {persona['nombre']} {persona['apellido']}. Tienes {persona['edad']} años.")