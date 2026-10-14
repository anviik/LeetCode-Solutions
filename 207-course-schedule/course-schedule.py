class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = collections.defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        process = 0
        while q:
            cur = q.popleft()
            process += 1
            for j in adj[cur]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
        return process == numCourses