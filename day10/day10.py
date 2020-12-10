filename = "day10.txt"

data = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        line = int(line.strip())
        data.append(line)
        line = file.readline()


def calculate_differences():
    sortedData = sorted(data)
    sortedData.insert(0, 0)
    diff1 = 0
    diff3 = 0
    for i in range(len(sortedData)-1):
        diff = sortedData[i+1] - sortedData[i]
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 += 1
    diff3 += 1
    return diff1 * diff3


print("Answer to Part 1:", calculate_differences())
