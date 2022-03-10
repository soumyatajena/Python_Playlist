# Exercise ! - Print space inplace of 0 and * in 1

picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]


for item in picture:
    for i in item:
        if(i):# 0 : False and 1: True by default
            print('*', end='') # to end the code in the same line
        else:
            print(' ', end='')
    print()

#    *   
#   ***  
#  *****
# *******
#    *
#    *