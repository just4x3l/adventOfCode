from utils.io import read_input


def main():

    lines = read_input('input.txt')
    for line in lines:
        print(line)


class Entity:
    def get_size(self):
        pass


class File(Entity):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


class Directory(Entity):
    def __init__(self):
        self.files = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_size(self):
        size = 0
        for entity in self.entities:
            size += entity.get_size()