
dimensiones = int(input("Ingrese sus dimensiones "))

arreglo = [[None for i in range(dimensiones)] for j in range(dimensiones)]

i = int(0)
j = int(dimensiones / 2)

limiteX = dimensiones - 1;
limiteY = dimensiones - 1;
for contador in range(1,(dimensiones*dimensiones)+1):
    arreglo[int(i)][int(j)]=contador
    aux_x = j;
    aux_y = i;
    i = int(i - 1);

    if(i < 0):
        i = limiteY

    j = j + 1
    if(j > limiteX):
        j = 0

    if(arreglo[i][j] is not None and arreglo[i][j] > 0):
        j = aux_x;
        i = aux_y + 1

for i in range(dimensiones):
    for j in range(dimensiones):
        print(arreglo[i][j], end= " ")
    print()
