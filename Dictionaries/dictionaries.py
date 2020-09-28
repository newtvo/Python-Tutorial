# Create dictionary - using pointy bracket
dict1 = {'key1': 3,
         'key2': 'hello',
         'key3': [3, 4],
         'key1': [1, 2, 'tuple'],
         (0, 1, 23): 'value'
         }

print(type(dict1))
print(dict1)

# Get value from key
print(dict1['key3'])
print(type(dict1['key3']))

# Get all keys
print(dict1.keys())

# Get all values
print(dict1.values())

# Add entry to dictionary
dict1['key_n'] = 'new value'
print(dict1)

# Delete entry from dictionary
del(dict1['key3'])
print(dict1)

# Verify key in dictionary
print(('key3' in dict1))