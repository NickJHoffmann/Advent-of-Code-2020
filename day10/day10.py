filename = "day10.txt"

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


def find_paths(start):
    paths = 0

    # Base case, made it to the last device
    if start == data[-1]:
        return 1

    # Check if the path count has already been found for this adapter device
    if start in completePaths:
        return completePaths[start]

    # Adapters can adapt up to 3 joltage higher, so check paths for each adaption
    if start + 1 in setData:
        paths += find_paths(start + 1)
    if start + 2 in setData:
        paths += find_paths(start + 2)
    if start + 3 in setData:
        paths += find_paths(start + 3)

    # Assign path count to dictionary of already-checked paths to prevent having to fully recurse if this adapter
    # is encountered later
    completePaths[start] = paths
    return paths


print("Answer to Part 1:", calculate_differences())
print("Answer to Part 2:", find_paths(0))
