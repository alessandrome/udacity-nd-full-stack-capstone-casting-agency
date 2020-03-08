import unittest
import json
from . import dbunittest
from models import Actor


class ActorUnittest(dbunittest.DbUnittest):
    def test_actor_create(self):
        json_data = {'name': 'Lara Croft', 'age': 31, 'gender': 'female'}
        res = self.client().post('/actors', json=json_data)
        data = json.loads(res.data)
        test_actor = Actor.query.filter(
            (Actor.name == json_data['name']) &
            (Actor.age == json_data['age']) &
            (Actor.gender == json_data['gender'])).first()
        self.assertIsNotNone(test_actor)
        self.actors_id_to_delete.append(test_actor.id)
        self.assertEqual(res.status_code, 201)  # 201 code for 'Resource Created'
        self.assertIn('id', data)
        self.actors_id_to_delete.append(data['id'])
        self.assertEqual(data['name'], json_data['name'])
        self.assertEqual(data['age'], json_data['age'])
        self.assertEqual(data['gender'], json_data['gender'])

    def test_actor_list(self):
        res = self.client().get('/actors?page=1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('items', data)
        self.assertIn('total_items', data)
        self.assertIn('page', data)
        self.assertIn('pages', data)
        self.assertGreaterEqual(data['total_items'], len(data['items']))

    def test_actor_list_search(self):
        search_term = 'daniel'
        res = self.client().get('/actors?page=1&search_term={}'.format(search_term))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('items', data)
        actors = data['items']
        for actor in actors:
            self.assertIn(search_term.lower(), actor['name'].lower())

    def test_actor_get(self):
        actor_name = 'Daniel Radcliffe'
        actor_id = 3
        res = self.client().get('/actors/{}'.format(actor_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('id', data)
        self.assertIn('name', data)
        self.assertIn('age', data)
        self.assertIn('gender', data)
        self.assertEqual(data['name'], actor_name)

    def test_actor_patch(self):
        actor_edit_name = 'Edited'
        actor_edit_age = 10
        actor_edit_gender = 'other'
        actor = Actor(name='to_edit', age=50, gender='male')
        actor.insert()
        self.actors_id_to_delete.append(actor.id)
        json_data = {
            'name': actor_edit_name,
            'age': actor_edit_age,
            'gender': actor_edit_gender,
        }
        res = self.client().patch('/actors/{}'.format(actor.id), json=json_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIn('id', data)
        self.assertIn('name', data)
        self.assertIn('age', data)
        self.assertIn('gender', data)
        self.assertEqual(data['name'], actor_edit_name)
        self.assertEqual(data['age'], actor_edit_age)
        self.assertEqual(data['gender'], actor_edit_gender)

    def test_actor_delete(self):
        actor = Actor(name='to_delet', age=50, gender='male')
        actor.insert()
        self.actors_id_to_delete.append(actor.id)
        res = self.client().delete('/actors/{}'.format(actor.id))
        self.assertEqual(res.status_code, 204)
