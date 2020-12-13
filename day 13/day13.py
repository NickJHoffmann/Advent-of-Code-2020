filename = "day13.txt"


def part1():
    with open(filename, 'r') as file:
        earliest = int(file.readline().strip())
        allbusses = file.readline().strip().split(",")
        buslist = []
        for bus in allbusses:
            if bus != 'x':
                buslist.append(int(bus))

    currentTime = earliest
    while True:
        for bus in buslist:
            if currentTime % bus == 0:
                return bus * (currentTime - earliest)
        currentTime += 1


print("Answer for Part 1:", part1())
