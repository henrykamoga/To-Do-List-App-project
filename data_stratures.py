
"""
You have been tasked with developing a model your todo items in a system using data
structures in python
1. Model a todo item using an appropriate data structures.
2. Model a todo-list that has a specific title and list of todo items(modelled in 1 above) using
the appropriate data structures.
3. Add todo items to the list of items on the your todo.
4. Find a specific todo item on the list
5. Delete a specific todo item from the list
6. Edit a specific todo item on the list.
7. Write a function to clear the todo list

    solution
    --------
        The application will be implement with a
            dictionary data stracture
"""

import time # will be used to track time

# creating an empty dictionary
# to_do_list ={}

title = "Adela"

to_do_list = {'Adela': 'JoiningJoining1Joining2', 'Adela2': 'Joining2', 'Adela3': 'Joining3'}
def create_break ():
    """ Creat a space in the console 
    """
    print ("")

def display_data ():
    """
        This prints out all the data in the dictionary
            ie key and value (title and items)
    """
    for title, items in to_do_list.items():
        print ("Title ::: " + title)
        print ("Items ::: " + items)
        print("--------------------")

def add_items_to_list (title, items):
    """
        This add the title and items to the to_do_list dictionary
            it will ask the user to enter the title (as akey) 
                and a item (as values)
                    2 arguments are used...
    """
    
    create_break()
    print ("\t Adding your to do list")
    print ("Adding data to the data base...")
    time.sleep(4) # wait for 5 seconds
    to_do_list = {title:items} # add the title:item to the dictionary
    create_break()
    print ( title + "\t :: title Added well ")
    print ( items + "\t :: items Added well")
    create_break()
    print ("....operation done well....")
    create_break()
    
    
def find_specific_item (title_to_search):
    create_break()
    print ("\t Finding a items....")
    time.sleep(4)
    create_break()
    items_find = to_do_list[title_to_search]

    print ("\t title is ::: " + (title_to_search))
    print ("\t items are ::: " + items_find )

    create_break()


find_specific_item("Adela2")
def delete_specific_item (title_to_delete):
    create_break()
    print ("\tDeleting title and its items ")
    title = to_do_list.keys()
    """
        Collect all the keys in the dictionary into right_title var
    """
    right_title = to_do_list[title_to_delete]

    print ("Cheacking current list ::")
    time.sleep(4)
    display_data() # function call
    create_break()
    print ("Deleting title and items for >>> " + title_to_delete)
    time.sleep(4)
    to_do_list.pop(title_to_delete)
    create_break()
    display_data()
    print ("\t....Operation done well....")
    create_break()


# delete_specific_item('Adela2')

def clear_a_list ():
    create_break()
    print ("Cheacking current list")
    create_break()
    time.sleep(4)
    print ("\t List is ::")
    create_break()
    display_data() 
    create_break()
    print ("\tRemoving all the title and items")
    create_break()
    to_do_list.clear()
    time.sleep(4)
    print ("\tList is now Empty  create a new ...")
    create_break()
