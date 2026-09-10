class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []
        def bt(cur, i):
            if len(cur) == len(digits):
                res.append("".join(cur))
                return 
            for char in keys[int(digits[i])]:
                cur.append(char)
                bt(cur, i+1)
                cur.pop()
        bt([], 0)
        return res