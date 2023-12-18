data_dict = {}

for inc in range(5):
    #print(inc)
    data_dict.setdefault(inc, {})
    data_dict[inc]["aaa"] = 1
#print(data_dict)
     
nested_dict = {
    'first_level': {
        'key1': 'value1',
        'key2': 'value2',
        'nested_level': {
            'key3': 'value3',
            'key4': 'value4'
        }
    },
    'another_first_level': {
        'key5': 'value5',
        'key6': 'value6'
    }
}

# Define a recursive function to access nested values
def get_nested_value(dictionary, keys):
    return map(lambda key: dictionary[key] if key in dictionary else None, keys)

# Example usage:
keys_to_access = ['first_level', 'nested_level', 'key5']
result = list(get_nested_value(nested_dict, keys_to_access))

print(result)