import re

incorrect = [138]




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


def checkRegex(regex, string):
    return len(re.findall(regex, string)) == 1


def countValid(data, verifyFields):
    count = 0
    fieldStatus = fieldStatus = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False,
                           "pid": False}        # Initialize passport to no valid fields
    vals = {}
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for line in data:
        line = line.strip()

        # Found a blank line, meaning previous passport is finished loading and ready to check
        if len(line) == 0:
            currentKeys = list(fieldStatus.keys())
            if len(currentKeys) < len(required):
                pass
            else:
                validPassport = True

                # If flag to check part 2 is set
                if verifyFields:
                    for key in vals.keys():
                        if key == "cid":
                            continue
                        elif key == "byr":
                            reg = re.search(byr, vals[key].strip())
                            print(key, vals[key], sep=", ", end=": ")
                            print(reg, end=", length = ")
                            print(reg.string)
                            if reg is None:
                                validPassport = False
                                break
                        elif key == "iyr":
                            reg = re.search(iyr, vals[key].strip())
                            print(key, vals[key], sep=", ", end=": ")
                            print(reg, end=", length = ")
                            print(reg.string)
                            if reg is None:
                                validPassport = False
                                break
                        elif key == "eyr":
                            reg = re.search(eyr, vals[key].strip())
                            print(key, vals[key], sep=", ", end=": ")
                            print(reg, end=", length = ")
                            print(reg.string)
                            if reg is None:
                                validPassport = False
                                break
                        elif key == "hgt":
                            reg = re.search(hgt, vals[key].strip())
                            print(key, vals[key], sep=", ", end=": ")
                            print(reg, end=", length = ")
                            print(reg.string)
                            if reg is None:
                                validPassport = False
                                break
                        elif key == "hcl":
                            reg = re.search(hcl, vals[key].strip())
                            print(key, vals[key], sep=", ", end=": ")
                            print(reg, end=", length = ")
                            print(reg.string)
                            if reg is None:
                                validPassport = False
                                break
                        elif key == "ecl":
                            reg = re.search(ecl, vals[key].strip())
                            print(key, vals[key], sep=", ", end=": ")
                            print(reg, end=", length = ")
                            print(reg.string)
                            if reg is None:
                                validPassport = False
                                break
                        elif key == "pid":
                            reg = re.search(pid, vals[key].strip())
                            print(key, vals[key], sep=", ", end=": ")
                            print(reg, end=", length = ")
                            print(reg.string)
                            if reg is None:
                                validPassport = False
                                break
                        else:
                            continue
                        fieldStatus[key] = True
                else:
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
            vals = {}
        else:
            items = line.split()
            for elem in items:
                parts = elem.split(':')
                fieldStatus[parts[0]] = True
                vals[parts[0]] = parts[1]
    return count


print("Answer for Part 1: {}".format(countValid(inp, False)))
print("Answer for Part 2: {}".format(countValid(inp, True)))
