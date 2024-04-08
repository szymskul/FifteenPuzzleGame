import time

from moveFunctions import checkMovePossibility
from moveFunctions import moveFunction
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
         for i in range(4):
             if globalVariables.order[i] == "R":
                 if checkMovePossibility("R", current_board):
                    globalVariables.testedPositions += 1
                    if globalVariables.proceed and last_choose != 'L':
                        moveFunction("R", current_board)
                        globalVariables.path = globalVariables.path + "R"
                        dfs(current_board, "R", current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction("L", current_board)
             elif globalVariables.order[i] == "L":
                 if checkMovePossibility("L", current_board):
                    globalVariables.testedPositions += 1
                    if globalVariables.proceed and last_choose != 'R':
                        moveFunction("L", current_board)
                        globalVariables.path = globalVariables.path + "L"
                        dfs(current_board, "L", current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction("R", current_board)
             elif globalVariables.order[i] == "D":
                 if checkMovePossibility("D", current_board):
                    globalVariables.testedPositions += 1
                    if globalVariables.proceed and last_choose != 'U':
                        moveFunction("D", current_board)
                        globalVariables.path = globalVariables.path + "D"
                        dfs(current_board, "D", current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction("U", current_board)
             elif globalVariables.order[i] == "U":
                 if checkMovePossibility("U", current_board):
                    globalVariables.testedPositions += 1
                    if globalVariables.proceed and last_choose != 'D':
                        moveFunction("U", current_board)
                        globalVariables.path = globalVariables.path + "U"
                        dfs(current_board, "U", current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction("D", current_board)

def dfs_algorithm(current_board, last_choose, current_depth, final_board):
    start_time = time.time()
    testedPositions = set()
    dfs(current_board, last_choose, current_depth, final_board, testedPositions)
    testedPositions.clear()
    end_time = time.time()
    globalVariables.spentTime = float((end_time - start_time) * 1000)

