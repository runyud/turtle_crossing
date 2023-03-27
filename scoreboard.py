from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.player_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.player_score += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
