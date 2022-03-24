class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        self.sounds = sounds
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        self.sounds = sounds
        return f'{sounds}'


# 1 Add another Cat
class Jessi(Cat):
    def sing(self, sounds):
        self.sounds = sounds
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
simonCat = Simon('Simon cat', 23)
simonCat.sounds = "simonCat meow!"
sallyCat = Sally('Sally cat', 3)
sallyCat.sounds = "sallyCat meow!"
jessiCat = Jessi('Jessi cat', 27)
jessiCat.sounds = "jessiCat meow!"

my_cats = []
# 3 Instantiate the Pet class with all your cats use variable my_pets
my_cats.append(simonCat)
my_cats.append(sallyCat)
my_cats.append(jessiCat)

my_pets = Pets(my_cats)
# 4 Output all of the cats walking using the my_pets instance
for pet in my_pets.animals:
    print(pet.walk())  # This is already happening in Pet.walk()
for cat in my_cats:
    print(cat.sounds)
    # OR

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_cats = [Simon('Simon cat', 23), Sally(
    'Sally cat', 3), Jessi('Jessi cat', 27)]
# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()
