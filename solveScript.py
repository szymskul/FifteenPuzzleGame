import os
import mainFifteenPuzzleGame
def solveScript(algorithmType, order):
    directoryToSolve = "toSolve1"
    directoryToSolved = "Solved"
    directoryToStats = "solvedStats"
    os.makedirs("Solved", exist_ok=True)
    os.makedirs("solvedStats", exist_ok=True)
    for fileName in os.listdir(directoryToSolve):
        index = fileName.find('.txt')
        input_filename = os.path.join(directoryToSolve, fileName)
        output_filename = os.path.join(directoryToSolved,f'{fileName[:index]}_{algorithmType}_{order}_sol.txt')
        additional_output_filename = os.path.join(directoryToStats, f'{fileName[:index]}_{algorithmType}_{order}_stats.txt')
        mainFifteenPuzzleGame.mainFunction(algorithmType, order, input_filename, output_filename, additional_output_filename)

def solveDfs():
    search_orders = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for search_order in search_orders:
        solveScript("dfs", search_order)

def solveBfs():
    search_orders = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for search_order in search_orders:
        solveScript("bfs", search_order)

def aStar():
    search_heuristics = ['mnh','hamm']
    for search_heuristic in search_heuristics:
        solveScript("astr", search_heuristic)

if __name__ == '__main__':
    solveDfs()