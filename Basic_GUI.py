# Exercise ! - Print space inplace of 0 and * in 1

picture=[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,1,1,0,0,0]
]


for item in picture:
    for i in item:
        if(i==0):
            print(' ', end='')
        else:
            print('*', end='')
    print()

#    *   
#   ***  
#  *****
# *******
#    *
#   **