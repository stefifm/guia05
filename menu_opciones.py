print("Menú de opciones con triángulos")

#Datos
opcion = int(input("Elija una opción (1-superficie del trángulo 2-perímetro "
                   "del triángulo 3-longitud del lado menor): "))
lado_triangulo1 = int(input("Valor del lado 1: "))
lado_triangulo2 = int(input("Valor del lado 2: "))
lado_triangulo3 = int(input("Valor del lado 3: "))

if opcion == 1:
    h = (lado_triangulo1 * lado_triangulo2) / lado_triangulo3
    superficie = (lado_triangulo1 * h) / 2
    print("Superficie del trángulo:",superficie)
elif opcion == 2:
    perimetro = lado_triangulo1 + lado_triangulo2 + lado_triangulo3
    print("El perímetro del triángulo:",perimetro)
elif opcion == 3:
    if lado_triangulo1 < lado_triangulo2 and lado_triangulo1 < lado_triangulo3:
        menor = lado_triangulo1
    elif lado_triangulo2 < lado_triangulo3:
        menor = lado_triangulo2
    else:
        menor = lado_triangulo3
    print("Lado menor es:",menor)
else:
    print("Error")


