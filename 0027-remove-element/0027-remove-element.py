class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        index = 0
        for l in range (len(nums)):
            if nums[l] != val:
                nums[index] = nums[l] 
                index += 1
        return index
