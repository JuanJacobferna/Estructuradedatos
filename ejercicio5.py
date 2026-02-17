#Datos de entrada (Ejemplo con 3 productos)
descripciones = ["Producto A", "Producto B", "Producto C"]
pu = [25.0, 15.0, 30.0]  # Precio unitario
cc = [2, 5, 3]  # Cantidad comprada

#Calculo del total a pagar por cada producto
tg = []
for i in range(len(pu)):
    total = pu[i] * cc[i]
    tg.append(total)

    #Mostrar descripciones y totales del producto con mayot gasto
mayor_gasto = tg[0]
indice_mayor_gasto = 0

for i in range(1, len(tg)):
    if tg[i] > mayor_gasto:
        mayor_gasto = tg[i]
        indice_mayor_gasto = i

        #Mostrar el resultado
        print(f"El producto con mayor gasto es: {descripciones[indice_mayor_gasto]} con un total de: {mayor_gasto:.2f}")
        print(f" Arreglo TG: {tg}")
        total_general = sum(tg)
        print(f" Total general de la compra: ${total_general:.2f}")

