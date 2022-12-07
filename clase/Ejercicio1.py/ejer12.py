# Modifique el ejercicio anterior para que el usuario introduzca 
# las palabras a comprobar a través de la entrada estándar. 
# El script debe devolver la LONGITUD de la PALABRA MÁS LARGA que el 
# usuario ha introducido y el número de palabras que ha introducido. 
# El script detectará que el usuario ha dejado de introducir palabras cuando 
# el usuario introduzca una cadena compuesta únicamente por un punto "."

palabras = list()
palabras1 = input("Introduce una palabra cualquier: ")
while not palabras1 == ".":
    palabras.append(palabras1)
    palabras1 = input("Introduce otra palabra o un punto si no quieres seguir: ")

print(palabras)

long = 0
count = 0
for item in palabras:
    if len(item) > long:
        long = len(item)
    count = count +1

print ("El número de caracteres que tiene la palabra más larga son de ", long, "caracteres "  "y el número de palabras introducidas en total son ",count)
print ("")
# print("Número de palabras introducidas en total: ", count)

#------------------------------------------------------------



palabra=""
palabras=""
while palabra != ".":
    palabra = input("Introduzca una palabra: ")
    palabras = palabras + " " + palabra
lst2 = palabras.split()
leng = 0
string = " "
for i in range(len(lst2)):
    if len(lst2[i]) >= leng:
        leng = len(lst2[i])

for j in range(len(lst2)):
    if len(lst2[j]) == leng:
        string = lst2[j]
print("Palabras introducidas en total: ",lst2, "y el número de caracteres introducidas de la palabra más larga son",leng)
