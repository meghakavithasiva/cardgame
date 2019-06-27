import re


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def validate_email(self):
        return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", self.email))

    def validate_password(self):
        return bool(re.search(r"^[a-zA-Z0-9 ]*$", self.password))

    @staticmethod
    def create_user():
        name = input("Enter Username: ")
        email = input("Enter email:   ")
        pwd = input("Enter password:  ")
        new_user = User(name, email, pwd)
        if not new_user.validate_email():
            raise Exception("Not a valid email!!!")
        if not new_user.validate_password():
            raise Exception("Not a valid password!!!")
        f = open("user.txt", 'a')
        f.write('\n' + new_user.__str__())
        f.close()
        return new_user

    def print(self):
        print('Name: {}, Email: {}, Password: {}'.format(self.name, self.email, self.password))

    def __str__(self) -> str:
        return self.name + '|' + self.email + '|' + self.password


User.create_user()
