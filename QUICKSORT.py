def quick_sort(arr):
    if len(arr) <= 1:  # Base case: If the list has 0 or 1 elements, it's already sorted
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort and combine

# Example usage
numbers = [-54, 84, -65, 1, 0, 41, 90]
sorted_numbers = quick_sort(numbers)
print("Unsorted array:", numbers)
print("Sorted array:", sorted_numbers)
