
nums = int(input()) # Input array
expectedNums = int(input()) #The expected answer with correct length

#Function
class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        n = len(set(nums))
        lens = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[lens] = nums[i]
                lens = lens+1
        
        return lens

k = removeDuplicates(nums) # Calls your implementation

assert k == expectedNums.length
for i in range(k):
    assert nums[i] == expectedNums[i]

#Function
class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        n = len(set(nums))
        lens = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[lens] = nums[i]
                lens = lens+1
        
        return lens