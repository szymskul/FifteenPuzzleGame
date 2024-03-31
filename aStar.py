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

    for i in range(0, len(position)):
            print(i)
            distance = manhattan_distance_help_function(position[i], positivePosition[i])
            polesDictionary.append(distance)
    print(polesDictionary)
    for i in range(0, 15):
        suma += polesDictionary[i]
    return suma


def aStar(start_board, target_board, type):
    positionValue = []
    amountOfMoves = 0
    testedPositions = set()
    current_board = start_board
    while current_board != target_board:
        if tuple(map(tuple, current_board)) not in testedPositions:
            testedPositions.add(tuple(map(tuple, current_board)))
        if(type == "mnh"):
            for move in "UDRL":
                if(checkMovePossibility(move, current_board)):
                    temp_board = [row[:] for row in current_board]
                    score = manhattan_distance(moveFunction(move, temp_board), target_board)
                    globalVariables.all_path += move
                    positionValue.append((score + amountOfMoves, move))
        else:
            for move in "UDRL":
                if (checkMovePossibility(move, current_board)):
                    temp_board = [row[:] for row in current_board]
                    score = humming_metric(moveFunction(move, temp_board), target_board)
                    globalVariables.all_path += move
                    positionValue.append((score + amountOfMoves, move))
        min_positionValue = min(positionValue)
        amountOfMoves += 1
        current_board = moveFunction(min_positionValue[1],current_board)
        globalVariables.path += min_positionValue[1]
        positionValue.clear()
    globalVariables.testedPositions = len(testedPositions)
    globalVariables.proceededPositions = len(globalVariables.all_path)
    globalVariables.reached_depth = len(globalVariables.path)
    return current_board