"""
Ejercicio básico modificado:
Crea una tupla con los nombres de tres ciudades y la población de cada una (en millones).
Muestra el nombre de la segunda ciudad y su población utilizando índices y f-strings.
"""
ciudades = (("CDMX", 8.555 ) , ("Londres", 8.982) , ("Madrid" , 3.223))

segundaCiudad = ciudades[1][0]
poblacionCiudad = ciudades[1][1]

print(f"La poblacion de {segundaCiudad} es de {poblacionCiudad} millones")

         