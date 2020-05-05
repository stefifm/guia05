print("Observatorio meteorológico")

t1 = float(input("Ingrese la Temperatura 1: "))
t2 = float(input("Ingrese la Temperatura 2: "))
t3 = float(input("Ingrese la Temperatura 3: "))
t4 = float(input("Ingrese la Temperatura 4: "))


#Promedio de temperatura
p_diario = (t1 + t2 + t3 + t4) / 4


#Temperatura máxima

if t1 > t2 and t1 > t3 and t1 > t4:
    mayor = t1
else:
    if t2 > t3 and t2 > t4:
        mayor = t2
    else:
        if t3 > t4:
            mayor = t3
        else:
            mayor = t4

#Temperatura mínima
if t1 < t2 and t1 < t3 and t1 < t4:
    menor = t1
else:
    if t2 < t3 and t2 < t4:
        menor = t2
    else:
        if t3 < t4:
            menor = t3
        else:
            menor = t4

#Temperatura superior al promedio
if t1 > p_diario:
    print("Temperatura 1 supera al promedio")

if t2 > p_diario:
    print("Temperatura 2 supera al promedio")

if t3 > p_diario:
    print("Temperatura 3 supera al promedio")

if t4 > p_diario:
    print("Temperatura 4 supera al promedio")
#se puede usar bandera
print("La temperatura promedio:", p_diario)
print("Temperatura máxima:", mayor)
print("Temperatura mínima:", menor)
