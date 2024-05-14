import globalVariables
def checkMovePossibility(move, board):
    if globalVariables.zero_position is None:
        for i, row in enumerate(board):
            for j, number in enumerate(row):
                if number == 0:
                    globalVariables.zero_position = [i,j]
    if (move == "L"):
        if (globalVariables.zero_position[1] != 0):
            return True
    if (move == "R"):
        if (globalVariables.zero_position[1] != 3):
            return True
    if (move == "U"):
        if (globalVariables.zero_position[0] != 0):
            return True
    if (move == "D"):
        if (globalVariables.zero_position[0] != 3):
            return True
    return False

def moveFunction(move, board):
        if(move == "L"):
                change = board[globalVariables.zero_position[0]][globalVariables.zero_position[1]-1]
                board[globalVariables.zero_position[0]][globalVariables.zero_position[1]-1] = board[globalVariables.zero_position[0]][globalVariables.zero_position[1]]
                board[globalVariables.zero_position[0]][globalVariables.zero_position[1]] = change
                globalVariables.zero_position[1] -= 1
        if(move == "R"):
                change = board[globalVariables.zero_position[0]][globalVariables.zero_position[1] + 1]
                board[globalVariables.zero_position[0]][globalVariables.zero_position[1] + 1] = board[globalVariables.zero_position[0]][globalVariables.zero_position[1]]
                board[globalVariables.zero_position[0]][globalVariables.zero_position[1]] = change
                globalVariables.zero_position[1] += 1
        if(move == "U"):
                change = board[globalVariables.zero_position[0] - 1][globalVariables.zero_position[1]]
                board[globalVariables.zero_position[0] - 1][globalVariables.zero_position[1]] = board[globalVariables.zero_position[0]][globalVariables.zero_position[1]]
                board[globalVariables.zero_position[0]][globalVariables.zero_position[1]] = change
                globalVariables.zero_position[0] -= 1
        if(move == "D"):
                change = board[globalVariables.zero_position[0] + 1][globalVariables.zero_position[1]]
                board[globalVariables.zero_position[0] + 1][globalVariables.zero_position[1]] = board[globalVariables.zero_position[0]][globalVariables.zero_position[1]]
                board[globalVariables.zero_position[0]][globalVariables.zero_position[1]] = change
                globalVariables.zero_position[0] += 1
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


