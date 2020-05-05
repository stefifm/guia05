# La facultad pide un simple programa que pida las tres notas de un alumno en
# cualquier materia y mostrar si el alumno esta libre, regular o promocionado.
# Las tres notas son los dos parciales mas la nota de prácticos y las
# condiciones de regularidad están descriptas a continuacón:
# El promedio menor a 4 el alumno esta libre.
# El promedio comprendido entre 4 y 8 el alumno esta regular.
# El promedio mayor a 8 el alumno está promocionado.

print("Regularidad del alumno")

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
np = int(input("Ingrese nota de prácticos: "))

promedio = round((nota1 + nota2 + np) / 3, 2)

if promedio < 4:
    condicion = "Está libre"
elif promedio >= 4 and promedio < 8:
    condicion = "Es regular"
else:
    condicion = "Se encuentra promocionado"

print("El promedio del alumno es:",promedio,"\nLa condición del alumno es:",\
                                            condicion)

