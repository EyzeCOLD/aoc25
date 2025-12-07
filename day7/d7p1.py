import sys

class Beam:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Beam):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Beam({self.x}, {self.y})"


def print_err(msg: str, retval: int) -> int:
    print("Error:", msg, file=sys.stderr)
    return retval


def read_file(path: str) -> list[str]:
    with open(path, "rt") as f:
        return f.read().splitlines()


def shoot_beam(grid: list[str], x: int, y: int) -> int:
    splits: int = 0
    beams: set[Beam] = {Beam(x, y)}

    while len(beams) > 0:
        new_beams: set[Beam] = set()
        for b in beams:
            if b.y + 1 < len(grid):
                if grid[b.y + 1][b.x] == "^":
                    splits += 1
                    new_beams.add(Beam(b.x - 1, b.y + 1))
                    new_beams.add(Beam(b.x + 1, b.y + 1))
                else:
                    new_beams.add(Beam(b.x, b.y + 1))
        beams = new_beams

    return splits


def main() -> int:
    if (len(sys.argv) != 2):
        return print_err(f"Usage: {sys.argv[0]} <input>", 2)
    file: list[str] = []
    try:
        file = read_file(sys.argv[1])
    except OSError as e:
        print_err(f"read_file: {e}", 1)
    print(shoot_beam(file, file[0].find("S"), 0))
    return 0


if __name__ == "__main__":
    main()
