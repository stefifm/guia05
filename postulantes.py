print("Postulantes a un empleo")
print("=" * 80)

print("Datos del primer postulante\n")
postulante1 = input("Ingrese nombre del primer postulante: ")
total_pregunta1 = int(input("Total de preguntas del postulante 1: "))
correcta1 = int(input("Respuestas correctas del postulante 1: "))
porcentaje1 = round((correcta1 * 100) / total_pregunta1, 2)
print("=" * 80)

print("\nDatos del segundo postulante\n")
postulante2 = input("Ingrese nombre del segundo postulante: ")
total_pregunta2 = int(input("Total de preguntas del postulante 2: "))
correcta2 = int(input("Respuestas correctas del postulante 2: "))
porcentaje2 = round((correcta2 * 100) / total_pregunta2, 2)
print("=" * 80)

print("\nDatos del tercer postulante\n")
postulante3 = input("Ingrese nombre del tercer postulante: ")
total_pregunta3 = int(input("Total de preguntas del postulante 3: "))
correcta3 = int(input("Respuestas correctas del postulante 3: "))
porcentaje3 = round((correcta3 * 100) / total_pregunta3, 2)
print("=" * 80)

#nivel del postulante
if porcentaje1 > 90:
    nivel1 = "Superior"
elif porcentaje1 >= 75 and porcentaje1 < 90:
    nivel1 = "Medio"
elif porcentaje1 >= 50 and porcentaje1 < 75:
    nivel1 = "Regular"
else:
    nivel1 = "Fuera de nivel"

if porcentaje2 > 90:
    nivel2 = "Superior"
elif porcentaje2 >= 75 and porcentaje2 < 90:
    nivel2 = "Medio"
elif porcentaje2 >= 50 and porcentaje2 < 75:
    nivel2 = "Regular"
else:
    nivel2 = "Fuera de nivel"

if porcentaje3 > 90:
    nivel3 = "Superior"
elif porcentaje3 >= 75 and porcentaje3 < 90:
    nivel3 = "Medio"
elif porcentaje3 >= 50 and porcentaje3 < 75:
    nivel3 = "Regular"
else:
    nivel3 = "Fuera de nivel"

#Para determinar el postulante que ganó el puesto

if porcentaje1 > porcentaje2 and porcentaje1 > porcentaje3:
    mayor = postulante1
    nivel_mayor = nivel1
elif porcentaje2 > porcentaje1 and porcentaje2 > porcentaje3:
    mayor = postulante2
    nivel_mayor = nivel2
else:
    mayor = postulante3
    nivel_mayor = nivel3

print(postulante1,"Tiene un nivel:",nivel1)
print(postulante2,"Tiene un nivel:",nivel2)
print(postulante3,"Tiene un nivel:",nivel3)

print("Postulante que se queda con el puesto es:",mayor,"\nTuvo un nivel:",
      nivel_mayor)
