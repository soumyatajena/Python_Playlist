#Exercise 2: Check for the duplicates in list:

my_list=['a','b','c','b','c','C','d','m','n','n']

i=0
new_list=[]
duplicates=[]
for i in my_list:
    is_duplicate=False
    if(len(new_list)==0):
        new_list.append(i)
    else:
        for j in new_list:
            if i == j:
                duplicates.append(i)
                is_duplicate=True
                break
        if(not is_duplicate):
            new_list.append(i)

print("Duplicate Array:", duplicates)
print("Original Array:",my_list)
print("Array after removing duplicates:", new_list)

# Duplicate Array: ['b', 'c', 'n']
# Original Array: ['a', 'b', 'c', 'b', 'c', 'C', 'd', 'm', 'n', 'n']
# Array after removing duplicates: ['a', 'b', 'c', 'C', 'd', 'm', 'n']

#   ----------------------     OR     -------------------

for value in my_list:
    if my_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

# ['b', 'c', 'n']

