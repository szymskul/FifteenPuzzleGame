from collections import deque

dane = []
positiveDane = []

with open('data.txt', 'r') as file:
    for line in file:
        row = line.strip().split(' ')
        dane.append(list(map(int, row)))

with open('wzorzec.txt', 'r') as file:
    for line in file:
        positiveRow = line.strip().split(' ')
        positiveDane.append(list(map(int, positiveRow)))
def moveFunction(move, board):
    zero_positions = []
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number == 0:
                zero_positions.append((i, j))
    for position in zero_positions:
        if(move == "L"):
            if(position[1] != 0):
                change = board[position[0]][position[1]-1]
                board[position[0]][position[1]-1] = board[position[0]][position[1]]
                board[position[0]][position[1]] = change
        if(move == "R"):
            if(position[1] != 3):
                change = board[position[0]][position[1] + 1]
                board[position[0]][position[1] + 1] = board[position[0]][position[1]]
                board[position[0]][position[1]] = change
        if(move == "U"):
            if(position[0] != 0):
                change = board[position[0] - 1][position[1]]
                board[position[0] - 1][position[1]] = board[position[0]][position[1]]
                board[position[0]][position[1]] = change
        if(move == "D"):
            if(position[0] != 3):
                change = board[position[0] + 1][position[1]]
                board[position[0] + 1][position[1]] = board[position[0]][position[1]]
                board[position[0]][position[1]] = change
    zero_positions.clear()
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number == 0:
                zero_positions.append((i, j))

def checkingBoard(board, positiveBoard):
    for i in range(4):
        for j in range(4):
            if(board[i][j] != positiveBoard[i][j]):
                return False
    return True

def manhattan_distance(board, positiveBoard):
    polesDictionary = []
    for i in range(0, 16):
        position = []
        positivePosition = []

        for j, row in enumerate(board):
            for k, number in enumerate(row):
                if number == i:
                    position.append((j, k))
        for j, positiveRow in enumerate(positiveBoard):
            for k, number in enumerate(positiveRow):
                if number == i:
                    positivePosition.append((j, k))

        for position1 in position:
            for position2 in positivePosition:
                distance = abs((position1[0] - position2[0]) + (position1[1] - position2[1]))
                polesDictionary.append(distance)

    return polesDictionary

def bfs_algorithm(start_board, target_board):
    queue = deque()
    queue.append(start_board)
    testedPositions = set()
    testedPositions.add(tuple(map(tuple, start_board)))
    for i in range(30):
        current_board = queue.popleft()
        if checkingBoard(current_board, target_board):
            return current_board

        for move in ["L", "R", "U", "D"]:
            new_board = [row[:] for row in current_board]
            moveFunction(move, new_board)
            if tuple(map(tuple, new_board)) not in testedPositions:
                queue.append(new_board)
                testedPositions.add(tuple(map(tuple, new_board)))
                print(new_board)

bfs_algorithm(dane, positiveDane)