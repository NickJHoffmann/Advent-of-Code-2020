filename = "day3.txt"

# Determines the amount of trees intersected using a given slope
def findTrees(xSlope, ySlope):
    with open(filename, 'r') as file:
        mapRows = file.readlines()

    lineLength = len(mapRows[0])   # Max length of each line, stored for readability later
    treeCount = 0
    currentPos = 0              # Current horizontal position
    currentLine = 0
    while currentLine < len(mapRows):
        row = mapRows[currentLine]
        if row[currentPos] == '#':
            treeCount += 1
        currentPos += xSlope

        # If pointer is at the end of line, calculate "overflow" to determine what x position to start next line
        if currentPos >= lineLength-1:
            currentPos = currentPos - lineLength + 1

        currentLine += ySlope
    return treeCount

# Part 1
part1 = findTrees(3, 1)
print("Answer for Part 1: {}".format(part1))

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]   # Slopes given in Part 2, listed in (x, y) notation
numOfTrees = 1          # Need to multiply all answers, so initialize to 1 to allow me to use *= on each value
for slope in slopes:
    numOfTrees *= findTrees(slope[0], slope[1])
print("Answer for Part 2: {}".format(numOfTrees))
