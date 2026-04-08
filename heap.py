"""
Heap Data Structure

Heap is a special complete binary tree data structure:
- Min Heap: parent node <= child nodes
- Max Heap: parent node >= child nodes

Time Complexity:
- Insert: O(log n)
- Extract min/max: O(log n)
- Heapify: O(n)
"""


class MinHeap:
    """
    Min Heap - Parent is always <= children
    
    Applications:
    - Priority queue
    - Task scheduling
    - Top K problems
    """
    
    def __init__(self):
        """Initialize an empty heap"""
        self.heap = []
    
    def _parent(self, index: int) -> int:
        """Return parent index"""
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        """Return left child index"""
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        """Return right child index"""
        return 2 * index + 2
    
    def _swap(self, i: int, j: int) -> None:
        """Swap two elements"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self, index: int) -> None:
        """
        Move element up to maintain heap property
        Used after insertion
        """
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)
    
    def _heapify_down(self, index: int) -> None:
        """
        Move element down to maintain heap property
        Used after extraction
        """
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)
    
    def insert(self, value) -> None:
        """
        Insert a value into the heap
        Time Complexity: O(log n)
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        """
        Remove and return the minimum value (root)
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("Heap is empty, cannot extract")
        
        min_value = self.heap[0]
        
        # Move last element to root
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if not self.is_empty():
            self._heapify_down(0)
        
        return min_value
    
    def peek_min(self):
        """Return minimum value without removing it"""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def get_size(self) -> int:
        """Return heap size"""
        return len(self.heap)
    
    def is_empty(self) -> bool:
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def get_all(self) -> list:
        """Return all elements (unsorted order)"""
        return self.heap.copy()
    
    def __str__(self) -> str:
        """String representation"""
        if self.is_empty():
            return "[]"
        return str(self.heap)


class MaxHeap:
    """
    Max Heap - Parent is always >= children
    """
    
    def __init__(self):
        """Initialize an empty max heap"""
        self.heap = []
    
    def _parent(self, index: int) -> int:
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        return 2 * index + 2
    
    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self, index: int) -> None:
        """Heapify up for max heap"""
        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)
    
    def _heapify_down(self, index: int) -> None:
        """Heapify down for max heap"""
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)
    
    def insert(self, value) -> None:
        """Insert a value into the max heap"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        """Remove and return the maximum value"""
        if self.is_empty():
            raise IndexError("Heap is empty, cannot extract")
        
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        if not self.is_empty():
            self._heapify_down(0)
        
        return max_value
    
    def peek_max(self):
        """Return maximum value without removing it"""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def get_size(self) -> int:
        return len(self.heap)
    
    def is_empty(self) -> bool:
        return len(self.heap) == 0
    
    def __str__(self) -> str:
        if self.is_empty():
            return "[]"
        return str(self.heap)