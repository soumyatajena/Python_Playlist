# := - assignment expression - assigns values to variables as part of larger expression

a = 'Hheeelllooo'
# we are computing len() twice here
if(len(a)>10):
    print(f'too long {len(a)} elements')
# too long 11 elements

#  OR - use walrus op

if((n:=len(a))>10):
    print(f'too long {n} elements')
# too long 11 elements

while((n:=len(a)))>1:
    print(n)
    a=a[:-1] # assign one less letter
print(a)

# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# H