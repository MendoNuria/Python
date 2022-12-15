def leer_fichero(nombre_fichero):
    try:
        with open(nombre_fichero,"r") as f:
            lineas = f. readlines() 
            for linea in lineas:
                print ("Sin salto", linea.strip())
                print("Con salto", linea)
    except IOError:
        print("Problema al leer el fichero")
leer_fichero("prueba.txt")



