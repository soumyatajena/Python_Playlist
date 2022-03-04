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

