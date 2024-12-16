def is_empty(stack):
    return len(stack) == 0

def push(stack, value):
    stack.append(value)

def pop(stack):
    if is_empty(stack):
        print("Stack is empty! Cannot pop.")
        return None
    return stack.pop()