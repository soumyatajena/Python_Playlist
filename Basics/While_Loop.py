i=0
while i<5:
    print(i)
    i+=1
else:
    print('else exists in "while loop" which will get exeuted')

# 0
# 1
# 2
# 3
# 4
# else exists in "while loop" which will get exeuted only if there is no "break"

## ----------------------------  BREAK  ------------------------
# it BREAKS out of the current enclosing loop
i=0
while i<5:
    print(i)
    break
else:
    print('else exists in "while loop" which will get exeuted')

# 0

## ----------------------------  CONTINUE  ------------------------
# it CONTINUES to the current enclosing loop
i=0
while i<5:
    i+=1
    continue
    print(i)

# No output as continue tells the cursor to continue from beginning once it hits the "CONTINUE" keyword

## ----------------------------  PASS  ------------------------
# it used as PLACEHOLDER, just to tell the compiler to pass that code until any logic is written
i=0
while i<5:
    pass
# e.g. let's say till now I haven't decided what to write in the logic part hence i PASS it to avoid compile error 


