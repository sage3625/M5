#generate a Stack class with push, pop, peek, is_empty, and size methods. Then generate a BinaryExpressionTree class that builds an expression tree from a postfix string, supports evaluation, infix traversal, and postfix traversal. Use the Stack class in the BinaryExpressionTree implementation.

class Stack:

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
