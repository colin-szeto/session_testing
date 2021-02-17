from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"
    #this would be the defaul
    return "You are not logged in <br><a href = '/login'></b>" + \
           "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    #if the submit button was pressed
    if request.method == 'POST':
        session['username'] = request.form['username'] # reassigning values of the input
        return redirect(url_for('index'))

    #this is the default redirect of the user
    return ''' 
	
   <form action = "/login" method = "post">
      <p><input type = text name = username /></p>
      <p><input type = submit value = Login /></p>
   </form>
	
   '''

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, host='127.0.0.1', port='5000')