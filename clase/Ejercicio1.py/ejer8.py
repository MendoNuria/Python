# Implemente un script en Python que muestre en la salida estándar una cadena 
# formada por los dos primeros y los dos últimos caracteres de una cadena introducida por la entrada estándar.
# El script debe devolver una cadena vacía si la longitud de la cadena introducida es inferior a
# dos.

#str = input ("Introduce una secuencia de caracteres: ")
#if len(str) > 2:
#    print(str[:2]  + ("-") + str [-2:])
#else:
#    print(" ")

str = input ("Introduce una secuencia de caracteres: ")
if len(str) > 2:
    str = str[0:2]  + ("-") + str[len(str)-2:len(str)]
    print(str)
else:
    print(" ")