password = 0
value = 50
lines = 0

with open("input", "rt") as f:
    while (True):
        line = f.readline()
        if (line == ""):
            break
        lines += 1
        offset = int(line[1:])
        if (line.startswith('L')):
            value -= offset
        if (line.startswith('R')):
            value += offset
        value = value % 100
        if (value == 0):
            password += 1
    print(lines)
    print(password)
