""" user data"""


class UserModel:

    def __init__(self, users: dict):
        self.users = users

    def sign_up(self, user: dict):
        self.users.update({user.get('username'): user})
        return '{ message: "User added successful"}'

    def sign_in(self, username: str, password: str):
        self.users.fromkeys(password) == username
        return '{ message: "User singin successful"}'

    def read(self, username: str):
        return self.users.get(username)

    def update(self, user):
        if user.get('username'):
            self.users.update({user.get('username'): user})
            return '{ message: "User updated successful"}'

    def delete(self, username: str):
        self.users.pop(username)
        return '{ message: "User deleted successful"}'
