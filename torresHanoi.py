###definimos la funcion recursiva

def Hanoi (discos,TorreOrigen=1,TorreAuxiliar=2,TorreDestino=3):
    ##declaramos la condicion de parada
    if discos==1:
        print (TorreOrigen,"a",TorreDestino)
        
    else:
        Hanoi(discos-1,TorreOrigen,TorreDestino,TorreAuxiliar)
        print(TorreOrigen,"a",TorreDestino)
        Hanoi (discos-1,TorreAuxiliar,TorreOrigen,TorreDestino)
    return

###programa principal

D=int(input('ingrese la cantidad de discos: '))

## llamamos a la funcion asignandole el nro de discos

Hanoi(D)
