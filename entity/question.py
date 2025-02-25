
class Question:
    def __init__(self, question, correct_answer, answers):
        self.question = question
        self.correct_answer = correct_answer
        self.answers = answers

    def __str__(self):
        return f"{self.question}, {self.correct_answer}, {self.answers}"
