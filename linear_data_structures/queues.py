from nodes import Node


class Queue:
    def __init__(self, max_size=0):
        self.head: None | Node = None
        self.tail: None | Node = None
        self.max_size: int = max_size
        self.size: int = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def peek(self):
        if self.size > 0:
            return self.head.value
        else:
            return 'Queue is empty'

    def has_space(self):
        if self.max_size == 0:
            return True
        else:
            return self.size < self.max_size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            if self.is_empty():
                self.head, self.tail = item_to_add, item_to_add
            else:
                self.tail.link_node = item_to_add
                self.tail = item_to_add
            self.size += 1
        else:
            print('Queue is full')

    def dequeue(self):
        if self.size > 0:
            item_to_remove = self.head
            if self.size == 1:
                self.head, self.tail = None, None
            else:
                self.tail.link_node = item_to_remove
            self.size -= 1
            return item_to_remove.value
        print('Queue is empty')

    def stringify_list(self):
        string_list = ""
        current_node = self.head
        while current_node:
            if current_node.value is not None:
                string_list += str(current_node.value) + "\n"
            current_node = current_node.link_node
        return string_list


if __name__ == '__main__':
    print("Creating a deli line with up to 10 orders...\n------------")
    deli_line = Queue(10)
    print("Adding orders to our deli line...\n------------")
    deli_line.enqueue("egg and cheese on a roll")
    deli_line.enqueue("bacon, egg, and cheese on a roll")
    deli_line.enqueue("toasted sesame bagel with butter and jelly")
    deli_line.enqueue("toasted roll with butter")
    deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
    deli_line.enqueue("two fried eggs with home fries and ketchup")
    deli_line.enqueue("egg and cheese on a roll with jalapenos")
    deli_line.enqueue("plain bagel with plain cream cheese")
    deli_line.enqueue("blueberry muffin toasted with butter")
    deli_line.enqueue("bacon, egg, and cheese on a roll")

    # ------------------------ #
    # Uncomment the line below:
    deli_line.enqueue("western omelet with home fries")
    # ------------------------ #
    print(deli_line.stringify_list())

    print("------------\nOur first order will be " + deli_line.peek())
    print("------------\nNow serving...\n------------")
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    # ------------------------ #
    # Uncomment the line below:
    deli_line.dequeue()
    # ------------------------ #
    print(deli_line.stringify_list())
