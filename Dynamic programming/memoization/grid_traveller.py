'''
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your
goal is to travel to the bottom-right corner. you may only move down or right

In how many ways can you travel to the goal on a grid with dimensions M x N

Write a function gridTraveler(m,n) that calculates this
'''

print("----------------brute force recursion--------------------")


def grid_traveller(m, n):
    if(m == 1 and n == 1):
        return 1
    if(m <= 0 or n <= 0):
        return 0
    return grid_traveller(m-1, n) + grid_traveller(m, n-1)


print(grid_traveller(1, 1))  # 1
print(grid_traveller(2, 3))  # 3
print(grid_traveller(3, 2))  # 3
print(grid_traveller(3, 3))  # 6
# print(grid_traveller(18, 18))  # 2333606220


print("----------------memoization--------------------")


def grid_traveller_memoizatoin(m, n, memo={}):
    key = str(m) + "," + str(n)
    if(key in memo):
        return memo[key]
    if(m == 1 and n == 1):
        return 1
    if(m <= 0 or n <= 0):
        return 0
    memo[key] = grid_traveller_memoizatoin(
        m-1, n, memo) + grid_traveller_memoizatoin(m, n-1, memo)
    return memo[key]


print(grid_traveller_memoizatoin(1, 1))  # 1
print(grid_traveller_memoizatoin(2, 3))  # 3
print(grid_traveller_memoizatoin(3, 2))  # 3
print(grid_traveller_memoizatoin(3, 3))  # 6
print(grid_traveller_memoizatoin(18, 18))  # 2333606220
