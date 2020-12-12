
filename = "day9.txt"

data = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        data.append(int(line.strip()))
        line = file.readline()

# Find the first number that cannot be summed to from 2 numbers in the previous $preamble amount of numbers
def find_num():
    preamble = 25
    for i in range(preamble, len(data)):
        target = data[i]
        valid = False
        for j in range(i-preamble, i-1):
            for k in range(i-preamble+1, i):
                if data[j] + data[k] == target:
                    valid = True
        if not valid:
            return tuple((i, target))

# Find a set of numbers that add to the number found in part 1, and return max + min numbers of that set
def sum_to(index, target):
    for i in range(len(data)-1):
        x = i + 1
        if i == index or x == index:
            continue
        usedNums = [data[i], data[x]]
        sum = data[i] + data[x]
        while sum < target:
            x += 1
            sum += data[x]
            usedNums.append(data[x])
        if sum == target:
            usedNums = sorted(usedNums)
            return usedNums[0] + usedNums[-1]


targetIndex, targetNum = find_num()
print("Answer for Part 1:", targetNum)
print("Answer for Part 2:", sum_to(targetIndex, targetNum))

