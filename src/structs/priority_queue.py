from src.structs.heap import *

def max_heap(arr):
    if arr:
        return arr[0]
    return None

def extract_max_heap(arr):
    if len(arr) == 0:
        return None
    max_value = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, len(arr), 0)
    return max_value

def increase_key_heap(arr, i, key):
    if key < arr[i]:
        print("New key is smaller than current key!")
        return
    arr[i] = key
    while i > 0 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)

def insert_max_heap(arr, key):
    arr.append(float('-inf'))
    increase_key_heap(arr, len(arr)-1, key)