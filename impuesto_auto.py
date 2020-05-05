print("Impuesto Automotor")

anio_fabricacion = int(input("Año de fabricación del coche: "))
tipo_auto = int(input("Ingrese tipo de auto (1 Particular, 2 Taxi, 3 Remis): "))
anio_actual = 2020
antiguedad = anio_actual - anio_fabricacion
if tipo_auto == 1:
    if antiguedad < 10:
        pagar = 200
    elif antiguedad >= 10 and antiguedad < 20:
        pagar = 150
    else:
        pagar = "No debe pagar impuestos"
else:
    if tipo_auto == 2:
        if antiguedad < 10:
            pagar = 200 + 150
        elif antiguedad >= 10 and antiguedad < 20:
            pagar = 150 + 150
        else:
            pagar = 150
    if tipo_auto == 3:
        pagar = antiguedad * 100

print("Impuesto a pagar en pesos:",pagar)
