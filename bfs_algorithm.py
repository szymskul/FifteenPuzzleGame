from collections import deque

import globalVariables
import moveFunctions

class State:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move

def bfs_algorithm(start_board, target_board, order):
    queue = deque()
    start_state = State(start_board)
    queue.append(start_state)
    testedPositions = set()
    testedPositions.add(tuple(map(tuple, start_board)))
    while queue:
        current_state = queue.popleft()
        current_board = current_state.board
        if moveFunctions.checkingBoard(current_board, target_board):
            path = []
            while current_state.parent is not None:
                path.append(current_state.move)
                current_state = current_state.parent
            path.reverse()
            globalVariables.testedPositions = len(testedPositions)
            globalVariables.proceededPositions = len(globalVariables.all_path) + 1
            globalVariables.reached_depth = len(path)
            for i in range(len(path)):
                globalVariables.path += str(path[i])
            return current_board
        for move in order:
            new_board = [row[:] for row in current_board]
            if moveFunctions.checkMovePossibility(move, new_board):
                moveFunctions.moveFunction(move, new_board)
                globalVariables.all_path = globalVariables.all_path + move
                if tuple(map(tuple, new_board)) not in testedPositions:
                    new_state = State(new_board, current_state, move)
                    queue.append(new_state)
                    testedPositions.add(tuple(map(tuple, new_board)))