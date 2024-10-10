class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        idx = self.count

        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            if parent > child:
                self.heap_list[idx], self.heap_list[self.parent_idx(idx)] = parent, child
            idx = self.parent_idx(idx)
        print(self.heap_list)

    def heapify_down(self):
        idx = 1
        while self.child_presence(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)

            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            if parent > child:
                self.heap_list[idx], self.heap_list[smaller_child_idx] = child, parent
            idx = smaller_child_idx
        print(self.heap_list)

    def retrieve_min(self):
        if self.count == 0:
            return None

        min_ = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count -= 1

        print(self.heap_list)
        self.heapify_down()
        return min_

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)

        left_child = self.heap_list[self.left_child_idx(idx)]
        right_child = self.heap_list[self.right_child_idx(idx)]

        if left_child < right_child:
            return self.left_child_idx(idx)
        else:
            return self.right_child_idx(idx)

    # Auxiliar functions
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_presence(self, idx):
        return self.left_child_idx(idx) <= self.count


if __name__ == '__main__':
    from random import randrange

    heap = MinHeap()

    random_nums = [randrange(1, 101) for _ in range(6)]

    for el in random_nums:
        heap.add(el)

    print(heap.retrieve_min())
    print(heap.heap_list)

    print("Retrieving min")
    while len(heap.heap_list) != 1:
        heap.retrieve_min()
