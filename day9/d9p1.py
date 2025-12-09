import sys


class Tile:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Tile({self.x},{self.y})"

    def area(self, other) -> int:
        dx = abs(self.x - other.x) + 1
        dy = abs(self.y - other.y) + 1
        return dx * dy


def error(msg: str, retval: int) -> int:
    print("Error", msg, file=sys.stderr)
    return retval


def read_file(filename: str) -> list[Tile]:
    tiles: list[Tile] = []
    lines: list[str] = []
    with open(filename, "rt") as f:
        lines = f.read().splitlines()
    for l in lines:
        x = int(l.split(',')[0])
        y = int(l.split(',')[1])
        tiles.append(Tile(x, y))
    return tiles


def bsq(tiles: list[Tile]) -> int:
    record: int = 0
    for i, tile_a in enumerate(tiles):
        for tile_b in tiles[i + 1:]:
            record = max(record, tile_a.area(tile_b))
    return record


def main() -> int:
    if (len(sys.argv) != 2):
        return error(f"Usage: {sys.argv[0]} <input>", 2)
    try:
        map = read_file(sys.argv[1])
    except OSError as e:
        return error(f"read_file: {e}", 1)
    tiles: list[Tile] = read_file(sys.argv[1])
    print(bsq(tiles))
    return 0


if (__name__ == "__main__"):
    main()
