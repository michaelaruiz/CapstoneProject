# Michaela Ruiz #001323526
import mentalhealthsurvey


# creates hashtable

class HashTable:

    def __init__(self):
        self.size = 2500
        self.hashmap = [[] for _ in range(self.size)]
        # print(self.hashmap)
    # space time complexity O(1)
    # creates constructor

    def hashing_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key
    # creates the hash key
    # O(1)

    def insert(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if not key_exists:
            bucket.append((key, value))
    # O(N)
    # inserts the key(pid) and value into the hashtable

    def get(self, key):
        hash_key = self.hashing_func(key)
        bucket = self.hashmap[hash_key]
        for kv in bucket:
            k, v = kv
            if key == k:
                return v
        return None
    # O(N)
    # retrieves the value using the key

    def remove(self, key):
        hash_key = key

        if self.hashmap[hash_key] is None:
            return False
        for i in range(len(self.hashmap[hash_key])):
            if self.hashmap[hash_key][i][0] == key:
                self.hashmap[hash_key].pop(i)
                return True
    # space time complexity is O(N)
    # removes and returns the value from the hashtable

    def get_all_keys(self):
        result = []
        for bucket in self.hashmap:
            for item in bucket:
                result.append(item[0])
        return result
    # O(N^2)
    # retrieves all the keys

    def print(self):
        print('package')
        for m in self.hashmap:
            if m is not None:
                print(str(m))
