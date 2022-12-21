#2. Escribe las siguientes dos funciones Python append_file que recibe el nombre del fichero y
#  el contenido a añadir al final del fichero write_file que recibe el nombre del fichero y 
# el contenido a añadir en el fichero (sobrescribiendo)  
# Prueba tus funciones Python con datos. Debes incluir el manejo de excepciones.


with open("prueba.txt","a") as fichero:
    fichero.write("holaa")
    fichero.write('\n')
    # contenido_fichero = fichero.readlines()
    # for linea_fichero in contenido_fichero:
    #     print(linea_fichero.strip())

# with open("prueba.txt","w") as fichero:
#     fichero.write("holaa")
#     fichero.write('\n')
    # contenido_fichero = fichero.readlines()
    # for linea_fichero in contenido_fichero:
    #     print(linea_fichero.strip())


with open("prueba.txt","r") as fichero:
    # fichero.write("holaa")
    contenido_fichero = fichero.readlines()
    for linea_fichero in contenido_fichero:
        print(linea_fichero.strip())

