#Given a list of house values arranged in a circle, find the maximum amount you can rob without robbing two adjacent houses.

def rob_linear(nums):
    prev, curr = 0, 0
    for n in nums:
        prev, curr = curr, max(curr, prev + n)
    return curr

def rob(nums):
    if len(nums) == 1:
        return nums[0]
    # Case 1: Rob from 0 to n-2
    # Case 2: Rob from 1 to n-1
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

#Test
nums = [2,3,2]
print(rob(nums))  # Output: 3

nums2 = [1,2,3,1]
print(rob(nums2)) # Output: 4
