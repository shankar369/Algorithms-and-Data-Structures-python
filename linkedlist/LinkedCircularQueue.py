class LinkedCircularQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        header = self._tail._next
        return header._element

    def enqueue(self, element):
        newest = self._Node(element, None)
        if(self.is_empty()):
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        old_head = self._tail._next
        if(self._size == 1):
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element

    def rotate(self):
        if(not self.is_empty()):
            self._tail = self._tail._next


lcq = LinkedCircularQueue()
print(lcq.is_empty())
for i in range(10):
    lcq.enqueue(i)

print(lcq.dequeue())
print(lcq.first())
lcq.rotate()
lcq.rotate()
lcq.rotate()
print(lcq.dequeue())
print(lcq.first())
