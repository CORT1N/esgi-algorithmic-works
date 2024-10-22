def search(arr, type, x):
    # print(f'Starting { type } search... for value : { x }')
    # print(f'Array : { arr }\n')
    if type == 'dichotomic':
        index = dichotomic_search(arr, 0, len(arr) - 1, x)
    if type == 'linear':
        index = linear_search(arr, x)
    # if index == -1:
    #     print(f'The value { x } is not present in the array.')
    # else:
    #     print(f'The value { x } is at index { index }')

def dichotomic_search(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return dichotomic_search(arr, low, mid-1, x)
        else:
            return dichotomic_search(arr, mid + 1, high, x)
    else:
        return -1
    
def linear_search(arr, x):
    for i in range(0, len(arr)):
        if (arr[i] == x):
            return i
    return -1