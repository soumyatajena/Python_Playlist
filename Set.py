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

## *************************** Set Methods ******************************************

# 1. .difference() - operates as A-B in sets
my_set={1,2,3,4,5}
your_set={3,4,9,0,1}
print(my_set.difference(your_set)) # {2, 3, 5}
print(your_set.difference(my_set)) # {0, 9}

# 2. .difference_update - modifies the given set after operation
print(my_set) # {1, 2, 3, 4, 5}
my_set.difference_update(your_set)
print(my_set) # {2, 3, 5}

# 3. .discard() - remove the value and update the set
my_set.discard(5)
print(my_set) # {2, 3}

# 4. .intersection()- A int B
print(my_set.intersection(your_set))
print(my_set & your_set) 

#5. .isdisjoint()- are the two sets have anything in common?
# True - nothing in common
print(my_set.isdisjoint(your_set)) # True

#6. .union - added both sets unique elements
print(my_set.union(your_set)) # {0, 1, 2, 3, 4, 9}
print(my_set | your_set) # {0, 1, 2, 3, 4, 9}

#7. .issubset()
my_set={3,4}
your_set={3,4,9,0,1}
print(my_set.issubset(your_set)) # True

#8. .issuperset
print(my_set.issuperset(your_set)) # False
print(your_set.issuperset(my_set)) # True