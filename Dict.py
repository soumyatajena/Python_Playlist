# Unstructered Data type - [key,value] pair where key = unique unhashable type i.e. has to be immutable type
                                         # incase key = not unique - value get overriden with latest value

dictionary = {
    'a':[1,2,3],
    'b':"Soumyata",
    'g':True
}
print(f'Dictionary : {dictionary}')

my_list = [
    {
    'a':[1,2,3],
    'b':"Soumyata",
    'g':True
},
{
    12:[4,6],
    'b':"Jena",
    'g':False
}
]
print(my_list[0]['a'][1]) #2
print(my_list[1][12][0]) #4
print(dictionary['a'][2]) #3

# .get() method in dictionary - checks if the key exists, if not, returns None

print(dictionary.get('age')) # None
print(dictionary.get('g')) # true
print(dictionary.get('x', 'Default value incase key is not present'))
dictionary = {
    'a':[1,2,3],
    'b':"Soumyata",
    'g':True,
    'x':'key is present'
}
print(dictionary.get('x', 'Default value incase key is not present'))
print(dictionary)

# Another way to create new dictionary
new_dict = dict(name='Python')
print(new_dict)

# Look for an item in dictionary
dictionary = {
    'a':[1,2,3],
    'b':"Soumyata",
    'g':True,
    'x':'key is present'
}

print('b' in dictionary.keys()) # true
print(True in dictionary.values()) # true
# .items() grab the entire key-value pair and search within it
print('is' in dictionary.items()) # false
print('xg' in dictionary.items()) # false
# .items() returns a tuple [(),(),()] as output
print(dictionary.items()) # dict_items([('a', [1, 2, 3]), ('b', 'Soumyata'), ('g', True), ('x', 'key is present')])

new_dict= dictionary.copy()
print(dictionary.clear()) # None
print(new_dict) # {'a': [1, 2, 3], 'b': 'Soumyata', 'g': True, 'x': 'key is present'}

# removes the specific key-value from the dict and o/p the resp value
print(new_dict.pop('a')) # [1, 2, 3]

# remove sthe last element in the dict
print(new_dict.popitem()) # ('x', 'key is present')
print(new_dict) # {'b': 'Soumyata', 'g': True}

# Update - updates the dict with the value provided. 
# Incase, key is not present, it creates the new key and add the value
new_dict.update({'x':'Updated value added'})
print(new_dict) # {'b': 'Soumyata', 'g': True, 'x': 'Updated value added'}