from doctest import FAIL_FAST


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
