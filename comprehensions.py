from sys import getsizeof

n = 1000

list_comprehension = [k*k for k in range(n)]
set_comprehension = {k*k for k in range(n)}
dict_comprehension = {k: k*k for k in range(n)}
generator_comprehension = (k*k for k in range(n))

# print(list_comprehension)
# print(set_comprehension)
# print(dict_comprehension)
# print(generator_comprehension)

print("size of list comprehension", getsizeof(list_comprehension))
print("size of set comprehension", getsizeof(set_comprehension))
print("size of dict comprehension", getsizeof(dict_comprehension))
print("size of generator comprehension", getsizeof(generator_comprehension))
