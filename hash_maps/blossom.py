class HashMap:
    def __init__(self, size):
        self.size = size
        self.array: list[None] | list[int] = [None] * size

    def hash(self, key) -> int:
        return sum(key.encode())

    def compress(self, hash_code: int) -> int:
        return hash_code % self.size

    def assign(self):
        pass

    def retrieve(self, key):
        pass
