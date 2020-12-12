filename = "day12.txt"

data = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        data.append(line.strip())
        line = file.readline()

def part1():
    directionList = ["N", "E", "S", "W"]
    directions = {"N": 0, "E": 0, "S": 0, "W": 0}
    lastDir = "E"
    for i in range(len(data)):
        inst = data[i][0]
        val = int(data[i][1:])
        if inst == "F":
            directions[lastDir] += val
        elif inst == "L":
            dir = val // 90
            lastDir = directionList[directionList.index(lastDir) - dir]
        elif inst == "R":
            dir = val // 90
            lastIndex = directionList.index(lastDir)
            if lastIndex + dir > len(directionList):
                dir = lastIndex + dir - len(directionList)
            elif lastIndex + dir == len(directionList):
                dir = 0
            else:
                dir = lastIndex + dir
            lastDir = directionList[dir]
        else:
            directions[inst] += val

    NS = abs(directions["N"] - directions["S"])
    EW = abs(directions["E"] - directions["W"])
    return NS + EW


print("Answer to Part 1:", part1())
