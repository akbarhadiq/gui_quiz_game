import tkinter
import tkinter as ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.question_answered = 0

        # receive quizbrain object, with this you can call quizbrain function within this class,
        # I don't know why they didn't use inheritance it's the tutorial
        self.quiz = quiz_brain

        # user answer check to write ui
        self.user_answer = None

        # Create the window
        self.window = tkinter.Tk()
        self.window.configure(background=THEME_COLOR)
        self.window.title("Quizzler")

        # create the score text
        self.score_text = ttk.Label(text=f"Score:{self.score}", background=THEME_COLOR, foreground="white", pady=20,
                                    padx=20)
        self.score_text.grid(column=2, row=1)

        # create the canvas for the quiz
        self.quiz_canvas = tkinter.Canvas()
        self.quiz_canvas.configure(height=250, width=300)
        self.quiz_canvas.grid(column=1, row=2, columnspan=2, sticky="EW", pady=20, padx=20)

        # create the button

        # button img
        self.check_button_image = tkinter.PhotoImage(file="images/true.png")
        self.cross_button_image = tkinter.PhotoImage(file="images/false.png")

        # button ttk object
        self.check_button = tkinter.Button(image=self.check_button_image, padx=20, pady=20, background=THEME_COLOR,
                                           highlightthickness=0, command=self.check_button_press)
        self.cross_button = tkinter.Button(image=self.cross_button_image, padx=20, pady=20, background=THEME_COLOR,
                                           highlightthickness=0, command=self.cross_button_press)

        # put the button on window
        self.check_button.grid(column=1, row=3, pady=20)
        self.cross_button.grid(column=2, row=3, pady=20)

        # put the text : to canvas
        self.quiz_text = self.quiz_canvas.create_text((150, 125), text="This is where your \nquestion lay", font=FONT,
                                                      width=280)

        self.get_next_question()

        # window mainloop
        self.window.mainloop()

    # get the next question using imported quiz_brain model of self.quiz in ui
    def get_next_question(self):
        question_text = self.quiz.next_question()
        # configure canvas text!
        self.quiz_canvas.itemconfigure(self.quiz_text, text=question_text)

    def check_button_press(self):
        self.user_answer = "True"
        self.check_answer(self.user_answer)

    def cross_button_press(self):
        self.user_answer = "False"
        self.check_answer(self.user_answer)

    def check_answer(self, user_answer):

        is_user_correct = self.quiz.check_answer(user_answer)
        if is_user_correct:
            self.score = self.score + 1
            self.score_text.configure(text=f"Score:{self.score}")
            print("correct")
        else:
            print("false")

        self.get_next_question()
