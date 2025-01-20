class QuizBrain:
    def __init__(self,question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"The next question is from '{current_question.category.title()}', the difficulty is '{current_question.difficulty.title()}'.")
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right!.")
        else:
            print("That's wrong.")
            print(f"The correct answer was {correct_answer}.")
        if self.still_has_questions():
            print(f"Your current score is: {self.score}/{self.question_number}.")
            print('\n')
        else:
            print('\n')
            print("The quiz is completed.")
            print(f"Your final score is: {self.score}/{self.question_number}.")



