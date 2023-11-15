##### diseñar un algoritmo que cambie las palabras de 4 letras por 4 asteriscos #####
##### y tmb imprima la longitud de la cadena #####

### subprograma para imprimir la longitud de la cadena ###

def impLong(chainUser):
    print(f'la cadena ingresada tiene una longitud de {len(chainUser)} caracteres.')
    return (len(chainUser))

### subprograma para buscar y reemplazar palabras de 4 letras ###

def bus4letras(chainUser):
    contLetras = 0
    newChain = ""
    for i in range(len(chainUser)):
        palabra = ""
        if chainUser[i] != " ":
            palabra = palabra + chainUser[i]
            contLetras = contLetras + 1
        else:
            if contLetras == 4:
                for i in range(find(palabra)+3):
                    palabra[i] = chr(42)
        newChain = newChain + palabra + " "
    print(newChain)
    return (newChain)

# programa principal #

chainUser=str(input('ingrese la cadena: '))
longitud = impLong
newChain = bus4letras
print(longitud)
print(newChain)