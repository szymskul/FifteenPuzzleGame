import globalVariables

def readFile(fileName):
    with open(fileName, 'r') as file:
        for i, line in enumerate(file):
            row = line.strip().split(" ")
            if i == 0:
                globalVariables.sizeOfBoard.append(list(map(int, row)))
            else:
                globalVariables.dane.append(list(map(int,row)))