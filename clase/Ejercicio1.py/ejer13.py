# Crea el siguiente script con Python con listas, 
# para que salude a todos los presentes a la vez.
# por ejemplo, si hay dos personas en clase llamadas 
# Juan y Pedro, el script debería imprimir Hola, ['Juan','Pedro'].


    

numero_alumnos = int(input("¿Cuantos alumnos hay en clase? "))
nombres_alumnos=[]
for i in range (numero_alumnos):
    nombre=input('¿Cómo te llamas? ')
    nombres_alumnos.append(nombre)
print("Hola, " + str(nombres_alumnos) + ".")





