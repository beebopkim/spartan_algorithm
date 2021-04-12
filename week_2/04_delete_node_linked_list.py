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


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!
print(linked_list.get_node(0).data)

# linked_list.add_node(0, 11)

print(linked_list.print_all())

train_list = LinkedList("자갈")
train_list.append("밀가루")
train_list.append("우편")
train_list.add_node(0, "흑연")

print(train_list.print_all())
print(train_list.del_node(0))
print(train_list.print_all())
print(train_list.del_node(2))
print(train_list.print_all())
