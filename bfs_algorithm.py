from collections import deque

import globalVariables
import moveFunctions

def bfs_algorithm(start_board, target_board, order):
    queue = deque()
    queue.append(start_board)
    testedPositions = set()
    testedPositions.add(tuple(map(tuple, start_board)))
    while queue:
        current_board = queue.popleft()
        if moveFunctions.checkingBoard(current_board, target_board):
            globalVariables.testedPositions = len(testedPositions)
            globalVariables.proceededPositions = len(globalVariables.all_path) + 1
            return current_board
        for move in order:
            new_board = [row[:] for row in current_board]
            globalVariables.all_path = globalVariables.all_path + move
            if(moveFunctions.checkMovePossibility(move, new_board)):
                moveFunctions.moveFunction(move, new_board)
                globalVariables.path = globalVariables.path + move
            if tuple(map(tuple, new_board)) not in testedPositions:
                queue.append(new_board)
                testedPositions.add(tuple(map(tuple, new_board)))