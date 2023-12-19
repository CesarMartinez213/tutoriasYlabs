def quicksortAlg(array):
    
    quicksort(array, 0, len(array)-1)

def quicksort(array, s, e):
    if s < e:
        medio = (s + e)//2
        pivote = array[medio]
        indice = partition(array, s, e, pivote)
        quicksort(array, s, indice-1)
        quicksort(array, indice, e)

def partition(array, l, r, pivote):

    while (l <= r):

        while (array[l] < pivote):
            l=l+1
        
        while (pivote < array[r]):
            r=r-1
        
        if (l <= r):
            array[l],array[r] = array[l],array[r]
            l = l+1
            r = r-1
    return l 

array = [2, 5, 3, 1, 4]
print(f'before sort: {array}' )
quicksortAlg(array)     
print(f'after sort: {array}')  