import unittest
import os
from app import create_app
from models import setup_db, db, Movie, Actor, ActorMoviePivot


class DbUnittest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app.config['WTF_CSRF_ENABLED'] = False  # In case of WTF from use
        self.client = self.app.test_client
        setup_db(self.app, os.environ['TEST_DATABASE_URL'])

        # binds the app to the current context
        with self.app.app_context():
            self.db = db
            self.actors_id_to_delete = []
            self.movies_id_to_delete = []

    def tearDown(self) -> None:
        """Executed after reach test. Deleting models created to test"""
        Movie.query.filter(Movie.id.in_(self.movies_id_to_delete)).delete(synchronize_session=False)
        self.movies_id_to_delete = []
        Actor.query.filter(Actor.id.in_(self.actors_id_to_delete)).delete(synchronize_session=False)
        self.actors_id_to_delete = []
        self.db.session.commit()
