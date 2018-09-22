'''
The expected output is a console application that
you can use to manage your to do list. 
It allows you to create an account and manipulate tasks

I have provided a structure for the code: FOLLOW INSTRUCTIONS
--------------------------------------------------------------
                    INSTRUCTIONS
--------------------------------------------------------------
1. Create a folder called src
hen1
2. Create the following files:
    - accounts.py
    - tasks.py
    - app.py

In the files, do the following:
'''
# --- accounts.py --
# This file contains code for managing your account

accounts = {}  # dictionary where key is the  password and value is User

# Write a function adds user details to accounts


def add_account(name, password):
    """
    Adds the key value pair to the accounts dictionary
    """
    pass


def login(name, password):
    """
    returns true if the password and corresponding name exist in the 
    accounts dicitionary
    """
    pass


# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = []

# Write a function creates a task


def create_task(task):
    """
    Adds the task (string value) to todo_list
    """
    pass

# Write a function deletes a task


def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    pass

# Write a function that marks a task finished


def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    pass

# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    pass


# ---- app.py ----
# This file contains the entry point to your tasks
# and the logic to manage it

from tasks import todo_list, create_task  # import other functions as well
from accounts import accounts, add_account  # import the function as well


if __name__ == "__main__":
    """
        Allow a person to input a name and a password

        E.g
    """
    name = input("Enter your name: ")

    """
        Let the person sign in. If there details do not exist,
        create an account for them

        E.g 
    """
    add_account("brian", "ndela35$$")


    """
        Provide options:
            1. creating a task
            2. deleting a task 
            3. deleting all tasks
            4. Marking a task finished

        E.g
    """

    print("Select Option:")
    print("1: Create Task")
# ..... skipped code
    selection = input("selection: ")

#Write code that implements the selected option

"""
The above should appear as
    Select Options:
        1. Create Task
        2 .... 
        3 ....
        4 ....

    selection:
"""

1. Commit yourselves to learning as much as you can.
2. Collaborate and communicate with your colleagues to ease the learning process.
3. Choose the right resources that will help you understand concepts.
4. Get familiar with the basics.
5. Avoid breaking under pressure or feel competitive against one another. Only push yourself to becoming a better developer.
6. Learn to think out of the box.
7. Join programming channels.
8. Get mentors.
9. Learn how to read code and documentation. Better yet, write code that you would love to read.
10. Avoid negativity or bias when approaching new languages.
11. Practice, practice and more practice. What you read should not stop in the book, you only get better with practice.
12. Do not fear to ask questions.
13. Have goals and commit yourselves to seeing them through.
14. Have patience, you cannot become a world class developer over night but aim at being a leader of your domain.

solo
===
Write a program which keeps prompting the user to guess a word.
The user is allowed up to ten guesses – write your code in such a way 
that the secret word and the number of allowed guesses are easy to change.
Print messages to give the user feedback.