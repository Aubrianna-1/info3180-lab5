# Add any model classes for Flask-SQLAlchemy here
from . import db
import datetime

class Movies(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True) #autoIncrement=True
    title = db.Column(db.String(150))
    description = db.Column(db.Text)
    poster = db.Column(db.String(100)) 
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at 
    
    def get_id(self):
        try:
            return #unicode(self, id) #python 2 support
        except NameError:
            return str(self.id) #python 3 support
        
    def __repr__(self):
        return '<User %r>' % (self.username)
        #return f'<Movie %r>' %(self.title)