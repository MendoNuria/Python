# 1. Escribe un programa en Python que reciba a través de la entrada estándar las
#siguientes opciones (1, 2 ó 3):

#1. Calculará el área de un triángulo.
#2. 2.Calculará el área de un rectángulo.
#3.Calculará el área de un círculo.
#Los datos necesarios para calcular cada una de las áreas deben obtenerse del estándar de entrada.
#El diseño del programa debe contener:
#Una función principal
#Una función para cada uno de los cálculos de áreas. Estas funciones deben:
#Obtener de la entrada estándar los valores necesarios para realizar el cálculo.
#Devolver los resultados de sus operaciones al programa principal.


import math # hacer llamadas a bibliotecas matemáticas  y creamos un metodo math
# def main():
#   area = 0.0
#       entrada = input("1 area triangula\n, 2 area rectangualo\n, 3 area del circulo. Elije opcion 1,2 o 3")
#       if (entrada == "1"):
#         areqa = calcula_triangulo
#         print("El araea del triangulo es ", area)
##calcula el area del triangulo
#       elif (entrada == "2"):
#calculael area de rectangulo 
#       
#       elif (entrada == "3"):
#calcula area del circulo
#       pass
#       else:
#       print("La opcion no es válida ")
#
#
#def calcula_area_triangulo():
#   area_triangulo = 0.0
#   base = float(input("Introduce"))
# NO TERMINADO






def triangulo(base, altura):
    return (base*altura)/2
def rectangulo(base, altura):
    return (base*altura)
def circunferencia(radio):
    return (math.pi*(radio**2))
def recoleccion_valores():
    try:
        opcion = int(input("Introduce la opción de área (1, 2 o 3): "))
        if opcion == 1:
            #Opción área del triángulo
            bass = float(input("Introduce la base del triángulo: "))
            alt = float(input("Introduce la altura del triángulo: "))
            print("Área: ",triangulo(bass, alt))
        elif opcion == 2:
            #Opción área del rectángulo
            bass = float(input("Introduce la base del rectángulo: "))
            alt = float(input("Introduce la altura del rectángulo: "))
            print("Área: ",rectangulo(bass, alt))
        elif opcion == 3:
            #Opción área de la circunferencia
            rad = float(input("Introduce el radio de la circunferencia: "))
            print("Área: ",circunferencia(rad))
        else:
            raise ValueError
    except ValueError:
        print ("Error de introducción de opciones.")
        exit()
def main():
    recoleccion_valores()
    exit()

main()
#Proposito de las excepciones es para gestionar errores no gestionado