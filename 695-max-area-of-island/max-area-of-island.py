class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = 0
        seen = set()
        def bfs(r, c):
            count = 0
            seen.add((r,c))
            q = collections.deque()
            q.append((r,c))
            
            while q:
                count += 1
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                r,c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr,nc))
            return count

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in seen:
                    length = max(length, bfs(r,c))
        return length