import ioFunctions
import globalVariables
from bfs_algorithm import bfs_algorithm
from dfs_algorithm import dfs_algorithm
from aStar import aStar

def resetAllValues():
    globalVariables.sizeOfBoard = []
    globalVariables.dane = []
    globalVariables.target_board = []
    globalVariables.path = ""
    globalVariables.reached_depth = 0
    globalVariables.depth = 20
    globalVariables.proceed = True
    globalVariables.queue = []
    globalVariables.order = ""
    globalVariables.proceededPositions = 0
    globalVariables.testedPositions = 0
    globalVariables.spentTime = 0.0

def mainFunction(algorithmType, order, fileToRead, fileToWriteSolution, fileToWriteDetailsOfSolution):
    resetAllValues()
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
