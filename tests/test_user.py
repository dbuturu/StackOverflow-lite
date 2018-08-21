
from app.api.user import model


class TestUser:
    @classmethod
    def setup_class(cls):
        cls.user = {
            'name': 'User Userson',
            'username': 'username',
            'password': 'password'
        }

    @classmethod
    def teardown_class(cls):
        cls.user.clear()

    def test_user_post(self):
        data = self.user
        user = model.UserModel({})
        expected_message = '{ message: "User added successful"}'
        message = user.sign_up(data)
        assert expected_message == message

    def test_user_get(self):
        data = self.user
        user = model.UserModel({})
        user.sign_up(data)
        username = data.get('username')
        password = data.get('password')
        message = '{ message: "User singin successful"}'
        assert message == user.sign_in(username, password)
        assert data == user.read(data.get('username'))

    def test_user_put(self):
        data = self.user
        update = {
            'name': 'User Bingo',
            'username': 'username',
            'password': 'password'
        }
        user = model.UserModel({})
        user.sign_up(data)
        message: str = '{ message: "User updated successful"}'
        assert message == user.update(update)

    def test_user_delete(self):
        data = self.user
        user = model.UserModel({})
        user.sign_up(data)
        message = '{ message: "User deleted successful"}'
        assert message == user.delete(data.get('username'))
