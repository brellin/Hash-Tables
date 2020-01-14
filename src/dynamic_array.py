class DynamicArray:

    def __init__(self, capacity=0):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            self.resize()
        for i in range(self.count, index):
            self.storage[i] = self.storage[i - 1]
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def resize(self):
        if self.capacity == 0:
            self.capacity = 1
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

    def replace(self, index, value):
        self.storage[index] = value

    def unshift(self, value):
        self.insert(0, value)

    def slice(self, index1, index2):
        if index1 == None:
            index1 = 0
        if index2 == None:
            index2 = self.count
        subarr = [None] * (index2 - index1)
        while index1 < index2:
            subarr[index1] = self.storage[index1]
            index1 += 1
        return subarr


arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)

print(arr.slice(0, 2))
