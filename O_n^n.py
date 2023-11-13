# O(n*n) double loop - find pairs with sum
def find_pairs_with_sum(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

# Beispielverwendung
my_list = [2, 3, 5, 7, 9, 11]
target = 10

result = find_pairs_with_sum(my_list, target)
if result:
    for pair in result:
        print(f"Paar mit Summe {target}: {pair[0]} und {pair[1]}")
else:
    print(f"Keine Paare mit Summe {target} gefunden.")