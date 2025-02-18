class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_down(self, index):
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0 and self.heap[(index - 1) // 2] > self.heap[index]:
            parent = (index - 1) // 2
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self._heapify_down(0)
        return min_value

    def __str__(self):
        return str(self.heap)


# Exemplo:
heap = MinHeap()
heap.insert(3)
heap.insert(1)
heap.insert(6)
heap.insert(5)
heap.insert(2)
heap.insert(4)

print("Heap antes da remoção:", heap)
print("Elemento removido:", heap.pop())
print("Heap após remoção:", heap)
