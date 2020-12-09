'''
write a function howSum(targetsum, numbers) 

the function should return an array containing any combinations of elements
that add up to exactly the targetsum. If there is no combinations that adds
up to the tartet sum, then return null

if there are multiple combinations possible, you may return any single one
'''

print("------------brute force recursion --------")


def how_sum(target_sum, numbers):
    if(target_sum == 0):
        return []
    if(target_sum < 0):
        return None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers)
        if(remainder_result != None):
            remainder_result.append(num)
            return remainder_result
    return None


print(how_sum(7, [2, 3]))  # [3,2,2]
print(how_sum(7, [5, 3, 4, 7]))  # [4,3]
print(how_sum(7, [2, 4]))  # Null
print(how_sum(8, [2, 3, 5]))  # [2,2,2,2]
# print(how_sum(300, [7, 14]))  # Null

print("------------memoization------------------")


def how_sum_memoization(target_sum, numbers, memo=None):
    if(memo is None):
        memo = {}
    if(target_sum in memo):
        return memo[target_sum]
    if(target_sum == 0):
        return []
    if(target_sum < 0):
        return None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum_memoization(remainder, numbers, memo)
        if(remainder_result != None):
            remainder_result.append(num)
            memo[target_sum] = remainder_result
            return remainder_result
    memo[target_sum] = None
    return None


print(how_sum_memoization(7, [2, 3]))  # [3,2,2]
print(how_sum_memoization(7, [5, 3, 4, 7]))  # [4,3]
print(how_sum_memoization(7, [2, 4]))  # Null
print(how_sum_memoization(8, [2, 3, 5]))  # [2,2,2,2]
print(how_sum_memoization(280, [3, 2]))  # Null


'''
m = target sum
n = len of numbers 

time: 
    bruteforce : O(n^m)
    memoization : O(n*m)
space:
    bruteforce : O(m)
    memoization : O(m^2) every element has an array of m elements in memo object
'''
