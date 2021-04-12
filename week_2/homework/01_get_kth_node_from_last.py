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

    def get_kth_node_from_last(self, k):
        return self.get_node(len(self) - k)

    def __len__(self):
        cur = self.head
        len_cnt = 0
        while cur:
            len_cnt += 1
            cur = cur.next
        return len_cnt

    def get_node(self, index):
        cnt = 0
        cur = self.head
        while cnt < index:
            cnt += 1
            cur = cur.next
        return cur

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(len(linked_list))

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!