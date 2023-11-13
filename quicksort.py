# O(n log n) quick_sort - divide an conquer
def quick_sort(arr):
    # Base case: If the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Choose a Pivot
    pivot = arr[0]  # Choose the first element as the pivot

    # Step 2: Partition the Array
    left = []  # Elements smaller than the pivot
    right = []  # Elements greater than the pivot

    for element in arr[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    # Step 3: Recursively Sort the Sub-Arrays
    left = quick_sort(left)  # Recursively sort the left sub-array
    right = quick_sort(right)  # Recursively sort the right sub-array

    # Step 4: Combine and Return
    return left + [pivot] + right