def add(queue, a, b):
    queue.put(a + b)


def subtract(queue, a, b):
    queue.put(a - b)


def divide(queue, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    queue.put(a / b)


def multiply(queue, a, b):
    queue.put(a * b)
