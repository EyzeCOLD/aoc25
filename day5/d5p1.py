import sys


def print_err(msg: str, ret: int) -> int:
    print("Error:", msg, file=sys.stderr)
    return ret


def read_file(filename: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges: list[tuple[int, int]] = []
    ids: list[int] = []

    with open(filename, "rt") as f:
        lines = f.read().splitlines()

    it = iter(lines)

    for line in it:
        if line == "":
            break
        limits = line.split('-')
        start = int(limits[0])
        end = int(limits[1])
        if end < start:
            raise RuntimeError("Invalid range")
        ranges.append((start, end))

    for line in it:
        ids.append(int(line))

    return ranges, ids


def merge_overlapping(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_ranges: list[tuple[int, int]] = sorted(ranges, key=lambda r: r[0])
    merged: list[tuple[int, int]] = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        prev_start, prev_end = merged[-1]
        if start <= prev_end:
            merged[-1] = prev_start, max(prev_end, end)
        else:
            merged.append((start, end))

    return merged


def ids_in_range(ids: list[int], ranges: list[tuple[int, int]]) -> int:
    ret: int = 0
    for i in ids:
        for r in ranges:
            if (i >= r[0] and i <= r[1]):
                ret += 1
                break
    return ret


def main() -> int:
    if len(sys.argv) != 2:
        return print_err(f"Usage: {sys.argv[0]} <input file>", 2)

    ranges: list[tuple[int, int]]
    ids: list[int]

    try:
        ranges, ids = read_file(sys.argv[1])
    except OSError as e:
        return print_err(f"read_file: {e}", 1)
    except RuntimeError as e:
        return print_err(f"read_file: {e}", 1)
    print(ids_in_range(ids, merge_overlapping(ranges)))

    return 0


if __name__ == "__main__":
    main()
