class SmallestInfiniteSet:

    def __init__(self):
        self.nums = set()
        self.vals = []
        self.smallval = 1

    def popSmallest(self) -> int:
        if self.vals:
            val = heapq.heappop(self.vals)
            self.nums.remove(val)
            return val
        num = self.smallval
        self.smallval += 1
        return num 

    def addBack(self, num: int) -> None:
        if num < self.smallval and num not in self.nums:
            self.nums.add(num)
            heapq.heappush(self.vals, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)