# ----------------------------------  FUNCTIONS v/s METHODS -------------------------------

# Built-in Functions
list()
min()
max()
print()
input
type()

# User-build Functions


def some_random_fun():
    pass


some_random_fun()

# ==================================================================
# Built-in Methods - method names come after '.'

'helloo'.capitalize()
'helloo'.count()
[1, 2, 3].append()

# User-build Methods


# ----------------------------------  DOCSTRINGS -------------------------------

# DOCSTRINGS - is written between ''' ... ''' . GIves out info about the function

# 1 - using docstring
def some_random_fun():
    '''
    This function does nothing. Hover over the calling function to check its work.
    '''
    pass


some_random_fun()

# 2 - using help method
help(some_random_fun)  # another way to show the function info

# Help on function some_random_fun in module __main__:

# some_random_fun()
#     This function does nothing. Hover over the calling function to check its work.

# 3 - using dunder
print(some_random_fun.__doc__)
# This function does nothing. Hover over the calling function to check its work.


# ----------------------------------  ARGS v/s KWARGS -------------------------------

def super_func(*args):
    print(args)  # prints the item list as a tuple
    print(*args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5, 6))

# (1, 2, 3, 4, 5, 6)
# 1 2 3 4 5 6
# 21


def super_func(*args, **kwargs):
    print(kwargs)  # prints the item list as a dictionary
    print(*args)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, 6, num1=7, num2=8))

# {'num1': 7, 'num2': 8}
# 1 2 3 4 5 6
# 36

# RULE : Ordering  of arguments :
# params, *args, default parameters, **kwargs


def order_args(name, *args, i='HI', **kwargs):
    print(name, i, args, kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(order_args('Soumyata', 1, 2, 4, 3.6, num1=8.9, num2=-3))

# Soumyata HI (1, 2, 4, 3.6) {'num1': 8.9, 'num2': -3}
# 16.5
