# Escribe un script en Python que pida dos números a través de la entrada estándar 
# y muestre en la salida estándar si dichos números son iguales o cuál es el mayor 
# de los dos.
# Debes implementar el manejo de errores necesario para verificar que se cargan los 
# valores numéricos. Pista: Python tiene un método para verificar si un carácter de entrada es numérico o no. Tienes que buscarlo.


num1 = input("Escribe un número: ")
num2 = input("Escribe un segundo número: ")

if num1.isnumeric() and num2.isnumeric():
        num1 = int(num1)
        num2 = int(num2)
        if num1 == num2:
            print("Son iguales")
        elif num1 > num2:
            print(f"El {num1} es mayor que {num2}")
        else:
            print(f"El {num2} es mayor que {num1}")
else:
        print("Lo que es ha introducido no es un número")
 # f es para concatenar con llaves