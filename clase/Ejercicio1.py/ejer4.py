#Escribe un script en Python que pida un carácter a través de la entrada estándar
# y muestre a la salida estándar si el usuario ha introducido un carácter en mayúsculas, 
# un carácter en minúsculas, un número u otro tipo de carácter.
# Sugerencia: Python tiene varios métodos incorporados para realizar estas comprobaciones. 
# Si el usuario no introduce ningún carácter, el script debe mostrar un mensaje de error.



miCaracter = input("Escribe un caracter ")

if len(miCaracter) != 1:
    print("Recuerda, un caracter")
elif miCaracter.isupper():
    print("Es una mayúscula")
elif miCaracter.islower():
    print("Es una minúscula")
elif miCaracter.isnumeric():
    print("Es un número")
else:
    print("No es ni una letra ni un número")




