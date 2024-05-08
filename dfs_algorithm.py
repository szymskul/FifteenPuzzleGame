import time

from moveFunctions import checkMovePossibility
from moveFunctions import moveFunction
from moveFunctions import checkingOppositeMove
from moveFunctions import returningOppositeMove

import globalVariables
def dfs(current_board, last_choose, current_depth, final_board, testedPositions):
     globalVariables.proceededPositions += 1
     if current_depth > globalVariables.max_depth:
         return None
     if(current_depth > globalVariables.reached_depth):
         globalVariables.reached_depth = current_depth
     if tuple(map(tuple, current_board)) not in testedPositions:
        testedPositions.add(tuple(map(tuple, current_board)))
     if current_board == final_board:
         globalVariables.proceed = False
         return current_board
     elif globalVariables.proceed:
         for move in globalVariables.order:
                 if checkMovePossibility(move, current_board):
                    globalVariables.testedPositions += 1
                    if globalVariables.proceed and checkingOppositeMove(move, last_choose):
                        moveFunction(move, current_board)
                        globalVariables.path = globalVariables.path + move
                        dfs(current_board, move, current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction(returningOppositeMove(move), current_board)

def dfs_algorithm(current_board, last_choose, current_depth, final_board):
    start_time = time.time()
    testedPositions = set()
    dfs(current_board, last_choose, current_depth, final_board, testedPositions)
    end_time = time.time()
    globalVariables.spentTime = float((end_time - start_time) * 1000)

