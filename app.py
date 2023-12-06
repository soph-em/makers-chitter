from flask import Flask, render_template, g, redirect, url_for, request, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import * 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/create_account')
def get_create_account():
    return render_template("create_account.html")

@app.route("/create_account", methods=['POST'])
def create_account():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    print('failing here')

    user = User(None, request.form['username'], request.form['display_name'], request.form['email'], request.form['password'])
    if not user.is_valid():
        print('user not valid')
        return render_template('create_account.html', user=user, errors = user.generate_errors()), 400
    print('failing here 2')
    user = repository.create(user)
    print('created user')
    return redirect('/dashboard')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run(debug=True)