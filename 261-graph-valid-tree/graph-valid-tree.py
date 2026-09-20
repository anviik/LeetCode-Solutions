class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        seen = set()
        vals = collections.defaultdict(list)

        for n1, n2 in edges:
            vals[n1].append(n2)
            vals[n2].append(n1)
        
        def bfs(node):
            q = collections.deque()
            seen.add(node)
            q.append((-1,node))
            
            while q:
                parent, x = q.popleft()
                for i in vals[x]:
                    if i == parent:
                        continue
                    if i in seen:
                        return False
                    q.append((x,i))
                    seen.add(i)
            return True
        
        return bfs(0) and len(seen) == n
