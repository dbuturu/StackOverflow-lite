
from app.api.question import model
from unittest import TestCase


class TestQuestion(TestCase):
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
        self.assertEquals(message, question.create(data))

    def test_question_get(self):
        data = self.question
        question = model.QuestionModel({})
        question.create(data)
        self.assertEquals(data, question.read(data.get('id')))
