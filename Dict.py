# Unstructered Data type - [key,value] pair where key = string element
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
    'a':[4,6],
    'b':"Jena",
    'g':False
}
]
print(my_list[0]['a'][1]) #2
print(dictionary['a'][2]) #3