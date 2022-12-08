from flask import Blueprint, render_template, request, flash
from . import auth
from StudenDiri.models.UserRepo import UserRepo

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
        firstname = request.form.get('inputFirstname')
        lastname = request.form.get('inputLastname')
        email = request.form.get('inputEmail')
        college = request.form.get('college-select')
        idnumber = request.form.get('inputIdnumber')
        course = request.form.get('course-select')
        password = request.form.get('inputPassword')
        gender = request.form.get('Gender')
        username = request.form.get('inputUsername')
        
        #function for verification
        if len(password) < 8:
            flash('Password is too short', category='error') 
            
        else:
             signup = UserRepo.signup(username,idnumber, firstname, lastname, email, course, college, password, gender,)
             flash('Account Created', category='success')
             pass

    return render_template("auth/signup-page.html")
