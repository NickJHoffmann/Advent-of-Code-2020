import math

filename = "day5.txt"

with open(filename, 'r') as file:
     passes = file.readlines()

# Calculate seat id of a given boarding pass
def getSeats(data):
    line = data.strip()

    # Establish row and column bounds based on given prompt
    rowLower = 0
    rowUpper = 127

    colLower = 0
    colUpper = 7

    for char in line:
        # Change the bounds of the current partition depending on what character is encountered
        if char == "B":
            rowLower += math.ceil((rowUpper-rowLower)/2)
        elif char == "F":
            rowUpper -= math.ceil((rowUpper-rowLower)/2)
        elif char == "L":
            colUpper -= math.ceil((colUpper-colLower)/2)
        elif char == "R":
            colLower += math.ceil((colUpper-colLower)/2)
        else:
            print("Invalid character in boarding pass")
    seatID = rowLower * 8 + colLower    # Given formula to calculate seat ID
    return seatID


# Part 1
maxSeat = 0
for item in passes:
    maxSeat = max(maxSeat, getSeats(item))
print("Answer for Part 1: {}".format(maxSeat))

# Part 2
seats = []
for item in passes:
    seats.append(getSeats(item))
seats = sorted(seats)
for i in range(1, len(seats)-1):
    if seats[i+1] - seats[i-1] != 2:
        print("Answer for Part 2: {}".format(seats[i]+1))
        break
