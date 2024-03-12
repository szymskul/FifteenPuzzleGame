sizeOfBoard = []
dane = []
path = "X"
reached_depth = 0
depth = 2
proceed = True
queue = []
all_path = "X"

def readFile(fileName):
    with open(fileName, 'r') as file:
        for i, line in enumerate(file):
            row = line.strip().split(" ")
            if i == 0:
                sizeOfBoard.append(list(map(int, row)))
            else:
                dane.append(list(map(int,row)))


#def mainFunction(algorithmType, order, fileToRead, fileToWrite, fileToWriteStats):

#dfs_algorithm(dane, 'N', 0, positiveDane, "LRUD")
#bfs_algorithm(dane, positiveDane)
#manhattan_distance(dane, positiveDane)
#aStar(dane, "hamm")
