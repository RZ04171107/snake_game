from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.get_highest_score()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}   Highest: {self.highest_score}", False, align='center', font=FONT)

    def upgrade_score(self):
        self.score = self.score + 1
        self.refresh_score()

    def game_over(self):
        self.check_high_score()
        self.goto(0, 0)
        self.write('GAME OVER', False, align='center', font=FONT)

    def get_highest_score(self):
        with open("highest.txt") as file:
            content = file.read()
            print(f"highest score: {content}")

        if content == "":
            highest = 0
        else:
            highest = int(content)
        self.highest_score = highest

    def check_high_score(self):
        if self.score > self.highest_score:
            with open("highest.txt", "w") as file:
                file.write(str(self.score))

        self.score = 0
