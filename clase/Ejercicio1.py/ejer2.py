# Utilizando un script de Python, imprime un número natural que cumpla 
# las tres condiciones siguientes:
# Ser mayor que el resultado de la operación 13 * 6
# Ser menor que el resultado de la operación 5 * 17
# Ser divisible por 10

# Nota: Prueba con un rango de números dentro de un bucle for.


for elem in range(78,85):
    if elem > 13 * 6 and elem< 5 *17 and elem % 10 == 0:
            print(elem)
    else:
            print("No")
