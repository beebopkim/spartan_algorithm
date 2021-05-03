class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        pp = len(self.items) - 1
        while pp > 1:
            parent_p = pp // 2
            if self.items[pp] > self.items[parent_p]:
                self.items[pp], self.items[parent_p] = self.items[parent_p], self.items[pp]
                pp = parent_p
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!