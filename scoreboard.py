from turtle import Turtle
ALIGNMENT = "Center"
FONT=("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE : {self.score} HIGH SCORE : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w" ) as data_score:
                h_s=str(self.high_score)
                data_score.write(h_s)
        self.score=0
        self.update_scoreboard()




