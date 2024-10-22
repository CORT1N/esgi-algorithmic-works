def sort(arr, type):
    arr_to_sort = arr.copy()
    # print(f'Starting { type } sort...')
    # print(f'Array before sorting : { arr }\n')
    if type == 'bubble':
        sorted_arr = bubble_sort(arr_to_sort)
    elif type == 'selection':
        sorted_arr = selection_sort(arr_to_sort)
    elif type == 'insertion':
        sorted_arr = insertion_sort(arr_to_sort)
    elif type == 'quick':
        sorted_arr = quick_sort(arr_to_sort)
    elif type == 'dutch':
        sorted_arr = dutch_sort(arr_to_sort)
    elif type == 'merge':
        sorted_arr = merge_sort(arr_to_sort, 0, len(arr_to_sort) - 1)
    # print(f'Sorted array : { sorted_arr }\n')

def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def dutch_sort(arr):
    c0 = 0
    c1 = 0
    c2 = 0
    for n in arr:
        if n == 0:
            c0 += 1
        elif n == 1:
            c1 += 1
        else:
            c2 += 1
    idx = 0
    for _ in range(c0):
        arr[idx] = 0
        idx += 1
    for _ in range(c1):
        arr[idx] = 1
        idx += 1
    for _ in range(c2):
        arr[idx] = 2
        idx += 1
    return arr

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr