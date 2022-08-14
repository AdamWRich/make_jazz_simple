from MJS_App import app
from flask import render_template, redirect, request, session, flash
from MJS_App.models import QuizCheck, Badge, User

@app.route('/quiz/grade', methods=['POST'])
def grade_quiz():
    user_answers = [
        request.form['q1'],
        [request.form['q2']],
        request.form['q3'],
        request.form['q4'],
        [request.form['q5']]
    ]
    results = {
        'topic': QuizCheck.find_topic(request.form['topic']),
        'score': QuizCheck.grade(user_answers),
        'user_id':session['user_id'],
        'id': None
    }
    if results['score'] >= 4 :
        user = User.User.get_user_by_id(request.form['user_id'])
        for badge in user.badges:
            results['id'] = badge.id
            print(badge.topic)
            if QuizCheck.find_topic(badge.topic) == results['topic']:
                updated_badge_id = Badge.Badge.update_badge(results)
                return redirect(f'/quiz/results/{badge.id}')
        badge_id = Badge.Badge.award_badge(results)
        return redirect(f'/quiz/results/{badge_id}')
    else:
        score = results['score']
        return redirect(f"/quiz/results/{request.form['topic']}/{score*35}")


@app.route('/quiz/results/<int:badge_id>')
def passed_quiz_results(badge_id):
    if 'user_id' not in session:
        return redirect('/logout')
    badge = Badge.Badge.get_badge_by_id(badge_id)[0]
    print(badge)
    return render_template("quiz_results.html", theme = "pass", badge = badge, score = badge['score'])

@app.route('/quiz/results/<int:topic>/<int:adj_score>')
def failed_quiz_results(topic, adj_score):
    if 'user_id' not in session:
        return redirect('/logout')
    score = int(adj_score / 35)
    return render_template("quiz_results.html", theme = "fail", score = score, topic = QuizCheck.find_topic(topic))
