with open("day2.txt", 'r') as file:
    line = file.readline()
    validP1 = 0
    validP2 = 0
    while line:
        data = line.split()
        nums = data[0].split('-')
        num1 = int(nums[0])
        num2 = int(nums[1])
        letter = data[1].replace(':', "")
        password = data[2]

        #Part 1
        occur = password.count(letter)
        if num1 <= occur <= num2:
            validP1 += 1

        #Part 2
        if (password[num1-1] == letter and not password[num2-1] == letter) or (not password[num1-1] == letter and password[num2-1] == letter):
            validP2 += 1
        line = file.readline()
    print(validP1)
    print(validP2)