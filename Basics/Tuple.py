# Tuple - immutable list
# Benefits : 1. non mutable
#            2. faster access than list
#            3. Only two methods - Count() and Index()

my_tuple= (1,2,4,5,8)
# my_tuple[1]='z' # TypeError: 'tuple' object does not support item assignment

print(my_tuple[3]) # 5
print(8 in my_tuple) # true

# .items() returns a output [(),(),()] as TUPLE
dictionary = {
    (1,2):[1,2,3],
    'b':"Soumyata",
    'g':True,
    'x':'key is present'
}
print(dictionary.items()) # dict_items([((1, 2), [1, 2, 3]), ('b', 'Soumyata'), ('g', True), ('x', 'key is present')])
print(dictionary[(1,2)]) # [1, 2, 3]

# Slice method
sliced_tuple=my_tuple[0:3] # (1, 2, 4)
sliced_tuple=my_tuple[0:1] # (1,) - contains a comma at end unlike list
print(sliced_tuple) 

x,y,z, *other=(1,2,3,4,5,6,7,7)
print(other) #[4, 5, 6, 7, 7]

# Count() - count the number of occurances
print(other.count(7)) # 2

# Index() - returns the index of first matched value
print(other.index(7)) # 3

#Len() - finds the tuple length
print(len(other)) # 5