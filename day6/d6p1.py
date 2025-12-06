import sys

class Bucket:
    multiplication: int
    addition: int

    def __init__(self, n: int) -> None:
        self.multiplication = n
        self.addition = n

    def add_number(self, n: int) -> None:
        self.multiplication *= n
        self.addition += n


def solve(filename: str) -> int:
    with open(filename, "rt") as f:
        lines = f.read().splitlines()
    if len(lines) < 3:
        raise RuntimeError("Not enough lines for operation")
    buckets: list[Bucket] = []

    for token in lines[0].split():
        buckets.append(Bucket(int(token)))

    for line in lines[1:-1]:
        bucket_idx: int = 0
        for token in line.split():
            if bucket_idx >= len(buckets):
                raise RuntimeError("Not enough buckets!")
            buckets[bucket_idx].add_number(int(token))
            bucket_idx += 1

    solution: int = 0
    bucket_idx = 0
    for token in lines[-1].split():
        if bucket_idx >= len(buckets):
            raise RuntimeError("Not enough buckets!")
        if token == "+":
            solution += buckets[bucket_idx].addition
        elif token == "*":
            solution += buckets[bucket_idx].multiplication
        else:
            raise RuntimeError("Invalid operator!")
        bucket_idx += 1
    return solution


def print_err(msg: str, retval: int) -> int:
    print("Error:", msg, file=sys.stderr)
    return retval


def main() -> int:
    if len(sys.argv) != 2:
        return print_err(f"Usage: {sys.argv[0]} <filename>", 2)
    try:
        solution: int = solve(sys.argv[1])
    except OSError as e:
        return print_err(f"solve: {e}", 1)
    except RuntimeError as e:
        return print_err(f"solve: {e}", 1)
    print(solution)
    return 0


if __name__ == "__main__":
    main()
