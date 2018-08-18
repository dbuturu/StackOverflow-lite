from app.api.comment import model


class TestComment():
    @classmethod
    def setup_class(self):
        self.comment = {
            'id': '1',
            'title': 'The symbols used wrongly',
            'comment': '== in not the same as ==='
        }

    @classmethod
    def teardown_class(self):
        self.comment.clear()

    def test_comment_post(self):
        data = self.comment
        comment = model.CommentModel({})
        message = '{ message: "comment added successful"}'
        assert message == comment.create(data)

    def test_comment_get(self):
        data = self.comment
        comment = model.CommentModel({})
        assert data == comment.read(data.get('id'))

    def test_comment_put(self):
        data = self.comment
        comment = model.CommentModel({})
        message = '{ message: "comment updated successful"}'
        assert message == comment.update(
            data.get('id'))

    def test_comment_delete(self):
        data = self.comment
        comment = model.CommentModel({})
        message = '{ message: "comment deleted successful"}'
        assert message == comment.delete(data.get('id'))
