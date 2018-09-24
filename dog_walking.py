
"""
    Author kamoga henry
    Tel :: 0701243139
    
"""

"""
    Task
    =====
Next, add a walk() method to both the Pets and Dog classes so that 
    when you call the method on the Pets class, each dog instance assigned to
    the Pets class will walk(). Save this as dog_walking.py. 
     This is slightly more difficult.

Start by implementing the method in the same manner as the speak() 
    method. As for the method in the Pets class, you will need to iterate
    through the list of dogs, then call the method itself.

The output should look like this:

Tom is walking!
Fletcher is walking!
Larry is walking!

"""


import time # to be used the apllication to stop for a while

print("")
print ("\t :::::::::::::: Welcome to the walking dog ::::::::::::::")
print("")
time.sleep(4)
# =========================== DOG INHERITANCE =========================
class Dog:
    # the sekelton of my class (attributes)
    def __init__(self, name, amount_of_dogs ):
        self.name = name
        self.amount_of_dogs = amount_of_dogs
        

    def speak (self,voice):
        # this sets the is_hungry to a bool (False) 
        return "%s voice is %s" %(self.name,voice)
    
    def walk (self):
        return "%s is walking " %(self.name)


#  local_dog comes from dog
class local_dog (Dog):
    pass

#  none_local_dog comes from dog
class none_local_dog (Dog):
    pass


class Pests:
    # creating my Empty tuple to hold instances of dogs
    my_dogs = ()
    def __init__(self,my_dogs):
        self.my_dogs = my_dogs

    def walk (self):
        for dog in self.my_dogs:
            print (dog.walk())
            time.sleep(4)


# defining dogs instances as a tuple passing in 3 class
DOGS_OBJECT = (local_dog("Tom",6),none_local_dog("Fletcher", 7), Dog("Larry", 9))

# PESTS instance takeing in a tuple of dogs
PESTS = Pests(DOGS_OBJECT)  

# method call
PESTS.walk() 
time.sleep(4)
print("")
print ("\t\tBy By By")
print("")
time.sleep(4)