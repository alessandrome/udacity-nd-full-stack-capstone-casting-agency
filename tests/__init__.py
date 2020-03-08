import unittest
from tests.test_actor import ActorUnittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ActorUnittest('test_actor_create'))
    suite.addTest(ActorUnittest('test_actor_list'))
    suite.addTest(ActorUnittest('test_question_list_search'))
    suite.addTest(ActorUnittest('test_actor_get'))
    suite.addTest(ActorUnittest('test_actor_patch'))
    suite.addTest(ActorUnittest('test_actor_delete'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
