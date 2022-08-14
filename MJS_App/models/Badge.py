from MJS_App.config.mysqlconnection import connectToMYSQL
from MJS_App import app
from MJS_App.models import QuizCheck

db = "make_jazz_simple"


class Badge:
    def __init__ (self, data):
        self.id = data['badges.id']
        self.topic = QuizCheck.find_topic(data['topic'])
        self.score = data['score']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def award_badge(cls, data):
        query = "INSERT INTO badges (topic, score, user_id, created_at, updated_at) VALUES ( %(topic)s, %(score)s, %(user_id)s, NOW(), NOW() );"
        return connectToMYSQL(db).query_db(query, data)

    @classmethod
    def get_badge_by_id(cls, id):
        query = "SELECT * FROM badges WHERE badges.id = %(id)s;"
        data = {
            "id":id
        }
        return connectToMYSQL(db).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM badges WHERE id = %(id)s;"
        return connectToMYSQL(db).query_db(query, data)

    @classmethod
    def update_badge(cls, data):
        query = "UPDATE badges SET score = %(score)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMYSQL(db).query_db(query, data)