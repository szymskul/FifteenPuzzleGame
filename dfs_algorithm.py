from moveFunctions import checkMovePossibility
from moveFunctions import moveFunction
import globalVariables

def dfs_algorithm(current_board, last_choose, current_depth, final_board, order):

    if len(globalVariables.path) > globalVariables.reached_depth:
        reached_depth = len(globalVariables.path)
    if current_board == final_board:
        proceed = False
        print(globalVariables.path)
        print(current_board)
        print(globalVariables.all_path)
        return
    elif globalVariables.proceed:
        if current_depth >= globalVariables.depth:
            return
        for i in range(4):
            if order[i] == "R":
                all_path = globalVariables.all_path + "R"
                if globalVariables.proceed and last_choose != 'L' and checkMovePossibility("R", current_board): #Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                    moveFunction("R", current_board)
                    path = globalVariables.path + "R"
                    dfs_algorithm(current_board, "R", current_depth + 1, final_board)
                    if globalVariables.proceed:
                        path = path[:-1]
                    moveFunction("L", current_board)
            elif order[i] == "L":
                all_path = globalVariables.all_path + "L"
                if globalVariables.proceed and last_choose != 'R' and checkMovePossibility("L", current_board): #Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                    moveFunction("L", current_board)
                    path = globalVariables.path + "L"
                    dfs_algorithm(current_board, "L", current_depth + 1, final_board)
                    if globalVariables.proceed:
                        path = path[:-1]
                    moveFunction("R", current_board)
            elif order[i] == "D":
                all_path = globalVariables.all_path + "D"
                if globalVariables.proceed and last_choose != 'U' and checkMovePossibility("D", current_board): # Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                    moveFunction("D", current_board)
                    path = globalVariables.path + "D"
                    dfs_algorithm(current_board, "D", current_depth + 1, final_board)
                    if globalVariables.proceed:
                        path = path[:-1]
                    moveFunction("U", current_board)
            elif order[i] == "U":
                all_path = globalVariables.all_path + "U"
                if globalVariables.proceed and last_choose != 'D' and checkMovePossibility("U", current_board):  # Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                    moveFunction("U", current_board)
                    path = globalVariables.path + "U"
                    dfs_algorithm(current_board, "U", current_depth + 1, final_board)
                    if globalVariables.proceed:
                        path = path[:-1]
                    moveFunction("D", current_board)
