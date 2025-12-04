import sys


def print_err(msg: str) -> None:
    print("Error", msg, file=sys.stderr)


def read_file(filename: str) -> list[str]:
    with open(filename, "rt") as f:
        return f.readlines()


def solve(map: list[str]) -> int:
    solution: int = 0
    y: int = 0
    while y < len(map):
        x: int = 0
        while x < len(map[y]):
            if map[y][x] == '@' and surround_check(map, x, y):
                solution += 1
            x += 1
        y += 1
    return solution


def surround_check(map: list[str], x: int, y: int) -> bool:
    x_off: int = -1
    y_off: int = -1
    adj_rolls: int = 0
    while True:
        if y + y_off >= 0 and y + y_off < len(map) and \
                x + x_off >= 0 and x + x_off < len(map[y + y_off]):

            if (map[y + y_off][x + x_off] == '@'):
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


def main() -> int:
    if (len(sys.argv) != 2):
        print("Usage:", {sys.argv[0]}, "<filename>")
        return 2
    try:
        map = read_file(sys.argv[1])
    except OSError as e:
        print_err(e)
        return 1
    solution: int = solve(map)
    print(solution)
    return 0


if (__name__ == "__main__"):
    main()
