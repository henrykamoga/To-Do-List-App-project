import time
from tasks import todo_list, create_task,delete_task,delete_all_tasks, mark_as_finished 
from accounts import accounts, add_account,log_in

def Create_a_break():
    # print an empty space
    print ("")

def display_data ():
    for  items in todo_list:
        print ("task to do ::: " + items)
        print("-------------------------")


# this will be promting user for a selection
def user_feed_back():
    print ("Select your options by typing a number:")
    print ("=======================================")
    user_options = "\t 0. Log out \n\t 1. Creat a task \n \t 2. Delete a task \n \t 3. Deleting all tasks \n \t 4. Mark a finished task\n\t 6. To view your data"
    print (user_options)

def start_the_application_interface (): 
    Create_a_break()
    user_feed_back()

    """ Geting user input selecton.."""
    Create_a_break()

    while 1:
        user_input_option = int(input("Your number  ==> "))
        """ Cheacking the inputs from user"""
        # option 1
        if user_input_option == 0:
            print ("...loging out user...")
            print ("\t thank for using the app")
            time.sleep(5)
            break

        if user_input_option == 1:
            Create_a_break()
            print ("Option 1 :: Creating a task")
            time.sleep(3)
            """ Getting user input task """
            user_task = input("\t Please Enter your task name \n>>> ")
            print ("task name to be added is :: " + user_task)
            time.sleep(4)
            create_task(user_task)
            print ("...Option Done well...")
            time.sleep(3)
            user_feed_back()
            Create_a_break()

        # option 2
        if user_input_option == 2:
            Create_a_break()
            print ("\t Option 2 :: Deleting a task")
            time.sleep(3)
            # check wheather list is empty or not
            if todo_list == []:
                print ("\t\t No items in the list to delete !!!")
                Create_a_break()
                print ("...Option Done well...")
                time.sleep(3)
                user_feed_back()
            else:
                # show what is in the list
                Create_a_break()
                print ("\t\t Items that are stored")
                print ("\t\t =====================")
                time.sleep(4)
                display_data()
                # get user input
                Create_a_break()
                item_to_delete = input("\t\t Enter item name to delete\n >>> ")
                
                # call my delete function
                delete_task(item_to_delete)
                Create_a_break()
                print ("\t\t Now the list is ")
                print ("\t\t ----------------")
                time.sleep(4)
                display_data()
                print (item_to_delete + " has been delete")
                time.sleep(4)
                print ("...Option Done well...")
                time.sleep(3)
                Create_a_break()
                Create_a_break()
                user_feed_back()


        if user_input_option == 3:
            Create_a_break()
            print ("\t Option 3 :: deleting all tasks")
            time.sleep(3)
            # function call
            print ("This is what in the task")
            Create_a_break()
            display_data()
            Create_a_break()
            print ("Deleting all tasks")
            time.sleep(4)
            # function call
            delete_all_tasks()
            Create_a_break()
            print ("...Option Done well...")
            time.sleep(3)
            user_feed_back()
            Create_a_break()

        if user_input_option == 4:
            Create_a_break()
            print ("\t Option 4 :: Marking a task finished")
            if todo_list == []:
                print ("\tNothing is in the list create a task first")
                print ("...Option Done well...")
                time.sleep(3)
                user_feed_back()
                Create_a_break()
            else:
                task_name_to_labeled = input("Enter the task label name to mark\n >>>") 
                # function call
                mark_as_finished(task_name_to_labeled)
                Create_a_break()
                print(task_name_to_labeled + " label marked well as follows")
                time.sleep(4)
                display_data()
                print ("...Option Done well...")
                Create_a_break()
                user_feed_back()

        if user_input_option == 6:
            Create_a_break()
            display_data ()
            Create_a_break()

def account_set_up ():
    #Adding account ie user name and password eg henry and hello respectively
    Create_a_break()
    print ("\t\t Welcome to To Do List APP")
    print ("\t\t +++++++++++++++++++++++++")
    time.sleep(5)

    print ("\t...Creating your account fisrt...")
    user_name = input("Enter your User name \n >>> ")
    password = input("Enter your Password \n >> ")
    # function call  from accounts.py
    add_account (user_name, password)
    print (" Account created well....")
    print ("\tRegistered user name ::: " + user_name)
    print ("\tRegistered user name ::: " + password)
    time.sleep(5)
    Create_a_break()
    Create_a_break()

def athenticate_user ():
    print ("\tLog in into the application")
    Entered_user_name = input("Enter your User name \n >>> ")
    Entered_password = input("Enter your Password \n >> ")

    # calling my function log_in 
    if log_in(Entered_user_name, Entered_password):
        start_the_application_interface()
    
    else:
        print ("\t user name " + Entered_user_name)
        print ("\t Password " + Entered_password)
        athenticate_user()

def Entery_of_the_App ():
    account_set_up()
    athenticate_user()    

if __name__ == '__main__':
    # calling my main method for the application
    Entery_of_the_App()
