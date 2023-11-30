


def ArregloVocales (chain):
    ListaPalabras=[]
    palabra=''
    contA=contE=contI=contO=contU=0
    i=z=0

    for i in range(len(chain)):
        if chain[i] != ' ' and chain[i] != ',' and chain[i] != '.':
            palabra = palabra + chain[i]
        else:
            for z in range(len(palabra)):
                if palabra[z] in 'AÁaá':
                    contA = 1
                elif palabra[z] in 'EÉeé':
                    contE = 1
                elif palabra[z] in 'IÍií':
                    contI = 1
                elif palabra[z] in 'OÓoó':
                    contO = 1
                elif palabra[z] in 'UÚuú':
                    contU = 1
            if (contA + contE + contI + contO + contU >= 3):
                ListaPalabras.append(palabra) 
            palabra=''
            contA=contE=contI=contO=contU=0
                ## falta ordenar el arreglo ##
    return (ListaPalabras)

### definimos un subprograma el cual hara uso del metodo burbuja para ordenar el arreglo de palabras ###

def BubbleSort (ListaPalabras):
    ListaPalabras = ArregloVocales(chain)
    for i in range(len(ListaPalabras)):
        for j in range(len(ListaPalabras)-i-1):
            if len(ListaPalabras[j])< len(ListaPalabras[j+1]):
                temp = ListaPalabras[j]
                ListaPalabras[j] = ListaPalabras[j+1]
                ListaPalabras[j+1] = temp
    return(ListaPalabras)

# programa principal #

chain=str(input('ingrese la cadena a evaluar: '))
ListaPalabras = ArregloVocales(chain)
ArrOrdenado = BubbleSort(ListaPalabras)
print(ArrOrdenado)