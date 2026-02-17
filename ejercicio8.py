mayor = None
menor = None

contador_mayor = 0
contador_menor = 0

numeros = []

# Leer 30 numeros del usuario
for i in range(30):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

    # Actualizar mayor y menor
    if mayor is None or numero > mayor:
        mayor = numero
        contador_mayor = 1
    elif numero == mayor:
        contador_mayor += 1

    if menor is None or numero < menor:
        menor = numero
        contador_menor = 1
    elif numero == menor:
        contador_menor += 1

# Mostrar resultados
print(f"El número mayor es: {mayor} y se repite {contador_mayor} veces.")
print(f"El número menor es: {menor} y se repite {contador_menor} veces.")
