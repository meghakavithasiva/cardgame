import re
import subprocess
import platform
import os.path


class User:
    def __init__(self, name, password):
        self.name = name
        self.validate_user_length()
        self.validate_user_duplicate()
        self.password = password
        self.validate_passsword_length()
        self.validate_specialcase()

    def validate_user_length(self):
        name_length = len(self.name)
        if name_length < 4 or name_length > 10:
            raise Exception('Sorry, name length must be >=4 and <=10')

    def validate_passsword_length(self):
        password_length = len(self.password)
        if password_length < 6 or password_length > 8:
            raise Exception('Sorry, password length must be >=6 and <=8')

    def validate_specialcase(self):
        if '|' in self.password:
            raise Exception('Sorry you cannot use this symbol in password')
        if '|' in self.name:
            raise Exception('Sorry you cannot use this symbol in username')


    def validate_user_duplicate(self):
        if os.path.isfile('user.txt'):
            with open('user.txt', 'r') as f:
                for line in f:
                    splitted = line.split('|')
                    if self.name == splitted[0]:
                        raise Exception('Duplicate user name')
                    else:
                        print('user name is not duplicate')
        else:
            print('no validations')

    def validate_password(self):
        return bool(re.search(r"^[a-zA-Z0-9 ]*$", self.password))

    @staticmethod
    def create_user():
        name = input("Enter Username: ")
        pwd = input("Enter password:  ")

        new_user = User(name, pwd)
        if not new_user.validate_password():
            raise Exception("Not a valid password!!!")
        f = open("user.txt", 'a')
        f.write(new_user.__str__() + '\n')
        f.close()
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


