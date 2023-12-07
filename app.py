from flask import Flask, render_template, g, redirect, url_for, request, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import * 
from lib.peep_repository import *

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key="anystringhere"



@app.route("/")
def index():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps = repository.list_timeline_peeps()

    return render_template("index.html", peeps=peeps)

@app.route('/create_account')
def get_create_account():
    return render_template("create_account.html")

#POST Create account
@app.route("/create_account", methods=['POST'])
def create_account():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    user = User(None, request.form['username'], request.form['display_name'], request.form['email'], request.form['password'])
    if not user.is_valid():
        return render_template('create_account.html', user=user, errors = user.generate_errors()), 400

    user = repository.create(user)
    return redirect('/dashboard')

@app.route('/login_account')
def display_login():
    return render_template('login.html')

#POST login account
@app.route('/login_account', methods=['POST'])
def login_account():
    email = request.form['email']
    password_attempt = request.form['password']
    print(email)
    print(password_attempt)
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    if repository.check_password(email, password_attempt):
        user = repository.find_by_email(email)
        # Set the user ID in session
        print(user.id)
        session['user_id'] = user.id

        return redirect('/')
    else:
        return render_template('login.html')

@app.route('/account')
def account_page():
    if 'user_id' not in session:
        # No user id in the session so the user is not logged in.
        return redirect('/login_account')
    else:
        # The user is logged in, display their account page.
        return render_template('account.html')

@app.route('/logout')
def logout_account():
    session.clear()
    return redirect('/')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run(debug=True)