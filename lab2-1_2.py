#### crear un programa que determine si un nro es automorfico ####
#### automorfico: nro que al elevarlo a la N potencia, sus ultimos digitos son el mismo nro (76,5,25,etc) ####

### subprograma para determinar si el nro es automorfico ###

def nroPruebas(N,num):
    contCifras = 0
    nvoNumero = num
    automorfico = 0
    while ( nvoNumero != 0 ):
        nvoNumero = nvoNumero // 10
        contCifras = contCifras + 1
    print(contCifras)
    for i in range(1,N,1):
        divisor = 10**contCifras
        resto = (num**i) % divisor
        if (resto == num) :
            automorfico = 1
    print(divisor)
    print(resto)
    return (automorfico)

# Programa principal #

num=int(input('ingrese el nro a evaluar: '))
N=int(input('¿A que potencia desea elevar el numero? '))
automorfico = nroPruebas(N,num)
if (automorfico == 1):
    print(f'el numero {num} es automorfico')
else:
    print(f'el numero {num} no es un automorfico')