import time
from queue import PriorityQueue

import globalVariables
from moveFunctions import moveFunction
from moveFunctions import checkMovePossibility

def manhattan_distance_help_function(position, positivePosition):
    x = position[0] - positivePosition[0]
    y = position[1] - positivePosition[1]
    return abs(x) + abs(y)
def humming_metric(board, positiveBoard):
    humming = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] != 0):
                if(board[i][j] != positiveBoard[i][j]):
                    humming += 1
    return humming
def manhattan_distance(board, positivePosition):
    suma = 0
    for j, row in enumerate(board):
        for k, number in enumerate(row):
            distance = 0
            if(board[j][k] != 0):
                distance = manhattan_distance_help_function((j,k), positivePosition[int(board[j][k]) - 1])
            suma += distance
    return suma

def aStar(start_board, target_board, type):
    start_time = time.time()
    positivePosition = []
    for i in range(1, 16):
        row = (i - 1) // 4
        col = (i - 1) % 4
        positivePosition.append((row, col))
    testedPositions = set()
    queueAstar = PriorityQueue()
    queueAstar.put((0, [start_board, "", 0]))
    max_depth = 0
    while not queueAstar.empty():
        current_board, path, moves_count = queueAstar.get()[1]
        globalVariables.zero_position = None
        globalVariables.proceededPositions += 1
        if current_board == target_board:
            globalVariables.path = path
            globalVariables.proceed = False
            end_time = time.time()
            globalVariables.spentTime = float((end_time - start_time) * 1000)
            return current_board
        testedPositions.add(tuple(map(tuple, current_board)))
        zero = globalVariables.zero_position
        for move in "UDRL":
            globalVariables.zero_position = zero
            if checkMovePossibility(move, current_board):
                globalVariables.testedPositions += 1
                temp_board = [row[:] for row in current_board]
                moveFunction(move, temp_board)
                if temp_board in tuple(map(tuple, testedPositions)):
                    continue
                moves_count_temp = moves_count + 1
                if type == "mnh":
                    cost = manhattan_distance(current_board, positivePosition) + moves_count_temp
                elif type == "hamm":
                    cost = humming_metric(current_board, target_board) + moves_count_temp
                else:
                    return False
                queueAstar.put((cost, [temp_board, path + move, moves_count_temp]))
                globalVariables.reached_depth = max(max_depth, len(path))
