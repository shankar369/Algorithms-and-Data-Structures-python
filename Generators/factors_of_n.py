import time


def factors(n):
    k = 1
    while k < n//2+1:
        if(n % k == 0):
            yield k
        k += 1


def factors_optimized(n):
    k = 1
    while k*k < n:
        if(n % k == 0):
            yield k
            yield n // k
        k += 1
    if(k*k == n):
        yield k


start_time = time.time()
for i in factors(99999999):
    # print(i)
    pass
end_time = time.time()

print("time taken for normal method : ", end_time - start_time)
start_time = time.time()
for i in factors_optimized(99999999):
    pass
    # print(i)
end_time = time.time()


print("time taken for optimized method", end_time - start_time)
