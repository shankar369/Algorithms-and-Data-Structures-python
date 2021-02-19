import sys
data = []
n = int(input("Enter value of n : "))
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)
