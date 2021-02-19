'''
write a function 'bestSum(targetSum,numbers) that takes in a targetSum and an array of numbers
as arguments

The function should return an array containing the shortest combination of numbers that add up to 
targetsum

if there is a tie for the shortest combination you may return any one of shortest

Eg: best_sum(8,[2,3,5]) 
[2,2,2,2]
[2,3,3]
[3,5]
here the answer would be [3,5]

'''
print("-----------bruteforce sum---------------")


def best_sum(target_sum, numbers):
    if(target_sum == 0):
        return []
    if(target_sum < 0):
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers)
        if(remainder_combination != None):
            remainder_combination.append(num)
            # if the current combination is shorter than the shortest_combination update it
            if(shortest_combination == None or (len(remainder_combination) < len(shortest_combination))):
                shortest_combination = remainder_combination

    return shortest_combination


print(best_sum(7, [5, 3, 4, 7]))  # [7]
print(best_sum(8, [2, 3, 5]))  # [3,5]
print(best_sum(8, [1, 4, 5]))  # [4,4]
# print(best_sum(30, [1, 2, 5, 25]))  # [25,25,25,25]

print("----------memoization----------------")


def best_sum_memoization(target_sum, numbers, memo=None):
    if(memo is None):
        memo = {}
    if(target_sum in memo):
        return memo[target_sum]
    if(target_sum == 0):
        return []
    if(target_sum < 0):
        return None
    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum_memoization(remainder, numbers, memo)
        if(remainder_combination != None):
            combination = remainder_combination.copy()
            combination.append(num)
            # if the current combination is shorter than the shortest_combination update it
            if(shortest_combination == None or (len(remainder_combination) < len(combination))):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination


print(best_sum_memoization(7, [5, 3, 4, 7]))  # [7]
print(best_sum_memoization(8, [2, 3, 5]))  # [3,5]
print(best_sum_memoization(8, [1, 4, 5]))  # [4,4]
print(best_sum_memoization(100, [1, 2, 5, 25]))  # [25,25,25,25]


'''
m = target sum
n = numbers.length

bruteforce:
    time: O(n^m * m)
    space: O(m^2)
memoized:
    time: O(m^2 *n)
    space: O(m^2)
'''
