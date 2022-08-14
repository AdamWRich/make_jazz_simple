from MJS_App import app
from MJS_App.models.User import User
from flask import render_template, redirect, session


@app.route('/lesson1')
def lesson1():
    return render_template("lesson1.html")

@app.route('/quiz1')
def quiz1():
    return render_template("quiz1.html")

@app.route('/user/<int:id>/settings')
def user_settings(id):
    current_user = User.get_user_by_id(id)
    return render_template('user_settings.html', user = current_user)