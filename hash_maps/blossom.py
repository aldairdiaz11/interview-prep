from linear_data_structures.linked_list import Node, LinkedList


class HashMap:
    def __init__(self, size):
        self.size: int = size
        self.array:  list[LinkedList: Node(list)] = [LinkedList()] * self.size

    def hash(self, key) -> int:
        return sum(key.encode())

    def compress(self, hash_code: int) -> int:
        return hash_code % self.size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array: LinkedList = self.array[array_index]

        for item in list_at_array:
            if item.get_value()[0] == key:
                item.set_value(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        payload: LinkedList(list) = self.array[array_index]

        # Todo: fix this implementation
        return payload.get_head_node().get_value()[1] if payload.get_head_node().get_value()[1] == key else None
