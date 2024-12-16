# Based on the assomption that this is a Max-Heap

def parent(i):
    return (i-1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def heapify(arr, n, i):
    largest = i
    left_child = left(i)
    right_child = right(i)

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)