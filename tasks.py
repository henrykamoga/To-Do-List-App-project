
"""
Author :: kamoga Henry
Tell :: 0701243139

"""

# creat an empty list
todo_list = {}

class User_task ():

    #  function to create a task
    def create_task(self,task_name, item_name):
        """
            This function creats a task from a user 
                in form of a word or sentence...
        """
        # add user input in the list
        todo_list[task_name] = item_name
        print (todo_list)

    #=====================
    def delete_all_tasks(self):
        # for task in todo_list:
        print(todo_list)
        del todo_list
        print(todo_list)

