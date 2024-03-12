from moveFunctions import moveFunction
def humming_metric(board, positiveBoard):
    humming = 0
    for i in range(4):
        for j in range(4):
            if(board[i][j] != 0):
                if(board[i][j] != positiveBoard[i][j]):
                    humming += 1
    return humming
def manhattan_distance(board, positiveBoard):
    polesDictionary = []
    suma = 0
    for i in range(0, 15):
        position = []
        positivePosition = []

        for j, row in enumerate(board):
            for k, number in enumerate(row):
                if number == i+1:
                    position.append((j, k))
        for j, positiveRow in enumerate(positiveBoard):
            for k, number in enumerate(positiveRow):
                if number == i+1:
                    positivePosition.append((j, k))

        for position1 in position:
            for position2 in positivePosition:
                distance = abs((position1[0] - position2[0]) + (position1[1] - position2[1]))
                polesDictionary.append(distance)
    for i in range(0, 15):
        suma += polesDictionary[i]
    return suma


def aStar(start_board, target_board, type):
    amountOfMoves = 0
    testedPositions = set()
    current_board = start_board
    while current_board != target_board: # tu bedzie petla ale usuwam ja na czas testow
        testedPositions.add(tuple(map(tuple, start_board)))
        if(type == "mnh"):
            leftPosition = manhattan_distance(moveFunction("L", current_board), target_board)
            rightPosition = manhattan_distance(moveFunction("R", current_board), target_board)
            downPosition = manhattan_distance(moveFunction("D", current_board), target_board)
            upPosition = manhattan_distance(moveFunction("U", current_board), target_board)
        else:
            leftPosition = humming_metric(moveFunction("L", current_board), target_board)
            rightPosition = humming_metric(moveFunction("R", current_board), target_board)
            downPosition = humming_metric(moveFunction("D", current_board), target_board)
            upPosition = humming_metric(moveFunction("U", current_board), target_board)

        positionValue = [(leftPosition + amountOfMoves,"L"),(rightPosition + amountOfMoves, "R"),(downPosition + amountOfMoves, "D"),(upPosition + amountOfMoves, "U")]
        min_positionValue = min(positionValue)
        print(current_board)
        moveFunction(min_positionValue[1],current_board)
    return
