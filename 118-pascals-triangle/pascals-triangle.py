class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1): #len of res
            cur = [0] + res[-1] + [0]
            temp = []
            for j in range(len(res[-1]) + 1):
                temp.append(cur[j]+cur[j+1])
            res.append(temp)
        return res