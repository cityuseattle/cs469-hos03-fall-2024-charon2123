def fibonacci(n):
    '''Calculate the fibonacci of n'''

    # Base case
    if n == 0 or n == 1:
        return n
    
    return fibonacci (n - 1) + fibonacci (n-2)

for i in range (2 ** 10):
    print(f"F({i}) = ", fibonacci(i))