import os
from datetime import datetime
from sqlalchemy import Column
from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()


def setup_db(app, database_path):
    """
    setup_db(app)
        binds a flask application and a SQLAlchemy service
    """
    database_path = database_path or os.environ['DATABASE_URL']
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


class ModelAction(db.Model):
    __abstract__ = True
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def long(self):
        raise NotImplementedError

    def short(self):
        raise NotImplementedError


class User(ModelAction):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def base_info(self):
        oauth_accounts = []
        for oauth in self.oauth_accounts:
            oauth_accounts.append(oauth.oauth_id)
        return {
            'id': self.id,
            'name': self.name,
            'oauth_id_list': oauth_accounts,
        }

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class UserAccount(ModelAction):
    __tablename__ = 'user_accounts'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    oauth_id = db.Column(db.String(255), primary_key=True)
    user = db.relationship('User', backref='oauth_accounts')

    def long(self):
        pass

    def short(self):
        pass


class Actor(ModelAction):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(32), nullable=True)
    movies = db.relationship('Movie', secondary='actor_movie_pivot', single_parent=True)
    _available_genders = ['male', 'female', 'other']

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

    def long(self):
        movies = []
        for movie in self.movies:
            movies.append(movie.short())
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'movies': self.movies,
        }

    @staticmethod
    def get_available_genders():
        return Actor._available_genders


class Movie(ModelAction):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.Date)
    actors = db.relationship('Actor', secondary='actor_movie_pivot', single_parent=True)

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def short(self):
        actors = []
        for actor in self.actors:
            actors.append(actor.short())
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': actors,
        }


class ActorMoviePivot(ModelAction):
    __tablename__ = 'actor_movie_pivot'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    actor = db.relationship('Actor', cascade='all, delete-orphan')
    movie = db.relationship('Movie', cascade='all, delete-orphan')
    __table_args__ = (db.UniqueConstraint('actor_id', 'movie_id', name='actor_movie_unique_participation_key'),)

    def long(self):
        pass

    def short(self):
        pass
