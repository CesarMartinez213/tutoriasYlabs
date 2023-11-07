numeroEstados = int(input("Ingrese el número de estados "))

#definimos el sexo k = 0 para el hombre y el sexo k = 1 para la mujer

DIAS_SEMANA = 7

estadosRegistrados = []
posicionesEstados = []
cantContagiosMujeresPorEstado = []
sumaContagiosMujeres = 0
sumaContagiosHombres = 0

casos = [[[None for i in range(2)] for j in range(7)] for k in range(23)]

print(casos)
for i in range(numeroEstados):
    #Primero pedimos el nombre del estado
    nombreEstado = input("Ingrese el nombre del estado ")
    #Luego lo agregamos a nuestro arreglo vacio
    estadosRegistrados.append(nombreEstado)
    #Luego registramos para cada dia de la semana
    for j in range(DIAS_SEMANA):
        print("Dia {}".format(j))
        casos[i][j][0] = (int(input("Ingrese la cantidad de hombres contagiados ")))
        casos[i][j][1] = (int(input("Ingrese la cantidad de mujeres contagiadas ")))

for i in range(numeroEstados):
    for j in range(DIAS_SEMANA):
        if(j == 5 or j==6):
            sumaContagiosHombres = sumaContagiosHombres + casos[i][j][0]

        if(casos[i][j][1] is not None):
            sumaContagiosMujeres = sumaContagiosMujeres + casos[i][j][1]
    cantContagiosMujeresPorEstado.append(sumaContagiosMujeres)
    sumaContagiosMujeres = 0;

print(cantContagiosMujeresPorEstado)
print("La suma de todos los hombres contagiados en el fin de semana es {}".format(sumaContagiosHombres))

for i in range(numeroEstados):
    for j in range(numeroEstados - i - 1):
      if cantContagiosMujeresPorEstado[j] < cantContagiosMujeresPorEstado[j + 1]:
        cantContagiosMujeresPorEstado[j], cantContagiosMujeresPorEstado[j + 1] = cantContagiosMujeresPorEstado[j + 1], cantContagiosMujeresPorEstado[j]
        estadosRegistrados[j], estadosRegistrados[j+1] = estadosRegistrados[j+1],estadosRegistrados[j]

print("El ranking de estados con mas contagios de mujeres es: ")
for i in range (numeroEstados):
    print(estadosRegistrados[i])