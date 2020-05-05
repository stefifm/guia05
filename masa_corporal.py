print("Masa corporal")

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = round(peso / altura**2,2)
print("Su índice es: ", imc)

if imc <= 16:
    print("Necesita asistencia médica")
elif imc <= 17:
    print("Tiene infrapeso")
elif imc <= 18:
    print("Tiene bajo peso")
elif imc >= 18 and imc <= 26:
    print("Tiene un peso saludable")
elif imc >= 26 and imc < 30:
    print("Tiene sobrepeso Grado I")
elif imc >= 30 and imc <= 35:
    print("Tiene obesidad Grado II")
elif imc > 35 and imc <= 40:
    print("Tiene obesidad Grado III")
else:
    print("Tiene obesidad Grado IV")
