# Crea un script de Python que pida dos numeros e imprima los numeros 
# entre ellos (del menor al mayor1, pero saltando tres numeros a la vez. 
# Deberá implementar el manejo de errores necesarios para verificar que 
# se introduce valores numéricos.


num1 = input("Introduce un número ")
num2 = input("Introduce otro número ")

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)

    if num1 > num2:
        for i in range(num2+1,num1,3):
            print(i)
    elif num2 > num1:
            for i in range(num1+1,num2,3):
                print(i)
    else:
        print("Los números son iguales")
else:
    print("Tienes que poner un número ")
            

        

