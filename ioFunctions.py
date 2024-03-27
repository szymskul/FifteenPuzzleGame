import globalVariables

def readFile(fileName):
    with open(fileName, 'r') as file:
        for i, line in enumerate(file):
            row = line.strip().split(" ")
            if i == 0:
                globalVariables.sizeOfBoard.extend(map(int, row))
            else:
                globalVariables.dane.append(list(map(int,row)))
    iteration = 1
    for i in range(globalVariables.sizeOfBoard[0]):
        row = []
        for j in range(globalVariables.sizeOfBoard[1]):
            if i == globalVariables.sizeOfBoard[0] - 1 and j == globalVariables.sizeOfBoard[1] - 1:
                row.append(0)
            else:
                row.append(iteration)
                iteration += 1
        globalVariables.target_board.append(row)