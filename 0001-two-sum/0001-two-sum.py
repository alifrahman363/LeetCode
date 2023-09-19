class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          
        hashMap = {} # value: index
        for i, n in enumerate(nums): # n = value, i = index of "nums" list
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i] #indices of the integers
            hashMap[n] = i # means hashmaps value n goes to index i
            


