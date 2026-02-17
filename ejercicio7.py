
#Definimos el arreglo original con 10 valores
arreglo_original = [53, 34, 15, 90, 12, 60, 75, 20, 85, 50]

#Crear un nuevo arreglo con los valores multiplicados por 2
arreglo_multiplicado = []
for valor in arreglo_original:
    arreglo_multiplicado.append(valor * 2)

#Mostrar los arreglos
print("Arreglo original:", arreglo_original)
print("Arreglo multiplicado por 2:", arreglo_multiplicado)
pares = [x for x in arreglo_multiplicado if x % 2 == 0]
print(f"Arreglo de pares: {pares}")
print(f"Arreglo de impares: {[x for x in arreglo_multiplicado if x % 2 != 0]}")


