# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.load_factor = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xFFFFFFFF

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if self.load_factor > .7:
            self.resize(True)
        elif self.load_factor < .2:
            self.resize(False)

        new_node = LinkedPair(key, value)
        index = self._hash_mod(key)
        if self.storage[index] == None:
            self.storage[index] = new_node
        elif self.storage[index].key == key:
            self.storage[index].value = value
        else:
            self.insert_next(self.storage[index], new_node)

        self.load_factor = self.count_each_row() / self.capacity

    def insert_next(self, node, value):
        if node.next == None:
            node.next = value
        elif node.next.key == value.key:
            node.next.value = value.value
        else:
            return self.insert_next(node.next, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        if node != None:
            check = None
            while node:
                if node.key == key:
                    if check:
                        check.next = node.next
                    else:
                        self.storage[index] = node.next
                check = node
                node = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        return self.find_match(self.storage[index], key)

    def find_match(self, node, key):
        if node == None or node.key == key:
            return node.value if node != None else node
        else:
            return self.find_match(node.next, key)

    def resize(self, big=True):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2 if big else self.capacity // 2
        old = [node for node in self.storage if node != None]
        self.storage = [None] * self.capacity
        for node in old:
            self.re_insert(node)

    def re_insert(self, node):
        self.insert(node.key, node.value)
        if node.next:
            self.re_insert(node.next)

    def count_each_row(self, print_on=False):
        load = 0
        for row in self.storage:
            if row is not None:
                count = self.count_row(row, print_on)
                load += count
        return load

    def count_row(self, node, print_on=False, count=0):
        if print_on:
            print(node.value)
        count += 1
        if node.next is not None:
            return self.count_row(node.next, print_on, count)
        return count


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("line_4", "4")
    ht.insert("line_5", "5")
    ht.insert("line_6", "6")
    ht.insert("line_7", "7")
    ht.insert("line_8", "8")
    ht.insert("line_9", "9")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
