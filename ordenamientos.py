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

def partition(vectorOrd, low, high):
    pivot = vectorOrd[high]
    i = low - 1
    for j in range(low, high):
        if vectorOrd[j] <= pivot:
            i = i + 1
            if vectorOrd[i] is not None:
                vectorOrd[i], vectorOrd[j] = vectorOrd[j], vectorOrd[i]
    print(f"se establece el indice en la posicion {i + 1}")
    vectorOrd[i + 1], vectorOrd[high] = vectorOrd[high], vectorOrd[i + 1]
    return i + 1

def quickSort(vectorOrd, low, high):
    if low < high:
        pi = partition(vectorOrd, low, high)
        print(f'{vectorOrd} ------------------------------------------------')
        print(f"acomodando los nros en subListas desde el {low} hasta {pi - 1}")  # Imprime la llamada recursiva para la sublista izquierda
        quickSort(vectorOrd, low, pi - 1)
        print(f'{vectorOrd} ------------------------------------------------')
        print(f"acomodando nros en la sublista desde el {pi + 1} hasta {high}")  # Imprime la llamada recursiva para la sublista derecha
        quickSort(vectorOrd, pi + 1, high)


### metodo de busqueda binaria (luego de usar quicksort) ###

def busquedaBinaria(vectorOrd , k, N ):

    Encontrado = False
    primero = 0
    ultimo = N - 1
    
    while (primero <= ultimo) and not Encontrado:
        
        # z es el punto medio de la lista
        z = (primero + ultimo)//2
        if (vectorOrd[z] == k):
            Encontrado = True
        else:
            if k < vectorOrd[z]:
                ultimo = z - 1
            else:
                primero = z + 1

    return Encontrado

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

        vectorOrd = vector
        print(vectorOrd)
        low = 0
        high = len(vector)-1
        print(f' el vector desordenado se veria asi: {vector}')
        vectorOrd = quickSort(vectorOrd, low, high)
        print(f'el vector ordenado se veria asi: {vectorOrd}')
        print('--------------------------------------------------------------------')
        print('1)insercion directa(baraja) ; 2)intercambio directo(burbuja)')
        print('3)seleccion directa ; 4)ordenamiento recursivo(quicksort)')
        print('5)si desea saber si algun nro esta dentro del arreglo ;0)si desea cerrar el programa')
        opcion=int(input('ingrese el metodo de ordenamiento que desea realizar: '))
        print('--------------------------------------------------------------------')

        if (opcion == 5):
        
            k = int(input('¿Qué numero desea buscar?  '))
            Encontrado = busquedaBinaria(vectorOrd, k, N)
            if Encontrado == False :
                print('El numero no se encuentra en la lista')
            else:
                print('el numero se encuentra en la lista, asi se veria la lista ordenada:')
                print(vectorOrd)