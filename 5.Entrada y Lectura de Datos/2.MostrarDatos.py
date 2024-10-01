nombre = input("Ingresa tu nombre:")
edad = int(input("Ingresa tu edad:"))

#print(nombre,edad)                                     #Consola estandar
#print(edad)                                            #Consola estandar
#print("Tu nombre es:", nombre,"tienes:",edad)          #Concatenando
#print("Tu nombre es: " + nombre + "tienes:", edad )    #Concatenando
print("hola {} tienes {}".format(nombre,edad))          #Format 
print(f"Hola {nombre} tienes {edad}")                   #f string
