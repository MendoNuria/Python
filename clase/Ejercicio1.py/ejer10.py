# Escriba un programa en Python que envíe a la salida estándar 
# la palabra más larga de una lista de cadenas 
# que irán prefijadas en el código del script y serán siempre las 
# mismas.
# Por ejemplo: ["Hola", "Adiós", "Saludos"]
# split    separas

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

palabras1 = "Hola, Adiós, Saludos"
palabra_mas_larga = 0
indice = 0
indice_palabra_mas_larga = 0
for palabra1 in palabras1:
    if len(palabra1) > palabra_mas_larga:
        palabra_mas_larga = len(palabra1)
        indice_palabra_mas_larga = indice
    indice+= 1
print("Longitudd palabra más larga: ", palabra_mas_larga)
print("Longitudd palabra más larga: ", palabras1[indice_palabra_mas_larga])

#