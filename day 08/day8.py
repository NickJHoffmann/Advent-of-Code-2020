import re

filename = "day8.txt"

data = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        data.append(line.strip())
        line = file.readline()


def test_boot(dataSet, inPart2):
    used = set()
    accum = 0
    i = 0
    while i < len(dataSet):
        if i in used:
            # Part 1 and Part 2 require different return results when encountering an infinite loop
            if inPart2:
                return False
            else:
                return accum
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

        # Check if opcode is "nop" or "jump" and swap it accordingly, then test program with that switch
        if re.search("^nop", testData[i]) is not None:
            testData[i] = re.sub("^nop", "jmp", testData[i])
            res = test_boot(testData, True)
            if res is not False:
                return res
        elif re.search("^jmp", testData[i]) is not None:
            testData[i] = re.sub("^jmp", "nop", testData[i])
            res = test_boot(testData, True)
            if res is not False:
                return res

        # Reset test data to original to prevent compounding changes
        testData = data.copy()


print("Answer for Part 1: {}".format(test_boot(data, False)))
print("Answer for Part 2: {}".format(part2()))
