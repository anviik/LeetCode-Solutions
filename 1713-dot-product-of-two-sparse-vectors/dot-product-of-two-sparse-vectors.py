class SparseVector:
    def __init__(self, nums: List[int]):
        self.hm = {}
        for i, v in enumerate(nums):
            if v != 0:
                self.hm[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i, v in vec.hm.items():
            if i in self.hm:
                total += self.hm[i] * v
        return total
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)