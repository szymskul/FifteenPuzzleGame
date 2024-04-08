from moveFunctions import checkMovePossibility
from moveFunctions import moveFunction
import globalVariables
def dfs(current_board, last_choose, current_depth, final_board, testedPositions):
     if len(globalVariables.path) > globalVariables.reached_depth:
         globalVariables.reached_depth = len(globalVariables.path)
     if tuple(map(tuple, current_board)) not in testedPositions:
        testedPositions.add(tuple(map(tuple, current_board)))
     if(current_depth > globalVariables.reached_depth):
         globalVariables.reached_depth = current_depth
     if current_board == final_board:
         globalVariables.proceed = False
         globalVariables.proceededPositions = len(testedPositions)
         globalVariables.testedPositions = len(globalVariables.all_path) + 1
         return current_board
     elif globalVariables.proceed:
         if current_depth >= globalVariables.depth:
             return
         for i in range(4):
             if globalVariables.order[i] == "R":
                 if checkMovePossibility("R", current_board):
                    globalVariables.all_path = globalVariables.all_path + "R"
                    if globalVariables.proceed and last_choose != 'L': #Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                        moveFunction("R", current_board)
                        globalVariables.path = globalVariables.path + "R"
                        dfs(current_board, "R", current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction("L", current_board)
             elif globalVariables.order[i] == "L":
                 if checkMovePossibility("L", current_board):
                    globalVariables.all_path = globalVariables.all_path + "L"
                    if globalVariables.proceed and last_choose != 'R': #Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                        moveFunction("L", current_board)
                        globalVariables.path = globalVariables.path + "L"
                        dfs(current_board, "L", current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction("R", current_board)
             elif globalVariables.order[i] == "D":
                 if checkMovePossibility("D", current_board):
                    globalVariables.all_path = globalVariables.all_path + "D"
                    if globalVariables.proceed and last_choose != 'U': # Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                        moveFunction("D", current_board)
                        globalVariables.path = globalVariables.path + "D"
                        dfs(current_board, "D", current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction("U", current_board)
             elif globalVariables.order[i] == "U":
                 if checkMovePossibility("U", current_board):
                    globalVariables.all_path = globalVariables.all_path + "U"
                    if globalVariables.proceed and last_choose != 'D':  # Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                        moveFunction("U", current_board)
                        globalVariables.path = globalVariables.path + "U"
                        dfs(current_board, "U", current_depth + 1, final_board, testedPositions)
                        if globalVariables.proceed:
                            globalVariables.path = globalVariables.path[:-1]
                        moveFunction("D", current_board)

def dfs_algorithm(current_board, last_choose, current_depth, final_board):
    testedPositions = set()
    dfs(current_board, last_choose, current_depth, final_board, testedPositions)
    testedPositions.clear()

