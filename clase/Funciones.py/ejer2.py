#2. Escribe un programa en Python que tenga una función llamada clasificar_numeros que reciba por parámetro tres listas:

#- Una lista contendrá varios enteros desordenados (siempre más de un entero).
#- Dos listas vacías. En una de ellas se almacenarán los números pares de la primera. En la otra se almacenarán los números impares.

#El programa debe mostrar la lista de números pares y la lista de números impares ordenadas ambas de forma ascendente (de menor a mayor).

#Nota: El método sort() de Python permite ordenar una lista.


def clasificarNumeros(listaDesordenada, listPar, listImpar):
    #Ordeno la lista principal desde el principio
    listaDesordenada.sort()
    for i in listaDesordenada:
        if i%2 == 0:
            listPar.append(i)
        else:
            listImpar.append(i)
    print("Lista de pares: ",listPar)
    print("Lista de impares: ",listImpar)

def main():
    try:
        listaParVacia= [] #list()
        listaImparVacia= [] #list()
        listaEntero = ["b",-1,7,6,5]
        clasificarNumeros(listaEntero,listaParVacia,listaImparVacia)
    except TypeError:
        print("La lista sólo debe contener números")
main()