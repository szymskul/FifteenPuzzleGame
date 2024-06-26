import time
from collections import deque

import globalVariables
import moveFunctions

class State:
    def __init__(self, board, parent=None, last_move=None):
        self.board = board
        self.parent = parent
        self.last_move = last_move

def bfs_algorithm(start_board, target_board, order):
    start_time = time.time()
    queue = deque()
    start_state = State(start_board)
    queue.append(start_state)
    testedPositions = set()
    testedPositions.add(tuple(map(tuple, start_board)))
    while queue:
        globalVariables.zero_position = None
        current_state = queue.popleft()
        globalVariables.proceededPositions += 1
        current_board = current_state.board
        last_move = current_state.last_move
        if current_board == target_board:
            path = []
            while current_state.parent is not None:
                path.append(current_state.last_move)
                current_state = current_state.parent
            path.reverse()
            globalVariables.reached_depth = len(path)
            for i in range(len(path)):
                globalVariables.path += str(path[i])
            globalVariables.proceed = False
            end_time = time.time()
            globalVariables.spentTime = float((end_time - start_time) * 1000)
            return current_board
        zero = globalVariables.zero_position
        for move in order:
            new_board = [row[:] for row in current_board]
            if moveFunctions.checkMovePossibility(move, new_board) and moveFunctions.checkingOppositeMove(move, last_move):
                moveFunctions.moveFunction(move, new_board)
                globalVariables.testedPositions += 1
                if tuple(map(tuple, new_board)) not in testedPositions:
                    new_state = State(new_board, current_state, move)
                    queue.append(new_state)
                    testedPositions.add(tuple(map(tuple, new_board)))
                globalVariables.zero_position = zero