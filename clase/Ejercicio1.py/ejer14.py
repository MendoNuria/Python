# Modifica el script Python anterior para que 
# el saludo sea visiblemente más presentable. 
# Ejemplo: si hay dos personas en clase llamadas Juan y Pedro, 
# la ejecución debería devolver ahora lo siguiente... Hola, Juan, Pedro 

# Tienes que hacerlo de dos maneras diferentes:

# Seguirás guardando los nombres en una lista, pero ahora utilizando una variable llamada 
# saludo, que será la que tengas que imprimir 
# para mostrar la salida deseada. 
# Esta variable contendrá inicialmente la cadena "Hola", pero la modificarás para que 
# incluya también los nombres de los alumnos presentes en el aula.

# Convirtiendo la lista en una cadena (revisa las diapositivas de Aula para hacerlo)



numpersonas=int(input("Hola, ¿cuántos estáis en el aula?: "))
list=[]
string="Hola: "
for i in range(numpersonas):
    nombre=input("¿Cómo te llamas?: ")
    list.append(nombre)
string = string + " , ".join(list)
print(string + ".")


#----------------------------
numpersonas=int(input("Hola, ¿cuántos estáis en el aula?: "))
list=[]
string = " "
#string = "Hola:"
for i in range(numpersonas):
    nombre=input("¿Cómo te llamas?: ")
    list.append(nombre)
    
for j in range(len(list)):
    string = string + list[j] + " , "  
print("Hola: " +string + " . ")

