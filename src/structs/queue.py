def enqueue(queue, value):
    queue.append(value)

def dequeue(queue):
    if not queue:
        print("Queue is empty! Cannot dequeue.")
        return None
    return queue.pop(0)