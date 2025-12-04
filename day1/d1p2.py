import sys

password = 0
value = 50
lines = 0

if (len(sys.argv) != 2):
    print("need an input file, champ")
    exit()
with open(sys.argv[1], "rt") as f:
    while (True):
        line = f.readline()
        if (line == ""):
            break
        sign = 1
        if (line.startswith('L')):
            sign = -1
        elif (line.startswith('R')):
            sign = 1
        offset = int(line[1:])
        offset *= sign
        while (offset != 0):
            value += sign
            offset -= sign
            if (value % 100 == 0):
                password += 1
        value = value % 100
    print(password)
