NUM_MESES=12

############################################################################################################

print('ingrese el valor correspondiente para cada accion:')

############################################################################################################

opcion = 1
nroTiendas = 1
nroProd = 1
totVxP = 0
totVentas = [None for i in range(nroProd)]
nombreTienda = [None for i in range(nroTiendas)]
nombreProd = [[None for i in range(nroProd)] for k in range(nroTiendas)]
ventas = [[[None for i in range(nroProd)] for j in range(NUM_MESES)] for k in range(nroTiendas)]

############################################################################################################
while (opcion>0):
    print('1 = si desea agregar una tienda ; 2 = si desea agregar un producto')
    print('3 = si desea ingresar las ventas ; 4 = si desea saber la tienda con menor ventas')
    print('5 = si desea buscar las ventas de una tienda X en un mes Y ; 6 = si desea saber que tienda tuvo mayor ventas en Y mes')
    print('0 = si desea terminar la simulacion')
    opcion=int(input('ingrese la accion a realizar: '))
    if opcion==1:
        nombreT=str(input(f'ingrese el nombre de la tienda {nroTiendas} : '))
        nombreTienda.append(nombreT)
        nroTiendas=nroTiendas+1
    elif opcion==2:
        nombreP=str(input('ingrese el nombre del producto: '))
        nombreProd[nroTiendas][nroProd]=str(nombreP)
        nroProd=nroProd+1
    elif opcion==3:
        for k in range(nroTiendas):
            for i in range(nroProd):
                for j in range(NUM_MESES):
                    prod=int(input(f'ingrese las ventas del {nombreProd[k][i]}, en el mes {j+1}: '))
                    ventas[i][j][k]=int(prod)
                    totVxP = totVxP + ventas[i][j][k]
                totVentas[i] = totVxP
    elif opcion==4:
        menor=9999999
        for i in range(nroProd):
            if totVentas[i]<menor:
                menor=nombreT
        for i in range(nroProd):
            if totVentas[i]==menor:
                print('la tienda con menor ventas es : ')
    elif opcion==5:
        print(f'{nroTiendas}')
    elif opcion==6:
        print('6')
