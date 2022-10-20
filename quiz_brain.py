import html
from tkinter import messagebox


class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.score = 0
        self.question_number = 0
        self.current_question = None
        self.correct_answer = None
        self.user_answer = None

    def next_question(self):
        try:
            self.current_question = self.question_list[self.question_number]
            self.question_number = self.question_number + 1
            question_text = html.unescape(self.current_question.question)
            self.correct_answer = self.current_question.answer
            return f"Q.{self.question_number} : {question_text}"

        except IndexError:
            messagebox.showinfo("Quiz Finished", message="You answered all the questions!")
            return "Quiz Finished"

    def check_answer(self, user_answer):
        if user_answer == self.correct_answer:
            return True
        else:
            return False
