from linear_data_structures.linked_list import LinkedList, Node


class HashMap:
    def __init__(self, size):
        self.size: int = size
        self.array = [LinkedList() for _ in range(self.size)]

    def hash(self, key) -> int:
        return sum(key.encode())

    def compress(self, hash_code: int) -> int:
        return hash_code % self.size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for element in list_at_array:
            try:
                if element.get_value()[0] == key:
                    element.get_value()[1] = value
            except AttributeError:
                continue

        list_at_array.insert_beginning(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))

        list_at_index = self.array[array_index]
        for element in list_at_index:
            try:
                if element.get_value()[0] == key:
                    return element.get_value()[1]
            except AttributeError:
                continue
        return


if __name__ == '__main__':
    # Tests
    flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'],
                          ['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'],
                          ['magnolia', 'dignity'], ['morning glory', 'unrequited love'],
                          ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'],
                          ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]

    blossom = HashMap(len(flower_definitions))

    for flower_def in flower_definitions:
        blossom.assign(flower_def[0], flower_def[1])

    print(blossom.retrieve('daisy'))
    blossom.assign('begonia', 'new value')
    print(blossom.retrieve(key='begonia'))
