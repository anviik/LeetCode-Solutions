class Solution:
    def compress(self, chars: list[str]) -> int:
        r, l, v = 0, 0, 0
        while r < len(chars):
            curval = chars[l]
            while r < len(chars) and chars[r] == curval:
                r += 1
            chars[v] = curval
            v += 1
            total = (r-l)
            if total > 1:
                for digit in str(total):
                    chars[v] = digit
                    v += 1
            l = r
        return v
