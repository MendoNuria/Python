fichero = input("Nombre del fichero: ")

def leeFichero(fichero):
    with open(fichero,"r") as f:
        lineas = f.readlines()
        for i in lineas:
            lista = i.strip()
            print(lista)

leeFichero(fichero)