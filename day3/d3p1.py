import sys


def print_error(message: str) -> None:
    print("Error:", message, file=sys.stderr)


def load_banks_from_file(filename: str) -> list[str]:
    file = open(filename, "rt")
    banks = file.read().splitlines()
    file.close()
    return banks


def solve(banks: list[str]) -> int:
    sum = 0
    for bank in banks:
        if (len(bank) < 2):
            raise RuntimeError("Bank doesn't have enough batteries")
        first = max(bank[:-1])
        first_i = bank.index(first)
        second = max(bank[first_i + 1:])
        sum += int(first) * 10 + int(second)
    return sum


def main() -> int:
    if (len(sys.argv) != 2):
        print("Usage:", {sys.argv[0]}, "<filename>")
        return 2
    try:
        banks = load_banks_from_file(sys.argv[1])
    except OSError as e:
        print_error(e)
        return 1
    solution = solve(banks)
    print(solution)
    return 0

main()
