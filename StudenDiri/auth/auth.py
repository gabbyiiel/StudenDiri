from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    return render_template  

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("loginpage.html", boolean=True)


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
        email = request.form.get('email')
        gender = request.form.get('gender')
        
        #function for verification
        if len(password) < 8:
            flash('Password is too short', category='error') 
            
        else:
            flash('Account Created', category='success')
            pass

    return render_template("signuppage.html")
