def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.
    
    Parameters:
    arr (list): The array representing the heap
    n (int): Size of the heap (number of elements to consider)
    i (int): Index of the root of the subtree to heapify
    
    Returns:
    None (modifies the array in-place)
    
    Time complexity: O(log n)
    Space complexity: O(1) (iterative version would be O(1), recursive uses call stack)
    """
    largest = i          # Assume root is the largest
    left = 2 * i + 1     # Left child index (0-based indexing)
    right = 2 * i + 2    # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def build_max_heap(arr):
    """
    Build a max-heap from an unsorted array.
    
    Parameters:
    arr (list): The array to be converted into a max-heap
    
    Returns:
    None (modifies the array in-place)
    
    Time complexity: O(n)
    """
    n = len(arr)
    # Start from the last non-leaf node and go up to the root
    # Last non-leaf node index = n//2 - 1 (for 0-based indexing)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    """
    Sort an array in ascending order using the Heap Sort algorithm.
    
    Parameters:
    arr (list): The array to be sorted
    
    Returns:
    None (modifies the array in-place)
    
    Time complexity: O(n log n) for best, worst, and average cases
    Space complexity: O(1) (in-place sorting)
    
    Algorithm:
    1. Build a max-heap from the input array
    2. Repeatedly extract the maximum element (root) and swap it with the last element
    3. Reduce heap size by 1 and heapify the root
    4. Repeat until the heap is empty
    """
    n = len(arr)
    
    # Step 1: Build a max-heap
    build_max_heap(arr)
    
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (maximum) to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap (size = i)
        heapify(arr, i, 0)


def heap_sort_with_steps(arr):
    """
    Same as heap_sort but prints intermediate steps for demonstration.
    Useful for understanding how the algorithm works.
    
    Parameters:
    arr (list): The array to be sorted
    
    Returns:
    None (modifies the array in-place, prints steps)
    """
    n = len(arr)
    print(f"Original array: {arr}")
    
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print(f"After building max-heap: {arr}")
    
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f"  Swap arr[0]={arr[0]} with arr[{i}]={arr[i]}")
        heapify(arr, i, 0)
        print(f"  After heapify (heap size={i}): {arr}")
    
    print(f"Sorted array: {arr}")


# ==================================================
# Test Cases
# ==================================================

def test_heap_sort():
    """Run multiple test cases to verify correctness."""
    
    test_cases = [
        [4, 10, 3, 5, 1],
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 1, 2, 0, 0],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
    
    for i, test_arr in enumerate(test_cases):
        # Make a copy to preserve original for display
        original = test_arr.copy()
        heap_sort(test_arr)
        print(f"Test {i+1}: {original} -> {test_arr}")
        
        # Verify correctness
        expected = sorted(original)
        assert test_arr == expected, f"Failed: {original} sorted to {test_arr}, expected {expected}"
    
    print("\nAll test cases passed!")


def interactive_mode():
    """Allow user to input custom arrays for sorting."""
    print("\n=== Interactive Heap Sort ===")
    print("Enter numbers separated by spaces (e.g., 5 2 8 1 9)")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("> ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        try:
            numbers = [int(x) for x in user_input.split()]
            if not numbers:
                print("Please enter at least one number.")
                continue
            
            print(f"Original: {numbers}")
            heap_sort_with_steps(numbers)
            print(f"Sorted: {numbers}\n")
            
        except ValueError:
            print("Invalid input. Please enter integers only.\n")


# ==================================================
# Main Entry Point
# ==================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Heap Sort Implementation - Task 2")
    print("Student: Wang Hanyi (13357481)")
    print("=" * 50)
    
    # Run automated tests
    test_heap_sort()
    
    # Example with step-by-step printing
    print("\n=== Step-by-step Example ===")
    example_arr = [4, 10, 3, 5, 1]
    heap_sort_with_steps(example_arr)
    
    # Interactive mode (optional, uncomment to use)
    # interactive_mode()
