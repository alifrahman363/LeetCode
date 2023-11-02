class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dc = defaultdict(lambda:0) 
        #when I call x[k] for a nonexistent key k (such as a statement like v=x[k]), 
        #the key-value pair (k,0) will be automatically added to the dictionary, 
        #as if the statement x[k]=0 is first executed
        for a in nums1:
            dc[a] = 1

        nums2=set(nums2) 
        # Converts the list to a set, removing duplicates 
        #[1, 2, 2, 3, 4, 4, 5] ---> {1, 2, 3, 4, 5}
        for a in nums2:
            if(dc[a]==1):
                res.append(a)
        return res



        
