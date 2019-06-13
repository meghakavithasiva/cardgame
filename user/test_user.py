from unittest import TestCase

import user


class TestUser(TestCase):
    def test_print(self):
        user1 = user.User('TestUser', 'Testpassword', 'testpwd')
        self.assertEqual(user1.name, 'TestUser')

    def test_validate_email(self):
        user1 = user.User('','invalidemail', '')
        self.assertFalse(user1.validate_email())
