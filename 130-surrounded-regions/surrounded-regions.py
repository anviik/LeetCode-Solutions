class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "O":
                        board[nr][nc] = "!"
                        q.append((nr,nc))

        for r in range(len(board)):
            if board[r][0] == "O":
                board[r][0] ="!"
                bfs(r,0)
        for r in range(len(board)):
            if board[r][len(board[0])-1] == "O":
                board[r][len(board[0])-1] ="!"
                bfs(r,len(board[0])-1)
        for c in range(len(board[0])):
            if board[0][c] == "O":
                board[0][c] ="!"
                bfs(0,c)
        for c in range(len(board[0])):
            if board[len(board)-1][c] == "O":
                board[len(board)-1][c] ="!"
                bfs(len(board)-1,c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c] == "O"):
                    board[r][c] = "X"

                if (board[r][c] == "!"):
                    board[r][c] = "O"
       