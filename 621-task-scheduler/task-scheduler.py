class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        total = 0
        maxheap = [-c for c in counter.values()]
        heapq.heapify(maxheap)
        queue = deque()
        while queue or maxheap:
            total += 1
            if maxheap:
                cnt = heapq.heappop(maxheap) + 1
                if cnt != 0:
                    queue.append([total+n, cnt])
            if queue and queue[0][0] == total:
                heapq.heappush(maxheap, queue.popleft()[1])
        return total

