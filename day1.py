with open("day1.txt") as file:
    data = file.read().splitlines()
    for i in range(len(data)):
        data[i] = int(data[i])
    numToCheck = int(input("Enter number of entries to combine: "))
    num1 = 0
    num2 = 0
    num3 = 0
    if numToCheck == 2:
        for entry in data:
            temp = 2020-entry
            if temp in data:
                num1 = entry
                num2 = temp
                break
        print(num1 * num2)
    elif numToCheck == 3:
        try:
            for entry1 in data:
                for entry2 in data:
                    check = 2020 - (entry1 + entry2)
                    if check in data:
                        print(entry1 * entry2 * check)
                        raise Exception("Done")
        except:
            pass