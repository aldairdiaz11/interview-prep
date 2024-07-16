class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    @property
    def link_node(self):
        return self._link_node

    @link_node.setter
    def link_node(self, value):
        self._link_node = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


if __name__ == '__main__':
    # Add your code below:
    yacko = Node("likes to yak")
    wacko = Node("has a penchant for hoarding snacks")
    dot = Node("enjoys spending time in movie lots")

    yacko.link_node = dot
    dot.link_node = wacko

    dots_data = yacko.link_node.value
    wackos_data = dot.link_node.value

    print(dots_data)
    print(wackos_data)
