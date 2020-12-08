import re

filename = "day8.txt"

data = []
#testData = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        data.append(line.strip())
        line = file.readline()

#testData = data.copy()

def part1(oplist):
    used = set()
    accum = 0
    i = 0
    while i < len(data):
        if i in used:
            return accum
            break
        parts = data[i].split()
        op = parts[0]
        val = int(parts[1])
        if op == "nop":
            pass
        elif op == "acc":
            accum += val
        elif op == "jmp":
            used.add(i)
            i += val
            continue
        else:
            print("Bad op")
        used.add(i)
        i += 1

def check_each_p2(dataSet):
    used = set()
    accum = 0
    i = 0
    while i < len(dataSet):
        if i in used:
            return False
        parts = dataSet[i].split()
        op = parts[0]
        val = int(parts[1])
        if op == "nop":
            pass
        elif op == "acc":
            accum += val
        elif op == "jmp":
            used.add(i)
            i += val
            continue
        else:
            print("Bad op")
        used.add(i)
        i += 1
    return accum

def part2():
    testData = data.copy()
    for i in range(len(data)):
        if re.search("^nop", testData[i]) is not None:
            testData[i] = re.sub("^nop", "jmp", testData[i])
            res = check_each_p2(testData)
            if type(res) == int:
                return res
        elif re.search("^jmp", testData[i]) is not None:
            testData[i] = re.sub("^jmp", "nop", testData[i])
            res = check_each_p2(testData)
            if type(res) == int:
                return res
        testData = data.copy()



print("Answer for Part 1: {}".format(part1(data)))
print("Answer for Part 2: {}".format(part2()))
