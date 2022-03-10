# Iterable - object/collection that can be iterated over
# eg. List, Dictionary, Tuple, Set, String

# CLASS	    DESCRIPTION	            IMMUTABLE	MUTABLE
#-------------------------------------------------------
# bool	    Boolean Values	        Yes	        No
# int	    Integer Values	        Yes	        No
# float	    Floating-point 	        Yes	        No
#           numbers
# complex	Complex Numbers	        Yes	        No
# str	    String Values	        Yes	        No
# tuple	    An immutable    	    Yes	        No
#           sequence of objects
# frozenset	An immutable version 	Yes	        No
#           of set class
#-------------------------------------------------------
# dict	    Dictionary          	No	        Yes
# list	    A mutable sequence 	    No	        Yes
#           of objects
# set	    Mutable collection 	    No	        Yes
#           of distinct objects


# -------------------------  Dictionary  ---------------

user={
    'name':'Soumyata',
    'age':24,
    'can_paint':True,
    (1):'Checking tuple is immutable'
}

for item in user.items():
    print(item)

# ('name', 'Soumyata')
# ('age', 24)
# ('can_paint', True)
# (1, 'Checking tuple is immutable')

for item in user.values():
    print(item)

# Soumyata
# 24
# True
# Checking tuple is immutable

for item in user.keys():
    print(item)

# name
# age
# can_paint
# 1

for item in user:
    print('->',item)

# -> name
# -> age
# -> can_paint
# -> 1

##----------------------   POINTS TO REMEMBER  -------------------

for item in user.items():
    k,v=item
    print(k,v)

#   OR

for k,v in user.items():
    print(k,v)

# name Soumyata
# age 24
# can_paint True
# 1 Checking tuple is immutable

# .keys() /.values() / user will produce error - ValueError: too many values to unpack

# for item in 50:
#     print(item)
# ERROR : TypeError: 'int' object is not iterable

##----------------------  COUNTER  -------------------------

#   todo : Find the sum of the elements of the list 
my_list=[1,5,6,0,7,7,8,4,5,0,-1]
sum=0
for item in my_list:
    sum+=item
print('Sum is:', sum) # Sum is: 43


##----------------------  RANGE  -------------------------
#Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. 
# Starts from 0 and Step over by 1 by default 

print(range(100)) # range(0, 100)

for item in range(2,10):
    print(item)

#2,3,4,5,6,7,8,9

for item in range(2,10,2):
    print('->',item)

# -> 2
# -> 4
# -> 6
# -> 8

for item in range(2,10,-1):
    print(item)
# -1 - Does not work - no output

# But, it works incase of reverse iteration
for item in range(10,2,-2):
    print('->',item)

# -> 10
# -> 8
# -> 6
# -> 4

for item in range(10,2,-2):
    print('=',list(range(10)))

# = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]