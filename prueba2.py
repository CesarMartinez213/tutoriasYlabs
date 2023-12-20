def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            print(f"Swapping {array[i]} and {array[j]}")  # Imprime los intercambios
            array[i], array[j] = array[j], array[i]
    print(f"Placing pivot {pivot} at index {i + 1}")  # Imprime la colocación del pivote
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        print(f"Recursively sorting left subarray: {array[:pi]}")  # Imprime la llamada recursiva para la sublista izquierda
        quickSort(array, low, pi - 1)
        print(f"Recursively sorting right subarray: {array[pi + 1:]}")  # Imprime la llamada recursiva para la sublista derecha
        quickSort(array, pi + 1, high)

array = [10, 2, 37, 8, 1, 49, 13]
low = 0
high = len(array) - 1
quickSort(array, low, high)

print(f"Sorted array: {array}")
