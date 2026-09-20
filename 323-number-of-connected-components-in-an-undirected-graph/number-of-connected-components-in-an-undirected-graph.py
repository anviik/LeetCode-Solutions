class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        seen = set()
        count = 0
        vals = collections.defaultdict(list)
        for n1, n2 in edges:
            vals[n1].append(n2)
            vals[n2].append(n1)
        
        def dfs(node):
            for i in vals[node]:
                if i not in seen:
                    seen.add(i)
                    dfs(i)
        
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        return count