import random
''' crear un programa que ordene un arreglo, implementando los metodos:
        insercion directa(baraja)
        intercambio directo(burbuja)
        seleccion directa
        ordenamiento directo(quicksort) '''
###---------------------------------------------------------------------------

### metodo baraja ###

def baraja(vector , N):

    vectorOrd = vector
    for i in range(N):
        elemento = vectorOrd[i]
        j = i-1
        while (j>=0) and (vectorOrd[j]>elemento):
            vectorOrd[j+1] = vectorOrd[j]
            j = j - 1
        vectorOrd[j+1] = elemento

    return vectorOrd

### metodo burbuja ###

def burbuja(vector , N):

    vectorOrd = vector
    for i in range (N):

        for j in range(N-i-1):

            if (vectorOrd[j]>vectorOrd[j+1]):

                AUX = vectorOrd[j]
                vectorOrd[j] = vectorOrd[j+1]
                vectorOrd[j+1] = AUX
                
    return vectorOrd

### metodo de seleccion directa ###

def SelDirecta(vector):

    vectorOrd = vector
    for i in range(0, len(vectorOrd)-1):
        aux = vectorOrd[i]
        posMinimo = i
        for j in range(i+1, len(vector)):
            if (vectorOrd[j] < aux):
                aux = vectorOrd[j]
                posMinimo = j
        vectorOrd[posMinimo] = vectorOrd[i]
        vectorOrd[i] = aux

    return vectorOrd


### metodo de quicksort ###


def quicksort(vector):
    vectorOrd = vector
    if len(vectorOrd) <= 1:
        return vectorOrd

    pivote = vectorOrd[len(vectorOrd) // 2]
    sublista_izquierda = [x for x in vectorOrd if x <= pivote]
    sublista_derecha = [x for x in vectorOrd if x > pivote]

    print("Lista original:", vectorOrd)
    print("Pivote:", pivote)
    print("Sublista izquierda:", sublista_izquierda)
    print("Sublista derecha:", sublista_derecha)

    return quicksort(sublista_izquierda) + [pivote] + quicksort(sublista_derecha)



### metodo de busqueda binaria (luego de usar quicksort) ###

def busquedaBinaria(vectorOrd , numABuscar):

    numEncontrado = 0
    return

### programa pprincipal ------------------------------------------------------
N=int(input('ingrese el tamaño del vector: '))

vector = []

for i in range(N):
    vector.append(random.randint(0, 100))

print('--------------------------------------------------------------------')
print('1)insercion directa(baraja) ; 2)intercambio directo(burbuja)')
print('3)seleccion directa ; 4)ordenamiento recursivo(quicksort)')
print('0)si desea cerrar el programa')
opcion=int(input('ingrese el metodo de ordenamiento que desea realizar: '))
print('--------------------------------------------------------------------')

while (opcion != 0):
    
    if (opcion == 1):
        
        print(f' el vector desordenado se veria asi: {vector}')
        vectorOrd = baraja(vector , N)
        print(f'el vector ordenado se veria asi : {vectorOrd}')
        print('--------------------------------------------------------------------')
        print('1)insercion directa(baraja) ; 2)intercambio directo(burbuja)')
        print('3)seleccion directa ; 4)ordenamiento recursivo(quicksort)')
        print('0)si desea cerrar el programa')
        opcion=int(input('ingrese el metodo de ordenamiento que desea realizar: '))
        print('--------------------------------------------------------------------')

    elif (opcion == 2):

        print(f' el vector desordenado se veria asi: {vector}')
        vectorOrd = burbuja(vector , N)
        print(f'el vector ordenado se veria asi : {vectorOrd}')
        print('--------------------------------------------------------------------')
        print('1)insercion directa(baraja) ; 2)intercambio directo(burbuja)')
        print('3)seleccion directa ; 4)ordenamiento recursivo(quicksort)')
        print(' 0)si desea cerrar el programa')
        opcion=int(input('ingrese el metodo de ordenamiento que desea realizar: '))
        print('--------------------------------------------------------------------')
    
    elif (opcion == 3):
    
        print(f' el vector desordenado se veria asi: {vector}')
        vectorOrd = SelDirecta(vector)
        print(f'el vector ordenado se veria asi : {vectorOrd}')
        print('--------------------------------------------------------------------')
        print('1)insercion directa(baraja) ; 2)intercambio directo(burbuja)')
        print('3)seleccion directa ; 4)ordenamiento recursivo(quicksort)')
        print(' 0)si desea cerrar el programa')
        opcion=int(input('ingrese el metodo de ordenamiento que desea realizar: '))
        print('--------------------------------------------------------------------')
    
    elif (opcion == 4):

        print(f' el vector desordenado se veria asi: {vector}')
        vectorOrd = quicksort(vector)
        print(f'el vector ordenado se veria asi : {vectorOrd}')
        print('--------------------------------------------------------------------')
        print('1)insercion directa(baraja) ; 2)intercambio directo(burbuja)')
        print('3)seleccion directa ; 4)ordenamiento recursivo(quicksort)')
        print(' 0)si desea cerrar el programa')
        opcion=int(input('ingrese el metodo de ordenamiento que desea realizar: '))
        print('--------------------------------------------------------------------')