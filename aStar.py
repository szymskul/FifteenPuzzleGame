import time
from queue import PriorityQueue

import globalVariables
from moveFunctions import moveFunction
from moveFunctions import checkMovePossibility

def manhattan_distance_help_function(position, positivePosition):
    x = abs(position[0] - positivePosition[0])
    y = abs(position[1] - positivePosition[1])
    return abs(x) + abs(y)
def humming_metric(board, positiveBoard):
    humming = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] != 0):
                if(board[i][j] != positiveBoard[i][j]):
                    humming += 1
    return humming
def manhattan_distance(board, positiveBoard):
    polesDictionary = []
    position = []
    positivePosition = []
    suma = 0
    for i in range(0, 15):

        for j, row in enumerate(board):
            for k, number in enumerate(row):
                if number == i+1:
                    position.append((j, k))
        for j, positiveRow in enumerate(positiveBoard):
            for k, number in enumerate(positiveRow):
                if number == i+1:
                    positivePosition.append((j, k))
    print(position)
    print(positivePosition)
    for i in range(0, len(position)):
            distance = manhattan_distance_help_function(position[i], positivePosition[i])
            polesDictionary.append(distance)
    print(polesDictionary)
    for i in range(0, 15):
        suma += polesDictionary[i]
    return suma

def aStar(start_board, target_board, type):
    start_time = time.time()
    testedPositions = set()
    queueAstar = PriorityQueue()
    queueAstar.put((0, [start_board, "", 0]))
    max_depth = 0
    while not queueAstar.empty():
        current_board, path, moves_count = queueAstar.get()[1]
        globalVariables.proceededPositions += 1
        if current_board == target_board:
            globalVariables.path = path
            globalVariables.proceed = False
            end_time = time.time()
            globalVariables.spentTime = float((end_time - start_time) * 1000)
            return current_board
        testedPositions.add(tuple(map(tuple, current_board)))
        for move in "UDRL":
            if checkMovePossibility(move, current_board):
                globalVariables.testedPositions += 1
                temp_board = [row[:] for row in current_board]
                moveFunction(move, temp_board)
                if temp_board in tuple(map(tuple, testedPositions)):
                    continue
                moves_count_temp = moves_count + 1
                if type == "mnh":
                    cost = manhattan_distance(current_board, target_board) + moves_count_temp
                elif type == "hamm":
                    cost = humming_metric(current_board, target_board) + moves_count_temp
                else:
                    return False
                queueAstar.put((cost, [temp_board, path + move, moves_count_temp]))
                globalVariables.reached_depth = max(max_depth, len(path))
