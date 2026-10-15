class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = collections.defaultdict(list)
        x = [0] * numCourses
        seen = set()
        for a, b in prerequisites:
            adj[b].append(a)
            x[a] += 1

        ans = []
        q = collections.deque()
        for i in range(numCourses):
            if x[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            ans.append(cur)
            for i in adj[cur]:
                x[i] -= 1
                if x[i] == 0:
                    if i in seen:
                        return []
                    else:
                        q.append(i)
                        seen.add(i)
        return ans if len(ans) == numCourses else []

