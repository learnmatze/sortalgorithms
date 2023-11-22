class Hashtable:
    def __init__(self, size):
        # Initialisierung der Hashtabelle mit einer bestimmten Größe
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # Beispiel einer einfachen Hashfunktion: Summe der ASCII-Werte der Buchstaben im Schlüssel
        hash_value = sum(ord(char) for char in key)
        return hash_value % self.size  # Modulo-Operation, um sicherzustellen, dass der Wert innerhalb der Größe der Hashtabelle liegt

    def insert(self, key, value):
        # Fügt ein Schlüssel-Wert-Paar in die Hashtabelle ein
        index = self.hash_function(key)
        self.table[index] = (key, value)

    def search(self, key):
        # Sucht nach einem Schlüssel in der Hashtabelle und gibt den zugehörigen Wert zurück
        index = self.hash_function(key)
        entry = self.table[index]
        if entry and entry[0] == key:
            return entry[1]  # Der gesuchte Schlüssel wurde gefunden, gibt den Wert zurück
        else:
            return None  # Schlüssel nicht gefunden

# Beispiel für die Verwendung der Hashtabelle
my_table = Hashtable(10)  # Größe der Hashtabelle: 10

# Einfügen von Schlüssel-Wert-Paaren
my_table.insert("apple", 5)
my_table.insert("banana", 8)
my_table.insert("cherry", 12)

# Suche nach einem Schlüssel
result = my_table.search("banana")

if result is not None:
    print(f"Der Wert für 'banana' ist {result}.")
else:
    print("Schlüssel nicht gefunden.")
