"""
Heap Sort Algorithm

Heap sort is a comparison-based sorting algorithm using heap data structure.
Time Complexity: O(n log n) for all cases (best, average, worst)
Space Complexity: O(1) - in-place sorting
Stability: Not stable

Steps:
1. Build a max heap from the array
2. Swap root (max) with last element
3. Reduce heap size and heapify root
4. Repeat until sorted
"""


def heapify(arr, n, i):
    """
    Heapify subtree rooted at index i
    
    Args:
        arr: Array to heapify
        n: Size of heap
        i: Root index of subtree
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child exists and is larger
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child exists and is larger
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapify_min(arr, n, i):
    """
    Heapify for min heap (used for descending sort)
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_min(arr, n, smallest)


def heap_sort(arr):
    """
    Sort array in ascending order using heap sort
    
    Args:
        arr: List to be sorted
    
    Returns:
        Sorted list (ascending order)
    """
    n = len(arr)
    
    if n <= 1:
        return arr
    
    # Step 1: Build max heap
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify reduced heap
        heapify(arr, i, 0)
    
    return arr


def heap_sort_desc(arr):
    """
    Sort array in descending order using heap sort
    
    Args:
        arr: List to be sorted
    
    Returns:
        Sorted list (descending order)
    """
    n = len(arr)
    
    if n <= 1:
        return arr
    
    # Build min heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(arr, n, i)
    
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_min(arr, i, 0)
    
    return arr


def heap_sort_simple(arr):
    """
    Heap sort using MinHeap class (creates new array)
    Easier to understand but uses extra space O(n)
    
    Args:
        arr: List to be sorted
    
    Returns:
        Sorted list (ascending order)
    """
    from heap import MinHeap
    
    heap = MinHeap()
    
    # Insert all elements into heap
    for value in arr:
        heap.insert(value)
    
    # Extract min values one by one
    result = []
    while not heap.is_empty():
        result.append(heap.extract_min())
    
    return result