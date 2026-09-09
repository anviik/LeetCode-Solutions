class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [[-v, k] for k,v in count.items()]
        res = []
        prev = None
        heapq.heapify(maxheap)
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt, char = heapq.heappop(maxheap)
            res.append(char)
            cnt += 1
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return "".join(res)