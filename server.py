
from flask import Flask, request, flash
from flask import redirect, render_template, Response, make_response
from accounts import User_Accounts 
from tasks import User_task

app = Flask(__name__)
app.secret_key = 'henry'
user_accounts = User_Accounts()
user_action = User_task()

def reply_to_remote(reply):
    response = Response(reply)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

# main pages for navigetion
@app.route('/')
def get_index ():
    return reply_to_remote(render_template('index.html'))

@app.route('/index')
def serve_index ():
    return reply_to_remote(render_template('index.html'))


@app.route('/register')
def serve_register ():
    return reply_to_remote(render_template('register.html'))

@app.route('/profile')
def serve_profile ():
    return reply_to_remote(render_template('profile.html'))


@app.route('/user_log_in', methods = ['POST'])
def user_log_in ():
    if request.method == 'POST':
        
        user_stored_name = 'henry'
        user_stored_password = 'moga'
        user_name = request.form['user_name']
        user_password =  request.form['user_password']
        # get the user name and password from the accounts
        if user_name == user_stored_name and user_password == user_stored_password:
            return reply_to_remote(render_template('profile.html'))

        else:
            return reply_to_remote(render_template('index.html'))
    
        
        

@app.route('/user_register', methods = ['POST'])
def user_register ():
    if request.method == 'POST':
        user_name = request.form['username']
        user_password = request.form['password']
        print ("")
        # get the use name and password and store the in a dictionary (accounts)
        user_accounts.add_account(user_name,user_password)
        return reply_to_remote(render_template('about.html'))


"""
    user taks
"""


@app.route('/create_task', methods = ['POST'])
def create_task ():
    if request.method == 'POST':
        task_name = request.form['task_name'] 
        item_name = request.form['item_name']        
        if item_name and task_name:
            user_action.create_task(item_name,task_name)
            return reply_to_remote(render_template('profile.html'))
        else:
            return reply_to_remote("Please enter our task !!!")


@app.route('/delete_all_tasks',methods=['GET'])
def delete_all_tasks ():
    delete_action = user_action.delete_all_tasks()
    return reply_to_remote ( delete_action ) #'Task deleted well....'


if __name__=="__main__":
    app.debug=1
    
    app.run(threaded=1)
    # app.run("0.0.0.0",44444, threaded=1)