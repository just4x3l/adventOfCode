from utils.io import read_input
from day6.part1 import CharacterMemory


def main():
    input_string = read_input('input.txt')[0].strip()
    character_memory = CharacterMemory(14)
    for i in range(len(input_string)):
        character = input_string[i]
        if character_memory.marker_in_memory():
            return print(i)
        character_memory.add_character(character)


if __name__ == '__main__':
    main()
