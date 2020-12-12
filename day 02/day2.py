with open("day2.txt", 'r') as file:
    line = file.readline()
    p1Count = 0
    p2Count = 0
    while line:
        data = line.split()
        nums = data[0].split('-')
        lowerBound = int(nums[0])
        upperBound = int(nums[1])
        letter = data[1].replace(':', "")
        password = data[2]

        #Part 1
        occurances = password.count(letter)
        if lowerBound <= occurances <= upperBound:
            p1Count += 1

        #Part 2
        if bool(password[lowerBound - 1] == letter) ^ bool(password[upperBound - 1] == letter):
            p2Count += 1

        line = file.readline()
    print("Answer to Part 1: {}".format(p1Count))
    print("Answer to Part 2: {}".format(p2Count))
