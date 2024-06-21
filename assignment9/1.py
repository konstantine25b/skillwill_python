# List
my_list = [1, 2, 3, 4, 5]
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Sliced list:", my_list[2:4])
my_list.append(6)
print("Appended list:", my_list)
my_list.remove(3)
print("List after removing element:", my_list)
print("Length of the list:", len(my_list))

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Value for 'a':", my_dict['a'])
my_dict['d'] = 4
print("Dictionary after adding new pair:", my_dict)
del my_dict['b']
print("Dictionary after removing 'b':", my_dict)
if 'c' in my_dict:
    print("'c' exists in the dictionary")
print("Length of the dictionary:", len(my_dict))

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Sliced tuple:", my_tuple[2:4])
print("Length of the tuple:", len(my_tuple))
another_tuple = my_tuple + (6, 7)
print("Concatenated tuple:", another_tuple)
a, b, *rest = my_tuple
print("Unpacked values:", a, b, rest)

# Set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)
my_set.add(6)
print("Set after adding element:", my_set)
my_set.remove(3)
print("Set after removing element:", my_set)
if 2 in my_set:
    print("2 exists in the set")
print("Length of the set:", len(my_set))
