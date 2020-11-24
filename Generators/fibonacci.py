def fibonacci(n):
    a = 0
    b = 1
    while (a <= n):
        yield a
        a, b = b, a+b


for i in fibonacci(99999999999999999999999999):
    print(i)
