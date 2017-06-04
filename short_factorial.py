# Not the most optimal one, but one of the shortest
factorial = lambda n: factorial(n - 1) * n if n else 1

print(factorial(5))
