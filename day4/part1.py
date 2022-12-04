from utils.io import read_input


def main():
    amount = 0
    lines = read_input('input.txt')
    for line in lines:
        [first_elf_range, second_elf_range] = line.strip().split(",")
        [first_elf_start, first_elf_end] = map(lambda e: int(e), first_elf_range.split("-"))
        [second_elf_start, second_elf_end] = map(lambda e: int(e), second_elf_range.split("-"))
        if overlap(first_elf_start, first_elf_end, second_elf_start, second_elf_end):
            amount += 1
    print(amount)


def overlap(start1, end1, start2, end2):
    return max(start1, start2) <= min(end1, end2)


if __name__ == '__main__':
    main()
