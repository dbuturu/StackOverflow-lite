
class CommentModel():
    def __init__(self, comments: dict):
        self.comments = comments

    def create(self, comment):
        self.comments.append({comment.get('id'): comment})
        return '{ message: "comment added successful"}'

    def read(self, answer_id):
        comment = [
            comment for comment in self.comments
            if comment["answer_id"] == answer_id
        ]
        if comment:
            return comment

    def update(self, comment):
        if comment.get('id'):
            self.comments.append({comment.get('id'): comment})
            return '{ message: "comment updated successful"}'

    def delete(self, comment_id):
        self.comments.pop(comment_id)
        return '{ message: "comment deleted successful"}'
