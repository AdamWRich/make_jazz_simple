from MJS_App import app
from MJS_App.models.User import User
from flask import render_template, redirect, session


@app.route('/lesson1')
def lesson1():
    return render_template("lesson1.html")

@app.route('/quiz1')
def quiz1():
    return render_template("quiz1.html")