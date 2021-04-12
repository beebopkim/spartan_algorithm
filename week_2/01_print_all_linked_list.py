class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        all_list = []
        cur = self.head
        while cur:
            all_list.append(str(cur.data))
            cur = cur.next
        return "Linked List: [" + ", ".join(all_list) + "]"


ll = LinkedList(3)
ll.append(4)
ll.append(5)

print(ll.print_all())
