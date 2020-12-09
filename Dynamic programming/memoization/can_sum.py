'''
Write a functoin canSum(targetSum,numbers) that takes in a targetsum and an array of numbers
as arguments

The function should return boolean indicating whether or not it  is possible
to generate the target sum using numbers from the array

you may use an element of the array as many times as needed

you may assume that all inputs numbers are non-negative

'''

print("---------------recursion-----------------------")


def can_sum(target_sum, numbers):
    if(target_sum == 0):
        return True
    if(target_sum < 0):
        return False
    for num in numbers:
        if(can_sum(target_sum-num, numbers)):
            return True

    return False


print(can_sum(7, [2, 3]))  # true
print(can_sum(7, [5, 3, 4, 7]))  # true
print(can_sum(7, [2, 4]))  # false
print(can_sum(8, [2, 3, 5]))  # true
# print(can_sum(7000, [7, 14]))  # false


print("--------------------memoization------------------")


'''
const can_sum = (target_sum, numbers, memo = {}) => {
  if (target_sum in memo) return memo[target_sum];
  if (target_sum === 0) return true;
  if (target_sum < 0) return false;
  for (let num of numbers) {
    if (can_sum(target_sum - num, numbers, memo) === true) {
      memo[target_sum] = true;
      return true;
    }
  }
  memo[target_sum] = false;
  return false;
};
'''


def can_sum_memoization(target_sum, numbers, memo=None):
    if(memo == None):
        memo = {}
    # print(target_sum)
    if(target_sum in memo):
        return memo[target_sum]
    if(target_sum == 0):
        return True
    if(target_sum < 0):
        return False
    for num in numbers:
        remainder = target_sum - num
        if(can_sum_memoization(remainder, numbers, memo) == True):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


if(__name__ == "__main__"):

    print(can_sum_memoization(7, [2, 3]))  # true
    print(can_sum_memoization(7, [5, 3, 4, 7]))  # true
    print(can_sum_memoization(7, [2, 4]))  # false
    print(can_sum_memoization(8, [2, 3, 5], {}))  # true
    print(can_sum_memoization(300, [7, 14], {}))  # false


'''
time: 
    bruteforce : O(n^m)
    memoization : O(n*m)
space:
    O(m) for both
'''
