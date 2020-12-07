import re

# Incorrect: 117 (too low)
filename = "example.txt"

p1sum = 0
bags = {}
def checkBags(bag):
    global p1sum
    print(bag.items())
    for bagName, bagVal in bag.items():
        #print(bagName)
        if bagName == "shiny gold":
            p1sum += 1
            raise Exception("Found valid bag path")
        elif bags[bagName] != 0:
            checkBags(bags[bagName])
        else:
            return


def part1():
    with open(filename, 'r') as file:
        line = file.readline().strip()

        while line:
            line = line.split()
            keyBag = "{adj} {col}".format(adj=line[0], col=line[1])
            valBags = {}
            for i in range(4, len(line)):
                if line[i] == "no":
                    valBags = 0
                    break
                elif re.search("^[0-9]$", line[i]) is not None:
                    tempBagNum = int(line[i])
                    tempBagKey = "{adj} {col}".format(adj=line[i+1], col=line[i+2])
                    valBags[tempBagKey] = tempBagNum
            bags[keyBag] = valBags
            line = file.readline().strip()
    for outerBag in bags.keys():
        if bags[outerBag] != 0:
            try:
                checkBags(bags[outerBag])
            except:
                continue
    print(p1sum)


part1()