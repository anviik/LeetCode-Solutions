class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while r >= l:
            m = (r+l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
            if hours <= h:
                r = m- 1
            else:
                l = m + 1
        return l