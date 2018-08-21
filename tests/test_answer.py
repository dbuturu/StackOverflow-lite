
from app.api.answer import model


class TestAnswer():
    @classmethod
    def setup_class(cls):
        cls.answer = {
            'id': '1',
            'title': 'The words wrongly spelt',
            'question': 'Big is not the same as big'
        }

    @classmethod
    def teardown_class(cls):
        cls.answer.clear()

    def test_answer_post(self):
        data = self.answer
        answer = model.AnswerModel({})
        message = '{ message: "answer added successful"}'
        assert message == answer.create(data)
