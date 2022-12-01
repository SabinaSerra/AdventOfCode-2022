
from os import environ

def read_input(file_name):
    input_vals = []
    with open(file_name) as f:
        curr_vals = []
        for row in f:
            row = row.strip()
            if row == '':
                input_vals.append(curr_vals)
                curr_vals = []
            else:
                curr_vals.append(int(row))
    return [sum(cals) for cals in input_vals]

def solve_part2(input_vals):
    num_vals = 3
    res = []
    for _ in range(num_vals):
        val = max(input_vals)
        res.append(val)
        input_vals.remove(val)
    return sum(res)

def main():
    part = environ.get('part')
    input_vals = read_input("input.txt")
    if part == 'part1':
        print(max(input_vals))
    else:
        print(solve_part2(input_vals))


if __name__ == "__main__":
    main()