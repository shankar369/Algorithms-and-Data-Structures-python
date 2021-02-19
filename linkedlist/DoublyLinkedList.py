class _DoublyLinkedList:
    class _Node:
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        # linking sentinels to each other
        # here sentinels are dummy nodes act as header and trailers to make things easy
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        new_node = self._Node(element, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node_to_delete):
        predecessor = node_to_delete._prev
        successor = node_to_delete._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        answer = node_to_delete._element
        node_to_delete._element = node_to_delete._prev = node_to_delete._next = None

        return answer
