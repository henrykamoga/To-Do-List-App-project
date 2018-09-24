"""
    Author kamoga henry
    Tel :: 0701243139
    
"""

"""
    Task
    ====
Create a Pets class that holds instances of dogs; this class is 
    completely separate from the Dog class. In other words, the Dog class 
    does not inherit from the Pets class. Then assign three dog instances to an 
    instance of the Pets class. Start with the following code below. 
    Save the file as pets_class.py. 

Your output should look like this:

I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course.

"""

import time # to be used the apllication to stop for a while

print("")
print ("\t :::::::::::::: Welcome to the OOP appliction ::::::::::::::")
print("")
# =========================== DOG INHERITANCE =========================
class Dog:
    # the sekelton of my class (attributes)
    def __init__(self, name, amount_of_dogs ):
        self.name = name
        self.amount_of_dogs = amount_of_dogs
        self.is_hungry = True

    def eat (self):
        # this sets the is_hungry to a bool (False) 
        self.is_hungry = False


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


# defining dogs instances as a tuple passing in 3 class
DOGS_OBJECT = (local_dog("Tom",6),none_local_dog("Fletcher", 7), Dog("Larry", 9))

# PESTS instance takeing in a tuple of dogs
PESTS = Pests(DOGS_OBJECT)  

print("")
print("\t I have the following inheritence dogs")
print ("\t=====================================")
print ("")
time.sleep(3)
print ("I have {} dogs.".format(len(PESTS.my_dogs)))
time.sleep(3)
for dog in PESTS.my_dogs:
    print ("{} is {} ".format(dog.name, dog.amount_of_dogs))
    time.sleep(3)
time.sleep(3)
print ("And they're all mammals, of course")
print("---------------------------------------------")
print("")

time.sleep(5)
#========================== HUNGRY DOGS =====================
print("")
print ("\tChecking weather dogs are hungry or not")
print ("\t========================================")
print("")
time.sleep(4)
print ("I have {} dogs.".format(len(PESTS.my_dogs)))
time.sleep(3)
for dog in PESTS.my_dogs:
    print ("{} is {} ".format(dog.name, dog.amount_of_dogs))
    time.sleep(3)
time.sleep(3)
print ("And they're all mammals, of course")

hungry_dogs = False
for dog in PESTS.my_dogs:
    if dog.is_hungry:
        hungry_dogs = True

if hungry_dogs:
    print ("\t____________________________checking them_______")
    time.sleep(5)
    print("My dogs are hungry.")
else:
    pass
print("---------------------------------------------")
print ("")
print ("\t let me give them food")
time.sleep(3)
print ("\t \t By By By")
time.sleep(3)
print ("")