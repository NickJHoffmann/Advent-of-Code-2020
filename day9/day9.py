

filename = "day9.txt"

data = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        data.append(int(line.strip()))
        line = file.readline()

def find_num():
    preamble = 25
    for i in range(preamble, len(data)):
        target = data[i]
        valid = False
        for x in range(i-preamble, i-1):
            for j in range(i-preamble+1, i):
                #print(data[x], data[j])
                if data[x] + data[j] == target:
                    valid = True
        if not valid:
            return tuple((i, target))


targetIndex, targetNum = find_num()
print("Answer for Part 1:", targetNum)

