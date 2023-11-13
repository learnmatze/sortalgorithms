# O(log n) - binary_search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    n = 0 # anzahl der durchläufe der Schleife

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            print(f"Das array hat {len(arr)} Elemente und die Schleife wurde {n} mal durchlaufen. (n * log2 n)")
            return mid  # Element gefunden, gibt den Index zurück
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        n = n + 1
    print(f"Das array hat {len(arr)} Elemente und die Schleife wurde {n} mal durchlaufen. (n * log2 n)")
    return -1  # Element nicht gefunden

# Beispiel-Nutzung:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_element = 7

result = binary_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} gefunden an Index {result}.")
else:
    print(f"Element {target_element} nicht gefunden.")