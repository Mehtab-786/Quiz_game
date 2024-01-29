class QuizBrain:
    def __init__(self,list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    # def next_question(self,question_number,list):
    #     print(input(f"Q{question_number}. {list[question_number]}(True/False)  "))

    def still_has_question(self):
        return self.question_number < 12

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}.{current_question.text} (True/False)")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("Sorry,you are wrong")
            print(f"Correct answer:{current_answer}")

        print(f"Your score {self.score}/{self.question_number}\n")


