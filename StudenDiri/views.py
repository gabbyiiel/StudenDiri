from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/login')
def login():
    return render_template("loginpage.html")

@views.route('/signup')
def sign_up():
    return render_template("signuppage.html")

@app.route('/')
@app.route('/index')
def index():
    
    return 'Hello world'