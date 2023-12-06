from flask import Flask, render_template, g, redirect, url_for


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")



if __name__ == '__main__':
    app.run(debug=True)