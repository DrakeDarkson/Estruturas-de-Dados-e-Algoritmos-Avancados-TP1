class MaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        while index > 0 and self.heap[self._parent(index)] < self.heap[index]:
            self.heap[self._parent(index)], self.heap[index] = self.heap[index], self.heap[self._parent(index)]
            index = self._parent(index)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def __str__(self):
        return str(self.heap)

# Exemplo:

max_heap = MaxHeap()
max_heap.heap = [50, 30, 40, 10, 20, 35]

max_heap.insert(45)

print("MaxHeap após inserção de 45:", max_heap)
