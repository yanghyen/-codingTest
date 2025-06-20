class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, pos, elem):
        self.items.insert(pos, elem)
    
    def delete(self, pos):
        if pos >= len(self.items): return
        else: return self.items.pop(pos)

    def isEmpty(self):
        return self.size() == 0

    def getEntry(self, pos):
        return self.items[pos]

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []

    def find(self, item):
        return self.items.index(item)
    
    def replace(self, elem, pos):
        # return self.items.replace(elem, item)
        self.items[pos] = elem

    def sort(self):
        self.items.sort()

    def merge(self, lst):
        self.items.extend(lst)

    def display(self, msg="ArrayList: "):
        print(msg, '항목수=', self.size(), self.items)