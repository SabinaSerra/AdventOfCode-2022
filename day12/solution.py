from os import environ

from queue import PriorityQueue
from collections import namedtuple

Position = namedtuple("Position", "row col")

DIRECTIONS = [Position(1, 0), Position(-1, 0), Position(0, 1), Position(0, -1)]


def solve_part2(end, grid):
    unvisited = PriorityQueue()
    visited = {end: "E"}
    curr_elevation = ord("z") - ord("a")
    curr_pos, curr_prio = (end, 0)
    while curr_elevation != 0:
        next_pos = Position(curr_pos.row - 1, curr_pos.col)
        for direction in DIRECTIONS:
            next_pos = Position(curr_pos.row + direction.row, curr_pos.col + direction.col)
            if valid_step(next_pos, grid, visited) and grid[next_pos.row][next_pos.col] >= (curr_elevation - 1):
                unvisited.put((curr_prio + 1, next_pos)) 
                visited[next_pos] = curr_pos
        curr_prio, curr_pos = unvisited.get()
        curr_elevation = grid[curr_pos.row][curr_pos.col]
    path = get_path(curr_pos, end, visited)
    return len(path) - 1

def get_path(start, end, visited):
    curr_pos = start
    path = [curr_pos]
    while curr_pos != end:
        next_pos = visited[curr_pos]
        curr_pos = next_pos
        path.append(curr_pos)
    return path

def valid_step(next_pos, grid, visited):
    return ((0 <= next_pos.row < len(grid)) and (0 <= next_pos.col < len(grid[0])) and next_pos not in visited)
    
def solve_part1(start, end, grid):
    unvisited = PriorityQueue()
    visited = {start: "S"}
    curr_pos, curr_prio = (start, 0)
    while curr_pos != end:
        curr_elevation = grid[curr_pos.row][curr_pos.col]
        for direction in DIRECTIONS:
            next_pos = Position(curr_pos.row + direction.row, curr_pos.col + direction.col)
            if valid_step(next_pos, grid, visited) and grid[next_pos.row][next_pos.col] <= (curr_elevation + 1):
                unvisited.put((curr_prio + 1, next_pos)) 
                visited[next_pos] = curr_pos
        curr_prio, curr_pos = unvisited.get()
    return len(get_path(end, start, visited)) - 1


def parse_input(filename):
    with open(filename) as f:
        input_data = f.read().split("\n")
    start = Position(0, 0)
    end = Position(0, 0)
    grid = []
    for row_nr in range(len(input_data)):
        grid.append([])
        row = input_data[row_nr]
        for col_nr in range(len(row)):
            elevation = row[col_nr]
            if elevation == "S":
                elevation = "a"
                start = Position(row_nr, col_nr)
            elif elevation == "E":
                elevation = "z"
                end = Position(row_nr, col_nr)
            grid[-1].append(ord(elevation) - ord("a"))
    return (start, end, grid)

def main():
    part = environ.get('part')
    start, end, grid = parse_input('input.txt')
    if part == 'part1':
        res = solve_part1(start, end, grid)
    else:
        res = solve_part2(end, grid)
    print(f"Result: {res}")
    

if __name__ == "__main__":
    main()