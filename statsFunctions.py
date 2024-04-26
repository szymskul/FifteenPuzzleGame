import matplotlib.pyplot as plt
import os
import matplotlib.ticker as ticker


import numpy as np
def createPlotOfStatsOverall(numberOfLineToAdd):
    numberOfCountsDfs = [0,0,0,0,0,0,0]
    numberOfCountsAstar = [0, 0, 0, 0, 0, 0, 0]
    numberOfCountsBfs = [0,0,0,0,0,0,0]
    countDfs = [0,0,0,0,0,0,0]
    countBfs = [0,0,0,0,0,0,0]
    countAstar = [0, 0, 0, 0, 0, 0, 0]
    directoryToStats = "solvedStats"
    for fileName in os.listdir(directoryToStats):
        filePath = os.path.join(directoryToStats, fileName)
        with open(filePath, 'r') as file:
            lines = file.readlines()
            parts = fileName.split('_')
            if numberOfLineToAdd <= len(lines):
                if(parts[3] == "astr"):
                    countAstar[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsAstar[int(parts[1]) - 1] += 1
                elif(parts[3] == "bfs"):
                    countBfs[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsBfs[int(parts[1]) - 1] += 1
                elif(parts[3] == "Dfs"):
                    countDfs[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsDfs[int(parts[1]) - 1] += 1
            else:
                return "Podana linia nie istnieje w pliku."
    for i in range(len(countDfs)):
        zmienna = countDfs[i]
        dzielnik = numberOfCountsDfs[i]
        if(dzielnik != 0):
            countDfs[i] = zmienna / dzielnik
        zmienna1 = countBfs[i]
        dzielnik1 = numberOfCountsBfs[i]
        if(dzielnik1 != 0):
            countBfs[i] = zmienna1 / dzielnik1
        zmienna2 = countAstar[i]
        dzielnik2 = numberOfCountsAstar[i]
        if(dzielnik2 != 0):
            countAstar[i] = zmienna2 / dzielnik2
    print(countBfs)
    print(countAstar)
    return countBfs, countDfs, countAstar
def createPlotOfStatsAstar(numberOfLineToAdd):
    numberOfCountsHamm = [0,0,0,0,0,0,0]
    numberOfCountsManh = [0,0,0,0,0,0,0]
    countHamm = [0,0,0,0,0,0,0]
    countManh = [0,0,0,0,0,0,0]
    directoryToStats = "solvedStats"
    for fileName in os.listdir(directoryToStats):
        filePath = os.path.join(directoryToStats, fileName)
        with open(filePath, 'r') as file:
            lines = file.readlines()
            parts = fileName.split('_')
            if numberOfLineToAdd <= len(lines):
                if(parts[4] == "hamm"):
                    countHamm[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsHamm[int(parts[1]) - 1] += 1
                elif(parts[4] == "mnh"):
                    countManh[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsManh[int(parts[1]) - 1] += 1
            else:
                return "Podana linia nie istnieje w pliku."
    for i in range(len(countHamm)):
        zmienna = countHamm[i]
        dzielnik = numberOfCountsHamm[i]
        if(dzielnik != 0):
            countHamm[i] = zmienna / dzielnik
        zmienna = countManh[i]
        dzielnik = numberOfCountsManh[i]
        if(dzielnik != 0):
            countManh[i] = zmienna / dzielnik
    print(countManh)
    print(countHamm)
    return countManh, countHamm

def createPlotOfStatsBfsDfs(numberOfLineToAdd):
    numberOfCountsRDUL = [0,0,0,0,0,0,0]
    numberOfCountsRDLU = [0,0,0,0,0,0,0]
    numberOfCountsDRUL = [0,0,0,0,0,0,0]
    numberOfCountsDRLU = [0,0,0,0,0,0,0]
    numberOfCountsLUDR = [0,0,0,0,0,0,0]
    numberOfCountsLURD = [0,0,0,0,0,0,0]
    numberOfCountsULDR = [0,0,0,0,0,0,0]
    numberOfCountsULRD = [0,0,0,0,0,0,0]
    countRDUL = [0,0,0,0,0,0,0]
    countRDLU = [0,0,0,0,0,0,0]
    countDRUL = [0,0,0,0,0,0,0]
    countDRLU = [0,0,0,0,0,0,0]
    countLUDR = [0,0,0,0,0,0,0]
    countLURD = [0,0,0,0,0,0,0]
    countULDR = [0,0,0,0,0,0,0]
    countULRD = [0,0,0,0,0,0,0]
    directoryToStats = "solvedStats"
    for fileName in os.listdir(directoryToStats):
        filePath = os.path.join(directoryToStats, fileName)
        with open(filePath, 'r') as file:
            lines = file.readlines()
            parts = fileName.split('_')
            if numberOfLineToAdd <= len(lines):
                if(parts[4] == "RDUL"):
                    countRDUL[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsRDUL[int(parts[1]) - 1] += 1
                elif(parts[4] == "RDLU"):
                    countRDLU[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsRDLU[int(parts[1]) - 1] += 1
                elif(parts[4] == "DRUL"):
                    countDRUL[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsDRUL[int(parts[1]) - 1] += 1
                elif (parts[4] == "DRLU"):
                    countDRLU[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsDRLU[int(parts[1]) - 1] += 1
                elif (parts[4] == "LUDR"):
                    countLUDR[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsLUDR[int(parts[1]) - 1] += 1
                elif (parts[4] == "LURD"):
                    countLURD[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsLURD[int(parts[1]) - 1] += 1
                elif (parts[4] == "ULDR"):
                    countULDR[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsULDR[int(parts[1]) - 1] += 1
                elif (parts[4] == "ULRD"):
                    countULRD[int(parts[1]) - 1] += float(lines[numberOfLineToAdd])
                    numberOfCountsULRD[int(parts[1]) - 1] += 1
            else:
                return "Podana linia nie istnieje w pliku."
    for i in range(len(countRDUL)):
        zmienna = countRDUL[i]
        dzielnik = numberOfCountsRDUL[i]
        if(dzielnik != 0):
            countRDUL[i] = zmienna / dzielnik

        zmienna1 = countRDLU[i]
        dzielnik1 = numberOfCountsRDLU[i]
        if(dzielnik1 != 0):
            countRDLU[i] = zmienna1 / dzielnik1

        zmienna2 = countDRUL[i]
        dzielnik2 = numberOfCountsDRUL[i]
        if(dzielnik2 != 0):
            countDRUL[i] = zmienna2 / dzielnik2

        zmienna3 = countDRLU[i]
        dzielnik3 = numberOfCountsDRLU[i]
        if(dzielnik3 != 0):
            countDRLU[i] = zmienna3 / dzielnik3

        zmienna4 = countLUDR[i]
        dzielnik4 = numberOfCountsLUDR[i]
        if(dzielnik4 != 0):
            countLUDR[i] = zmienna4 / dzielnik4

        zmienna5 = countLURD[i]
        dzielnik5 = numberOfCountsLURD[i]
        if(dzielnik5 != 0):
            countLURD[i] = zmienna5 / dzielnik5

        zmienna6 = countULDR[i]
        dzielnik6 = numberOfCountsULDR[i]
        if(dzielnik6 != 0):
            countULDR[i] = zmienna6 / dzielnik6

        zmienna7 = countULRD[i]
        dzielnik7 = numberOfCountsULRD[i]
        if(dzielnik2 != 0):
            countULRD[i] = zmienna7 / dzielnik7
    return countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD


def genPlotsOverall(lista1, lista2, lista3):
    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    indeksy = range(len(lista1))
    plt.bar(indeksy, lista1, bar_width, label='Lista 1', color='blue')
    plt.bar([i + bar_width for i in indeksy], lista2, bar_width, label='Lista 2', color='green')
    plt.bar([i + 2 * bar_width for i in indeksy], lista3, bar_width, label='Lista 3', color='red')
    plt.xlabel('Indeks')
    plt.ylabel('Wartość')
    plt.title('Wykres wartości dla trzech list')
    plt.xticks([i + bar_width for i in indeksy], [i + 1 for i in indeksy])
    plt.legend()
    plt.grid(False)
    plt.show()
def genPlotsAstar(lista1, lista2):
    plt.figure(figsize=(14, 8))
    bar_width = 0.35
    indeksy = range(1, len(lista1) + 1)
    plt.bar(indeksy, lista1, bar_width, label='Manhattan', color='blue')
    plt.bar([i + bar_width for i in indeksy], lista2, bar_width, label='Hamming', color='green')
    plt.title("A*",fontsize=24)
    plt.xticks([i + bar_width/2 for i in indeksy], indeksy)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=17)
    plt.grid(False)
    plt.show()

def genPlotsBfs(*lists, title):
    plt.figure(figsize=(14, 8))
    bar_width = 0.1
    num_lists = len(lists)
    indeksy = range(len(lists[0]))
    colors = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan', 'magenta']
    label = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for i, lista in enumerate(lists):
        plt.bar([j + i * bar_width for j in indeksy], lista, bar_width, label=label[i], color=colors[i])
    plt.title('BFS', fontsize=24)
    plt.xlabel('Głębokość', fontsize=23)
    if title == 0:
        plt.ylabel('Średnia długość drogi rozwiązania', fontsize=23)
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    if title == 1:
        plt.yscale('log')
        plt.ylabel('Średnia liczba stanów odwiedzonych', fontsize=23)
    if title == 2:
        plt.yscale('log')
        plt.ylabel('Średnia liczba stanów przetworzonych', fontsize=23)
    if title == 3:
        plt.ylabel('Średnia maksymalna głębokość rekursji', fontsize=23)
        plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    if title == 4:
        plt.yscale('log')
        plt.ylabel('Średni czas procesu obliczeniowego (ms)',fontsize=23)
    plt.xticks([j + (num_lists - 1) * bar_width / 2 for j in indeksy], [j + 1 for j in indeksy])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=17)
    plt.grid(False)
    plt.show()

countManh, countHamm = createPlotOfStatsAstar(0)
genPlotsAstar(countManh, countHamm)
countManh, countHamm = createPlotOfStatsAstar(1)
genPlotsAstar(countManh, countHamm)
countManh, countHamm = createPlotOfStatsAstar(2)
genPlotsAstar(countManh, countHamm)
countManh, countHamm = createPlotOfStatsAstar(3)
genPlotsAstar(countManh, countHamm)
countManh, countHamm = createPlotOfStatsAstar(4)
genPlotsAstar(countManh, countHamm)

countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD = createPlotOfStatsBfsDfs(0)
genPlotsBfs(countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD,title = 0)
countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD = createPlotOfStatsBfsDfs(1)
genPlotsBfs(countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD,title = 1)
countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD = createPlotOfStatsBfsDfs(2)
genPlotsBfs(countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD,title = 2)
countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD = createPlotOfStatsBfsDfs(3)
genPlotsBfs(countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD,title = 3)
countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD = createPlotOfStatsBfsDfs(4)
genPlotsBfs(countRDUL, countRDLU, countDRUL, countDRLU, countLUDR, countLURD, countULDR, countULRD,title = 4)


