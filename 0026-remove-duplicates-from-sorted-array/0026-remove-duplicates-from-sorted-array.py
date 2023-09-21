class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #set left pointer to index 1. As the first value will always remain on the index = 0. Because this is a ascending sorted list. Also set right pointer to index 1.
        l = 1  
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r] #Set value of nums[r] to index[l]
                l += 1
                # We dont need to increase the value of r pointer as the for loop takes care of it 
        return l


