class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(item)
    def denqueue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)