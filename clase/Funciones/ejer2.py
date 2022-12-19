#2. Escribe un programa en Python que tenga una función llamada clasificar_numeros que reciba por parámetro tres listas:

#- Una lista contendrá varios enteros desordenados (siempre más de un entero).
#- Dos listas vacías. En una de ellas se almacenarán los números pares de la primera. En la otra se almacenarán los números impares.

#El programa debe mostrar la lista de números pares y la lista de números impares ordenadas ambas de forma ascendente (de menor a mayor).

#Nota: El método sort() de Python permite ordenar una lista.


def clasificarNumeros(listaDesordenada: list(), listPar: list()):
    #Ordeno la lista principal desde el principio
    #listaDesordenada.sort()
    listImpar= []
    print(listaDesordenada)
    for i in listaDesordenada:
        if i%2 == 0:
            listPar.append(i)
        else:
            listImpar.append(i)
    print("Lista de pares: ",listPar)
    print("Lista de impares: ",listImpar)
    listImpar.sort()
    print(listImpar)
    #print("Lista ordenada de impares",listImpar.sort())

def main():
    try:
        a = int(input("Introducir un valor: "))
        listaParVacia= [] 
        listaImparVacia= [] 
        listaEntero = [-1,9,2,20,-2,8-7,1]
        clasificarNumeros(listaEntero,listaParVacia)
    
    except TypeError:
        print("La lista sólo debe contener números")
        
main()

#Proposito de las excepciones es para gestionar errores no gestionadO. 