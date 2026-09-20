"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        copy = {}
        def dfs(node):
            if node not in copy:
                newnode = Node(node.val)
                copy[node] = newnode
            else:
                return copy[node]

            for n in node.neighbors:
                newnode.neighbors.append(dfs(n))
            return newnode
        return dfs(node)

        