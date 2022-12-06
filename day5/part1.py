from utils.io import read_input


def main():
    lines = read_input('input.txt')
    stacks = create_stack(lines, 8, 9)
    for line in lines[10:]:
        [_, amount, _, from_stack, _, to_stack] = line.strip().split(" ")
        move_items(stacks, int(from_stack) - 1, int(to_stack) - 1, int(amount))
    result = ""
    for stack in stacks:
        result += stack[-1]
    print(result)


def create_stack(lines, max_height, amount):
    stacks = [[], [], [], [], [], [], [], [], []]
    for i in range(max_height-1, -1, -1):
        line = lines[i]
        counter = 0
        for j in range(1, amount * 4 - 2, 4):
            if line[j] != ' ':
                stacks[counter].append(line[j])
            counter += 1
    return stacks


def move_items(stacks, from_stack, to_stack, amount):
    if amount < 1:
        return
    item = stacks[from_stack].pop()
    stacks[to_stack].append(item)
    move_items(stacks, from_stack, to_stack, amount-1)


if __name__ == '__main__':
    main()
