import re
import subprocess
import platform
import os.path

# from user.exceptions import EmptyValueException, SpecialCaseErrorException, LengthLimitException
from exceptions import EmptyValueException, SpecialCaseErrorException, LengthLimitException, DuplicateUserException
# from exceptions.EmptyValueException


class User:
    def __init__(self, name, password, file_name='user.txt'):
        self.file_name = file_name
        self.name = name.strip()
        self.password = password.strip()
        self.validate_empty_space()
        self.validate_user_length()
        self.validate_user_duplicate()
        self.validate_password_length()
        self.validate_special_case()


    def validate_user_length(self):
        name_length = len(self.name)
        if name_length < 4 or name_length > 10:
            raise LengthLimitException('Sorry, name length must be >=4 and <=10')

    def validate_password_length(self):
        password_length = len(self.password)
        if password_length < 6 or password_length > 8:
            raise LengthLimitException('Sorry, password length must be >=6 and <=8')

    def validate_special_case(self):
        if '|' in self.password:
            raise SpecialCaseErrorException('Sorry you cannot use | symbol in password')
        if '|' in self.name:
            raise SpecialCaseErrorException('Sorry you cannot use | symbol in username')

    def validate_empty_space(self):
        if len(self.name) == 0:
            raise EmptyValueException('Sorry, no empty spaces should be used in username')
        if len(self.password) == 0:
            raise EmptyValueException('Sorry, no empty spaces should be used in password')

    def validate_user_duplicate(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'r') as f:
                for line in f:
                    splitted = line.split('|')
                    if self.name == splitted[0]:
                        raise DuplicateUserException('Duplicate user name')

    def add_user(self):
        f = open(self.file_name, 'a')
        f.write(self.name + '|' + self.password + '\n')
        f.close()

    @staticmethod
    def create_user():
        name = input("Enter Username: ")
        pwd = input("Enter password:  ")
        new_user = User(name, pwd)
        new_user.add_user()
        return new_user

    def print(self):
        print('Name: {}, Password: {}'.format(self.name, self.password))
        print('\n\n\n')

    def __str__(self) -> str:
        return self.name + '|' + self.password

    @staticmethod
    def cls():
        command = "cls" if platform.system().lower() == "windows" else "clear"
        # Action
        return subprocess.call(command) == 0

user1 = User.create_user()
