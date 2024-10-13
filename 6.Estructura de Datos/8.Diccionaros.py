persona  = {'nombre': 'Juan', 'edad': 28, 'ciudad': 'Madrid'}

print(persona)
print(persona['edad'])
print(persona['ciudad'])

persona['edad'] = 29
print(persona['edad'])

persona['profesion'] = 'ingeniero'
print(persona)

del persona['nombre']
print(persona)