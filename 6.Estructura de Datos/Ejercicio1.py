"""
Ejercicio avanzado:
Pide al usuario que ingrese su nombre y apellido. Luego, 
utiliza debanado y f-strings para crear y mostrar por consola un mensaje de bienvenida que incluya solo la primera letra del nombre y del apellido, 
seguidas por un punto. 
Por ejemplo, si el usuario ingresa "Ada Lovelace", el mensaje debería ser: "Bienvenida, A.L."
"""
nombre = input("Por favor, ingresa su nombre:")
apellido = input("Por favor, ingrese su apellido:")

abreviado1 = nombre[:1]
abreviado2 = apellido[:1]

print(f"Bienvenido, {abreviado1}. {abreviado2}.")
  