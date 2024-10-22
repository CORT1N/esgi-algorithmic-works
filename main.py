from src.search import search
from src.measure import measure

all_sort_types = ['bubble', 'selection', 'insertion', 'quick', 'dutch', 'merge']
# Created this because dutch sort can't play with more than 3 different values
sort_types = ['bubble', 'selection', 'insertion', 'quick', 'merge']
search_types = ['dichotomic', 'linear']

iterations = 100
arr_lengths = [10, 100, 1000]
min_value = 0
max_values = [2, 9, 99, 999]

for max_value in max_values:
    for arr_length in arr_lengths:
        if max_value == 2:
            measure(all_sort_types, iterations, arr_length, min_value, max_value)
        else:
            measure(sort_types, iterations, arr_length, min_value, max_value)
            
searched_value = 1

for max_value in max_values:
    for arr_length in arr_lengths:
        measure(search_types, iterations, arr_length, min_value, max_value, searched_value)

# # On 10 different values, with an array of 10
# measure(all_sort_types, iterations, 10, 0, 9)
# # On 10 different values, with an array of 100
# measure(all_sort_types, iterations, 100, 0, 9)
# # On 10 different values, with an array of 1000
# measure(all_sort_types, iterations, 1000, 0, 9)

# # On 10 different values, with an array of 10
# measure(sort_types, iterations, 10, 0, 9)
# # On 10 different values, with an array of 100
# measure(sort_types, iterations, 100, 0, 9)
# # On 10 different values, with an array of 1000
# measure(sort_types, iterations, 1000, 0, 9)

# # On 100 different values, with an array of 10
# measure(sort_types, iterations, 10, 0, 99)
# # On 100 different values, with an array of 100
# measure(sort_types, iterations, 100, 0, 99)
# # On 100 different values, with an array of 1000
# measure(sort_types, iterations, 1000, 0, 99)

# # On 1000 different values, with an array of 10
# measure(sort_types, iterations, 10, 0, 999)
# # On 1000 different values, with an array of 100
# measure(sort_types, iterations, 100, 0, 999)
# # On 1000 different values, with an array of 1000
# measure(sort_types, iterations, 1000, 0, 999)

# sort(arr, 'bubble')
# sort(arr, 'selection')
# sort(arr, 'insertion')
# sort(arr, 'quick')
# sort(arr, 'dutch')
# sort(arr, 'merge')
# search(arr, 'dichotomic', 1)
# search(arr, 'linear', 1)