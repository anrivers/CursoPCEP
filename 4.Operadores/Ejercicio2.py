"""
Ejercicio avanzado:

Dadas las siguientes variables que representan las calificaciones de tres estudiantes en dos exámenes:

calificacion1_examen1 = 85
calificacion1_examen2 = 90
calificacion2_examen1 = 80
calificacion2_examen2 = 95
calificacion3_examen1 = 70
calificacion3_examen2 = 75
Utiliza operadores de comparación y aritméticos para determinar si:

a) El promedio de las calificaciones de los dos exámenes de calificacion1 es igual al promedio de las calificaciones de los dos exámenes de calificacion2

b) El promedio de las calificaciones de los dos exámenes de calificacion1 es menor que el promedio de las calificaciones de los dos exámenes de calificacion3

c) El promedio de las calificaciones de los dos exámenes de calificacion2 es mayor o igual que el promedio de las calificaciones de los dos exámenes de calificacion3
"""
calificacion1_examen1 = 85
calificacion1_examen2 = 90
calificacion2_examen1 = 80
calificacion2_examen2 = 95
calificacion3_examen1 = 70
calificacion3_examen2 = 75

promedioCalificacion1 = (calificacion1_examen1 + calificacion1_examen2) / 2
promedioCalificacion2 = (calificacion2_examen1 + calificacion2_examen2) / 2
promedioCalificacion3 = (calificacion3_examen1 + calificacion3_examen2) / 2

comparacionCalificacion1 = promedioCalificacion1 == promedioCalificacion2
print("El promedio de las calificaciones de los dos exámenes de calificacion1 es igual al promedio de las calificaciones de los dos exámenes de calificacion2:", comparacionCalificacion1)

comparacionCalificacion2 = promedioCalificacion1 < promedioCalificacion3
print("El promedio de las calificaciones de los dos exámenes de calificacion1 es menor que el promedio de las calificaciones de los dos exámenes de calificacion3:", comparacionCalificacion2)

comparacionCalificacion3 = promedioCalificacion2 >= promedioCalificacion3
print("El promedio de las calificaciones de los dos exámenes de calificacion2 es mayor o igual que el promedio de las calificaciones de los dos exámenes de calificacion3:",comparacionCalificacion3)

