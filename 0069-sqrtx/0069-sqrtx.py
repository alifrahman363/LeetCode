class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        a = 0
        b = x
        
        while abs(a-b) != 1:
            mid = (a+b) // 2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                b = mid
            else: a = mid 
        return a

        