#3. Escribe una función Python llamada mostrar_usuarios_sistema que muestre 
# el nombre de todos los usuarios existentes en un sistema Linux y pruébala.

with open("/etc/passwd","r") as fichero:
    contenido = fichero.readlines()
    for linea in contenido:
        usuario = linea.split(":")[0]
        print(usuario)
    #fichero.write('\n')
    # contenido_fichero = fichero.readlines()
    # for linea_fichero in contenido_fichero:
    #     print(linea_fichero.strip())