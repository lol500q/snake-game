from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score=0



        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"score : {self.score}", font=('Arial', 15, 'italic'))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score : {self.score}", font=('Arial', 15, 'italic'))





