import re


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def validate_email(self):
        return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", self.email))

    def print(self):
        print('Name: {}, Email: {}, Password: {}'.format(self.name, self.email, self.password))


user = User('siva', 'siva@siva.com', 'sivap')
user.print()
