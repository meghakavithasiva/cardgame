import re
import subprocess
import platform


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

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
User.cls()
user1.print()
