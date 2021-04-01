from DoublyLinkedList import _DoublyLinkedList


class LinkedDequeue(_DoublyLinkedList):
    def first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self._header._next._element

    def last(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self._trailer._prev._element

    def insert_first(self, element):
        return self._insert_between(element, self._header, self._header._next)

    def insert_last(self, element):
        return self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self._delete_node(self._trailer._prev)


ldq = LinkedDequeue()
ldq.insert_first(3)
ldq.insert_last(4)
print(ldq.first())
print(ldq.last())
print(len(ldq))
print(ldq.delete_first())
print(len(ldq))
print(ldq.delete_last())
print(len(ldq))
