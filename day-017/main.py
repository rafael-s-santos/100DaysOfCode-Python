from question_model import Question
from data import question_data


question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_quetion = Question(question_text, question_answer)
    question_bank.append(new_quetion)

print(question_bank[11].answer)
