from moveFunctions import checkMovePossibility
from moveFunctions import moveFunction

def dfs_algorithm(current_board, last_choose, current_depth, final_board, order):
    global reached_depth
    global proceed
    global path
    global all_path
    global depth
    if len(path) > reached_depth:
        reached_depth = len(path)
    if current_board == final_board:
        proceed = False
        print(path)
        print(current_board)
        print(all_path)
        return
    elif proceed:
        if current_depth >= depth:
            return
        for i in range(4):
            if order[i] == "R":
                all_path = all_path + "R"
                if proceed and last_choose != 'L' and checkMovePossibility("R", current_board): #Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                    moveFunction("R", current_board)
                    path = path + "R"
                    dfs_algorithm(current_board, "R", current_depth + 1, final_board)
                    if proceed:
                        path = path[:-1]
                    moveFunction("L", current_board)
            elif order[i] == "L":
                all_path = all_path + "L"
                if proceed and last_choose != 'R' and checkMovePossibility("L", current_board): #Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                    moveFunction("L", current_board)
                    path = path + "L"
                    dfs_algorithm(current_board, "L", current_depth + 1, final_board)
                    if proceed:
                        path = path[:-1]
                    moveFunction("R", current_board)
            elif order[i] == "D":
                all_path = all_path + "D"
                if proceed and last_choose != 'U' and checkMovePossibility("D", current_board): # Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                    moveFunction("D", current_board)
                    path = path + "D"
                    dfs_algorithm(current_board, "D", current_depth + 1, final_board)
                    if proceed:
                        path = path[:-1]
                    moveFunction("U", current_board)
            elif order[i] == "U":
                all_path = all_path + "U"
                if proceed and last_choose != 'D' and checkMovePossibility("U", current_board):  # Dodac trzeeba onecne polozenie zera aby sprawdzic czy mozna przesuwac bez problemu
                    moveFunction("U", current_board)
                    path = path + "U"
                    dfs_algorithm(current_board, "U", current_depth + 1, final_board)
                    if proceed:
                        path = path[:-1]
                    moveFunction("D", current_board)
