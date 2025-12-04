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
        if (is_repeating(start)):
            ret += start
        start += 1
    return ret


def is_repeating(number):
    string = str(number)
    sequence_len = 1
    while (sequence_len <= len(string) // 2):
        if (len(string) % sequence_len != 0):
            sequence_len += 1
            continue

        i = sequence_len
        while (i < len(string)):
            if (string[:sequence_len] != string[i:i + sequence_len]):
                break
            i += sequence_len

        if (i == len(string)):
            return True
        sequence_len += 1
    return False


main()
