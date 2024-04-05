import os

def createPlotOfStatsOverall(numberOfLineToAdd):
    wynikiBfs = []
    wynikiDfs = []
    wynikiAstar = []
    numberOfCounts = [0,0,0]
    countBfs = [0,0,0,0,0,0,0]
    countDfs = [0,0,0,0,0,0,0]
    countAstar = [0,0,0,0,0,0,0]
    directoryToStats = "solvedStats"
    for fileName in os.listdir(directoryToStats):
        parts = fileName.split('_')
        with open(fileName, 'r') as file:
            lines = file.readlines()
            if numberOfLineToAdd <= len(lines):
                if(parts[2] == "bfs"):
                    countBfs[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[0] += 1
                elif(parts[2] == "dfs"):
                    countDfs[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[1] += 1
                else:
                    countAstar[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[2] += 1
            else:
                return "Podana linia nie istnieje w pliku."
    for number in countBfs:
        wynikiBfs.append(number/numberOfCounts[0])
    for number in countDfs:
        wynikiDfs.append(number / numberOfCounts[1])
    for number in countAstar:
        wynikiAstar.append(number/numberOfCounts[2])

def createPlotOfStatsAstar(numberOfLineToAdd):
    wynikiHamm = []
    wynikiManh = []
    numberOfCounts = [0,0]
    countHamm = [0,0,0,0,0,0,0]
    countManh = [0,0,0,0,0,0,0]
    directoryToStats = "solvedStats"
    for fileName in os.listdir(directoryToStats):
        parts = fileName.split('_')
        with open(fileName, 'r') as file:
            lines = file.readlines()
            if numberOfLineToAdd <= len(lines):
                if(parts[2] == "hamm"):
                    countHamm[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[0] += 1
                elif(parts[2] == "manh"):
                    countManh[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[1] += 1
            else:
                return "Podana linia nie istnieje w pliku."
    for number in countHamm:
        wynikiHamm.append(number/numberOfCounts[0])
    for number in countManh:
        wynikiManh.append(number / numberOfCounts[1])

def createPlotOfStatsBFSDFS(numberOfLineToAdd):
    wynikiDRLU = []
    wynikiRDLU = []
    wynikiDRUL = []
    wynikiRDUL = []
    wynikiLUDR = []
    wynikiULDR = []
    wynikiLURD = []
    wynikiULRD = []
    numberOfCounts = [0,0,0,0,0,0,0,0]
    countDRLU = [0,0,0,0,0,0,0]
    countRDLU = [0,0,0,0,0,0,0]
    countDRUL = [0,0,0,0,0,0,0]
    countRDUL = [0,0,0,0,0,0,0]
    countLUDR = [0,0,0,0,0,0,0]
    countULDR = [0,0,0,0,0,0,0]
    countLURD = [0,0,0,0,0,0,0]
    countULRD = [0,0,0,0,0,0,0]
    directoryToStats = "solvedStats"
    for fileName in os.listdir(directoryToStats):
        parts = fileName.split('_')
        with open(fileName, 'r') as file:
            lines = file.readlines()
            if numberOfLineToAdd <= len(lines):
                if(parts[3] == "DRLU"):
                    countDRLU[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[0] += 1
                elif(parts[3] == "RDLU"):
                    countRDLU[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[1] += 1
                elif(parts[3] == "DRUL"):
                    countDRUL[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[1] += 1
                elif(parts[3] == "RDUL"):
                    countRDUL[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[1] += 1
                elif(parts[3] == "LUDR"):
                    countLUDR[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[1] += 1
                elif(parts[3] == "ULDR"):
                    countULDR[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[1] += 1
                elif(parts[3] == "LURD"):
                    countLURD[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[1] += 1
                else:
                    countULRD[int(parts[1])] += lines[numberOfLineToAdd]
                    numberOfCounts[2] += 1
            else:
                return "Podana linia nie istnieje w pliku."
    for number in countDRLU:
        wynikiDRLU.append(number/numberOfCounts[0])
    for number in countRDLU:
        wynikiRDLU.append(number / numberOfCounts[1])
    for number in countDRUL:
        wynikiDRUL.append(number/numberOfCounts[2])
    for number in countRDUL:
        wynikiRDUL.append(number/numberOfCounts[0])
    for number in countLUDR:
        wynikiLUDR.append(number / numberOfCounts[1])
    for number in countULDR:
        wynikiULDR.append(number/numberOfCounts[2])
    for number in countLURD:
        wynikiLURD.append(number/numberOfCounts[0])
    for number in countULRD:
        wynikiULRD.append(number / numberOfCounts[1])

#WYKRESY GENEROWANIE

