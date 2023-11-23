from math import sqrt
#### crear un programa que use subprogramas para calcular las raices de una ecuacion cuadratica ####

### subprograma para calcular el discriminante ###

def Discriminante(a,b,c):
    d = b**2 - 4*a*c
    return (d)

## subprograma para cuando a es 0 y b no lo es ##

def raizUnica(b,c):
    rUnica = -c/b
    return(rUnica)

# programa principal #

a=int(input('ingrese el valor de a: '))
b=int(input('ingrese el valor de b: '))
c=int(input('ingrese el valor de c: '))
if (a==0) and (b==0):
    print('la ecuacion es degenerada')
elif (a==0) and (b!=0):
    rUnica = raizUnica(b,c)
    print(f'la ecuacion cuenta con una raiz unica de valor: {rUnica}')
elif (a!=0) and (b!=0):
    d = Discriminante(a,b,c)
    # ahora se usa la resolvente cuadratica para buscar las 2 raices de la ecuacion #
    if (d>=0):
        x_1 = (-b+(sqrt(b**2-4*a*c)))/2*a
        x_2 = (-b-(sqrt(b**2-4*a*c)))/2*a
        print(f'las raices de la ecuacion son: {x_1} y {x_2}')
    elif (d<0):
        J = -b/2*a
        Q = (sqrt(abs(d)))/2*a
        print(f'las raices complejas de la ecuacion son: ({J}) + ({Q})i y ({J}) - ({Q})i')