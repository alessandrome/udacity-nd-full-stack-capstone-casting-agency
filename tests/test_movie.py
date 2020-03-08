import unittest
import json
from . import dbunittest
from models import Movie


class MovieUnittest(dbunittest.DbUnittest):
    def test_movie_create(self):
        json_data = {'title': 'Test film', 'release_date': '1999-01-01'}
        res = self.client().post('/movies', json=json_data)
        data = json.loads(res.data)
        test_movie = Movie.query.filter(
            (Movie.title == json_data['title']) &
            (Movie.release_date == json_data['release_date'])).first()
        self.assertIsNotNone(test_movie)
        self.movies_id_to_delete.append(test_movie.id)
        self.assertEqual(res.status_code, 201)  # 201 code for 'Resource Created'
        self.assertIn('id', data)
        self.movies_id_to_delete.append(data['id'])
        self.assertEqual(data['title'], json_data['title'])
        self.assertEqual(data['release_date'], json_data['release_date'])

    def test_movie_list(self):
        res = self.client().get('/movies?page=1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('items', data)
        self.assertIn('total_items', data)
        self.assertIn('page', data)
        self.assertIn('pages', data)
        self.assertGreaterEqual(data['total_items'], len(data['items']))

    def test_movie_list_search(self):
        search_term = 'potter'
        res = self.client().get('/movies?page=1&search_term={}'.format(search_term))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('items', data)
        movies = data['items']
        for movie in movies:
            self.assertIn(search_term.lower(), movie['title'].lower())

    def test_movie_get(self):
        movie_name = 'Harry Potter and the Philosopher\'s Stone'
        movie_id = 1
        res = self.client().get('/movies/{}'.format(movie_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('id', data)
        self.assertIn('title', data)
        self.assertIn('release_date', data)
        self.assertIn('actors', data)
        self.assertEqual(data['title'], movie_name)

    def test_movie_patch(self):
        movie_edit_title = 'Edited'
        movie_edit_release_date = '2020-12-25'
        movie = Movie(title='to_edit', release_date='1998-01-01')
        movie.insert()
        self.movies_id_to_delete.append(movie.id)
        json_data = {
            'title': movie_edit_title,
            'release_date': movie_edit_release_date,
        }
        res = self.client().patch('/movies/{}'.format(movie.id), json=json_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('id', data)
        self.assertIn('title', data)
        self.assertIn('release_date', data)
        self.assertIn('actors', data)
        self.assertEqual(data['title'], movie_edit_title)
        self.assertEqual(data['release_date'], movie_edit_release_date)

    def test_movie_delete(self):
        movie = Movie(title='to_delete', release_date='1998-01-01')
        movie.insert()
        self.movies_id_to_delete.append(movie.id)
        res = self.client().delete('/movies/{}'.format(movie.id))
        self.assertEqual(res.status_code, 204)
