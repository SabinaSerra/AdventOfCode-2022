from os import environ
from collections import namedtuple

Section = namedtuple("Section", "bottom top")

def is_overlapping_range(pair):
    sec1, sec2 = pair
    return not (sec1.top < sec2.bottom or sec1.bottom > sec2.top)

def is_within_range(pair):
    sec1, sec2 = pair
    return (sec1.bottom >= sec2.bottom and sec1.top <= sec2.top) or (sec1.bottom <= sec2.bottom and sec1.top >= sec2.top)

def solve_part2(input_data):
    return sum(map(is_overlapping_range, input_data))

def solve_part1(input_data):
    return sum(map(is_within_range, input_data))

def get_section(assignment):
    bottom, top = assignment.split("-")
    return Section(int(bottom), int(top))

def parse_input(filename):
    with open(filename) as f:
        data = f.read().split("\n")
    return [[get_section(assignment) for assignment in line.split(",")] for line in data]

def main():
    part = environ.get('part')
    input_data = parse_input('input.txt')
    res = solve_part1(input_data) if part == 'part1' else solve_part2(input_data)
    print(f"Result: {res}")
    
if __name__ == "__main__":
    main()