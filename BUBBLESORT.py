def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  
        for j in range(n - i - 1):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", numbers)

bubble_sort(numbers)  # Sort the array in place

print("Sorted array:", numbers)
