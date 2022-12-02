from utils.io import read_input
from day2.part1 import move_score, round_output


def main():
    total = 0
    lines = read_input('input.txt')
    for line in lines:
        [opponent_move, desired_output] = line.strip().split(" ")
        move_to_play = move_to_obtain_desired_output(output_to_numerical(desired_output), opponent_move)
        total += (output_to_numerical(desired_output) + move_score(move_to_play))
    print(total)


def output_to_numerical(output):
    if output == "X":
        return 0
    elif output == "Y":
        return 3
    elif output == "Z":
        return 6
    return 0


def move_to_obtain_desired_output(desired_output, opponent_move):
    for move in ["X", "Y", "Z"]:
        if round_output(move, opponent_move) == desired_output:
            return move
    return ""


if __name__ == '__main__':
    main()
