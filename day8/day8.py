filename = "day8.txt"


data = []
with open(filename, 'r') as file:
    line = file.readline()
    while line:
        data.append(line.strip())
        line = file.readline()

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

print("Answer for Part 1: {}".format(part1(data)))
