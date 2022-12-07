from os import environ
from collections import defaultdict

COMMAND = "$"
MOVE = "cd"
SHOW = "ls"
DIR = "dir"
HOME = "/"
UP = ".."

def solve_part2(input_data):
    dirs = get_dir_sizes(input_data)
    needed_size = 30000000
    tot_size = 70000000
    size_to_free = needed_size - (tot_size - dirs["/"]) 
    smallest_size = tot_size
    smallest_dir = ""
    for dir, size in dirs.items():
        if size_to_free < size < smallest_size:
            smallest_dir = dir
            smallest_size = size
    return smallest_dir, smallest_size

def get_dir_sizes(input_data):
    dirs = defaultdict(lambda: 0)
    for file, size in input_data.items():
        parts = file.split("/")
        part = ""
        for i in range(len(parts)-1):
            part += parts[i] + "/"
            dirs[part] += int(size)
    return dirs
    
def solve_part1(input_data):
    dirs = get_dir_sizes(input_data)
    res = []
    res_size = 0
    for dir, size in dirs.items():
        if size <= 100000:
            res_size += size
            res.append(dir)
    return res_size


def parse_input(filename):
    with open(filename) as f:
        input_data = f.read().split("\n")
    curr_dir = ""
    data = {}
    for line_nr in range(len(input_data)):
        line = input_data[line_nr]
        values = line.split(" ")
        if values[0] == COMMAND:
            if values[1] == MOVE:
                if values[2] == HOME:
                    curr_dir == "/"
                elif values[2] == UP:
                    curr_dir = "/".join(curr_dir.split("/")[:-1])
                else:
                    curr_dir +=  f"/{values[2]}"
            elif values[1] == SHOW:
                pass
        elif values[0] == DIR:
            pass
        else:
            data[f"{curr_dir}/{values[1]}"] = values[0]
    return data

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