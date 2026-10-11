class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()
        def bfs(city):
            q = deque([city])
            visited.add(city)
            while q:
                cur = q.popleft()
                for i in range(len(isConnected)):
                    if isConnected[i][cur] == 1 and i not in visited:
                        visited.add(i)
                        q.append(i)

        for i in range(len(isConnected)):
            if i not in visited:
                res += 1
                bfs(i)
        return res