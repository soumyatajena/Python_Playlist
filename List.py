## String is immutatable - can be replaced but content can not be changed
string_immutable='Soumyata'

#string_immutable[0]='s' # will produce error - TypeError: 'str' object does not support item assignment
string_immutable = 'jena' # o/p = jena [instead of Soumyata]
print(string_immutable)

## String slicing - str[start_index:stop_index:step_over]
print(string_immutable[0:2:1])
print(string_immutable[::])

## List is mutable data structure
amazon_list=['notebooks','pen','pencil','charger']
print(f'Old list:{amazon_list}')
amazon_list=['laptop','pen','pencil','charger']

## Copying list
new_list=amazon_list[:] # as the reference is to the newly created list memory location
new_list[0]='mac-book'
print(f'Copied New amazon-list:{amazon_list}')
print(f'Copied New list:{new_list}')

## Modifying list
new_list=amazon_list # as the reference is to the real list memory location
new_list[0]='mac-book'
print(f'Modified New amazon-list:{amazon_list}') 
print(f'Modified New list:{new_list}')

## List Slicing
print(f'New list sliced:{amazon_list[0:4:2]}') #'laptop', 'pencil'


## *************************** List methods ******************************************

integer_list = [45,0,9,-1,5,8,8]

# 1. Sort() - sortlist elements in ascending order
integer_list.sort() # does not return anything - None 
print(f'Sort() list is: {integer_list}') 
integer_list.sort(reverse=True)
print(f'Sort(Desc) list is: {integer_list}') 

# NOTE : sorted() method accepts any iterable whereas the sort() method only works with lists.

# 2. Sorted() - sort the elements and returns the sorted list
sorted(integer_list)
print(f'Sorted(Asc) list is: {integer_list}') 
sorted(integer_list,reverse=False)
print(f'Sorted(Desc) list is: {integer_list}') 

# 3. Count - count the number of similar elements in the list
print(f'No of occurance of 8 is: {integer_list.count(8)}')

# 4. Append - add value to list
integer_list.append(10)    # does not return anything - None
print(f"Appended list: {integer_list}")

# 5. Pop - removes the last value from list
popped_value= integer_list.pop()
print(f"Default popped list: {integer_list}")
popped_value = integer_list.pop(2)
print(f"Index 2 popped value is : {popped_value} and popped list: {integer_list}")

# 6. Remove - remove the given value
integer_list.remove(-1) # does not return anything - None
print(f"list after removal of 1 is: {integer_list}")

# 7. Reverse - reverses the list
integer_list.reverse()
print(f'Reversed list:{integer_list}')
integer_list.reverse()
print(f'Double Reversed[Asc] list:{integer_list[::]}')

# 8. Range - print from starting given value to ending value
print(list(range(-2,101)))

# 9. Clear - clears the entire list and makes the list empty []
integer_list.clear() # does not return anything - None
print(f"Cleared list: {integer_list}")

# 10. Join - string method- joins the string on basis of the given original string

str_list="!"
new_str=str_list.join(['hi','my', 'name','is','Soumyata']) # o/p : hi!my!name!is!Soumyata
str_list=" "
new_str=str_list.join(['hi','my', 'name','is','Soumyata'])  # o/p : hi my name is Soumyata
# or
new_str=' '.join(['hi','my', 'name','is','Soumyata']) # o/p : hi my name is Soumyata
print(new_str)

## *************************** List unpacking ******************************************

a,b,c,*other,d = [1,2,3,4,'Soumyata',6,7,8,9,0]
print(a) #1
print(b) #2
print(c) #3
print(*other) # 4 Soumyata 6 7 8 9
print(d) #0
