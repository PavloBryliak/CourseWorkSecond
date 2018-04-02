class Stack(object):
    """
    Class for building a stack with defined properties
    in which we can do some manipulations like
    to push or pop elements and to define whether
    stack is full or empty.
    """
    def __init__(self, maxSize):
        self.stack = list()
        self.maxSize = maxSize
        self.top = 0

    def push(self, data):
        if self.top >= self.maxSize:
            return "Full stack"
        self.stack.append(data)
        self.top += 1
        return True

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def isFull(self):
        if len(self.stack) == self.maxSize:
            return True
        else:
            return False

    def pop(self):
        if self.top <= 0:
            return "Empty stack"
        item = self.stack.pop()
        self.top -= 1
        return item

    def size(self):
        return self.top