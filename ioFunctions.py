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

def writeSolutionFile(fileName):
    with open(fileName, 'w') as file:
        if(globalVariables.path == "XX"):
            file.write("-1")
        else:
            file.write(str(len(globalVariables.path)))
            file.write('\n')
            file.write(globalVariables.path)

def writeDetailsOfSolutionFile(fileName):
    with open(fileName, 'w') as file:
        file.write(str(len(globalVariables.path)))
        file.write('\n')
        file.write(str(globalVariables.testedPositions))
        file.write('\n')
        file.write(str(globalVariables.proceededPositions))
        file.write('\n')
        file.write(str(globalVariables.reached_depth))
        file.write('\n')
        file.write(str(globalVariables.spentTime))