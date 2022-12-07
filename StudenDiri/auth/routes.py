from flask import Blueprint, render_template, request, flash
from . import auth
#from StudenDiri.models.UserRepo import UserRepo

@auth.route('/')
def index():
    return render_template("auth/signup-page.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("auth/loginpage.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p> logout</p>"


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        college = request.form.get('college')
        idnumber = request.form.get('idnumber')
        course = request.form.get('course')
        password = request.form.get('password')
        gender = request.form.get('gender')
        username = request.form.get('username')
        
        #function for verification
        if len(password) < 8:
            flash('Password is too short', category='error') 
            
        # else:
        #     signup = UserRepo.signup(username,idnumber, firstname, lastname, email, course, college, password, gender,)
        #     flash('Account Created', category='success')
        #     pass

    return render_template("auth/signuppage.html")
