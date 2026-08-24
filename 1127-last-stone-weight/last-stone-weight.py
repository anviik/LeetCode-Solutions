class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [0] * len(stones)
        for i in range(len(stones)):
            heap[i] = -1 * stones[i]
        heapq.heapify(heap)
        print(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, ((x-y)))
        return(-1* heap[0]) if heap else 0


