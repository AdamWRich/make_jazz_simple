import bcrypt
from MJS_App import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session, flash
from MJS_App.models.User import User

@app.route('/register')
def register():
    return render_template("index_register.html")

@app.route('/login')
def login():
    return render_template("log_in.html")

@app.route('/register/user', methods=['POST'])
def register_user():
    data = {
        "fname" : request.form['fname'],
        "lname": request.form['lname'],
        "email" : request.form['email'],
        "username" : request.form['username'],
        "password" : request.form['pass'],
        "confirm_password":request.form['confirm_pass']
    }
    if not User.verify_user(data):
        return redirect('/register')
    data['password'] = bcrypt.generate_password_hash(request.form['pass'])
    data.pop('confirm_password')
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect(f'/dashboard/{user_id}')

@app.route('/dashboard/<int:id>/')
def dashboard(id):
    return render_template('user_dash.html')
