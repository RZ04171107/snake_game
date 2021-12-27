from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align='center', font=FONT)

    def upgrade_score(self):
        self.score = self.score + 1
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, align='center', font=FONT)
