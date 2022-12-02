from os import environ

CONVERT_MOVE = {"X": "A", "Y": "B", "Z": "C"}
WINNING_PAIRS = {"A": "B", "B": "C", "C": "A" }
MOVE_POINT = {"A": 1, "B": 2, "C": 3}
GAME_POINT = {"win": 6, "draw": 3, "lose": 0}

def get_losing_move(move):
    for lose, win in WINNING_PAIRS.items():
        if win == move:
            return lose

def solve_part2(input_data):
    score = 0
    for opponent, me in input_data:
        if me == "Z":
            move = WINNING_PAIRS[opponent]
            score += MOVE_POINT[move]
            score += GAME_POINT["win"]
        elif me == "Y":
            score += MOVE_POINT[opponent]
            score += GAME_POINT["draw"]
        else:
            move = get_losing_move(opponent)
            score += MOVE_POINT[move]
            score += GAME_POINT["lose"]
    return score

    
def solve_part1(input_data):
    score = 0
    for opponent, me in input_data:
        move = CONVERT_MOVE[me]
        if WINNING_PAIRS[opponent] == move:
            score += MOVE_POINT[move]
            score += GAME_POINT["win"]
        elif opponent == move:
            score += MOVE_POINT[move]
            score += GAME_POINT["draw"]
        else:
            score += MOVE_POINT[move]
            score += GAME_POINT["lose"]
    return score
  

def parse_input(filename: str):
    input_data = []
    with open(filename) as f:
        for line in f:
            input_data.append(line.strip().upper().split())
    return input_data


def main():
    part = environ.get('part')
    input_data = parse_input('input.txt')
    if part == 'part1':
        print(solve_part1(input_data))
    else:
        print(solve_part2(input_data))
    

if __name__ == "__main__":
    main()