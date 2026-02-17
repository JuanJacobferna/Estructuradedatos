edades_a = (18, 25, 40, 12, 65)
edades_b = (20, 30, 50, 15, 70)


#Metodo 1: Usando un bucle for
for edad_a, edad_b in zip(edades_a, edades_b):
    if edad_a > edad_b:
        print(f"{edad_a} es mayor que {edad_b}")
    elif edad_a < edad_b:
        print(f"{edad_a} es menor que {edad_b}")
    else:
        print(f"{edad_a} es igual a {edad_b}")

        #Mettodo 2: Usando una comprensión de listas
comparaciones = [f"{edad_a} es mayor que {edad_b}" if edad_a > edad_b else f"{edad_a} es menor que {edad_b}" if edad_a < edad_b else f"{edad_a} es igual a {edad_b}"
                 for edad_a, edad_b in zip(edades_a, edades_b)]

for comparacion in comparaciones:
    print(comparacion)

    
