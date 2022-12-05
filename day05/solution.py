from os import environ
import queue
import re
from collections import defaultdict


def solve_parts(input_data, part="part1"):
    stacks, moves = input_data
    for move in moves: 
        nr_boxes, from_stack, to_stack = re.findall(r'\d+', move)
        nr_boxes, from_stack, to_stack = (int(nr_boxes), stacks[int(from_stack)], stacks[int(to_stack)])
        nr_moves = min(nr_boxes, from_stack.qsize())
        crates = [from_stack.get() for _ in range(nr_moves)]
        if part == "part2":
            crates = reversed(crates)
        for crate in crates:
            to_stack.put(crate)
    return "".join([stack.get() if not stack.empty() else "" for stack in stacks.values()])
  

def get_stacks(unparsed_stacks):
    num_stacks = int(unparsed_stacks[-1].split("  ")[-1])
    ind = 1
    stacks = defaultdict(queue.LifoQueue)
    for line in unparsed_stacks[-2::-1]:
        for stack_nr in range(1, num_stacks + 1):
            cargo = line[ind]
            if cargo != " ":
                stacks[stack_nr].put(cargo)
            ind += 4
        ind = 1
    return stacks


def parse_input(filename: str):
    with open(filename) as f:
        data = f.read().split("\n")
    seperator = data.index("")
    stacks = get_stacks(data[:seperator])
    moves = data[seperator + 1:]
    return (stacks, moves)


def main():
    part = environ.get('part')
    input_data = parse_input('input.txt')
    res = solve_parts(input_data, part=part)
    print(f"Result: {res}")
    

if __name__ == "__main__":
    main()