from collections import deque
import moveFunctions

def bfs_algorithm(start_board, target_board):
    queue = deque()
    queue.append(start_board)
    testedPositions = set()
    testedPositions.add(tuple(map(tuple, start_board)))
    while queue:
        current_board = queue.popleft()
        if moveFunctions.checkingBoard(current_board, target_board):
            return current_board

        for move in ["R", "D", "U", "L"]:
            new_board = [row[:] for row in current_board]
            if(moveFunctions.checkMovePossibility(move, new_board)):
                moveFunctions.moveFunction(move, new_board)
            if tuple(map(tuple, new_board)) not in testedPositions:
                queue.append(new_board)
                testedPositions.add(tuple(map(tuple, new_board)))