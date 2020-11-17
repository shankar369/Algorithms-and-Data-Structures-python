'''
STACK
FILO - first in last out
'''


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if(not self.is_empty()):
            return self.items[-1]
        return None

    def get_stack(self):
        return self.items


# stack = Stack()
# print(stack.is_empty())
# stack.push(1)
# stack.push(2)

# print(stack.get_stack())

# print(stack.peek())
# print(stack.pop())
# print(stack.get_stack())

# print(stack.is_empty())
