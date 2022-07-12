def add(ret, a, b):
    ret["result"] = a + b


def subtract(ret, a, b):
    ret["result"] = a - b


def divide(ret, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        ret["result"] = a / b


def multiply(ret, a, b):
    ret["result"] = a * b
