print("------------------normal recursion--------------")


def fib(n):
    if(n <= 2):
        return 1
    return fib(n-1) + fib(n-2)


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
# print(fib(50)) # 12586269025 tokes soo long time with the above approach

print("------------------memoization--------------")


def fib_memoization(n, memo=None):
    if(memo is None):
        memo = {}
    if(n in memo):
        return memo[n]
    if(n <= 2):
        return 1
    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]


print(fib_memoization(6))
print(fib_memoization(7))
print(fib_memoization(8))
print(fib_memoization(50))
