def linear_search(arr, target):
    """
    Führt eine lineare Suche in der Liste durch und gibt den Index des gesuchten Elements zurück, falls es vorhanden ist.
    Gibt -1 zurück, wenn das Element nicht gefunden wurde.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element gefunden, gibt den Index zurück
    return -1  # Element nicht gefunden

# Beispiel
my_list = [1, 3, 5, 7, 9, 11, 13]

# Suchen nach der Zahl 7
target_value = 7
result = linear_search(my_list, target_value)

if result != -1:
    print(f"Das Element {target_value} wurde an der Position {result} gefunden.")
else:
    print(f"Das Element {target_value} wurde nicht in der Liste gefunden.")
