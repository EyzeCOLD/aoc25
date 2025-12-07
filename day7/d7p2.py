import sys

class Beam:
    x: int
    y: int
    value: int

    def __init__(self, x: int, y: int, value: int = 1):
        self.x = x
        self.y = y
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Beam):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Beam({self.x},{self.y})"


def print_err(msg: str, retval: int) -> int:
    print("Error:", msg, file=sys.stderr)
    return retval


def read_file(path: str) -> list[str]:
    with open(path, "rt") as f:
        return f.read().splitlines()


def add_beam(beam: Beam, beams: set[Beam]) -> None:
    new_beam = Beam(beam.x, beam.y, beam.value)
    for b in beams:
        if b == new_beam:
            new_beam.value += b.value
            beams.remove(b)
            break
    beams.add(new_beam)


def shoot_beam(grid: list[str], x: int) -> set[Beam]:
    y: int = 1
    beams: set[Beam] = {Beam(x, y)}

    while True:
        new_beams: set[Beam] = set()
        for b in beams:
            if grid[y][b.x] == "^":
                add_beam(Beam(b.x - 1, y, b.value), new_beams)
                add_beam(Beam(b.x + 1, y, b.value), new_beams)
            else:
                add_beam(Beam(b.x, y, b.value), new_beams)
        beams = new_beams
        y += 1
        if y >= len(grid):
            return new_beams


def main() -> int:
    if (len(sys.argv) != 2):
        return print_err(f"Usage: {sys.argv[0]} <input>", 2)
    file: list[str] = []
    try:
        file = read_file(sys.argv[1])
    except OSError as e:
        print_err(f"read_file: {e}", 1)
    beams: set[Beam] = shoot_beam(file, file[0].find("S"))
    solution: int = 0
    for b in beams:
        solution += b.value
    print(solution)
    return 0


if __name__ == "__main__":
    main()
