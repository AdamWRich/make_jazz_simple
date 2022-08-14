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
    if not User.verify_user(data, 'registration'):
        return redirect('/register')
    data['password'] = bcrypt.generate_password_hash(request.form['pass'])
    data.pop('confirm_password')
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect(f'/dashboard/{user_id}')

@app.route('/login_user', methods=['POST'])
def login_user():
    user = User.get_user_by_username(request.form)
    if not user:
        flash("Username not found", 'login')
        return redirect('/login')
    if not bcrypt.check_password_hash(user[0]['password'], request.form['password']):
        flash("Invalid password", 'login')
        return redirect('/login')
    session['user_id'] = user[0]['id']
    current_user_id = session['user_id']
    return redirect(f'/dashboard/{current_user_id}')

@app.route('/dashboard/<int:id>/')
def dashboard(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if session['user_id'] != id:
        return redirect('/login')
    current_user = User.get_user_by_id(id)
    return render_template('user_dash.html', user = current_user)

@app.route('/user/update', methods=['POST'])
def update_user():
    data = {
        "id":request.form['id'],
        "fname" : request.form['fname'],
        "lname": request.form['lname'],
        "email" : request.form['email'],
        "username" : request.form['username'],
    }
    
    if not User.verify_user(data, 'update'):
        return redirect(f"/user/{session['user_id']}/settings")
    User.update_user(data)
    return redirect(f"/dashboard/{session['user_id']}")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/register')

