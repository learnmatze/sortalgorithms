# O(1) constant
def get_element(arr, index):
    if index < len(arr):
        return arr[index]
    else:
        return None

# Beispielverwendung
my_list = [2, 4, 6, 8, 10]
index_to_get = 2

result = get_element(my_list, index_to_get)
if result is not None:
    print(f"Das Element an Index {index_to_get} ist {result}.")
else:
    print("Der angegebene Index ist außerhalb des gültigen Bereichs.")