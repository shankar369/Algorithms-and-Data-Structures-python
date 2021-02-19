class LinkedQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def get_first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self._head._element

    def enqueue(self, element):
        new_node = self._Node(element, self._head)
        if(self.is_empty()):
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        first_element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if(self.is_empty()):
            self._tail = None
        return first_element


lq = LinkedQueue()

print(lq.is_empty())
lq.enqueue(1)
lq.enqueue(2)
lq.enqueue(1)
lq.dequeue()
lq.enqueue(3)
print(lq.dequeue())
print(len(lq))
