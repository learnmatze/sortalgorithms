# bubble_sort O(n^2) - loop in loop
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Flag to optimize the inner loop
        swapped = False
        # Last i elements are already in place, so no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

# Example usage
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array:", arr)