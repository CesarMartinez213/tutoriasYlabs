

###  definimos el subrograma para la funcion recursiva ###

def recorridoPiscina(profundidad):

    if profundidad == 0:
        print('llegamos al fondo de la piscina')
        return
    else:
        print(f'estamos a {profundidad}mt(s) de profundidad')
        recorridoPiscina(profundidad-1)
        print(f'falta(n) {profundidad} mt(s) para poder tocar el fondo de la  piscina')

### programa principal ###

profundidad=int(input('ingrese profundidad: '))

recorridoPiscina(profundidad)