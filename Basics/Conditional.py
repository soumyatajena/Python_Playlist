# Conditional Syntax

age=input('Enter your age:')
if int(age)>18:
    is_old=True
    is_licenced = True
elif int(age)==18:
    is_old=False
    is_licenced = True
else:
    is_old=False
    is_licenced = False

if is_old and is_licenced:
    print('You are old enough to drive!')
elif is_licenced:
    print('Hurray you have a learner license !')
else:
    print("Wait a bit longer to drive :(")

## ------------------------- Truthy v/s Falsy --------------------

username='Soumyata'
password = 12345

# here username and password is evaluated as boolean value 
if username and password: 
    print('User Exists')
else:
    print('Please register!!')

# o/p - User Exists

## ------------------------- Ternary Operator --------------------

is_friend=True

# condition_if_true if condition else condition_if_else
can_message="message allowed" if is_friend else 'not allowed to message'
print(can_message) # message allowed


## ------------------------- Logical Operators --------------------

print( 0 != 1) # True - coz 0 is not equal to 1
print( 0 != 0) # False - coz 0 is equal to 0

# not - operator is both function and keyword
print(not(True)) # False
print(not(1==1)) # False

## ------------------------- is v/s == --------------------

#Python does not convert type when checking with comparison operature

# == - checks the value
print(True == 1) # True

# is - checks the memory location
print(True is 1) # False

# WARNING - "is" with a literal. Did you mean "=="?
print('1' is '1') # True

# EXCEPTION - empty lists takes separate memory location
print([] is []) # False

