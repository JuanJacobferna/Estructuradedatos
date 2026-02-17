#Leer tamaño del arreglo
n = int(input("Ingrese el tamaño del arreglo:"))
A = []

#Leer los elementos del arreglo
for i in range(n):
    numero = int(input(f"Ingrese el elemento {i+1}: "))
    A.append(numero)

    #Crear los tres arreglos
    negativos = []
    positivos = []
    ceros = []

    #Clasificar los elementos
    for numero in A:
        if numero < 0:
            negativos.append(numero)
        elif numero > 0:
            positivos.append(numero)
        else:
            ceros.append(numero)

#Mostrar Resultado
print("Arreglo Original:", A)
print("Arreglo de Negativos:", negativos)
print("Arreglo de Positivos:", positivos)
print("Arreglo de Ceros:", ceros)
