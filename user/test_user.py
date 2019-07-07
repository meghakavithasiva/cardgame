from unittest import TestCase

from user import User
from exceptions import SpecialCaseErrorException, EmptyValueException, LengthLimitException, DuplicateUserException
import os

class TestUser(TestCase):
    def test_empty_username(self):
        try:
            u1 = User('     ', 'password')
        except EmptyValueException:
            self.assertTrue('true', 'caught expected exception')
        else:
            self.fail('failed ')

    def test_empty_password(self):
        try:
            u1 = User('megha', '      ')
        except EmptyValueException:
            self.assertTrue('true', 'caught expected exception')
        else:
            self.fail('failed ')

    def test_length_username(self):
        try:
            u1 = User('meg','password')
        except LengthLimitException:
            self.assertTrue('true', 'caught expected exception')
        else:
            self.fail('failed ')

    def test_length_password(self):
        try:
            u1 = User('username','priko')
        except LengthLimitException:
            self.assertTrue('true', 'caught expected exception')
        else:
            self.fail('failed ')

    def test_special_case_username(self):
        try:
            u1 = User('M|gha','password')
        except SpecialCaseErrorException:
            self.assertTrue('true', 'caught expected exception')
        else:
            self.fail('failed ')

    def test_special_case_password(self):
        try:
            u1 = User('username','m|ghja')
        except SpecialCaseErrorException:
            self.assertTrue('true', 'caught expected exception')
        else:
            self.fail('failed ')

    def test_duplicate_user(self):
        if os._exists('test_user.txt'):
            os.remove('test_user.txt')
        u1 = User('Megha', 'password', 'test_user.txt')
        u1.add_user()
        try:
            User('Megha', 'password', 'test_user.txt')
        except DuplicateUserException:
            self.assertTrue('true', 'caught expected exception')
            os.remove('test_user.txt')
        else:
            self.fail('failed')


    def test_duplicate_user(self):
        if os._exists('test_user.txt'):
            os.remove('test_user.txt')
        u1 = User('user1', 'password', 'test_user.txt')
        u1.add_user()
        u2 = User('user2', 'password', 'test_user.txt')
        u2.add_user()
        i = 1
        with open(u1.file_name, 'r') as f:
                for line in f:
                    splitted = line.split('|')
                    self.assertEqual('user' + str(i), splitted[0])
                    i = i + 1

        os.remove('test_user.txt')
