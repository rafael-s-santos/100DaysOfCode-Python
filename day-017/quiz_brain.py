

class QuizBrain:
    def __init__(self, q_list: list[str]) -> None:
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {
            current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print("\n")

        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is: {
                  self.score}/{self.question_number}")
            print("\n")
