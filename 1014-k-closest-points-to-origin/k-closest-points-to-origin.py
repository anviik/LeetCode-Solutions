class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #sort by dist
        res = []
        ans = []
        for x,y in points:
            res.append((math.sqrt((x*x)+ (y*y)), x, y))
        heapq.heapify(res)
        for i in range(k):
            dist, x, y = heapq.heappop(res)
            ans.append([x, y])
        return ans
