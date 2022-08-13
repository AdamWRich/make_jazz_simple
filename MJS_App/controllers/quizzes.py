from MJS_App import app
from flask import render_template, redirect, request, session, flash
from MJS_App.models import QuizCheck, Badge, User

@app.route('/quiz/grade', methods=['POST'])
def grade_quiz():
    user_answers = [
        request.form['q1'], 
        request.form['q2'], 
        request.form['q3'], 
        request.form['q4'], 
        request.form['q5']
    ]
    results = {
        'topic': request.form['topic'],
        'grade': QuizCheck.grade(user_answers),
        'user_id':session['user_id']
    }
    if results['grade'] >= 4 :
        Badge.award_badge(results)
        session['results'] = results
    return redirect('/quiz/results')

@app.route('/quiz/results/')
def quiz_results():
    session['results'] = {
        'topic': "Building Chords and extensions",
        'grade':0
    }
    if session['results']['grade'] < 4:
        theme = "fail"
    else:
        theme = "pass"
    return render_template("quiz_results.html", theme = theme, grade = session['results']['grade'], topic = session['results']['topic'])