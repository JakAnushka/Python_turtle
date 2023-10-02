from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)

    # def food_eaten(self):
    #     self.hideturtle()
    #     self.refresh()
    #     self.showturtle()