from MJS_App import app
from MJS_App.models.User import User
from MJS_App.models.Badge import Badge
from flask import render_template, redirect, session, request

@app.route('/badge/delete', methods=['POST'])
def delete_badge():
    data = {
        'id':request.form['id']
    }
    Badge.delete(data)
    return redirect(f"/dashboard/{request.form['user_id']}")