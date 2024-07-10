class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        self._next_node = next_node

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node):
        self._prev_node = prev_node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class DoublyLinkedList:
    def __init__(self):
        self.head_node: None | Node = None
        self.tail_node: None | Node = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        if current_head is not None:
            current_head.prev_node = new_head
            new_head.next_node = current_head

        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.next_node = new_tail
            new_tail.prev_node = current_tail

        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node

        if removed_head is None:
            return None

        self.head_node = removed_head.next_node

        if self.head_node is not None:
            self.head_node.set_prev_node = None

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.value

    def remove_tail(self):
        removed_tail = self.tail_node

        if removed_tail is None:
            return None

        self.tail_node = removed_tail.prev_node

        if self.tail_node is not None:
            self.tail_node.next_node = None

        if removed_tail is self.head_node:
            self.remove_head()

        return removed_tail.value

    def remove_by_value(self, value_to_remove):
        node_to_remove: None | Node = None
        current_node = self.head_node

        while current_node is not None:
            if current_node.value == value_to_remove:
                node_to_remove = current_node
                if node_to_remove == self.head_node:
                    self.remove_head()
                elif node_to_remove == self.tail_node:
                    self.remove_tail()
                else:
                    next_node: Node = node_to_remove.next_node
                    prev_node: Node = node_to_remove.prev_node

                    next_node.prev_node = prev_node
                    prev_node.next_node = next_node
                return node_to_remove
            current_node = current_node.next_node

        if node_to_remove is None:
            return None

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.value is not None:
                string_list += str(current_node.value) + "\n"
                current_node = current_node.next_node
        return string_list


if __name__ == '__main__':
    subway = DoublyLinkedList()
    subway.add_to_head("Times Square")
    subway.add_to_head("Grand Central")
    subway.add_to_head("Central Park")

    print(subway.stringify_list())

    subway.add_to_tail("Penn Station")
    subway.add_to_tail("Wall Street")
    subway.add_to_tail("Brooklyn Bridge")

    print(subway.stringify_list())

    subway.remove_head()
    subway.remove_tail()

    print(subway.stringify_list())

    subway.remove_by_value("Times Square")

    print(subway.stringify_list())
