INITIAL_SIZE = 50


class HashTable:

    # Space-Time complexity is O(1).
    def __init__(self):
        self.capacity = INITIAL_SIZE
        self.hashKeys = []
        self.size = 0
        self.map = [None] * self.capacity

    # Create hash key.
    # Space-Time complexity is O(n) because loop is present.
    # and key is not a constant.
    def _get_hash(self, key):
        hash_sum = 0
        for index, char in enumerate(key):
            hash_sum += (index + len(key)) ** ord(char)
            hash_sum = hash_sum % self.capacity
        return hash_sum

    # Insert key-Value pair into the hash table or update if key is present.
    # Worst Case is O(n) and this happens when a key is present.
    # Best Case is o(1) when there is not duplicated key.
    def insert(self, key, value):
        # Use the key to find the index
        key_hash = self._get_hash(key)
        key_value = [key, value]
        self.hashKeys.append(key)

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            self.size += 1
            return True
        else:
            # When the key is already present, update the value
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            self.size += 1
            return True

    # Get the values from the hash table by
    # Time-Complexity is O(n)
    def find(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Remove value from the table
    # Time-Complexity is O(n)
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                self.size -= 1
                return True

    # Will help iterate over the keys of the hash map.
    def keys(self):
        return self.hashKeys

    # Helpful for testing the data structure
    def print(self):
        print('--- Hash Table ---')
        for item in self.map:
            if item is not None:
                print(str(item))
