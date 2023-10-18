class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        #one less row as we have already made a row above
        for i in range(numRows -1):
            temp = [0] + result[-1] + [0]
            row = []
            #old row and add zero to the end and the beginning
            for j in range(len(result[-1]) +1):
                row.append(temp[j] + temp[j+1])
            result.append(row)
        return result



