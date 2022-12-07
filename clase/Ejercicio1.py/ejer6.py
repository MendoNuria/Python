# Crea un script en Python que calcule el factorial de un número. 
# El factorial de un número es el producto de todos los enteros desde 
# el 1 hasta ese número. Por ejemplo, el factorial de 6 es 1*2*3*4*5*6 = 720. 
# Teniendo en cuenta que el factorial de 0 es 1, el script debe comprobar 
# que el usuario no introduce un valor numérico cuyo factorial no pueda ser calculado.



num = input("Escribe un número: ")
factorial = 1

if num.isnumeric():
    num=int(num)
    if num < 0:
        print("No se puede hacer un factorial de negativos")
    elif num == 0:
        print("El factorial de 0 es 1")
    else:
        for i in range(1,num+1):
            factorial = factorial * i
        print(f"El factorial de {num} es {factorial}")
else:
    print("No has introducido un número")
