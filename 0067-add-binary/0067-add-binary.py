class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0 

        #reverse the input string
        a, b = a[::-1], b[::-1]

        #iterate through every digit/char of the string
        for i in range(max(len(a), len(b))):
             
            #as we are going through the max length of the strings to iterate through
            #there could be a possibility where one string is shorter than other
            #so to handle the error of converting a digit into integer we set value as 0:
            #digitA = a[i] if i<len(a) else 0

            #Using ascii value to convert string to integer
            #Dividing the ascii code of the char from ascii zero 
            #to get Integer value of digitA  
            digitA = ord(a[i]) - ord("0") if i<len(a) else 0
            digitB = ord(b[i]) - ord("0") if i<len(b) else 0

            total = digitA + digitB + carry 
            char = str(total%2) #converting to string to concatenate with res
            res = char + res
            carry = total // 2 
        
        #if still we have a carry we concatenate 1  with the result
        if carry:
            res = "1" + res
        return res