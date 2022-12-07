from os import environ
from collections import defaultdict

COMMAND = "$"
MOVE = "cd"
SHOW = "ls"
DIR = "dir"
HOME = "/"
UP = ".."

def solve_part2(input_data):
    needed_size = 30000000
    tot_size = 70000000
    size_to_free = needed_size - (tot_size - input_data[""]) 
    smallest_size = tot_size
    for size in input_data.values():
        if size_to_free < size < smallest_size:
            smallest_size = size
    return smallest_size

 
def solve_part1(input_data):
    res_size = 0
    for size in input_data.values():
        if size <= 100000:
            res_size += size
    return res_size

def move(curr_dir, move_to):
    if move_to == HOME:
        return ""
    elif move_to == UP:
        return curr_dir.rsplit("/", 1)[0]
    else: 
        return f"{curr_dir}/{move_to}"


def add_file_size(path, file_size, dir_sizes):
    dir_sizes[f"{path}"] += file_size
    if path:
        add_file_size(path.rsplit("/", 1)[0], file_size, dir_sizes)


def parse_input(filename):
    with open(filename) as f:
        input_data = f.read().split("\n")
    curr_dir = ""
    dir_sizes = defaultdict(lambda: 0)
    for line in input_data:
        args = line.split(" ")
        if args[0] == COMMAND and args[1] == MOVE:
            curr_dir = move(curr_dir, args[2])
        elif args[0] not in [COMMAND, DIR]:
            add_file_size(curr_dir, int(args[0]), dir_sizes)
    return dir_sizes


def main():
    part = environ.get('part')
    input_data = parse_input('input.txt')
    if part == 'part1':
        res = solve_part1(input_data)
    else:
        res = solve_part2(input_data)
    print(f"Result: {res}")
    

if __name__ == "__main__":
    main()