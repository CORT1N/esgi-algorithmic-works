import time

def measure_execution_time(function, *args):
    start = time.time()
    function(*args)
    end = time.time()
    return end - start

# Example of use
# t = [i for i in range(10000)]
# execution_time = measure_execution_time(bubble_sort, t)
