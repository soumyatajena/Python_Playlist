class PlayerCharacter:
    # Class Object Attribute - global in nature
    # It is not dynamic type - doesn't change acroos different attribute
    membership = True

    # Constructor method
    # It is dynamic - changes with each object
    def __init__(self, name, age):
        if(self.membership):
            self.name = name  # attributes
            self.age = age
            # OR
        if(PlayerCharacter.membership):
            self.name = name  # attributes
            self.age = age 
    
    def shout(self):
        print(f'my name is {self.name} and age is {self.age}')

player1 = PlayerCharacter('Soumyata', 25)
print(player1.membership) # True
player2 = PlayerCharacter('Sudee', 20)
print(player2.membership) # True

print(player1.shout())
print(player2.shout())

# Exercise

# Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1=Cat('meow1',3)
cat2=Cat('meow2',-39)
cat3=Cat('meow3',6)

# 2 Create a function that finds the oldest cat
def find_the_oldest(cat1,cat2,cat3):
    if(cat1.age>(cat2.age and cat3.age)):
        print(f"oldest is cat 1 with age {cat1.age}")
    elif(cat2.age>(cat1.age and cat3.age)):
        print(f"oldest is cat 2 with age {cat2.age}")
    else:
        print(f"oldest is cat 3 with age {cat3.age}")

find_the_oldest(cat1,cat2,cat3)
# oldest is cat 3 with age 6

#   OR

def get_oldest_cat(*args):
    return max(args)

print(f"The oldest cat is {get_oldest_cat(cat1.age,cat2.age,cat3.age)} years old")
# The oldest cat is 6 years old


