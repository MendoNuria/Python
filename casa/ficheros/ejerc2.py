
import random
def devuelve_aleatorio(lista_palabras):
   # lista palabras = list()

    for i in range(10):
        indice_random = random.randrange(0, len(lista_palabras))
        print(lista_palabras [îndice_random].strip())
  

def main():
    lista_palabras  = []

    try:
         with open("mbox.txt","r") as f:
            lista_palabras = f.readlines()
              #print("Lista vacias: " , lista_palabras)
    except IOError:
        print("Error de fichero")

