from MJS_App.config.mysqlconnection import connectToMYSQL
from MJS_App import app

db = "make_jazz_simple"

class Badge:
    def __init__ (self, data):
        self.topic = data['topic']
        self.correct_answers = data['correct_answers']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def award_badge(cls, data):
        query = "INSERT INTO badge (topic, correct_answers, user_id, created_at, updated_at) VALUES ( %(topic)s, %(grade)s, %(user_id)s, NOW(), NOW() );"
        return connectToMYSQL(db).query_db(query, data)

    