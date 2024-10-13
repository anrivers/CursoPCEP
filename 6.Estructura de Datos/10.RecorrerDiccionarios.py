miDiccionario = {"Nombre": 'Juan Carlos', "Edad": 20, "Idioma":"Ingles"}

for clave in miDiccionario.keys():
    print(clave)

for valor in miDiccionario.values():
    print(valor)

for clave, valor in miDiccionario.items():
    print(clave,":",valor)
    