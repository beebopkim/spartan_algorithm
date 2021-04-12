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

    def get_node(self, index):
        cnt = 0
        cur = self.head
        while cnt < index:
            cnt += 1
            cur = cur.next
        return cur


linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.print_all())
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!
print(linked_list.get_node(0).data)
