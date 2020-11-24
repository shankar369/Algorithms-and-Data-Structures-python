class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("previous node is not in the list")
        else:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node


llist = LinkedList()

llist.append("A")
llist.append("B")
llist.prepend("C")
llist.insert_after_node(llist.head.next, "D")
llist.print_list()
