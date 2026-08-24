class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return (-1*heap[0])