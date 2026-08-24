class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        x = Counter(nums)
        res = []
        for key, v in x.items():
            heapq.heappush(heap, (v,key))
        while len(heap) > k:
            heapq.heappop(heap)
        while heap:
            val, num = heapq.heappop(heap)
            res.append(num)
        return res
