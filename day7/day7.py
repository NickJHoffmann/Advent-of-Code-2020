import re

filename = "example1.txt"

p1sum = 0
bags = {}

p2sum = 0
usedBags = {}

# Recursive function to check if a bag can be traced to "shiny gold"
def checkBags(bag):
    global p1sum
    global usedBags
    for bagName, bagVal in bag.items():
        #print(bagName, bagVal)
        # If shiny gold has been reached, completely break out of function call for the given outer bag to move on
        if bagName == "shiny gold":
            p1sum += 1
            #print("made it here")
            return True
            #raise Exception("Found valid bag path")
        elif bags[bagName] != 0:
            if checkBags(bags[bagName]):
                try:
                    print(usedBags)
                    numUsed = usedBags[bagName][bagVal]
                    print(numUsed)
                    usedBags[bagName] = {bagVal: numUsed + 1}
                except:
                    usedBags[bagName] = {bagVal: 1}
                    print(usedBags)
                finally:
                    return True
            else:
                continue
        else:
            continue
    #return False


def part1():
    global p1sum
    global usedBags
    with open(filename, 'r') as file:
        line = file.readline().strip()
        while line:
            line = line.split()

            # The first two words of every line will always be the bag description
            keyBag = "{adj} {col}".format(adj=line[0], col=line[1])
            valBags = {}    # Stores which bags can be put into the current key bag

            # Start at index 4 because indexes 0-3 describe the initial bag, we need to parse rest of the line
            for i in range(4, len(line)):
                if line[i] == "no":
                    valBags = 0
                    break

                # If the current word is a number, it is guaranteed that the next two words are a bag description
                elif re.search("^[0-9]$", line[i]) is not None:
                    tempBagNum = int(line[i])
                    tempBagKey = "{adj} {col}".format(adj=line[i+1], col=line[i+2])
                    valBags[tempBagKey] = tempBagNum    # Add this inner bag to the list of bags that can be put in keyBag
            bags[keyBag] = valBags
            line = file.readline().strip()
    i = 1
    for outerBag in bags.keys():
        if bags[outerBag] != 0:

            # Checks if the current bag can be traced back to "shiny gold" bag
            # checkBags raises exception to break out of recursion if it reaches "shiny gold" at any point, so
            # it will increment the counter and move on to check the next outer bag
            checkBags(bags[outerBag])
            print(i)
            #print(usedBags)
            usedBags = {}
        i += 1

# Part 1
part1()
print("Answer to Part 1: {}".format(p1sum))