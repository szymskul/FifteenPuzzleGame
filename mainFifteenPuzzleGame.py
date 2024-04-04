import time
import sys
import ioFunctions
import globalVariables
from bfs_algorithm import bfs_algorithm
from dfs_algorithm import dfs_algorithm
from aStar import aStar
'''
def mainFunction(algorithmType, order, fileToRead, fileToWriteSolution, fileToWriteDetailsOfSolution):
    ioFunctions.readFile(fileToRead)
    if(algorithmType == "bfs"):
        start_time = time.time()
        bfs_algorithm(globalVariables.dane ,globalVariables.target_board ,order)
        end_time = time.time()
    elif(algorithmType == "dfs"):
        globalVariables.order = order
        start_time = time.time()
        dfs_algorithm(globalVariables.dane, "X", 1, globalVariables.target_board)
        end_time = time.time()
    else:
        start_time = time.time()
        aStar(globalVariables.dane, globalVariables.target_board, order)
        end_time = time.time()
    globalVariables.spentTime = float((end_time - start_time) * 1000)
    ioFunctions.writeSolutionFile(fileToWriteSolution)
    ioFunctions.writeDetailsOfSolutionFile(fileToWriteDetailsOfSolution)

mainFunction("bfs", "DRUL", "data.txt" , "solution.txt", "detailsOfSolution.txt")'''


def mainFunction(algorithmType, order, fileToRead, fileToWriteSolution, fileToWriteDetailsOfSolution):
    ioFunctions.readFile(fileToRead)

    start_time = time.time()
    if algorithmType == "bfs":
        bfs_algorithm(globalVariables.dane, globalVariables.target_board, order)
    elif algorithmType == "dfs":
        globalVariables.order = order
        dfs_algorithm(globalVariables.dane, "X", 1, globalVariables.target_board)
    elif algorithmType == "astr":
        aStar(globalVariables.dane, globalVariables.target_board, order)
    end_time = time.time()

    globalVariables.spentTime = float((end_time - start_time) * 1000)

    ioFunctions.writeSolutionFile(fileToWriteSolution)
    ioFunctions.writeDetailsOfSolutionFile(fileToWriteDetailsOfSolution)


if __name__ == "__main__":
    algorithmType = sys.argv[1]
    order = sys.argv[2]
    fileToRead = sys.argv[3]
    fileToWriteSolution = sys.argv[4]
    fileToWriteDetailsOfSolution = sys.argv[5]

    mainFunction(algorithmType, order, fileToRead, fileToWriteSolution, fileToWriteDetailsOfSolution)