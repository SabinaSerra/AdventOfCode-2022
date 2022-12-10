from os import environ

class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        
    def __repr__(self) -> str:
        return f"({self.row}, {self.col})"

DELTA_MAPPING = {"U": Position(1, 0), "D": Position(-1, 0), "R": Position(0, 1), "L": Position(0, -1)}

class Knot:
    def __init__(self, pos, id):
        self.pos = pos
        self.id = id
    
    def move(self, front_knot):
        delta = Position(front_knot.pos.row - self.pos.row, front_knot.pos.col - self.pos.col)
        if delta.row == 0 and abs(delta.col) > 1:
            self.pos.col += int(delta.col / abs(delta.col))
        elif delta.col == 0 and abs(delta.row) > 1:
            self.pos.row += int(delta.row / abs(delta.row))
        elif (abs(delta.col) > 1 and abs(delta.row) >= 1) or (abs(delta.col) >= 1 and abs(delta.row) > 1):
            self.pos.row += int(delta.row / abs(delta.row))
            self.pos.col += int(delta.col / abs(delta.col))

    def __repr__(self) -> str:
        return f"({self.id}: {self.pos})"


class Rope: 
    def __init__(self, head_pos, nr_knots):
        self.head = Knot(head_pos, "H")
        self.knots = [Knot(Position(head_pos.row, head_pos.col), nr) for nr in range(1, nr_knots+1)]
        self.end = nr_knots
    
    def move(self, delta):
        self.head.pos.row += delta.row
        self.head.pos.col += delta.col
        front_knot = self.head
        for knot in self.knots:
            knot.move(front_knot)
            front_knot = knot


def draw_rope(grid, rope):
    for knot in rope.knots + [rope.head]:
        grid_pos = grid[knot.pos.row][knot.pos.col]
        if grid_pos != rope.end:
            grid[knot.pos.row][knot.pos.col] = knot.id


def solve_part(input_data, nr_knots):
    start_row = 500
    start_col = 500
    grid = [["-" for _ in range(start_col*2)] for _ in range(start_row*2)]
    grid[start_row][start_col] = "s"
    head_pos = Position(row=start_row, col=start_col)
    rope = Rope(head_pos, nr_knots=nr_knots)
    for direction, steps in input_data:
        delta = DELTA_MAPPING[direction]
        for _ in range(steps):
            rope.move(delta)
            draw_rope(grid, rope)
    count = sum([row.count(rope.end) for row in grid])
    return count


def parse_input(filename):
    with open(filename) as f:
        input_data = f.read().split("\n")
    return [(line.split(" ")[0], int(line.split(" ")[1])) for line in input_data]


def main():
    nr_knots = 1 if environ.get('part') == "part1" else 9
    input_data = parse_input('input.txt')
    res = solve_part(input_data, nr_knots)
    print(f"Result: {res}")
    

if __name__ == "__main__":
    main()