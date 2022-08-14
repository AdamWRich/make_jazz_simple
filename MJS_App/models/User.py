from MJS_App.config.mysqlconnection import connectToMYSQL
from flask import flash
import re
from MJS_App import app
from MJS_App.models import Badge
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = "make_jazz_simple"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.username = data['username']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.badges = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, username, password, created_at, updated_at) VALUES ( %(fname)s, %(lname)s, %(email)s, %(username)s, %(password)s, NOW(), NOW() );"
        return connectToMYSQL(db).query_db(query, data)


    @classmethod
    def get_user_by_username(cls, data):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        return connectToMYSQL(db).query_db(query, data)

    @classmethod
    def get_user_by_id(cls, id):
        query = "SELECT * FROM users LEFT JOIN badges ON badges.user_id = users.id WHERE users.id = %(id)s;"
        data = {
            "id":id
        }
        result = connectToMYSQL(db).query_db(query, data)
        current_user = cls(result[0])
        if result[0]['topic']: 
            for row in result:
                current_user.badges.append(Badge.Badge(row))

        return current_user
    
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, username = %(username)s WHERE id = %(id)s;"
        return connectToMYSQL(db).query_db(query, data)


    @staticmethod
    def verify_user(user, usage):
        use = usage
        is_valid = True
        if user['fname'] and len(user['fname'])<2 :
            flash(f"First name must be at least 3 characters!", '{use}')
            print("line 31")
            is_valid = False
        if " " in user['fname'] or " " in user['lname']:
            flash(f"Please insert names without spaces!", '{use}')
            is_valid = False
        if user['fname'].isalpha() == False:
            flash(f"Please insert names without numbers!", '{use}')
        if user['lname'].isalpha() == False:
            flash(f"Please insert names without numbers!", '{use}')
        if user['lname'] and len(user['lname'])<2:
            flash(f"Last name must be at least 3 characters!", '{use}')
            is_valid = False
        if 'password' not in list(user.keys()):
            return is_valid
        if user['email'] == "":
            flash(f"Please insert an email!", '{use}')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']) or " " in user['email']:
            flash(f"Invalid email address!", '{use}')
            is_valid = False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMYSQL(db).query_db(query, user)        
        if len(results) >= 1:
            flash(f"Email already taken.", '{use}')
            print("line 49")
            is_valid = False
        if len(user['password']) < 8:
            flash(f"Password must be 8 characters!", '{use}')
            print("line 53")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash(f"Passwords must match!", '{use}')
            print("line 57")
            is_valid = False
        return is_valid
