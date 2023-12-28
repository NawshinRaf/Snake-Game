from turtle import Turtle,Screen


class Score():
    def __init__(self):
        self.score = 0
        self.score_board = Turtle()
        self.score_board.goto(0,220)
        self.score_board.color("white")
        self.score_board.write(f"Score: {self.score}", align="center", font="Arial,8,normal")



    def update_score(self):
        self.score_board.clear()
        self.score+=1
        self.score_board.write(f"Score: {self.score}", align="center", font="Arial,8,normal")
