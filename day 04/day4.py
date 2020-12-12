import re

filename = "day4.txt"

with open(filename, 'r') as file:
    inp = file.readlines()

# Regex expressions for each field for Part 2
byr = "(^19[2-9][0-9]$)|(^200[0-2]$)"
iyr = "^20(1[0-9]|20)$"
eyr = "^20(2[0-9]|30)$"
hgt = "^1([5-8][0-9]|9[0-3])cm|(59|(6[0-9]|7[0-6]))in$"
hcl = "^#[0-9a-f]{6}$"
ecl = "^(amb|blu|brn|gry|grn|hzl|oth)$"
pid = "^[0-9]{9}$"
regexs = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}


def countValid(data, verifyFields):
    count = 0
    fieldStatus = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                   "pid": False}  # Initialize passport to no valid fields
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for line in data:
        line = line.strip()

        # Found a blank line, meaning previous passport is finished loading and ready to check
        if len(line) == 0:
            currentKeys = fieldStatus.keys()
            if len(currentKeys) < len(required):
                pass
            else:
                validPassport = True
                for key in currentKeys:
                    if key == "cid":
                        continue
                    elif fieldStatus[key] == False:
                        validPassport = False
                        break

                if validPassport:
                    count += 1

            # Clear previous passport data to prepare for the next one
            fieldStatus = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                           "pid": False}
        else:
            items = line.split()
            for elem in items:
                parts = elem.split(':')
                field = parts[0]
                if field == "cid":
                    continue
                if verifyFields:
                    if re.search(regexs[field], parts[1]) is not None:
                        fieldStatus[field] = True
                else:
                    fieldStatus[field] = True
    return count


print("Answer for Part 1: {}".format(countValid(inp, False)))
print("Answer for Part 2: {}".format(countValid(inp, True)))
