class HashMap:
    def __init__(self, array_size: int):
        self.array_size = array_size
        self.array: list[list] | list[None] = [None] * self.array_size

    def hash(self, key):
        """Takes a key and returns the hash value of the key."""
        key_bytes = key.encode()
        return sum(key_bytes)

    def compressor(self, hash_code):
        """Takes a hash code and returns the compressed hash code."""
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        try:
            current_array_value = self.array[array_index]  # Handling collisions
            if current_array_value[0] == key:
                self.array[array_index] = [key, value]
        except TypeError:
            self.array[array_index] = [key, value]

    def retrieve(self, key):
        return self.array[self.compressor(self.hash(key))]


# ################### Tests
hash_map = HashMap(20)  # We want to use this has map to store geologic information - types of rocks
hash_map.assign("gneiss", "metamorphic")
print((hash_map.retrieve("gneiss")))  # prints 'metamorphic' in terminal
