class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bt(o,c,cur):
            if len(cur) == n*2:
                res.append("".join(cur))
                return 
            if o < n:
                cur.append("(")
                bt(o+1, c, cur)
                cur.pop()
            if o > c:
                cur.append(")")
                bt(o, c+1, cur)
                cur.pop()
        bt(0,0,[])
        return res