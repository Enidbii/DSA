
def twoSum(nums, target):
    i = 0
    while i < len(nums):
        j=0
        while j < len(nums):
            sum = nums[i] + nums[j]
            if sum == target:
                return i, j
            j+=1
        i+=1

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))