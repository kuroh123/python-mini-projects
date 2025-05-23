class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    def still_has_q(self):
        return self.question_number < len(self.question_list)
    
    def ask_q(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_q.text} (True/False): ')
        self.check_answer(user_answer, current_q.answer)
        print("\n")
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        