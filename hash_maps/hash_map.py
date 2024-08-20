class HashMap:
    def __init__(self, array_size: int):
        self.array_size = array_size
        self.array: list[list] | list[None] = [None] * self.array_size

    def hash(self, key, count_collisions=0):
        """Takes a key and returns the hash value of the key."""
        key_bytes = key.encode()
        return sum(key_bytes) + count_collisions

    def compressor(self, hash_code):
        """Takes a hash code and returns the compressed hash code."""
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        try:
            current_array_value = self.array[array_index]
            if current_array_value is None:
                self.array[array_index] = [key, value]
                return
            if current_array_value[0] == key:
                self.array[array_index] = [key, value]
            # Handling collisions
            number_collisions = 1
            while current_array_value[0] != key:
                new_hash_code = self.hash(key, number_collisions)
                new_array_index = self.compressor(new_hash_code)
                current_array_value = self.array[new_array_index]
                if current_array_value is None:
                    self.array[new_array_index] = [key, value]
                    return
                if current_array_value[0] == key:
                    self.array[new_array_index] = [key, value]
                    return
                number_collisions += 1
        except TypeError:
            self.array[array_index] = [key, value]

    def retrieve(self, key):
        possible_return_value = self.array[self.compressor(self.hash(key))]
        if possible_return_value is None:
            return
        if possible_return_value[0] == key:
            return possible_return_value[1]
        retrieval_collisions = 1
        while possible_return_value[0] != key:
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]
            if possible_return_value[0] == key:
                return possible_return_value[1]
            elif possible_return_value is None:
                return
            retrieval_collisions += 1


# ################### Tests
hash_map = HashMap(15)  # We want to use this has map to store geologic information - types of rocks

hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")

print((hash_map.retrieve("gabbro")))
print((hash_map.retrieve("sandstone")))
print((hash_map.retrieve("gneiss")))  # prints 'metamorphic' in terminal
