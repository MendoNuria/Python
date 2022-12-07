miNombre="Mi nombre es Nuria!"
print(miNombre)

#Asignación
mensaje = "Hola"
mensaje += " "
mensaje += "Nuria"
print (mensaje)

#Concatenación
mensaje1 =  "Holaaa"
espacio =  " "
nombre = "Nuria"
concatenacion = mensaje1 + espacio + nombre
print (mensaje1 + espacio + nombre)
print (concatenacion)

numero_uno = 4
numero_dos = 2
resultado = numero_uno + numero_dos
resultado = str(resultado) #Así se convierte un numeral a un string
print ("El resultado de la suma es: " + resultado) # resultado ya es un texto

# find encontrar. Contesta con la posición
mensaje2 = "Hola Naia"
buscar_subcadena = mensaje2.find("Naia")
print(buscar_subcadena)
