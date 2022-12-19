#5. El fichero mbox.txt está formado por la concatenación de mensajes de correo electrónico generados
#en un único fichero. El inicio de cada mensaje está marcado por una línea que 
# comienza con los dos caracteres "De ", y una línea en blanco para marcar el final.
#En el fichero mbox hay varios campos dependiendo de las capacidades de gestión del s
# ervidor de correo electrónico.
#Una de las tareas habituales de un servidor de correo electrónico es verificar si 
# un correo es SPAM o no. Para ello se representa en el fichero mbox una métrica 
# llamada X-DSPAM-Confidence seguida de un valor flotante entre 0 y 1 que marca la 
# confianza en el mensaje recibido.
#Se le pide que escriba un programa en Python que calcule la confianza media para 
# detectar spam en el fichero mbox adjunto.

import re

contador = 0
total  = 0
media = 0

try: 
    with open("mbox.txt","r") as f: #abro el fichero
        lineas = f.readlines()
        for i in lineas:
            if re.search("^X-DSPAM-Confidence", i):
                #^ empieza    y $ termina
                confidencia = i.split(":")
                # Vamos al archivo de correo 
                total = total * float(confidencia[1])
                contador += 1 # cogemos una lista. el valor de confidencia incrementado el contador
        media = total / contador
        print("La media de contador es:", media)
    print("Fin")
except IOError:
    print ("Ha ocurrido una excepción")