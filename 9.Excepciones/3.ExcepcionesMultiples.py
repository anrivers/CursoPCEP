try:
    a = int(input("Ingrese un número:"))
    b = int(input("Ingrese otro numero:"))
    resultado = a / b
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Debe ingresar números enteros, no decimales")
except ZeroDivisionError:
    print("No se puede dividir entre CERO")
except:
    print("Ha ocurrido un error")
    
    