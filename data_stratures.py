"""
Author :: kamoga Henry
Tell :: 0701243139

"""

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
to_do_list ={}

title = "Adela"

# to_do_list = {'Adela': 'JoiningJoining1Joining2', 'Adela2': 'Joining2', 'Adela3': 'Joining3'}
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
            to_do_list[title] = items # add the title:item to the dictionary
            create_break()
            print ( title + "\t :: title Added well ")
            print ( items + "\t :: items Added well")
            create_break()
            print ("....operation done well....")
            create_break()
            
            
def find_specific_item (title_to_search):
    create_break()
    time.sleep(4)
    create_break()
    items_find = to_do_list[title_to_search]

    print ("\t title is ::: " + (title_to_search))
    print ("\t items are ::: " + items_find )
    create_break()
    print ("\t....Operation done well....")
    create_break()


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

def edit_specific_item(title_to_edit,items_to_edit):
    create_break()
    print ("\t Data in data base ")
    time.sleep(4)
    display_data()
    # title_and_items =items_to_edit
    to_do_list[title_to_edit] = items_to_edit
    print ("\tData after editing")
    time.sleep(4)
    display_data()
    print ("\t....Operation done well....")
    create_break()


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
    print ("\t....Operation done well....")
    create_break()

def display_options ():
    create_break()
    print ("Select your operation")
    print ("----------------------")
    print ("\t 0. To view your data.\n\t 1. Add items to the list.\n\t 2. Find a specific todo item on the list\n \t 3. Delete a specific todo item from the list.\n \t 4. Edit a specific todo item on the list. \n\t 5. clear the todo list\n \t 6. Log out.")
    create_break()

def start_the_application_interface ():
    display_options()
    while 1:
        # get user option
        user_option = int(input("Your number  ==> "))

        if user_option == 0:
            create_break()
            display_data()
            print ("\t....Operation done well....")
            create_break()

        if user_option == 1:
            create_break()
            title = input("Enter your title \n >>> ")
            item = input("Enter your item \n >>> ")
            add_items_to_list(title, item) # calling my function
            display_options()

        if user_option == 2:
            create_break()
            print ("\t ....Finding a items....")
            my_item = input("Enter your title name \n >>> ")
            find_specific_item(my_item)
            time.sleep(5)
            display_options()
            create_break()

        if user_option == 3:
            create_break()
            print ("...Deleting a specific todo item...")
            my_title = input("Enter your title to be deleted.\n >>> ")
            delete_specific_item(my_title)
            display_options()
            
        if user_option == 4:
            create_break()
            print ("....Editing a specific todo item...")
            title_to_be_edited = input("Enter your title name\n >>> ")
            new_item = input("Enter your new item name\n >>> ")
            edit_specific_item(title_to_be_edited, new_item)
            time.sleep(5)
            display_options()
        
        if user_option == 5:
            clear_a_list()
            create_break()
            print("...clear the todo list...")
            display_options()

        if user_option == 6:
            print ("...loging out user...")
            print ("\t thank for using the app")
            time.sleep(5)
            break
       
if __name__=='__main__':
    start_the_application_interface ()
  
