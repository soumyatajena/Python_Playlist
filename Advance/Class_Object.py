# OOPs

class Student: # Class 
    pass

obj1=Student() # Object Instantiation

#=========================================================

class PlayerCharacter:
    # Constructor method
    '''
    self - keyword - it defines the player character
    '''
    def __init__(self,name):
        self.name = name
    
    # method 1 - return type is - None
    def run(self):
        print('run')
    
    # method 2 - return type is - Done
    def run(self):
        return 'done'
    
    ## NOTE : if there is two overload methods then the python compiler will take the last overloaded method,
    ## in this case - o/p : done
    ## in case I comment the method 2 then - o/p : run None

player1=PlayerCharacter('Soumyata')
print(player1)
#<__main__.PlayerCharacter object at 0x0000024C54C9EDD0>

print(player1.name)
# Soumyata

print(player1.run())
# done

player2=PlayerCharacter('Sudeepta')
player2.attack = 90

## NOTE : One can directly assign a new property with value to an object and call it directly
print(player2.name,player2.attack)
# Sudeepta 90

print(player1.name,player1.attack) # ERROR
#AttributeError: 'PlayerCharacter' object has no attribute 'attack'