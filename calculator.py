import math

def add(x, y):
    return x + y

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

def sin(x, N):
    r = 0
    for n in range(N+1):
        r += math.pow(-1, n)*math.pow(x, 2*n+1)/factorial(2*n+1)
    return r

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y
