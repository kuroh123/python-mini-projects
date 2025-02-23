from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_q = Question(text=question['question'], answer=question['correct_answer'])
    question_bank.append(new_q)

quiz_start = QuizBrain(question_list=question_bank)

while quiz_start.still_has_q():
    quiz_start.ask_q()

print("You've completed the quiz!")
print(f'Your final score is: {quiz_start.score}/{quiz_start.question_number}')