class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while r >= l:
            daysneeded, cur = 1, 0
            m = (l+r) // 2
            for w in weights:
                if w + cur > m:
                    daysneeded += 1
                    cur = 0
                cur += w
            if days >= daysneeded:
                r = m -1
            else:
                l = m + 1
        return l
