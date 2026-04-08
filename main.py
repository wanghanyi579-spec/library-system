"""
Main Program - Demonstration of Heap and Heap Sort

Run this file to see all demonstrations:
    python main.py
"""

from heap import MinHeap, MaxHeap
from heap_sort import heap_sort, heap_sort_simple


def demo1_min_heap():
    """Demonstration 1: Min Heap basic operations"""
    print("\n" + "=" * 60)
    print("Demo 1: Min Heap")
    print("=" * 60)
    
    heap = MinHeap()
    
    print("\n1. Inserting values: 5, 3, 8, 1, 6, 2")
    for value in [5, 3, 8, 1, 6, 2]:
        heap.insert(value)
        print(f"   After inserting {value}: {heap}")
    
    print(f"\n2. Heap size: {heap.get_size()}")
    print(f"   Minimum value (peek): {heap.peek_min()}")
    
    print("\n3. Extracting minimum values one by one:")
    while not heap.is_empty():
        min_val = heap.extract_min()
        print(f"   Extracted {min_val}, remaining heap: {heap}")


def demo2_max_heap():
    """Demonstration 2: Max Heap basic operations"""
    print("\n" + "=" * 60)
    print("Demo 2: Max Heap")
    print("=" * 60)
    
    heap = MaxHeap()
    
    print("\n1. Inserting values: 5, 3, 8, 1, 6, 2")
    for value in [5, 3, 8, 1, 6, 2]:
        heap.insert(value)
        print(f"   After inserting {value}: {heap}")
    
    print(f"\n2. Heap size: {heap.get_size()}")
    print(f"   Maximum value (peek): {heap.peek_max()}")
    
    print("\n3. Extracting maximum values one by one:")
    while not heap.is_empty():
        max_val = heap.extract_max()
        print(f"   Extracted {max_val}, remaining heap: {heap}")


def demo3_heap_sort():
    """Demonstration 3: Heap Sort algorithm"""
    print("\n" + "=" * 60)
    print("Demo 3: Heap Sort")
    print("=" * 60)
    
    # Test 1: Random array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n1. Original array: {arr1}")
    sorted_arr = heap_sort(arr1.copy())
    print(f"   Sorted ascending: {sorted_arr}")
    
    # Test 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    print(f"\n2. Already sorted array: {arr2}")
    sorted_arr2 = heap_sort(arr2.copy())
    print(f"   Sorted ascending: {sorted_arr2}")
    
    # Test 3: Reverse sorted array
    arr3 = [7, 6, 5, 4, 3, 2, 1]
    print(f"\n3. Reverse sorted array: {arr3}")
    sorted_arr3 = heap_sort(arr3.copy())
    print(f"   Sorted ascending: {sorted_arr3}")
    
    # Test 4: Array with duplicates
    arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print(f"\n4. Array with duplicates: {arr4}")
    sorted_arr4 = heap_sort(arr4.copy())
    print(f"   Sorted ascending: {sorted_arr4}")
    
    # Test 5: Single element
    arr5 = [42]
    print(f"\n5. Single element array: {arr5}")
    sorted_arr5 = heap_sort(arr5.copy())
    print(f"   Sorted ascending: {sorted_arr5}")
    
    # Test 6: Empty array
    arr6 = []
    print(f"\n6. Empty array: {arr6}")
    sorted_arr6 = heap_sort(arr6.copy())
    print(f"   Sorted ascending: {sorted_arr6}")


def demo4_priority_queue():
    """Demonstration 4: Heap as Priority Queue (Real-world application)"""
    print("\n" + "=" * 60)
    print("Demo 4: Real-world Application - Task Priority Queue")
    print("=" * 60)
    
    # Task scheduling system
    # Smaller number = higher priority
    task_queue = MinHeap()
    
    tasks = [
        (3, "Send email to team"),
        (1, "Fix critical bug"),      # Highest priority
        (5, "Backup database"),
        (2, "Generate monthly report"),
        (4, "Clean log files")
    ]
    
    print("\nAdding tasks (lower number = higher priority):")
    for priority, task in tasks:
        task_queue.insert((priority, task))
        print(f"  Added: [{priority}] {task}")
    
    print("\nProcessing tasks by priority:")
    while not task_queue.is_empty():
        priority, task = task_queue.extract_min()
        print(f"  Executing: [{priority}] {task}")


def demo5_performance_comparison():
    """Demonstration 5: Performance comparison"""
    print("\n" + "=" * 60)
    print("Demo 5: Performance Comparison")
    print("=" * 60)
    
    import time
    import random
    
    sizes = [1000, 5000, 10000]
    
    print("\nHeap Sort vs Python Built-in sort (for reference)")
    print("-" * 50)
    
    for size in sizes:
        # Generate random array
        arr = [random.randint(1, 10000) for _ in range(size)]
        
        # Heap sort
        arr_copy = arr.copy()
        start = time.time()
        heap_sort(arr_copy)
        heap_time = time.time() - start
        
        # Built-in sort (for reference)
        arr_copy2 = arr.copy()
        start = time.time()
        arr_copy2.sort()
        builtin_time = time.time() - start
        
        print(f"\nArray size: {size}")
        print(f"  Heap sort time: {heap_time:.6f} seconds")
        print(f"  Built-in sort time: {builtin_time:.6f} seconds")
    
    print("\nNote: Built-in sort is implemented in C and faster")
    print("But heap sort has O(1) space complexity (in-place)")


def demo6_heap_properties():
    """Demonstration 6: Heap properties visualization"""
    print("\n" + "=" * 60)
    print("Demo 6: Heap Properties")
    print("=" * 60)
    
    heap = MinHeap()
    
    # Insert values
    values = [10, 5, 15, 3, 8, 12, 18, 1, 7]
    print(f"\nInserting values: {values}")
    
    for v in values:
        heap.insert(v)
    
    print(f"\nHeap array representation (parent <= children):")
    print(f"  {heap}")
    
    print(f"\nHeap size: {heap.get_size()}")
    print(f"Is heap empty? {heap.is_empty()}")
    
    # Show tree structure (simplified)
    print(f"\nTree structure (index: value):")
    print(f"           {heap.heap[0] if len(heap.heap) > 0 else 'None'}")
    if len(heap.heap) > 2:
        print(f"         /    \\")
        print(f"       {heap.heap[1]}      {heap.heap[2]}")
    if len(heap.heap) > 4:
        print(f"      /  \\    /  \\")
        children = [heap.heap[3] if len(heap.heap) > 3 else '·',
                    heap.heap[4] if len(heap.heap) > 4 else '·',
                    heap.heap[5] if len(heap.heap) > 5 else '·',
                    heap.heap[6] if len(heap.heap) > 6 else '·']
        print(f"     {children[0]}   {children[1]}  {children[2]}   {children[3]}")


def main():
    """Run all demonstrations"""
    print("=" * 60)
    print("HEAP DATA STRUCTURE & HEAP SORT ALGORITHM")
    print("COMP2090SEF Self-Study Project - Task 2")
    print("=" * 60)
    print("\nThis demonstration covers:")
    print("  • Min Heap and Max Heap implementation")
    print("  • Insert and extract operations")
    print("  • Heap Sort algorithm")
    print("  • Priority queue application")
    print("  • Performance analysis")
    
    demo1_min_heap()
    demo2_max_heap()
    demo3_heap_sort()
    demo4_priority_queue()
    demo5_performance_comparison()
    demo6_heap_properties()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 60)
    print("\nSummary:")
    print("  • Heap: Complete binary tree with heap property")
    print("  • Insert/Extract: O(log n)")
    print("  • Heap Sort: O(n log n) time, O(1) space")
    print("  • Applications: Priority queues, task scheduling, Top K")


if __name__ == "__main__":
    main()