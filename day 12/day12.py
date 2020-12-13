import math

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

        # Left means move left in direction list, right means move right
        elif inst == "L":
            dir = val // 90
            lastDir = directionList[directionList.index(lastDir) - dir]

        elif inst == "R":
            # Calculate overflow if turning right past West
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


def part2():
    waypoint = (10, 1)  # Given that waypoint starts 10 east, 1 north
    ship = (0, 0)
    for i in range(len(data)):
        inst = data[i][0]
        val = int(data[i][1:])
        wayX, wayY = waypoint
        shipX, shipY = ship
        if inst == "F":
            shipX += val * wayX
            shipY += val * wayY
        elif inst == "N":
            wayY += val
        elif inst == "E":
            wayX += val
        elif inst == "S":
            wayY -= val
        elif inst == "W":
            wayX -= val
        elif inst == "L" or inst == "R":
            if inst == "R":
                val *= -1   # Positive degree means counter-clockwise rotation, negative means clockwise
            # Rotate waypoint around ship
            tempX = (wayX * round(math.cos(math.radians(val)))) - (wayY * round(math.sin(math.radians(val))))
            tempY = (wayX * round(math.sin(math.radians(val)))) + (wayY * round(math.cos(math.radians(val))))
            wayX = tempX
            wayY = tempY
        ship = (shipX, shipY)
        waypoint = (wayX, wayY)
    finalX, finalY = ship
    return abs(finalX) + abs(finalY)


print("Answer to Part 1:", part1())
print("Answer to Part 2:", part2())
