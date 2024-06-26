import ioFunctions
import globalVariables
import moveFunctions
from bfs_algorithm import bfs_algorithm
from dfs_algorithm import dfs_algorithm
from aStar import aStar
import sys

def mainFunction(algorithmType, order, fileToRead, fileToWriteSolution, fileToWriteDetailsOfSolution):
    ioFunctions.readFile(fileToRead)
    if algorithmType == "bfs":
        bfs_algorithm(globalVariables.dane, globalVariables.target_board, order)
    elif algorithmType == "dfs":
        globalVariables.order = order
        dfs_algorithm(globalVariables.dane, "X", 1, globalVariables.target_board)
    elif algorithmType == "astr":
        aStar(globalVariables.dane, globalVariables.target_board, order)
    if globalVariables.proceed == True:
        globalVariables.path = "XX"

    ioFunctions.writeSolutionFile(fileToWriteSolution)
    ioFunctions.writeDetailsOfSolutionFile(fileToWriteDetailsOfSolution)

if __name__ == "__main__":
    algorithmType = sys.argv[1]
    order = sys.argv[2]
    fileToRead = sys.argv[3]
    fileToWriteSolution = sys.argv[4]
    fileToWriteDetailsOfSolution = sys.argv[5]
    mainFunction(algorithmType,order,fileToRead,fileToWriteSolution,fileToWriteDetailsOfSolution)