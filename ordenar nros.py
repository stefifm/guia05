print ("Ordenar 3 números")

n1 = int(input("Ingrese N1: "))
n2 = int(input("Ingrese N2: "))
n3 = int(input("Ingrese N3: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
    if n2 > n3:
        medio = n2
        menor = n3
    else:
        medio = n3
        menor = n2
elif n2 >= n1 and n2 >= n3:
    mayor = n2
    if n1 > n3:
        medio = n1
        menor = n3
    else:
        medio = n3
        menor = n1
elif n3 >= n2 and n3 >= n1:
    mayor = n3
    if n2 > n1:
        medio = n2
        menor = n1
    else:
        medio = n1
        menor = n2

print("Mayor:", mayor, "Medio:", medio, "Menor:", menor)

resto = mayor % medio
if menor == resto:
    print("Tercero igual al resto de los dos")
else:
    print("Tercero no es igual al resto de los dos y valor es:", resto)


