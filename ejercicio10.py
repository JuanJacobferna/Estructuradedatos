#Leer el tamaño del arreglo 
n = int(input("Ingrese el tamaño del arreglo:"))
A = []

#Leer los elementos del arreglo 
for i in range(n):
    numero = int(input(f"Ingrese el elemento {i+1}: "))
    A.append(numero)

    B = []

    #Crear  nuevo arreglo  con suma de opuestos
    for i in range((n + 1) // 2):

        suma = A[i] + A[n - 1 - i]
        B.append(suma)

    print("El nuevo arreglo con la suma de opuestos es:")
    print(B)

    
