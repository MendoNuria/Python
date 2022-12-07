#  Implemente un script de Python en el que se BORRE el primer y el último carácter 
# de una cadena introducida. 
# La cadena resultante debe imprimirse en la salida estándar. 
# Debe comprobar que el usuario no introduce una cadena de longitud menor o igual a 2 caracteres.

# 1º Forma
#str = input("Introduce una frase o palabra cualquiera: ")
#if len(str) <= 2:
#        str=input("Introduciendo esa cantidad de caracteres no hacemos nada.")
#        exit()
#else:
#    print(str[1:-1])

# 2º Forma
#str = input("Introduce una frase o palabra cualquiera: ")
#if len(str) >= 2:
#    print(str[1:-1])
       
#else:
#     str=input("Escribe por lo menos 3 caracteres.")
    
# 3º Forma con While
str = input("Introduce una frase o palabra cualquiera: ")
while len(str) <= 2:
    str = input("Introduce un string más largo ")
print(str[1:-1])
