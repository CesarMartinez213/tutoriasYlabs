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
                for i in range(chainUser.find(palabra) , chainUser.find(palabra)+3 , 1):
                    chainUser[i] = "*"
    newChain = newChain + palabra + " "
    return (newChain)

# programa principal #

chainUser=str(input('ingrese la cadena: '))
longitud = impLong(chainUser)
newChain = bus4letras(chainUser)
print(longitud)
print(newChain)