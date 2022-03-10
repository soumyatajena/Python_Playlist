# def - define function

def say_hello():
    print('Hello!')


say_hello()
# Hello!

#-----------------------------------------------------------

# parameters


def say_hello(name, emoji):
    print(f'Hello {name}{emoji}')


# positional arguments - position matters for args
say_hello('Soumyata', ' 😊')
# Hello Soumyata 😊

#------------------------------------------------------------

# Default Parameters


def say_hello(emoji=' 😎', name='Default Name'):
    print(f'Hello {name}{emoji}')


# keyword arguments - not advised
say_hello(emoji=' 😊', name='Soumyata')
# Hello Soumyata 😊

say_hello()
# Hello Default Name 😎

#-------------------- FUNC WITH RETURN TYPE ---------------


def sum(num1, num2):
    return num1+num2


print(sum(8, 9))  # 17
