dane = []
positiveDane = []

with open('data.txt', 'r') as file:
    for line in file:
        row = line.strip().split(' ')
        dane.append(list(map(int, row)))

with open('wzorzec.txt', 'r') as file:
    for line in file:
        positiveRow = line.strip().split(' ')
        positiveDane.append(list(map(int, positiveRow)))
def moveFunction(move):
    zero_positions = []
    for i, row in enumerate(dane):
        for j, number in enumerate(row):
            if number == 0:
                zero_positions.append((i, j))
    for position in zero_positions:
        if(move == "L"):
            if(position[1] != 0):
                change = dane[position[0]][position[1]-1]
                dane[position[0]][position[1]-1] = dane[position[0]][position[1]]
                dane[position[0]][position[1]] = change
        if(move == "R"):
            if(position[1] != 3):
                change = dane[position[0]][position[1] + 1]
                dane[position[0]][position[1] + 1] = dane[position[0]][position[1]]
                dane[position[0]][position[1]] = change
        if(move == "U"):
            if(position[0] != 0):
                change = dane[position[0] - 1][position[1]]
                dane[position[0] - 1][position[1]] = dane[position[0]][position[1]]
                dane[position[0]][position[1]] = change
        if(move == "D"):
            if(position[0] != 3):
                change = dane[position[0] + 1][position[1]]
                dane[position[0] + 1][position[1]] = dane[position[0]][position[1]]
                dane[position[0]][position[1]] = change
    zero_positions.clear()
    for i, row in enumerate(dane):
        for j, number in enumerate(row):
            if number == 0:
                zero_positions.append((i, j))

    print(zero_positions[0])


def manhattan_distance():
    polesDictionary = []
    for i in range(0, 16):
        position = []
        positivePosition = []

        for j, row in enumerate(dane):
            for k, number in enumerate(row):
                if number == i:
                    position.append((j, k))
        for j, positiveRow in enumerate(positiveDane):
            for k, number in enumerate(positiveRow):
                if number == i:
                    positivePosition.append((j, k))

        for position1 in position:
            for position2 in positivePosition:
                distance = abs((position1[0] - position2[0]) + (position1[1] - position2[1]))
                polesDictionary.append(distance)

    return polesDictionary


polesDictionary = manhattan_distance()
print(polesDictionary)
print(dane)