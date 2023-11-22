#binary_search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:            
            return mid  # Element gefunden, gibt den Index zurück
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1        
    return -1  # Element nicht gefunden

# Beispiel-Nutzung:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = binary_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} gefunden an Index {result}.")
else:
    print(f"Element {target_element} nicht gefunden.")