
from app.api.user import model


class TestUser:
    @classmethod
    def setup_class(self):
        self.user = {
            'name': 'User Userson',
            'username': 'username',
            'password': 'password'
        }

    @classmethod
    def teardown_class(self):
        self.user.clear()

    def test_user_post(self):
        data = self.user
        user = model.UserModel({})
        expected_message = '{ message: "User added successful"}'
        message = user.sign_up(data)
        assert expected_message == message

    def test_user_get(self):
        data = self.user
        user = model.UserModel({})
        username = data.get('username')
        password = data.get('password')
        message = '{ message: "User singin successful"}'
        assert message == user.sign_in(username, password)
        assert data == user.read(data.get('username'))

    def test_user_put(self):
        user = model.UserModel({})
        message: str = '{ message: "User updated successful"}'
        assert message == user.update('username', 'bingo')

    def test_user_delete(self):
        data = self.user
        user = model.UserModel({})
        message = '{ message: "User deleted successful"}'
        assert message == user.delete(data.get('username'))
