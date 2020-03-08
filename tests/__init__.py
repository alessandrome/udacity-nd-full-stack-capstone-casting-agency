import unittest
from tests.test_actor import ActorUnittest
from tests.test_movie import MovieUnittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ActorUnittest('test_actor_create'))
    suite.addTest(ActorUnittest('test_actor_list'))
    suite.addTest(ActorUnittest('test_actor_list_search'))
    suite.addTest(ActorUnittest('test_actor_get'))
    suite.addTest(ActorUnittest('test_actor_patch'))
    suite.addTest(ActorUnittest('test_actor_delete'))

    suite.addTest(MovieUnittest('test_movie_create'))
    suite.addTest(MovieUnittest('test_movie_list'))
    suite.addTest(MovieUnittest('test_movie_list_search'))
    suite.addTest(MovieUnittest('test_movie_get'))
    suite.addTest(MovieUnittest('test_movie_patch'))
    suite.addTest(MovieUnittest('test_movie_delete'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
