def interpolation_search(data, key):
    """
    Führt eine Interpolationssuche in der sortierten Liste durch und gibt den Index des gesuchten Elements zurück, falls es vorhanden ist.
    Gibt -1 zurück, wenn das Element nicht gefunden wurde.
    """
    links, rechts = 0, len(data) - 1
    durchlauf = 1

    while links <= rechts and data[links] <= key <= data[rechts]:
        # Verwende die Interpolationsformel, um eine geschätzte Position zu berechnen
        mitte = int(links + (key - data[links]) / (data[rechts] - data[links]) * (rechts - links))

        if data[mitte] == key:
            return mitte, durchlauf  # Element gefunden, gibt den Index zurück
        elif data[mitte] < key:
            links = mitte + 1  # Das gesuchte Element ist im rechten Teil der Liste
        else:
            rechts = mitte - 1  # Das gesuchte Element ist im linken Teil der Liste
        durchlauf = durchlauf + 1

    return -1, durchlauf  # Element nicht gefunden

# Beispiel
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# sorted_list = [1, 4, 5, 6, 7, 8, 10, 11, 13, 14, 16, 18, 20, 21, 22]

# Suchen nach der Zahl 5
target_key = 5
# Suchen nach der Zahl 6
# target_key = 6
result, durchlauf = interpolation_search(sorted_list, target_key)

if result != -1:
    print(f"Das Element {target_key} wurde an der Position {result} gefunden. (in {durchlauf} durchläufen)")
else:
    print(f"Das Element {target_key} wurde nicht in der Liste gefunden. (in {durchlauf} durchläufen)")
