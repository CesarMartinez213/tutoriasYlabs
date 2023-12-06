from datetime import datetime
##### subprograma para la opcion d) #####

def ReportePalabras( M , N , Palabras , fecha):
    contTotPalabras=0
    Reporte = open('ReportePalabras.txt', 'w')
    Palabras = open('Palabras.txt', 'r')
    Reporte.write(f'{fecha}\n')
    Reporte.write(f'palabras con {M} y {N} consonantes:\n')
    for i in range(len(Palabras)):
        if (Palabras[contVocales]==M) and (Palabras[contConsonantes]==N):
            contTotPalabras = contTotPalabras + 1
            Reporte.write(f'{Palabras(palabra)}\n')
    Palabras.close()
    Reporte.write(f'\nhay {contTotPalabras} palabras en total\n')
    Reporte.close()
    return Reporte

#### subprograma para la opcion c) ####

def BorrarPalabras(cadenaU , subCad):
    
    nvaCadena = ''
    palabra = ''
    compSC = 1
    for i in range (len(cadenaU)):
        if cadenaU[i] not in ' .,':
            palabra = palabra + cadenaU[i]
        else:
            # utilizo estos condicionales en lugar de el delete o replace
            if subCad not in palabra:
                nvaCadena = nvaCadena + palabra
            else:
                nvaCadena = nvaCadena + ''
            #----------------------------------------------------    
            palabra = ''
    if (nvaCadena == cadenaU):
        bool=nvaCadena = False
    return nvaCadena

### subprograma para la opcion b) ###

def palindromo(cadenaU):
    palindromas = ''
    AuxCadena = ''
    palabra = ''
    Pinvertida = ''
    for i in range(len(cadenaU)):
        
        if cadenaU[i] != ' ' and cadenaU[i] != ',' and cadenaU[i] != '.':
            palabra = palabra + cadenaU[i]
            Pinvertida = cadenaU[i] + Pinvertida
        
        else:
            ###--------- ir guardando las palabras en una nueva cadena -------------#####
            if (palabra != Pinvertida):
                AuxCadena = AuxCadena + palabra + ' '
            else:   
               palindromas = palindromas + palabra + ','
               palabra = palabra.replace(f"{palabra}","*"*len(palabra))
               AuxCadena = AuxCadena + palabra + ' '
            ###--------------------------------------------------------------------------   
            palabra = ''
            Pinvertida = ''
    return AuxCadena , palindromas

## subprograma para a) ##

def Evpalabras(cadenaU):
    Palabras=open("Palabras.txt","w")
    vocales='AEIOUÁÉÍÓÚaeiouáéíóú'
    palabra=''
    contVoc=contConsonante=0
    for i in range(len(cadenaU)):
        if cadenaU[i] != ' ' and  cadenaU[i] != ',' and cadenaU[i] != '.':
            palabra = palabra + cadenaU[i]
            if cadenaU[i] in vocales:
                contVoc = contVoc + 1
            else:
                contConsonante = contConsonante + 1
        else:
            Palabras.writelines(palabra , len(palabra) , contVoc , contConsonante)
            contVoc=contConsonante=0
            palabra = ''
    Palabras.close()
    return(Palabras)

# programa principal #

Palabras=open("Palabras.txt","x")
Palabras.close()
Reportes=open("ReportePalabras.txt","x")
Reportes.close()

cadenaU=str(input("ingrese una cadena terminada en un punto(.): "))
opcion=int(input("ingrese la opcion a realizar: a)1 ; b)2 ; c)3 ; d)4 ; e)5(si desea terminar) :"))

while opcion !=5:

    if opcion == 1:

        Palabras = Evpalabras(cadenaU)
        opcion=(input("ingrese opcion a realizar:"))

    elif opcion == 2:

        AuxCadena = palindromo(cadenaU)
    
        opcion=(input("ingrese opcion a realizar:"))

    elif opcion == 3:
        
        subCad=str(input("ingrese la subcadena a buscar: "))
        nvaCadena = BorrarPalabras(cadenaU,subCad)
        if nvaCadena == False:
            print("subcadena no encontrada")
        else:
            print(nvaCadena)
        opcion=(input("ingrese opcion a realizar:"))
    
    elif opcion == 4:
        M=int(input('ingrese la cantidad de vocales que desea buscar en las palabras: '))
        N=int(input('ingrese la cantidad de consonantes que desea buscar en las palabras: '))
        fecha=datetime.now().strptime('d%-m%-y%')
        Reportes = ReportePalabras( M , N , Palabras , fecha)
        
        opcion=(input("ingrese opcion a realizar:"))
