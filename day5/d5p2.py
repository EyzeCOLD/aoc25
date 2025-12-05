import sys


def print_err(msg: str, ret: int) -> int:
    print("Error:", msg, file=sys.stderr)
    return ret


def read_file(filename: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []

    with open(filename, "rt") as f:
        lines = f.read().splitlines()

    for line in lines:
        if line == "":
            break
        limits = line.split('-')
        start = int(limits[0])
        end = int(limits[1])
        if end < start:
            raise RuntimeError("Invalid range")
        ranges.append((start, end))

    return ranges


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


def main() -> int:
    if len(sys.argv) != 2:
        return print_err(f"Usage: {sys.argv[0]} <input file>", 2)

    ranges: list[tuple[int, int]]

    try:
        ranges = read_file(sys.argv[1])
    except OSError as e:
        return print_err(f"read_file: {e}", 1)
    except RuntimeError as e:
        return print_err(f"read_file: {e}", 1)
    merged = merge_overlapping(ranges)
    total_fresh_ids = 0
    for r in merged:
        total_fresh_ids += abs(r[0] - r[1]) + 1
    print(total_fresh_ids)

    return 0


if __name__ == "__main__":
    main()
