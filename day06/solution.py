from os import environ

def solve_parts(input_data, seq_len):
    for i in range(len(input_data)):
        if len(set(input_data[i:i+seq_len])) == seq_len:
            return i+seq_len

def parse_input(filename):
    with open(filename) as f:
        input_data = f.read().strip()
    return input_data

def main():
    input_data = parse_input('input.txt')
    seq_len = 4 if environ.get('part') == "part1" else 14
    print(f"Res: {solve_parts(input_data, seq_len)}")
    
if __name__ == "__main__":
    main()