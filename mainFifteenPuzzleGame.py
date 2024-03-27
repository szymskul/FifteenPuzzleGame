from ioFunctions import readFile
import globalVariables
from bfs_algorithm import bfs_algorithm
from dfs_algorithm import dfs_algorithm
from aStar import aStar

def mainFunction(algorithmType, order, fileToRead, fileToWrite, fileToWriteStats):
    readFile(fileToRead)
    if(algorithmType == "bfs"):
        bfs_algorithm(globalVariables.dane ,globalVariables.target_board ,order)
    elif(algorithmType == "dfs"):
        globalVariables.order = order
        print(globalVariables.order)
        string = dfs_algorithm(globalVariables.dane, "X", 0, globalVariables.target_board)
        print(string)
    else:
        aStar(globalVariables.dane, globalVariables.target_board, order)

mainFunction("dfs", "DURL", "data.txt" , "data.txt", "data.txt")