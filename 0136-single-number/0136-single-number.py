class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #count instances of each number for every index
        for i in range(len(nums)):
            if(nums.count(nums[i])==1):
                return nums[i]

       

