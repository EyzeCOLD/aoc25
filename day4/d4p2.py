import sys


def print_err(msg: str) -> None:
    print("Error", msg, file=sys.stderr)


def read_file(filename: str) -> list[list[str]]:
    with open(filename, "rt") as f:
        return [list(r) for r in f.readlines()]


def mark_rolls(map: list[list[str]]) -> int:
    solution: int = 0
    y: int = 0
    while y < len(map):
        x: int = 0
        while x < len(map[y]):
            if map[y][x] == '@' and surround_check(map, x, y):
                map[y][x] = 'x'
                solution += 1
            x += 1
        y += 1
    return solution


def surround_check(map: list[list[str]], x: int, y: int) -> bool:
    x_off: int = -1
    y_off: int = -1
    adj_rolls: int = 0
    while True:
        if (y + y_off >= 0 and y + y_off < len(map) and
                x + x_off >= 0 and x + x_off < len(map[y + y_off])):

            if (map[y + y_off][x + x_off] == '@' or
                    map[y + y_off][x + x_off] == 'x'):
                adj_rolls += 1
                if (adj_rolls >= 4):
                    return False

        x_off += 1
        if (y_off == 0):
            x_off += 1
        if (x_off > 1):
            x_off = -1
            y_off += 1
            if (y_off > 1):
                return True


def clean_up_rolls(map: list[list[str]]) -> None:
    for line in map:
        for index, char in enumerate(line):
            if (char == 'x'):
                line[index] = '.'


def main() -> int:
    if (len(sys.argv) != 2):
        print("Usage:", {sys.argv[0]}, "<filename>")
        return 2
    try:
        map: list[list[str]] = read_file(sys.argv[1])
    except OSError as e:
        print_err(f"read_file: {e}")
        return 1
    solution: int = 0
    while True:
        rolls_marked: int = mark_rolls(map)
        if rolls_marked == 0:
            break
        clean_up_rolls(map)
        solution += rolls_marked
    print(solution)
    return 0


if (__name__ == "__main__"):
    main()
