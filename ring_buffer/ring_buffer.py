class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.counter = 0
        self.capacity = capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.counter] = item
        self.counter = self.counter + 1
        if self.counter >= self.capacity:
            self.counter = 0

    def get(self):
        return self.storage