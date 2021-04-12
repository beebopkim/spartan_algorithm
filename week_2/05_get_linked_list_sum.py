class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            old_node = self.get_node(index - 1)
            old_next = old_node.next
            new_node.next = old_next
            old_node.next = new_node

    def del_node(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            old_node = self.get_node(index - 1)
            if old_node.next:
                old_node.next =  old_node.next.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    return eval_link_list_sum(linked_list_1) + eval_link_list_sum(linked_list_2)


def eval_link_list_sum(linked_list):
    cur = linked_list.head
    sum = 0
    while cur:
        sum = (sum * 10) + cur.data
        cur = cur.next
    return sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
