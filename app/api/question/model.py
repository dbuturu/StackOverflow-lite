
class QuestionModel():

    def __init__(self, questions: dict):
        self.questions = questions

    def create(self, question):
        self.questions.update({question.get('id'): question})
        return '{ message: "question added successful"}'

    def read(self, id):
        return self.questions.get(id)

    def read_all(self):
        return self.questions

    def update(self, question):
        if question.get('id'):
            self.questions.update({question.get('id'): question})
            return '{ message: "question updated successful"}'

    def delete(self, id):
        self.questions.pop(id)
        return '{ message: "question deleted successful"}'
