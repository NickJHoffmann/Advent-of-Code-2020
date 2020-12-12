filename = "day6.txt"

with open(filename, 'r') as file:
    data = file.readlines()


def part1(info):
    sum = 0
    answers = set()
    for line in info:
        line = line.strip()
        if len(line) == 0:
            sum += len(answers)
            answers = set()
        else:
            for char in line:
                answers.add(char)
    return sum


def part2(info):
    sum = 0
    ansList = []
    for line in info:
        line = line.strip()
        if len(line) == 0:
            ansList[0] = set(ansList[0])

            # Convert each set of answers to Set object and get common items
            for answer in ansList:
                ansList[0] = ansList[0].intersection(answer)
            sum += len(ansList[0])
            ansList = []
        else:
            ansList.append(line)
    return sum


print("Answer for Part 1: {}".format(part1(data)))
print("Answer for Part 2: {}".format(part2(data)))