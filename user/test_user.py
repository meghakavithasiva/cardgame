from unittest import TestCase

import user


class TestUser(TestCase):
    def test_print(self):
        user1 = user.User('TestUser', 'testpwd')
        self.assertEqual(user1.name, 'TestUser')
