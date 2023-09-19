class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False 

        # we need to find the right and the left digit of the number  
        # If the number is 123 we need to devide it by 1000
        # If the number is 1234 we need to devide it by 10000

        div = 1
        while x >= div * 10 :
            div *= 10 
        
        while x: 
            right = x % 10 
            left = x // div #we use double // in python to floor division

            if left != right : return False 

            # 152 % 100= 52 removes left digit
            # 52 // 10 = 5 removes right digit 
            x = (x % div) // 10
            
            # As the operation removes 2 digits. we need to remove 2 digits form the div value also. 
            div = div / 100
        return True


        