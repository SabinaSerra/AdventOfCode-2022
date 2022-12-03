from os import environ


def calc_priority(packages):
    return sum([1 + ord(package) - ord("a") if package.islower() else 27 + ord(package) - ord("A")
                for package in packages])

def solve_part2(input_data):
    badges = []
    for p1, p2, p3 in input_data:
        for package in p1:
            if package in p2 and package in p3:
                badges.append(package)
    return calc_priority(badges)
    

def solve_part1(input_data):
    wrong_package = []
    for comp1, comp2 in input_data:
        for package in comp1:
            if package in comp2:
                wrong_package.append(package)
    return calc_priority(wrong_package)
  

def parse_input(filename: str):
    input_data = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            middle = int(len(line)/2)
            input_data.append((set(line[:middle]), set(line[middle:])))
    return input_data


def parse_input_part2(filename: str):
    input_data = []
    with open(filename) as f:
        data = f.read().split("\n")
    for line_nr in range(0, len(data), 3):
        input_data.append([set(data[line_nr]), set(data[line_nr + 1]), set(data[line_nr + 2])])
    return input_data


def main():
    part = environ.get('part')
    if part == 'part1':
        input_data = parse_input('input.txt')
        res = solve_part1(input_data)
    else:
        input_data = parse_input_part2('input.txt')
        res = solve_part2(input_data)
    print(f"Result: {res}")
    

if __name__ == "__main__":
    main()