# Set - unordered collection of unique objects - returns unique objects

my_list=[1,2,3,4,5,5,5,5,5,6]
my_set ={1,2,3,4,5,5,5,5,5,6}
print(my_set) # {1, 2, 3, 4, 5, 6}
my_set.add(1)
my_set.add(-1)
print(my_set) # {1, 2, 3, 4, 5, 6, -1}

# Convert list to set - remove the duplicates
print(my_list) # [1, 2, 3, 4, 5, 5, 5, 5, 5, 6]
print(set(my_list)) # {1, 2, 3, 4, 5, 6}

# NOTE: Set() does not support Indexing
#print(my_set[0]) # TypeError: 'set' object is not subscriptable

print(5 in my_set) # true

print(len(my_set)) # 7 - counts only the unique objects

# Convert set to list
print(list(my_set)) # [1, 2, 3, 4, 5, 6, -1]

new_set= my_set.copy()
print(list(my_set)) # [1, 2, 3, 4, 5, 6, -1]
my_set.clear()
print(new_set) # {1, 2, 3, 4, 5, 6, -1}
print(my_set) # empty set()
