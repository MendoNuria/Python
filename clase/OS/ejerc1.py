# Escribe un script en Python que, independientemente de la plataforma 
# en la que se ejecute, muestre la siguiente información en la salida estándar.




import sys, subprocess, os
# a. Sistema operativo donde se ejecuta

print("El sistema operativo es: ", sys.platform)
#b. Si el sistema operativo es Linux, la versión del kernel que está ejecutando

if sys.platform == 'linux':
    subprocess.run(['uname','-r'])
#c Directorio de trabajo actual

print("Directorio actual de trabajo: ", os.getcwd())
#d. Archivos y directorios del directorio de trabajo 

print("Listado fichero pasado por argumento mediante excepciones", os.listdir("."))
#e. Verificación de la existencia o no de un fichero pasado por argumento mediante
#excepciones
# 
if len(sys.orgv) <= 0 and len (sys.argv) >= 2:
    print("El numero de argumentos no es correcto")
else:
    try:
        with open(sys.argv[1],"r") as f:
            print("El archivo ", sys.argv[1], "existe y es accesible. ")

    except IOError:
        print("Archivo ", sys.argv[1], " no existe")