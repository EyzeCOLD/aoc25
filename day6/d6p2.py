import sys


class Bucket:
    result: int = 0
    operator: str = ""

    
    def __init__(self, operator: str) -> None:
        if (operator == "*" or operator == "+"):
            self.operator = operator
        else:
            raise RuntimeError("Invalid operator")

    def add_number(self, num: int) -> None:
        if (self.operator == "*"):
            if self.result == 0:
                self.result = num
            else:
                self.result *= num
        elif (self.operator == "+"):
            self.result += num
        

def read_file(filename: str) -> list[str]:
    with open(filename, "rt") as f:
        return f.read().splitlines()


def print_err(msg: str, retval: int) -> int:
    print("Error:", msg, file=sys.stderr)
    return retval


def make_buckets(lines: list[str]) -> list[Bucket]:
    buckets: list[Bucket] = []
    col: int = 0
    while col < len(lines[0]):
        if lines[-1][col] != " ":
            buckets.append(Bucket(lines[-1][col]))
        row: int = 0
        raw_num: str = ""
        while row < len(lines) - 1:
            if (lines[row][col] != " "):
                raw_num += lines[row][col]
            row += 1
        if raw_num != "":
            buckets[-1].add_number(int(raw_num))
        col += 1
    return buckets


def main() -> int:
    if len(sys.argv) != 2:
        return print_err(f"Usage: {sys.argv[0]} <filename>", 2)

    lines: list[str] = []
    try:
        with open(sys.argv[1], "rt") as f:
            lines = f.read().splitlines()
    except OSError as e:
        return print_err(f"solve: {e}", 1)

    buckets: list[Bucket] = make_buckets(lines)
    total: int = 0
    for bucket in buckets:
        total += bucket.result
    print(total)
    return 0


if __name__ == "__main__":
    main()
