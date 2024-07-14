class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    # to get index of parent
    def parent(self, index):
        return (index-1)//2
    
    # To insert a new node    
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    # To find the left node
    def left_child(self, index):
        return 2 * index + 1

    #To find the right node
    def right_child(self, index):
        return 2 * index + 2

    # heapify the heap and bring it back to structure following all rules, to the up stream
    def heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    # To heapify and bring back to structure when by down stream
    def heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[index] ,self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    # To get the maximum number or Root val and pop it
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    # to perform heap sort, helping heapify operation
    def heapify(self, length, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < length and self.heap[left] > self.heap[largest]:
            largest = left

        if right < length and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index] ,self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(length, largest)

    # To perform sort on heap
    def heap_sort(self):
        length = len(self.heap)

        for index in range(length//2 - 1, -1, -1):
            self.heapify(length, index)
        
        for index in range(length-1, 0, -1):
            self.heap[index], self.heap[0] = self.heap[0], self.heap[index]
            self.heapify(index, 0)

    # To print the heap
    def print_heap(self):
        print(self.heap)

arr = [3,6,2,1,88,66,55,44,33,22,99,100]
heap = MaxHeap()
heap.print_heap()
for index in arr:
    heap.insert(index)
heap.print_heap()
print(heap.parent(4))
heap.insert(3)
heap.print_heap()
print(heap.extract_max())
heap.heap_sort()
heap.print_heap()


class Min_heap:
    def __init__(self) -> None:
        self.heap = []
    
    def parent(self, index):
        return (index - 1)//2

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)
    
    def print_heap(self):
        print(self.heap)

arr = [22,55,77,88,55,44,33,22,1,22,3,45,67]
min_heap = Min_heap()
for i in arr:    
    min_heap.insert(i)
min_heap.print_heap()