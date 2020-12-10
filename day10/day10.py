filename = "example.txt"

data = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        line = int(line.strip())
        data.append(line)
        line = file.readline()
data = sorted(data)
data.insert(0, 0)


def calculate_differences():
    diff1 = 0
    diff3 = 0
    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 += 1
    diff3 += 1      # Device joltage will always be 3 higher than highest adapter
    return diff1 * diff3


completePaths = {}
setData = set(data)


def find_paths(index):
    # Incorrect: 11239424 (too low)

    paths = 0
    start = data[index]
    if start == data[-1]:
        return 1
    if start + 1 in setData:
        print("found start + 1:", start + 1)
        try:
            paths += completePaths[start+1]
        except Exception as e:
            found = find_paths(index+1)
            completePaths[start+1] = found
            paths += found
    if start + 2 in setData:
        print("found start + 2:", start + 2)
        try:
            paths += completePaths[start+2]
        except Exception as e:
            found = find_paths(index+2)
            completePaths[start+2] = found
            paths += found
    if start + 3 in setData:
        print("found start + 3:", start + 3)
        try:
            paths += completePaths[start+3]
        except Exception as e:
            found = find_paths(index+3)
            completePaths[start+3] = found
            paths += found
    return paths


print("Answer to Part 1:", calculate_differences())
print("Answer to Part 2:", find_paths(0))
