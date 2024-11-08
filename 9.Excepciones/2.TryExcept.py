try:
    x = 10
    y = 0
    resultado = x / y
    print(resultado)
except ZeroDivisionError:
    print("ERROR: No se puede dividir ente CERO")
    
try:
    numero = int("abc")
    print(numero)
except ValueError:
    print("ERROR: No se puede convertir una cadena de texto a entero")