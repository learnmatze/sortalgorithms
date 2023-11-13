# O(n) - sigle loop - find_element
def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Element nicht gefunden

# Beispielverwendung
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
element_to_find = 9

result = find_element(my_list, element_to_find)
if result != -1:
    print(f"Das Element {element_to_find} wurde an der Position {result} gefunden.")
else:
    print(f"Das Element {element_to_find} wurde nicht gefunden.")