# Escriba un programa en Python que envíe a la salida estándar 
# la palabra más larga de una lista de cadenas 
# que irán prefijadas en el código del script y serán siempre las 
# mismas.
# Por ejemplo: ["Hola", "Adiós", "Saludos"]


# 1º Forma
palabras = "Hola, Adiós, Saludos"
palabras1 =  palabras.split()

long = 0
count = 0
string = ""

for i in palabras1:
    if len(i) > long:
        long = len(i)
        count = count + 1
        string = i
print("Longitud máxima:", long)
print("Número de palabras: ", count)
print ("La palabra más larga es: ",  string)

# 2º Forma
# palabra = ["Holaaaaa", "Adios", "Saludos"] 

# long = 0
# string = ""

# for i in range(len(palabra)):
#     if len(palabra[i]) >= long:
#         long =len(palabra[i])
# for j in range(len(palabra)):
#     if len(palabra[j]) == long:
#             string = palabra[j]
# print(string)
