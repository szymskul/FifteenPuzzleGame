import os
import sys

def solveScript(algorithmType, order):
    directoryToSolve = "toSolve"
    directoryToSolved = "Solved"
    directoryToStats = "solvedStats"
    os.makedirs("Solved", exist_ok=True)
    os.makedirs("solvedStats", exist_ok=True)
    for fileName in os.listdir(directoryToSolve):
        input_filename = fileName
        index = fileName.find('.txt')
        output_filename = os.path.join(directoryToSolved,f'{fileName[:index]}_{algorithmType}_{order}_sol.txt')
        additional_output_filename = os.path.join(directoryToStats, f'{fileName[:index]}_{algorithmType}_{order}_stats.txt')
        sys.argv = [
            'mainFifteenPuzzleGame.py', algorithmType, order, input_filename, output_filename, additional_output_filename
        ]
        exec(open('mainFifteenPuzzleGame.py').read())

def solveDfs():
    search_orders = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for search_order in search_orders:
        solveScript("dfs", search_order)

def solveBfs():
    search_orders = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for search_order in search_orders:
        solveScript("bfs", search_order)

def aStar():
    search_heuristics = ['manh','hamm']
    for search_heuristic in search_heuristics:
        solveScript("dfs", search_heuristic)

if __name__ == '__main__':
    solveDfs()
    solveBfs()
    aStar()