def simple_numeric_hash_function(number, table_size):
    hash_value = number % table_size
    return hash_value

def simple_string_hash_function(key, table_size):
    hash_value = sum(ord(char) for char in key)
    index = hash_value % table_size
    return index

def improved_string_hash_function(key, table_size):
    hash_value = 0
    for i, char in enumerate(key):
        # Summiere den ASCII-Wert des Zeichens und seine Position im Schlüssel
        hash_value += (ord(char) + i)

    index = hash_value % table_size
    return index

# Beispielaufruf für nummer
table_size = 10
number = 123456789
index = simple_numeric_hash_function(number, table_size)
print(f"Der Index für die Zahl {number} in einer Tabelle der Größe {table_size} ist {index}.")

# Beispielaufruf für string
table_size = 10
key = "example_key"
index = simple_string_hash_function(key, table_size)
improved_index = improved_string_hash_function(key, table_size)
print(f"Der Index für den Schlüssel '{key}' in einer Tabelle der Größe {table_size} ist {index}.")
print(f"Der Index für den Schlüssel '{key}' in einer Tabelle der Größe {table_size} ist {improved_index}.")
