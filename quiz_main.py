from question_model import QuestionModel
from quiz_brain import QuizBrain
import data
from ui import UserInterface


def quiz_game():
    question_bank = []
    question_data = data.get_question()

    for question in question_data:
        question_text = question['question']
        question_answer = question['correct_answer']
        new_question = QuestionModel(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = UserInterface(quiz)


quiz_game()
