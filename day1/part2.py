from utils.io import read_input


def main():
    elves_total_calories = []
    current_sum = 0
    lines = read_input('input.txt')
    for line in lines:
        if line == '\n':
            elves_total_calories.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
    elves_total_calories.sort(reverse=True)
    print(elves_total_calories[0] + elves_total_calories[1] + elves_total_calories[2])


if __name__ == '__main__':
    main()
