from os import environ
import re
import math


def handle_item(monkey, monkeys, max_test_value, division=1):
    item = monkey["items"].pop(0)
    worry_value = int(monkey["operation"][-1]) if monkey["operation"][-1] != "old" else item
    if monkey["operation"][1] == "*":
        item *= worry_value
        item %= max_test_value
    else: 
        item += worry_value
    item = math.floor(item/division)
    if (item % monkey["test"] == 0):
        monkeys[monkey["test_true"]]["items"].append(item)
    else:
        monkeys[monkey["test_false"]]["items"].append(item)
    monkey["inspection_nr"] += 1


def solve_parts(input_data, nr_rounds, division):
    max_test_value = 1
    for monkey in input_data:
        max_test_value *= monkey["test"]
    for _ in range(nr_rounds):
        for monkey in input_data:
            while len(monkey["items"]) > 0:
                 handle_item(monkey, input_data, max_test_value, division)
    inspection_values = sorted([monkey["inspection_nr"] for monkey in input_data])
    return inspection_values[-1] * inspection_values[-2]
  

def parse_lines(filename: str):
    input_data = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(" ")
            if parts[0] == "Monkey":
                monkey = {"name": parts[1], "inspection_nr": 0}
            elif parts[0] == "":
                input_data.append(monkey)
            elif parts[0] == "Starting":
                items = re.findall(r'\d+', line)
                monkey["items"] = [int(item) for item in items]
            elif parts[0] == "Operation:":
                monkey["operation"] =  parts[3:]
            elif parts[0] == "Test:":
                monkey["test"] =  int(parts[-1])
            elif parts[1] == "true:":
                monkey["test_true"] = int(parts[-1])
            elif parts[1] == "false:":
                monkey["test_false"] = int(parts[-1])
    if monkey:
        input_data.append(monkey)
    return input_data

def main():
    input_data = parse_lines('input.txt')
    res = solve_parts(input_data, nr_rounds=20, division=3) if environ.get('part') == "part1" \
            else solve_parts(input_data, nr_rounds=10000, division=1) 
    print(f"Result: {res}")
    

if __name__ == "__main__":
    main()