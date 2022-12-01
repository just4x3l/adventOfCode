from utils.io import read_input


def main():
    current_max = 0
    current_sum = 0
    lines = read_input('input.txt')
    for line in lines:
        if line == '\n':
            current_max = max(current_max, current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
    print(current_max)


if __name__ == '__main__':
    main()
