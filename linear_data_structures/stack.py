from nodes import Node


class Stack:
    def __init__(self, name, max_size=1000):
        self.top_item: None | Node = None
        self.size: int = 0
        self.max_size: int = max_size
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def print_items(self):
        pointer = self.top_item
        print_list = []

        while pointer:
            print_list.append(pointer.value)
            pointer = pointer.link_node

        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.link_node = self.top_item
            self.top_item = item
            self.size += 1
            print(f"{item.value} added to stack")
        else:
            print("This stack is full")

    def peek(self):
        if self.size > 0:
            return self.top_item.value
        return "Stack is empty"

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.link_node
            self.size -= 1
            return item_to_remove.value
        print("Stack is empty")
        return None

    def has_space(self):
        return self.max_size > self.size

    def is_empty(self):
        return self.size == 0


if __name__ == "__main__":
    # Defining an empty pizza stack
    pizza_stack = Stack("Test", 6)
    # Adding pizzas as they are ready until we have
    pizza_stack.push("pizza #1")
    pizza_stack.push("pizza #2")
    pizza_stack.push("pizza #3")
    pizza_stack.push("pizza #4")
    pizza_stack.push("pizza #5")
    pizza_stack.push("pizza #6")

    # Uncomment the push() statement below:
    pizza_stack.push("pizza #7")

    # Delivering pizzas from the top of the stack down
    print("The first pizza to deliver is " + pizza_stack.peek())
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()

    # Uncomment the pop() statement below:
    pizza_stack.pop()
