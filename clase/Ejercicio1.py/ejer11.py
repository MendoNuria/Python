 # Modifica el ejercicio anterior para que calcule la LONGITUD
 # de la palabra MÁS LARGA de una cadena prefijada en el guión. 
 # Para simplificar el ejercicio, los signos de puntuación que 
 # pueda tener una frase se considerarán 
 # parte de la longitud de la palabra a la que están unidos. 
 # por ejemplo, querer, tendrá una longitud de 5 caracteres. 
 # debido a la coma. Además, el guión deberá mostrar 
 # cuántas palabras (repetidas o no, no importa) hay en la cadenapalabra = ["Hola", "Adios", "Saludo"] 

#lst = "Vamos a ponerlo dificilísimo!, vamos!!! vamos!"
#lst1 = lst.split()
#long = 0
#string = ""

#for i in range(len(lst1)):
#    if len(lst1[i]) >= long:
#        long =len(lst1[i])
#for j in range(len(lst1)):
#    if len(lst1[j]) == long:
#            string = lst1[j]
#print("La palabra más larga de la cadena de caracteres es: ", string)
#print("El número total de palabras son",len(lst1), ", la palabra más larga es",string,"y tiene un total de ",long,"caracteres")


lst = "Vamos a ponerlo facilísimo, vamos!!!, vamos!!."
lst1 = lst.split()
long = 0
count = 0
for item in lst1:
        if len(item) > long:
            long = len(item)
        count = count + 1
print("La palabra más lagra tiene", long, "caracteres")
print("Número de palabras en total: ", count)



#El split por cada espacio en blanco lo va a pasar a una lista, utilizando el espacio como caraacter de separacion.
# palabras = frase_prueba.split("u")   En este caso cogeria como separacion la u

