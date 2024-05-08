def checkMovePossibility(move, board):
    zero_positions = []
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number == 0:
                zero_positions.append((i, j))
    for position in zero_positions:
        if (move == "L"):
            if (position[1] != 0):
                return True
        if (move == "R"):
            if (position[1] != 3):
                return True
        if (move == "U"):
            if (position[0] != 0):
                return True
        if (move == "D"):
            if (position[0] != 3):
                return True
    return False

def moveFunction(move, board):
    zero_positions = []
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number == 0:
                zero_positions.append((i, j))
    for position in zero_positions:
        if(move == "L"):
                change = board[position[0]][position[1]-1]
                board[position[0]][position[1]-1] = board[position[0]][position[1]]
                board[position[0]][position[1]] = change
        if(move == "R"):
                change = board[position[0]][position[1] + 1]
                board[position[0]][position[1] + 1] = board[position[0]][position[1]]
                board[position[0]][position[1]] = change
        if(move == "U"):
                change = board[position[0] - 1][position[1]]
                board[position[0] - 1][position[1]] = board[position[0]][position[1]]
                board[position[0]][position[1]] = change
        if(move == "D"):
                change = board[position[0] + 1][position[1]]
                board[position[0] + 1][position[1]] = board[position[0]][position[1]]
                board[position[0]][position[1]] = change
    return board


def checkingOppositeMove(move, last_move):
    if move == "R" and last_move != "L":
        return True
    if move == "L" and last_move != "R":
        return True
    if move == "U" and last_move != "D":
        return True
    if move == "D" and last_move != "U":
        return True
    return False

def returningOppositeMove(move):
    if move == "R":
        return "L"
    if move == "L":
        return "R"
    if move == "D":
        return "U"
    if move == "U":
        return "D"


