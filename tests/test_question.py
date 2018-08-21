
from app.api.question import model


class TestQuestion():
    @classmethod
    def setup_class(self):
        self.question = {
            'id': '1',
            'title':
            'E1120:No value for argument Big in unbound method call',
            'question': 'frog.size(Big)'
        }

    @classmethod
    def teardown_class(self):
        self.question.clear()

    def test_question_post(self):
        data = self.question
        question = model.QuestionModel({})
        message = '{ message: "question added successful"}'
        assert message == question.create(data)

    def test_question_get(self):
        data = self.question
        question = model.QuestionModel({})
        question.create(data)
        assert data == question.read(data.get('id'))
