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
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        new_node = LinkedPair(key, value)
        index = self._hash_mod(key)
        if self.storage[index] == None:
            self.storage[index] = new_node
        elif self.storage[index].key == key:
            self.storage[index].value = value
        else:
            self.insert_next_node(self.storage[index], new_node)

    def insert_next_node(self, node, value):
        if node.next == None:
            node.next = value
        elif node.next.key == value.key:
            node.next.value = value.value
        else:
            return self.insert_next_node(node.next, value)

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
        if self.storage[index] == None:
            return self.storage[index]
        elif self.storage[index].key == key:
            return self.storage[index].value
        else:
            return self.find_match(self.storage[index].next, key)

    def find_match(self, node, key):
        if node == None or node.key == key:
            return node.value if node != None else node
        else:
            return self.find_match(node.next, key)

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        self.capacity *= 2
        old = [node for node in self.storage if node != None]
        self.storage = [None] * self.capacity
        for node in old:
            def insert_next(node):
                self.insert(node.key, node.value)
                if node.next:
                    insert_next(node.next)
            insert_next(node)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

    for node in ht.storage:
        print(node.value if node != None else node)
