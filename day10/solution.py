from os import environ

def solve_part2(input_data):
    cycle_values = get_cycles(input_data)
    draw = ""
    res = []
    curr_draw_x = 1
    for x in cycle_values:
        draw += "#" if x <= curr_draw_x <= x + 2 else "."
        curr_draw_x += 1
        if curr_draw_x == 41:
            res.append(draw)
            draw = ""
            curr_draw_x = 1
    for line in res:
        print(line)

    
def solve_part1(input_data):
    cycle_values = get_cycles(input_data)
    return sum([cycle_values[cycle-1] * cycle for cycle in [20, 60, 100, 140, 180, 220]])


def get_cycles(input_data):
    cycles = []
    x = 1
    for line in input_data:
        command = line.split(" ")
        cycles.append(x)
        if len(command) == 2:
            cycles.append(x)
            added_value = int(command[1])  
            x += added_value
    return cycles


def parse_input(filename):
    with open(filename) as f:
        input_data = f.read().split("\n")
    return input_data


def main():
    input_data = parse_input('input.txt')
    res = solve_part1(input_data) if environ.get('part') == 'part1' else solve_part2(input_data)
    print(f"Result: {res}")


if __name__ == "__main__":
    main()