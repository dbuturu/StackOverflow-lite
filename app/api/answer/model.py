
class AnswerModel():
    def __init__(self, answers: dict):
        self.answers = answers

    def create(self, answer):
        self.answers.append({answer.get('id'): answer})
        return '{ message: "answer added successful"}'

    def read(self, question_id):
        answer = [
            answer for answer in self.answers
            if answer["question_id"] == question_id
        ]
        if answer:
            return answer

    def update(self, answer):
        if answer.get('id'):
            self.answers.append({answer.get('id'): answer})
            return '{ message: "answer updated successful"}'

    def delete(self, id):
        self.answers.pop(id)
        return '{ message: "answer deleted successful"}'
