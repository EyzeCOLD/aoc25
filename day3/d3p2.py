import sys


def print_error(message: str) -> None:
    print("Error:", message, file=sys.stderr)


def load_banks_from_file(filename: str) -> list[str]:
    file = open(filename, "rt")
    banks = file.read().splitlines()
    file.close()
    return banks


def solve(banks: list[str], batteries_required: int) -> int:
    sum = 0
    for bank in banks:
        if (len(bank) < batteries_required):
            raise RuntimeError("Bank doesn't have enough batteries")
        sum += int(solve_bank(bank, batteries_required))
    return sum


def solve_bank(bank: str, batteries_required: int) -> str:
    if (len(bank) == 1):
        return (bank[0])
    if (batteries_required == 1):
        return max(bank)
    # Search for the biggest in the bank, but always leave atleast the amount
    # of batteries you still need at the end of the string
    sum = max(bank[:-(batteries_required - 1)])
    sub_bank = bank[bank.index(sum) + 1:]
    if (len(sub_bank) != 0):
        sum += solve_bank(sub_bank, batteries_required - 1)
    return sum


def main() -> int:
    if (len(sys.argv) != 2):
        print("Usage:", {sys.argv[0]}, "<filename>")
        return 2
    try:
        banks = load_banks_from_file(sys.argv[1])
    except OSError as e:
        print_error(f"load_banks_from_file: {e}")
        return 1
    try:
        solution = solve(banks, 12)
    except RuntimeError as e:
        print_error(f"solve: {e}")
        return 1
    print(solution)
    return 0


if __name__ == "__main__":
    main()
