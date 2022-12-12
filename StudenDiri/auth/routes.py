from flask import Blueprint, render_template, request, flash, redirect, session
from flask_login import login_user, login_required, logout_user, current_user
from StudenDiri import mysql

from . import auth
from .models import UserRepo

@auth.route('/')
def index():
    return render_template("landingpage/navbar.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form.get('inputUsername')
        password = request.form.get('inputPassword')
        user = UserRepo.login(username, password)
        if user:
            session['loggedin'] = True
            session['id'] = user
            session['username'] = username
            return redirect('/')
        else:
            return "<p> wrong? </p>"
    return render_template("auth/loginpage.html", boolean=True)

@auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect('login')


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
        print(firstname,lastname,gender)
        #function for verification
        if len(password) < 8:
            flash('Password must be at least 8 characters', category='error')
            return
            
        else:
            signup = UserRepo.signup(username,idnumber, firstname, lastname, email, course, college, password, gender,)
            flash('Account Created', category='success')
            return redirect('login')

    return render_template("auth/signup-page.html")


