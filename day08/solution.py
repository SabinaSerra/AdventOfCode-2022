from os import environ
import time
from collections import namedtuple

Position = namedtuple("Position", "row col")

def solve_part2(input_data):
    max_score = 0
    for row_nr in range(len(input_data)):
        for col_nr in range(len(input_data[0])):
            score = get_score(Position(row=row_nr, col=col_nr), input_data)
            if score > max_score:
                max_score = score
    return max_score

def is_visible(position, input_data):
    tree_height = input_data[position.row][position.col]
    if all(input_data[row][position.col] < tree_height for row in range(position.row + 1, len(input_data))):
        return True
    if all(input_data[row][position.col] < tree_height for row in range(0, position.row)):
        return True
    if all(input_data[position.row][col] < tree_height for col in range(position.col)):
        return True
    if all(input_data[position.row][col] < tree_height for col in range(position.col+1, len(input_data[0]))):
        return True
    return False

def get_score_in_direction(trees, tree_height):
    counter = 0
    for tree in trees:
        counter += 1
        if tree >= tree_height:
            return counter  
    return counter

def get_score(position, input_data):
    tree_height = input_data[position.row][position.col]
    counter = 1
    up = [input_data[row][position.col] for row in range(position.row + 1, len(input_data))]
    counter *= get_score_in_direction(up, tree_height)
    down = reversed([input_data[row][position.col] for row in range(position.row)])
    counter *= get_score_in_direction(down, tree_height)    
    left = reversed([input_data[position.row][col] for col in range(position.col)])
    counter *= get_score_in_direction(left, tree_height)  
    right = [input_data[position.row][col] for col in range(position.col+1, len(input_data[0]))]
    counter *= get_score_in_direction(right, tree_height) 
    return counter

    
def solve_part1(input_data):
    counter = 0
    for row_nr in range(len(input_data)):
        for col_nr in range(len(input_data[0])):
            if is_visible(Position(row=row_nr, col=col_nr), input_data):
                counter += 1
    return counter
  
def parse_input(filename):
    with open(filename) as f:
        input_data = f.read().split("\n")
    input_data = [[int(col) for col in row] for row in input_data]
    return input_data

def main():
    part = environ.get('part')
    start = time.time()
    input_data = parse_input('input.txt')
    if part == 'part1':
        res = solve_part1(input_data)
    else:
        res = solve_part2(input_data)
    end = time.time()
    print(f"Result: {res}")
    print(f"Time: {round((end - start)*1000, 4)}ms")
    

if __name__ == "__main__":
    main()