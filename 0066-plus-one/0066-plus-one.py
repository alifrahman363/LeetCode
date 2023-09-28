class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        concatStr = ""
        position = len(digits) + 1
        for i in range(0, len(digits)):
            concatStr = concatStr + str(digits[i])

        intStr = int(concatStr) + 1
        # map func.s 1st parameter works as function. here it converts the character to integer
        # 2nd parameter works as a list to iterate through
        arr = list(map(int, str(intStr)))
        return arr 

