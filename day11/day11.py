import copy

filename = "day11.txt"

raw = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        raw.append(list(line.strip()))
        line = file.readline()


def find_occupied_adjacent_p1(xVal, yVal, data):
    total = 0
    try:
        if data[yVal][xVal + 1] == "#":
            total += 1
    except IndexError:
        pass
    try:
        if xVal - 1 < 0:
            raise IndexError
        if data[yVal][xVal - 1] == "#":
            total += 1
    except IndexError:
        pass
    try:
        if data[yVal + 1][xVal] == "#":
            total += 1
    except IndexError:
        pass
    try:
        if yVal - 1 < 0:
            raise IndexError
        if data[yVal - 1][xVal] == "#":
            total += 1
    except IndexError:
        pass
    try:
        if data[yVal + 1][xVal + 1] == "#":
            total += 1
    except IndexError:
        pass
    try:
        if xVal - 1 < 0:
            raise IndexError
        if data[yVal + 1][xVal - 1] == "#":
            total += 1
    except IndexError:
        pass
    try:
        if yVal - 1 < 0:
            raise IndexError
        if data[yVal - 1][xVal + 1] == "#":
            total += 1
    except IndexError:
        pass
    try:
        if xVal - 1 < 0 or yVal - 1 < 0:
            raise IndexError
        if data[yVal - 1][xVal - 1] == "#":
            total += 1
    except IndexError:
        pass
    return total


def part1():
    modified = False
    data = copy.deepcopy(raw)
    newData = copy.deepcopy(data)
    while True:
        y = 0
        while y < len(data):
            x = 0
            while x < len(data[y]):
                if data[y][x] == "L":
                    occupiedAdjacent = find_occupied_adjacent_p1(x, y, data)
                    if occupiedAdjacent == 0:
                        newData[y][x] = "#"
                        modified = True
                elif data[y][x] == "#":
                    occupiedAdjacent = find_occupied_adjacent_p1(x, y, data)
                    if occupiedAdjacent >= 4:
                        newData[y][x] = "L"
                        modified = True
                x += 1
            y += 1
        data = copy.deepcopy(newData)
        if modified is True:
            modified = False
            continue
        else:
            break

    occupiedSeats = 0
    for row in data:
        for char in row:
            if char == "#":
                occupiedSeats += 1
    return occupiedSeats


print("Answer to Part 1:", part1())
