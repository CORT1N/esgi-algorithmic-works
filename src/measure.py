import time, random

from src.sort import sort
from src.search import search

def measure(types, iterations, arr_length, min_value, max_value, value=None):
    print(f'\nMeasuring on { arr_length } values between { min_value } and { max_value } for { iterations } iterations :\n')
    for type in types:
        average = 0
        for _ in range(iterations):
            arr = [random.randint(min_value, max_value) for _ in range(arr_length)]
            # execution_time = measure_execution_time(sort if value is None else search, arr, type, None if value is None else value)
            if value is None:
                execution_time = measure_execution_time(sort, arr, type)
            else:
                execution_time = measure_execution_time(search, arr, type, value)
            average += execution_time
        average = average / iterations
        print(f'The { type } { 'sort' if value == None else 'search' } function took on average { average } ms')

def measure_execution_time(function, *args):
    start = time.time()
    function(*args)
    end = time.time()
    return round((end - start) * 1000, 8)