#Datos de ejemplos 
n = 4  #Numero de viviendas
alquileres = [500.0, 750.0, 600.0, 800.0]  # Alquiler mensual de cada vivienda
porcentajes_aumento = [9.0, 15.0, 7.5, 12.0]  # Porcentaje de aumento para cada vivienda

#Crear el nuevo arreglo de ganancias
ganancias = []

for i in range(len(alquileres)):
    aumento = alquileres[i] * (porcentajes_aumento[i] / 100)
    nueva_ganancia = alquileres[i] + aumento
    ganancias.append(nueva_ganancia)

    #Arreglar el resultado al nuevo arreglo de ganancias
    ganancias.append(round(nueva_ganancia, 2))

#Mostrar el resultado
print("Nuevo arreglo de ganancias después del aumento:")
print(ganancias)
print(f"Total de ganancias después del aumento: ${sum(ganancias):.2f}")
print(f"Promedio de ganancias después del aumento: ${sum(ganancias)/len(ganancias):.2f}")
print(f"Ganancia máxima después del aumento: ${max(ganancias):.2f}")
