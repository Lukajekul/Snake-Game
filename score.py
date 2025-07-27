from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.update_scoreboar()
       

    def update_scoreboar(self):
        self.write(f"Score {self.score}", align= ALIGNEMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboar()

    def game_ower(self):
        self.goto(0,0)
        self.write(f"Game ower", align= ALIGNEMENT, font= FONT)