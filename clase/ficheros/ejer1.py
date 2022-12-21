#Administración de archivos y expresiones regulares
#1. Escribe una función Python llamada leer_fichero que reciba como 
# parámetro el nombre del fichero a leer. Dentro de ella, 
# la función leer_fichero debe abrir el fichero, almacenar su contenido en una lista y mostrar su contenido en la salida estándar. Debe incluir el manejo de excepciones.


#
#
#

def leer_fichero(nombre_fichero):
    try:
        with open(nombre_fichero,"r") as f:
            lineas = f. readlines() 
            for linea in lineas:
                print ("Sin salto", linea.strip())
                #print("Con salto", linea)
    except IOError:
        print("Problema al leer el fichero")
leer_fichero("prueba.txt")

#fichero = input("Nombre del fichero: ")

#def leeFichero(fichero):
#    with open(fichero,"r") as f:
#        lineas = f.readlines()
#        for i in lineas:
#            lista = i.strip()
#            print(lista)

#leerFichero(fichero)