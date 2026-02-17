#Leer tamño del arreglo 

n = int(input("Ingrese el tamaño del arreglo: "))

arreglo = []

#Leer los elementos del arreglo
for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    arreglo.append(numero)

    #Leer el número a buscar
    buscar = int(input("Ingrese el número a buscar: "))

    #Contar las veces que aparece el número a buscar
    contador = arreglo.count(buscar)

#Mostrar el resultado
print(f"El número {buscar} aparece {contador} veces en el arreglo.")
