from utils.io import read_input


def main():
    total = 0
    lines = read_input('input.txt')
    for line in lines:
        [opponent_move, my_move] = line.strip().split(" ")
        total += (move_score(my_move) + round_output(my_move, opponent_move))
    print(total)


def move_score(move):
    if move == "X":
        return 1
    elif move == "Y":
        return 2
    elif move == "Z":
        return 3
    return 0


def round_output(my_move, opponent_move):
    if my_move == "X":
        if opponent_move == "A":
            return 3
        if opponent_move == "B":
            return 0
        if opponent_move == "C":
            return 6
    elif my_move == "Y":
        if opponent_move == "A":
            return 6
        if opponent_move == "B":
            return 3
        if opponent_move == "C":
            return 0
    elif my_move == "Z":
        if opponent_move == "A":
            return 0
        if opponent_move == "B":
            return 6
        if opponent_move == "C":
            return 3
    return 0


if __name__ == '__main__':
    main()
