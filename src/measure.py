import time, random

from src.sort import sort
from src.search import search
from src.structs.heap import build_max_heap, heap_sort
from src.structs.priority_queue import *
from src.structs.stack import push, pop

def measure_execution_time(function, *args):
    start = time.time()
    function(*args)
    end = time.time()
    return round((end - start) * 1000, 8)

def measure_alg(types, iterations, arr_length, min_value, max_value, value=None):
    print(f'\nMeasuring on { arr_length } values between { min_value } and { max_value } for { iterations } iterations:\n')
    for type in types:
        average = 0
        for _ in range(iterations):
            arr = [random.randint(min_value, max_value) for _ in range(arr_length)]
            if value is None:
                execution_time = measure_execution_time(sort, arr, type)
            else:
                execution_time = measure_execution_time(search, arr, type, value)
            average += execution_time
        average = average / iterations
        print(f'The { type } { 'sort' if value == None else 'search' } function took on average { average } ms')
        
def measure_struct_ops(types, iterations, arr_length, min_value, max_value):
    print(f'\nMeasuring on { arr_length } values between { min_value } and { max_value } for { iterations } iterations:\n')
    for type in types:
        if type == 'heap':
            measure_heap_ops(iterations, arr_length, min_value, max_value)
        elif type == 'priority_queue':
            measure_priority_queue_ops(iterations, arr_length, min_value, max_value)
        elif type == 'stack':
            measure_stack_ops(iterations, arr_length)
        elif type == 'queue':
            measure_queue_ops(iterations, arr_length)
        elif type == 'linked_list':
            measure_linked_list_ops(iterations, arr_length)
            
def measure_heap_ops(iterations, arr_length, min_value, max_value):
    print("Heap operations:")
    average = 0
    for _ in range(iterations):
        arr = [random.randint(min_value, max_value) for _ in range(arr_length)]
        execution_time = measure_execution_time(build_max_heap, arr)
        average += execution_time
    average = average / iterations
    print(f'The build_max_heap function took on average { average } ms')
    
    average = 0
    for _ in range(iterations):
        arr = [random.randint(min_value, max_value) for _ in range(arr_length)]
        execution_time = measure_execution_time(heap_sort, arr)
        average += execution_time
    average = average / iterations
    print(f'The heap_sort function took on average { average } ms')
    
def measure_priority_queue_ops(iterations, arr_length, min_value, max_value):
    print("\nPriority queue operations:")
    average = 0
    for _ in range(iterations):
        arr = [random.randint(min_value, max_value) for _ in range(arr_length)]
        execution_time = measure_execution_time(max_heap, arr)
        average += execution_time
    average = average / iterations
    print(f'The max_heap function took on average { average } ms')
    
    average = 0
    for _ in range(iterations):
        arr = [random.randint(min_value, max_value) for _ in range(arr_length)]
        execution_time = measure_execution_time(extract_max_heap, arr)
        average += execution_time
    average = average / iterations
    print(f'The extract_max_heap_sort function took on average { average } ms')
            
    average = 0
    for _ in range(iterations):
        arr = [random.randint(min_value, max_value) for _ in range(arr_length)]
        index = random.randint(0, len(arr) - 1)
        new_key = arr[index] + random.randint(1, 100)
        execution_time = measure_execution_time(increase_key_heap, arr, index, new_key)
        average += execution_time
    average = average / iterations
    print(f'The increase_key_heap function took on average { average } ms')
    
    average = 0
    for _ in range(iterations):
        arr = [random.randint(min_value, max_value) for _ in range(arr_length)]
        index = random.randint(0, len(arr) - 1)
        new_key = arr[index] + random.randint(1, 100)
        key = random.randint(min_value, max_value)
        execution_time = measure_execution_time(insert_max_heap, arr, key)
        average += execution_time
    average = average / iterations
    print(f'The insert_max_heap function took on average { average } ms')
    
def measure_stack_ops(iterations, stack_size):
    print("\nStack operations:")
    
    average = 0
    for _ in range(iterations):
        stack = []
        average += measure_execution_time(lambda: [stack.append(i) for i in range(stack_size)])
    average = average / iterations
    print(f'The push function took on average { average } ms')
    
    average = 0
    for _ in range(iterations):
        stack = [i for i in range(stack_size)]
        average += measure_execution_time(lambda: [stack.pop() for _ in range(stack_size)])
    avg_pop_time = average / iterations
    print(f'The pop function took on average { average } ms')
    
def measure_queue_ops(iterations, queue_size):
    print("\nQueue operations:")
    
    average = 0
    for _ in range(iterations):
        queue = []
        average += measure_execution_time(lambda: [queue.append(i) for i in range(queue_size)])
    average = average / iterations
    print(f'The enqueue function took on average { average } ms')
    
    average = 0
    for _ in range(iterations):
        queue = [i for i in range(queue_size)]
        average += measure_execution_time(lambda: [queue.pop(0) for _ in range(queue_size)])
    average = average / iterations
    print(f'The dequeue function took on average { average } ms')

def measure_linked_list_ops(iterations, list_size):
    print("\nLinked List operations:")
    
    average = 0
    for _ in range(iterations):
        linked_list = []
        average += measure_execution_time(lambda: [linked_list.insert(0, i) for i in range(list_size)])
    average = average / iterations
    print(f'The insertion function took on average { average } ms')
    
    average = 0
    for _ in range(iterations):
        linked_list = [i for i in range(list_size)]
        key = random.randint(0, list_size - 1)
        average += measure_execution_time(lambda: key in linked_list)
    average = average / iterations
    print(f'The search function took on average { average } ms')
    
    average = 0
    for _ in range(iterations):
        linked_list = [i for i in range(list_size)]
        key = random.randint(0, list_size - 1)
        average += measure_execution_time(lambda: linked_list.remove(key) if key in linked_list else None)
    average = average / iterations
    print(f'The deletion function took on average { average } ms')