from utils.io import read_input
from day5.part1 import create_stack


def main():
    lines = read_input('input.txt')
    stacks = create_stack(lines, 8, 9)
    for line in lines[10:]:
        [_, amount, _, from_stack, _, to_stack] = line.strip().split(" ")
        move_items_bulk(stacks, int(from_stack) - 1, int(to_stack) - 1, int(amount))

    result = ""
    for stack in stacks:
        result += stack[-1]
    print(result)


def move_items_bulk(stacks, from_stack, to_stack, amount):
    items = []
    for _ in range(amount):
        item = stacks[from_stack].pop()
        items.append(item)
    items.reverse()
    stacks[to_stack] += items


if __name__ == '__main__':
    main()
