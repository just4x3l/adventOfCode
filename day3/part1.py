from utils.io import read_input


def main():
    total = 0
    lines = read_input('input.txt')
    for line in lines:
        [first_compartment, second_compartment] = [line.strip()[:len(line)//2], line.strip()[(len(line)//2):]]
        total += get_priority(find_common_item(first_compartment, second_compartment))
    print(total)


def get_priority(item):
    return ord(item) - 96 if ord(item) >= 97 else ord(item) - 38


def find_common_item(first_compartment, second_compartment):
    return ''.join(set(first_compartment).intersection(second_compartment))


if __name__ == '__main__':
    main()
