steps = 0

def fib_recursive(n):
    global steps
    steps += 1  # every function call counts as a step
    
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

n = int(input("Enter n: "))
steps = 0
fib = fib_recursive(n)
print(f"Fibonacci({n}) = {fib}")
print(f"Step count (recursive) = {steps}")

def fib_iterative(n):
    steps = 0
    if n <= 1:
        steps += 1
        return n, steps
    
    a, b = 0, 1
    steps += 2  # initialization
    
    for _ in range(2, n + 1):
        a, b = b, a + b
        steps += 1  # each loop iteration counts as a step
    
    return b, steps

n = int(input("Enter n: "))
fib, steps = fib_iterative(n)
print(f"Fibonacci({n}) = {fib}")
print(f"Step count (iterative) = {steps}")