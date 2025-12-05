import sys


def main():
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <filename>")
        return 2

    try:
        file = open(sys.argv[1], "rt")
    except OSError as e:
        print(e)
        return 1

    ranges = file.read().split(',')
    file.close()
    password = 0
    for r in ranges:
        password += calculate_invalids(r)
    print(password)


def calculate_invalids(range):
    limits = range.split('-')
    start = int(limits[0])
    end = int(limits[1])
    ret = 0
    while (start <= end):
        string = str(start)
        if (len(string) % 2 != 0):
            start += 1
            continue
        halfpoint = len(string) // 2
        if (string[0:halfpoint] == string[halfpoint:]):
            ret += int(string)
        start += 1
    return ret


if __name__ == "__main__":
    main()
