highest=0
def highest_even(num_list):
    for item in num_list:
        global highest
        if item%2==0 and item> highest:
            highest=item
    print(f'Highest even among {num_list} is {highest}')

num_list=[11,10,56,9,1,-3]
highest_even(num_list)

# Highest even among [11, 10, 56, 9, 1, -3] is 56

# OR

def highest_even(num_list):
    evens=[]
    for item in num_list:
        if item%2==0:
            evens.append(item)
    return max(evens)

print(highest_even(num_list=[11,10,56,9,1,-3]))

# 56 
