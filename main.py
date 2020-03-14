from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/new')
def new():
    return render_template("new.html")

app.run(host='0.0.0.0', port=8080)