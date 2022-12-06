from utils.io import read_input


def main():
    input_string = read_input('input.txt')[0].strip()
    character_memory = CharacterMemory(4)
    for i in range(len(input_string)):
        character = input_string[i]
        if character_memory.marker_in_memory():
            return print(i)
        character_memory.add_character(character)


class CharacterMemory:
    def __init__(self, size):
        self.characters = []
        self.size = size

    def add_character(self, character):
        if len(self.characters) == self.size:
            self.characters.pop(0)
        self.characters.append(character)

    def marker_in_memory(self):
        return len(self.characters) == self.size and len(set(self.characters)) == len(self.characters)


if __name__ == '__main__':
    main()
