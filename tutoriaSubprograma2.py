#### comprobar que un identificador es valido ####

### el identificador no puede tener mas de 255 caracteres ###

def comprobarLongitud(cadenaUsuario):
    longValida = 0
    if [len(cadenaUsuario) > 255]:
        print('La longitud del identificador supera el limite permitido')
    else:
        longValida=1
    return (longValida)

## la inicial del identificador no puede ser algo distinto de una letra ##

def comprobarInicial(cadenaUsuario):
    inicialValida = 0
    if [(chr(cadenaUsuario[0])>64) and (chr(cadenaUsuario)<91)] or [(chr(cadenaUsuario[0])>96) and (chr(cadenaUsuario)<123)]:
        inicialValida = 1
    else:
        print('el 1er carater del identificador es invalido')
    return (longValida)

## el resto del nombre no puede tener caracteres especiales ##
## que no sean: _ y - ##

def comprobarCaracteres(cadenaUsuario):
    caracteresValidos = 0
    for i in range(len(cadenaUsuario)):
        if [(chr(cadenaUsuario[i])>47) and (chr(cadenaUsuario[i])<58)] or [(chr(cadenaUsuario[i])>64) and (chr(cadenaUsuario[i])<91)] or [(chr(cadenaUsuario[i])>96) and (chr(cadenaUsuario[i])<123)] or [chr(cadenaUsuario[i])=45] or [chr(cadenaUsuario[i]=95)]:
            caracteresValidos = 1
        else:
            print('el identificador cuenta con un caracter invalido')
            i = len(cadenaUsuario)
    return (caracteresValidos)

# programa principal #
cadenaUsuario=str(input('ingrese el nombre del identificador: '))
longValida = comprobarLongitud(cadenaUsuario)
inicialValida = comprobarInicial(cadenaUsuario)
caracteresValidos = comprobarCaracteres(cadenaUsuario)
if longValida = 1 and inicialValida = 1 and caracteresValidos = 1:
    print(f'el identificador "{cadenaUsuario}" es valido')