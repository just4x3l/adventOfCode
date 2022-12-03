from utils.io import read_input
from day3.part1 import get_priority


def main():
    total = 0
    lines = read_input('input.txt')
    while len(lines) >= 2:
        [first_bag, second_bag, third_bag] = [lines.pop(0).strip(), lines.pop(0).strip(), lines.pop(0).strip()]
        total += get_priority(find_common_item(first_bag, second_bag, third_bag))
    print(total)


def find_common_item(first_bag, second_bag, third_bag):
    return ''.join(set(first_bag).intersection(second_bag).intersection(third_bag))


if __name__ == '__main__':
    main()
