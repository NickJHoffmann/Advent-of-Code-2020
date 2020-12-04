filename = "day4.txt"

with open(filename, 'r') as file:
    data = file.readlines()

count = 0
dict = {}
required = sorted(["byr", "iry", "eyr", "hgt", "hcl", "ecl", "pid"])
for item in data:
    item = item.strip()
    if len(item) == 0:
        currentKeys = list(dict.keys())
        if len(currentKeys) > len(required):
            count += 1
        elif len(currentKeys) < len(required):
            pass
        else:
            print("last key: " + currentKeys[-1])
            #print(currentKeys)
            flag = True
            for key in currentKeys:
                if key not in required:
                    if key == "cid":
                        continue
                    else:
                        bool = False
                        break
            if flag:
                print("made it")
                count += 1
        dict = {}
    else:
        items = item.split()
        #print(items)
        for elem in items:
            parts = elem.split(':')
            dict[parts[0]] = parts[1]
    #print(dict)
print(count)