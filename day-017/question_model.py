class Question:
    def __init__(self, question_text: str, question_answer: bool) -> None:
        self.text = question_text
        self.answer = question_answer


if __name__ == '__main__':
    question1 = Question('2 + 3 = 5', True)
    print(question1.text)
    print(question1.answer)
