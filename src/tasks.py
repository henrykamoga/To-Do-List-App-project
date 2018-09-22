
# creat an empty list
todo_list = []
#  function to create a task
def create_task(task):
    """
        This function creats a task from a user 
              in form of a word or sentence...
    """
    # add user input in the list
    todo_list.insert(0, task)

def delete_task(task):
    """
        This deletes an item from the list
    """
    todo_list.remove(task)


#=====================
def delete_all_tasks():
    # for task in todo_list:
    del todo_list[:]

delete_all_tasks()

#===================
""" this marks the finished item"""
def mark_as_finished(item_to_find):
    global todo_list
    for item in todo_list:
        if item == item_to_find:
            todo_list[todo_list.index(item_to_find)] = item+" [finished]"



