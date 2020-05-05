print("Alquiler del coche")

cantidad_km = int(input("Cargue los km recorridos: "))

if cantidad_km <= 300:
    importe = 500
else:
    if cantidad_km > 300 and cantidad_km <= 1000:
        importe = 500 + (cantidad_km - 300) * 3
    else:
        importe = 500 + (cantidad_km - 300) * 1.5

print("Importe es:", importe)